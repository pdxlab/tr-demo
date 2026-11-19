# tr-demo — Trust Review in action

This repo demonstrates [Trust Review (TR)](https://trustmodel.ai/trust-review-action) on a loan pre-screening AI agent.

## Three live PRs

These scenarios illustrate the intended scored-review experience. The pinned v1.0.2 preview records metadata and does not produce ten-dimension PR scores or findings.

| PR | What it shows |
|---|---|
| [#1 — Fairness regression](../../pulls/1) | TR catches a prompt change that drops the Fairness score from 78→61 |
| [#2 — Clean pass](../../pulls/2) | TR passes after a safety improvement — green across all dimensions |
| [#3 — Safety improvement](../../pulls/3) | TR shows before/after: Safety 65→84 after adding bias guardrails |

## Install TR on your repo

Save this as `.github/workflows/trust-review.yml` and add the `TRUSTMODEL_API_KEY` repository secret.

```yaml
# .github/workflows/trust-review.yml
name: Trust Review
on:
  pull_request:
    types: [opened, synchronize, reopened]

permissions:
  contents: read
  statuses: write
  pull-requests: write

concurrency:
  group: trust-review-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  trust-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
        with:
          fetch-depth: 0
          ref: ${{ github.event.pull_request.head.sha }}
          persist-credentials: false
      - uses: pdxlab/trustmodel-review-action@18ca657992bd8233cb97f6e9f3331820cd153262 # v1.0.2
        with:
          api_key: ${{ secrets.TRUSTMODEL_API_KEY }}
          threshold: 70
          framework: EEOC
```

Use an API key for the same environment and organization as your dashboard. The pinned v1.0.2 is a metadata preview, not a PR code evaluator; keep its check optional. Fork PRs are intentionally skipped because repository secrets are unavailable to them.

SHA pins do not update automatically. Configure Dependabot for the github-actions ecosystem to propose Action updates, then review and merge the new release SHA.

Pending checks still block merging if made required; keep this preview optional.

→ [GitHub Marketplace](https://github.com/marketplace/actions/trustmodel-review)  ·  [Docs](https://trustmodel.ai/trust-review-action)
