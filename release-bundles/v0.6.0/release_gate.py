"""GitHub Actions release gate: fixed official inputs, real updater classes, no game launch."""
from pathlib import Path
import base64,hashlib,json,os,re,shutil,subprocess,sys,urllib.request,zipfile
OUT=Path('release-out');M=json.loads((OUT/'manifest.json').read_text());REPO=os.environ['REPO'];REF=os.environ['REF']
PLATFORMS=['1.20.4','1.21.11','26.1','26.1.1','26.1.2','26.2','26.3']
assert M['version']=='0.6.0' and REPO=='starekingz/MultiServerZh-Translations'
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def gh(*args):return subprocess.check_output(['gh',*args])
def raw(name):
    assert re.fullmatch(r'[A-Za-z0-9_.-]+',name)
    return gh('api','-H','Accept: application/vnd.github.raw+json',f'repos/{REPO}/contents/release-bundles/v0.6.0/{name}?ref={REF}')
def call(args):subprocess.run(args,check=True)
def cp(*parts):return os.pathsep.join(map(str,parts))
def prepare():
    allowed={f'multiserverzh-0.6.0-mc{mc}.jar' for mc in PLATFORMS}|{'multiserverzh-0.6.0-multiversion-source.zip','legacy-updater-sources.zip'}
    assert {a['name'] for a in M['staged']}==allowed
    for item in M['staged']:
        p=OUT/item['name'];p.write_bytes(base64.b64decode(raw(item['name']+'.base64'),validate=True));assert digest(p)==item['sha256']
        with zipfile.ZipFile(p) as z:assert z.testzip() is None
    for mc in PLATFORMS:
        jar=OUT/f'multiserverzh-0.6.0-mc{mc}.jar'
        with zipfile.ZipFile(jar) as z:
            meta=json.loads(z.read('fabric.mod.json'));assert meta['version']=='0.6.0' and meta['depends']['minecraft']==mc
            dest=OUT/'classes'/mc;dest.mkdir(parents=True,exist_ok=True)
            for name in z.namelist():
                if re.fullmatch(r'dev/multiserverzh/ModRelease(?:\$Release)?\.class',name):
                    p=dest/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))
    shutil.copy2(OUT/'multiserverzh-0.6.0-mc1.21.11.jar',OUT/'multiserverzh-0.6.0.jar')
    for name,content in M['text_assets'].items():
        assert name in {'INSTALL.md','validation.json','release-notes.md','UniversalReleaseTest.java','ReleaseProbe.java'}
        (OUT/name).write_text(content,encoding='utf-8')
    with zipfile.ZipFile(OUT/'legacy-updater-sources.zip') as z:z.extractall(OUT/'legacy')
    for dep in M['ci_dependencies']:
        assert dep['url'].startswith(('https://maven.fabricmc.net/','https://libraries.minecraft.net/'))
        p=OUT/dep['name'];p.write_bytes(urllib.request.urlopen(dep['url'],timeout=60).read());assert digest(p)==dep['sha256']
    with zipfile.ZipFile(OUT/'multiserverzh-0.6.0-all-versions.zip','w',zipfile.ZIP_STORED) as z:
        files=[(mc+'/'+f'multiserverzh-0.6.0-mc{mc}.jar',OUT/f'multiserverzh-0.6.0-mc{mc}.jar') for mc in PLATFORMS]+[('INSTALL.md',OUT/'INSTALL.md'),('validation.json',OUT/'validation.json')]
        for name,p in files:
            info=zipfile.ZipInfo(name,(2026,11,16,0,0,0));info.create_system=3;info.external_attr=0o100644<<16;z.writestr(info,p.read_bytes())
    names=[a['name'] for a in M['assets']]
    for item in M['assets']:assert digest(OUT/item['name'])==item['sha256'],item['name']
    (OUT/'SHA256SUMS.txt').write_text(''.join(a['sha256']+'  '+a['name']+'\n' for a in M['assets']),encoding='ascii')
def test():
    deps=[OUT/'gson.jar',OUT/'fabric-loader.jar'];tests=OUT/'tests';tests.mkdir(exist_ok=True)
    call(['javac','-proc:none','-cp',cp(OUT/'classes/1.20.4',*deps),'-d',str(tests),str(OUT/'UniversalReleaseTest.java'),str(OUT/'ReleaseProbe.java')])
    for mc in PLATFORMS:
        result=subprocess.check_output(['java','-cp',cp(tests,OUT/'classes'/mc,*deps),'dev.multiserverzh.UniversalReleaseTest'],text=True)
        assert 'Passed 55 universal release checks' in result;print(mc,result.strip(),flush=True)
        dest=OUT/'legacy-classes'/mc;dest.mkdir(parents=True,exist_ok=True)
        call(['javac','-proc:none','-cp',cp(*deps),'-d',str(dest),str(OUT/'legacy'/mc/'ModRelease.java')])
def release_response():
    r=json.loads(gh('api',f'repos/{REPO}/releases/tags/v0.6.0'));assets={a['name']:a for a in r['assets']}
    expected={a['name']:a for a in M['assets']};expected['SHA256SUMS.txt']={'sha256':digest(OUT/'SHA256SUMS.txt')}
    assert set(assets)==set(expected)
    for name,a in expected.items():assert assets[name]['digest']=='sha256:'+a['sha256'] and assets[name]['size']==(OUT/name).stat().st_size,name
    return r
def probe(r):
    # GitHub draft responses are treated as public only within this pre-publication test fixture.
    r=dict(r);r['draft']=False;p=OUT/'release-response.json';p.write_text(json.dumps(r))
    deps=[OUT/'gson.jar',OUT/'fabric-loader.jar']
    for mc in PLATFORMS:
        for mode,classes in [('current',OUT/'classes'/mc),('legacy',OUT/'legacy-classes'/mc)]:
            call(['java','-cp',cp(OUT/'tests',classes,*deps),'dev.multiserverzh.ReleaseProbe',str(p),mc,mode])
command=sys.argv[1]
if command=='prepare':prepare()
elif command=='test':test()
elif command=='upload':call(['gh','release','upload','v0.6.0','--repo',REPO]+[str(OUT/a['name']) for a in M['assets']]+[str(OUT/'SHA256SUMS.txt')])
elif command=='verify-draft':
    r=release_response();assert r['draft'];probe(r)
elif command=='verify-public':
    r=release_response();assert not r['draft'] and not r['prerelease'];probe(r)
    latest=json.loads(gh('api',f'repos/{REPO}/releases/latest'));assert latest['tag_name']=='v0.6.0';print('Published release and all seven old/current updater paths verified.')
else:raise ValueError(command)
