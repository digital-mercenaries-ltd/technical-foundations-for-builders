# Issue tracker: GitHub

Issues and product requirement documents for this repository live in GitHub Issues at `digital-mercenaries-ltd/technical-foundations-for-builders`. Use the `gh` command-line interface from the public repository clone.

## Conventions

- Create issues with `gh issue create`.
- Read an issue and its discussion with `gh issue view <number> --comments`.
- List work with `gh issue list`, applying state and label filters appropriate to the task.
- Comment with `gh issue comment <number>`.
- Apply or remove labels with `gh issue edit <number>`.
- Close completed or rejected work with `gh issue close <number>` and a short explanatory comment.

Infer the repository from the public clone's `origin`; do not run public issue operations from the private research clone.

## Pull requests as a triage surface

External pull requests are not treated as feature requests or fed into the issue-triage queue. Review pull requests through the repository's normal review workflow.

## Skill terminology

When an engineering skill says to publish to the issue tracker, create a GitHub issue in the public repository. When it says to fetch a ticket, read the complete GitHub issue and its comments.
