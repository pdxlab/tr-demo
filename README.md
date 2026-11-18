# tr-demo — Trust Review in action

This repo demonstrates [Trust Review (TR)](https://trustmodel.ai/trust-review-action) on a loan pre-screening AI agent.

## Three live PRs

| PR | What it shows |
|---|---|
| [#1 — Fairness regression](../../pulls/1) | TR catches a prompt change that drops the Fairness score from 78→61 |
| [#2 — Clean pass](../../pulls/2) | TR passes after a safety improvement — green across all dimensions |
| [#3 — Safety improvement](../../pulls/3) | TR shows before/after: Safety 65→84 after adding bias guardrails |

## Install TR on your repo

\`\`\`yaml
- uses: pdxlab/trustmodel-review-action@v1
  with:
    api_key: ${{ secrets.TRUSTMODEL_API_KEY }}
\`\`\`

**Free for public repos. Advisory by default. Never blocks a fresh install.**

→ [GitHub Marketplace](https://github.com/marketplace/actions/trustmodel-review)  ·  [Docs](https://trustmodel.ai/trust-review-action)
