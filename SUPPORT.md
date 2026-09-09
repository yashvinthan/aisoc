# Getting help with AiSOC

There are a few places to ask, in roughly the order you should try them:

## 1. Docs

The Docusaurus site at <https://tryaisoc.com/docs> mirrors [`apps/docs/docs/`](apps/docs/docs/) in this repo.
Hit the search box first — it covers connectors, quickstarts, operations
runbooks, the eval-harness methodology, deployment guides, and the API
reference.

Useful starting points:

- [Quickstart](apps/docs/docs/quickstart.md) — four ways to bring up a stack.
- [Installation](apps/docs/docs/installation.md) — zero-prerequisite installer.
- [Architecture](apps/docs/docs/architecture.md) — service map and data flow.
- [Operations](apps/docs/docs/operations/) — credentials, security, multi-region.

## 2. GitHub Discussions

For questions, ideas, show-and-tell, and roadmap input:

- **Q&A** — <https://github.com/aisoc/aisoc/discussions/categories/q-a> (answers can be marked accepted)
- **Show and tell** — <https://github.com/aisoc/aisoc/discussions/categories/show-and-tell>
- **Ideas** — <https://github.com/aisoc/aisoc/discussions/categories/ideas>
- **Announcements** — <https://github.com/aisoc/aisoc/discussions/categories/announcements> (read-only for non-maintainers)

Please don't open a GitHub *issue* for a question — they're reserved for
bugs, feature requests, detection-rule proposals, and benchmark
submissions, each of which has its own template.

## 3. Try the live demo

<https://tryaisoc.com> is a hosted demo instance. It can
go offline (see [docs/operations/live-demo-runbook.md](docs/operations/live-demo-runbook.md)).

## 4. File a bug

If you've found a reproducible bug, open a [Bug report](https://github.com/aisoc/aisoc/issues/new?template=bug_report.yml).
Please include:

- AiSOC `VERSION` (from `VERSION` or the `/api/v1/version` endpoint)
- Deployment path (Docker Compose / Render / Fly.io / Helm / Terraform / installer)
- Exact reproduction steps
- Logs from the failing service (`docker compose logs --tail=200 <service>`)

## 5. Report a security issue (privately)

**Do not open a public issue or discussion for a security issue.**
Use [GitHub Security Advisories](https://github.com/aisoc/aisoc/security/advisories/new)
or follow the [SECURITY.md](SECURITY.md) policy. We follow coordinated disclosure.

## Response expectations

AiSOC is community-maintained; response times are best-effort:

- Security advisories: usually triaged within 48 h.
- Bug reports: triaged within a week for most weeks.
- Feature requests / discussions: no SLA — community traction (👍, replies,
  PRs) is what drives prioritisation. See the
  [v8.0 roadmap discussion](https://github.com/aisoc/aisoc/discussions/categories/announcements)
  for what's currently in flight.
