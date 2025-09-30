# Contributing to Invoco

Thanks for your interest in contributing!

## Getting Started
- Clone the repo: `git clone git@github.com:beingpythonic/invoco.git`
- Create the environment: `hatch env create`
- Run tests: `make test`

## Development Workflow
- Lint: `make lint`
- Format: `make format`
- Typecheck: `make typecheck`
- Docs: `make docs`

See the full [Developer Guide](https://beingpythonic.github.io/invoco/dev_guide.html) for details.

## Working on an Issue

Invoco uses a protected `main` branch for stable releases. Active development happens in the `develop` branch.

### Workflow

1. **Pick or Create an Issue**
   - Use the issue templates (Feature, Bug, Docs, Chore).
   - Assign the issue to the appropriate milestone.

2. **Create a Branch**
   - Branch from `develop`, not `main`.
   - Branch naming:
     - `feat/<short-description>` for new features
     - `fix/<short-description>` for bug fixes
     - `docs/<short-description>` for documentation
     - `chore/<short-description>` for maintenance
     - `refactor/<short-description>` for internal changes
     - `test/<short-description>` for test-related work
   - Example:
     ```
     git checkout develop
     git checkout -b feat/task-registry
     ```

3. **Make Commits**
   - Follow the commit message convention:
     ```
     type(scope): short summary
     ```
   - Reference issues where relevant, e.g.:
     ```
     feat(registry): expand task registry #12
     ```

4. **Open a Pull Request**
   - Open a PR from your feature branch into `develop`.
   - In the PR description, include `Closes #<issue-number>`.
   - Fill out the PR template (summary, details, related issues, checklist).

5. **Release Process**
   - When a milestone is complete, a `release/x.y.z` branch is created from `develop`.
   - Version bump and changelog updates happen there.
   - The release branch is merged into both `main` (tagged release) and `develop`.

## Commit Messages

Invoco follows a structured commit message format for clarity and consistency.

### Format
```
<type>(<scope>): <short summary>
```

- **type**: feat, fix, docs, style, refactor, test, chore
- **scope**: optional, e.g., registry, cli, docs
- **summary**: imperative tense, no period

### Examples
```
feat(registry): add task lookup by name
fix(cli): correct JSON parsing error
docs: update installation instructions
style(core): apply Black formatting
```

### Conventions
- Reference an issue number where relevant:  
  ```
  feat(registry): expand task registry #12
  ```
- Keep summaries concise (max ~72 characters).
- Use the body of the commit message for additional context when needed.

## Pull Requests

Pull requests are used to propose changes before merging into `develop`.

### Guidelines
- Each PR should address a single issue or related set of changes.
- Use the PR template to summarize the work, provide context, and link issues.
- Include `Closes #<issue-number>` to automatically close linked issues on merge.
- Ensure all checks (pre-commit, tests, CI) pass before requesting a review.
- Keep PRs focused and avoid unrelated changes.

## Code Style

- Formatting is enforced with `black` and `ruff`.
- Type checking is enforced with `mypy`.
- Pre-commit hooks run automatically on commit to enforce consistency.
- Do not commit code that fails lint, type check, or formatting checks.

## Tests

- Tests use `pytest`.
- Run all tests with:
  ```
  make test
  ```
- New features and fixes must include test coverage.
- Tests should be isolated, deterministic, and pass consistently.

## Release Process

1. Ensure all issues in the milestone are closed and `develop` is stable.
2. Create a release branch:
   ```
   git checkout develop
   git checkout -b release/x.y.z
   ```
3. Update `CHANGELOG.md` and bump version in code.
4. Run full test suite and verify CI passes.
5. Merge the release branch into `main` and tag the release:
   ```
   git checkout main
   git merge --no-ff release/x.y.z
   git tag -a vX.Y.Z -m "Release vX.Y.Z"
   git push origin main --tags
   ```
6. Merge the release branch back into `develop`:
   ```
   git checkout develop
   git merge --no-ff release/x.y.z
   git push origin develop
   ```
7. Optionally, publish the package to PyPI once the project is ready.

---

For more details, see the [Developer Guide](https://beingpythonic.github.io/invoco/dev_guide.html).

