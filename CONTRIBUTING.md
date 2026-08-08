# Contributing to Wanderlight

This is a 5-person team project (fictional, for practice). These are our
conventions — follow them the same way you would on a real team.

## Branch naming

Every change gets its own branch off `main`. Never commit directly to `main`.

Format: `type/short-description`

Types we use:
- `feature/` — new functionality (e.g. `feature/inventory-system`)
- `fix/` — bug fixes (e.g. `fix/shopkeeper-repeats-dialogue`)
- `content/` — narrative/text changes, Jordan's tickets (e.g. `content/coldharbor-description`)
- `test/` — adding or fixing tests

## Commit messages

Short, present-tense, describes what the commit does:

Good: `fix shopkeeper dialogue repeating on second visit`
Avoid: `fixed stuff` or `updates`

## Pull requests

1. Push your branch, open a PR against `main`.
2. Fill in: what you changed, why, and how you tested it.
3. Wait for review before merging — on this team, that's Sam (or, in
   practice, your AI reviewer) for code, Jordan for narrative content.
4. Address every review comment individually. Don't just push a fix
   silently — reply to the comment so the reviewer knows it's handled.

## Running tests

Instructions coming once the test suite exists.

## Code style

Keep it simple and readable — this codebase is meant to be easy for a
beginner to read end to end. Favor clarity over cleverness.
