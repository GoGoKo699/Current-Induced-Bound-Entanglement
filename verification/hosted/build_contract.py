"""Add explicit content expectations for headline and reformatted expressions."""
import argparse
import json
from pathlib import Path
import subprocess
from check_rendered_math import expressions

RULES = [
    ('README.md', r'\Phi_t\text{ is PPT}', ['PPT', 'entanglement breaking', '⇔']),
    ('README.md', r't_{\rm PPT}(\eta,\gamma)', ['PPT', 'EB', 'η', 'γ', '≤']),
    ('README.md', r't_*&=1.26188944840409', ['1.26188944840409', '0.0391427404380864', 'η']),
    ('science/model.md', r'\Phi_t(E_{ij})&=', ['Φ', 'c', 'exp', 'q']),
    ('science/cycle.md', r'P(t)&=p_0I', ['P', 'p', 'cos', 'θ', 'π']),
    ('science/cycle.md', r't_*-t_{\rm PPT}&=K', ['PPT', 'K', '0.0391427404380864', 'η']),
    ('science/operational.md', r'Q_2(\Phi)>0&', ['Q2', 'non-PPT', 'PPT', '⇔']),
    ('learning/TUTORIAL.md', r'D_1(1.25)&=', ['0.0075006931', '1.0085795716', 'R']),
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--revision', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    result = []
    for path, marker, required in RULES:
        source = subprocess.check_output(['git','--no-replace-objects','show',f'{args.revision}:{path}'],cwd=root).decode('utf-8')
        matches = [e for e in expressions(source) if marker in e['tex']]
        if len(matches) != 1:
            raise ValueError(f'{path}: expected one contract expression, found {len(matches)}')
        e = matches[0]
        result.append({'path':path,'index':e['index'],'source_sha256':e['source_sha256'],'required_text':required})
    args.output.write_text(json.dumps({'schema_version':1,'expressions':result},indent=2)+'\n',encoding='utf-8')

if __name__ == '__main__':
    main()
