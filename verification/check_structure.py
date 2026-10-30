"""Validate the reader route and project-intrinsic milestone map, offline."""
from pathlib import Path
import json
import re
from urllib.parse import unquote


def main():
    root=Path(__file__).resolve().parents[1]
    errors=[]
    pages=sorted(root.rglob('*.md'))
    checked=0
    for page in pages:
        text=page.read_text()
        for raw in re.findall(r'\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)',text):
            if '://' in raw or raw.startswith(('mailto:','#')):
                continue
            path=unquote(raw.split('#',1)[0])
            target=(page.parent/path).resolve()
            if root not in target.parents and target!=root:
                errors.append(f'{page.relative_to(root)}: link escapes repository: {raw}')
            elif not target.is_file():
                errors.append(f'{page.relative_to(root)}: missing target: {raw}')
            checked+=1
    text=(root/'learning/MILESTONES.md').read_text()
    ids=re.findall(r'^### (M\d\d) ',text,re.M)
    expected=[f'M{i:02}' for i in range(1,31)]
    if ids!=expected:
        errors.append('milestone IDs must be exactly M01–M30 in order')
    blocks=re.split(r'^### ',text,flags=re.M)[1:]
    for i,block in enumerate(blocks,1):
        for label in ('Central question','Understanding target','Dependencies','Connection and story role','Sources'):
            if f'**{label}:**' not in block:
                errors.append(f'M{i:02}: missing {label}')
        dep=re.search(r'\*\*Dependencies:\*\*([^\n]*)',block)
        if dep:
            for earlier in re.findall(r'M(\d\d)',dep[1]):
                if not 1<=int(earlier)<i:
                    errors.append(f'M{i:02}: non-earlier dependency M{earlier}')
    split=text.find('## Narrative/innovation')
    if len(re.findall(r'^### M\d\d ',text[:split],re.M))!=12:
        errors.append('background phase must contain 12 targets')
    for path in ('README.md','llms.txt','science/README.md','learning/README.md','learning/ANCHOR_BRIDGE.md','learning/TUTORIAL.md','references/references.bib','verification/results.json','verification/requirements.txt'):
        if not (root/path).is_file():
            errors.append('missing route: '+path)
    for page in pages:
        if page.name.upper()=='COACHING.MD':
            errors.append('personal coaching contract belongs outside the scientific repository')
    report={'status':'pass' if not errors else 'fail','markdown_pages':len(pages),'local_links_checked':checked,'milestones':len(ids),'background_milestones':12,'innovation_milestones':18,'errors':errors,'limits':'Offline link and learning structure checks only; no hosted-rendering or scientific-proof verdict.'}
    print(json.dumps(report,indent=2))
    if errors:
        raise SystemExit(1)

if __name__=='__main__':
    main()
