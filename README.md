# Template Github Workflows

## Release Management

This project uses [Release Please](https://github.com/googleapis/release-please) from Google to automate the release process. The tool handles versioning and changelog generation based on commit messages.

### Conventional Commits

To ensure releases are generated correctly, we follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. Commit messages should be structured as follows:

- _feat_: A new feature
- _fix_: A bug fix
- _docs_: Documentation only changes
- _style_: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
- _refactor_: A code change that neither fixes a bug nor adds a feature
- _perf_: A code change that improves performance
- _test_: Adding missing or correcting existing tests
- _build_: Changes that affect the build system or external dependencies
- _ci_: Changes to our CI configuration files and scripts
- _chore_: Other changes that don't modify src or test files
- _revert_: Reverts a previous commit

Example:

```
feat: add new workflow to handle peppermint

```

### Breaking Changes and Major Versions

When introducing breaking changes, follow these steps to ensure a new major version is released:

1. **Prefix the commit message with `BREAKING CHANGE:`**: Indicate that the commit introduces breaking changes.
2. **Describe the breaking change in the commit message**: Provide details about what changes are being made and how they affect existing functionality.
3. **Merge the commit**: Once the breaking change commit is merged, `Release Please` will automatically create a new major version.

Example commit message for a breaking change:

```
feat!: add new workflow to handle peppermint

BREAKING CHANGE: This update changes the way the Datadog monitor module interacts with the API, requiring updates to existing configurations.
```

The `!` after `feat` indicates a breaking change, and the `BREAKING CHANGE:` section provides details about the change.
