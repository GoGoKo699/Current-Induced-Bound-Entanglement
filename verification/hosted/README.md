# Hosted mathematics verification

These read-only tools compare the actual commit-pinned GitHub renderer with the mathematical source. A local TeX compilation is only the reference side of the comparison.

The collector requires Node.js 18+, Python 3.10+, Git, Playwright and MathJax. Install dependencies outside the repository, then run against an exact checked-out commit:

```bash
npm install --prefix /tmp/cibe-hosted-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/cibe-hosted-deps/node_modules/.bin/playwright install chromium
python verification/hosted/build_contract.py --revision "$(git rev-parse HEAD)" --output /tmp/cibe-math-contract.json
NODE_PATH=/tmp/cibe-hosted-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Current-Induced-Bound-Entanglement \
  --revision "$(git rev-parse HEAD)" --output /tmp/cibe-hosted-evidence \
  --contract /tmp/cibe-math-contract.json
```

Use a new empty output directory for each attempt. The collector inventories all tracked Markdown pages, compiles their source expressions, visits the actual GitHub pages in an unsigned-in browser at widths 1440 and 760, and records accessible MathML, source/host structure comparisons, text contracts, geometry, HTML and screenshots. It stops on an access or policy failure rather than switching identities or hosts.

The generated `hosted-report.json` is bound to the source commit, tree, expression counts and artifact hashes. Its structural pass is not a scientific-proof verdict and does not replace human inspection of representative screenshots, equation bodies, tables and navigation. The read-only CI workflow uploads these diagnostic captures; its temporary artifact retention is not permanent research preservation.

The two generic helpers are kept unchanged as a matched pair. Their Git blob identities are `bd075f4bc53029230fad1b18c6b07d603d45f44f` (collector) and `1d3bf9810d0dfadb844a48b354af80f9b66924bc` (source checker). Project-specific text expectations live in `build_contract.py`; they cannot suppress missing expressions or structural mismatches.
