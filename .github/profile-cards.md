# Profile cards

`profile-cards.yml` refreshes the cards daily at 06:23 UTC. It can also be run from the Actions tab with **Run workflow**, and runs when its workflow or generator changes on `main`.

The stats and Fang cards use [GitHub Stats Extended](https://github.com/stats-organization/github-stats-extended) through its maintained Action. The Action's name still contains `github-readme-stats`, but its renderer is Stats Extended, pinned to version 2.3.0. Both light and dark cards are stored in this repository.

The workflow uses the built-in `GITHUB_TOKEN`; no personal access token or separate hosting is needed. It needs permission to write repository contents. Failed API requests stop the job before the commit, so the last successful cards remain visible.

## What the numbers mean

- The merged-PR card counts `is:pr is:merged is:public author:shalashaska117 -user:shalashaska117`. It excludes private repositories and my own repositories, including my forks. Its four bars show selected projects, not a breakdown of the entire total.
- Each project's count comes from the search API's `total_count`, so it does not depend on a page size or the 1,000-result retrieval limit. An incomplete search fails the update.
- The GitHub activity card uses Stats Extended's public activity metrics. Its merged-PR count can include my own repositories; commits and contributed repositories use the renderer's default time windows.
- The Fang card shows repository metadata, including stars and the language reported by GitHub. That language is based on repository contents, not a ranking of language proficiency.

`profile/contributions.json` records the public counts and the UTC date of the last successful fetch. To update that card locally with an authenticated GitHub CLI:

```sh
python scripts/update_contributions.py
```

GitHub may delay scheduled runs. Public-repository schedules can also be disabled after 60 days without activity; re-enable the workflow from the Actions tab if needed. See [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).
