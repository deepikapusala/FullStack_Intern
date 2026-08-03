# Fullstack-Intern

## Overview
This repository contains my Full Stack internship practicals and learning progress at **Sandlogic**. Every topic I learn — starting Day 1 — is documented and committed here, following a structured branch-per-topic workflow.

## Technologies
- Git
- GitHub
- HTML / CSS
- JavaScript
- Node.js
- React.js
- Next.js
- PostgreSQL

## Repository Structure
```
Fullstack-Intern/
│
├── .github/
│   └── pull_request_template.md
│
├── .gitignore
├── README.md
│
└── week-01-central-repo-git-branching-strategy/
    ├── notes.md
    └── screenshots/
```

## Branch Naming Convention
Use the following format for every practical:

```
week-NN-topic-slug
```

Examples:
- `week-01-central-repo-git-branching-strategy`
- `week-01-semantic-html-accessibility`
- `week-02-positioning-flexbox-grid`
- `week-03-js-execution-context-scope-closures`

`NN` is always a 2-digit week number (01, 02, 03...) so branches sort chronologically, and `topic-slug` is a short, lowercase, hyphen-separated version of the topic name.

## Contribution Workflow
Every practical in this plan follows the same trunk-based-friendly loop — `main` is always stable, and all work happens on short-lived branches merged in via reviewed PRs:

1. Pull the latest changes from `main`.
2. Create a new branch (`week-NN-topic-slug`).
3. Make your changes.
4. Commit with a meaningful, conventional message (e.g., `docs:`, `feat:`, `fix:`).
5. Push your branch.
6. Open a Pull Request using the PR template.
7. Self-review (or mentor review) the diff.
8. Merge into `main` after checks pass.
9. Pull `main` locally again before starting the next topic.

## Branch Protection
`main` is protected on this repo:
- No direct pushes — all changes go through a Pull Request.
- PR must be reviewed/approved before merging.
- History stays clean and traceable, topic by topic.

## Learning Log
Each week's folder contains the notes, code, and exercises for that topic, along with a short write-up of what I learned. This README will be updated as the internship progresses.
