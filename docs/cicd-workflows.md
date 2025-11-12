# CI/CD Workflows Orchestration

This document outlines the recommended improvements for the repository's CI/CD workflows orchestration.

## Current State

The repository uses GitHub Actions for automating various tasks. The main workflows are:
- `gemini-researcher.yml`: Researches free VPS offers and updates `free-vps.md`.
- `iflow-maintenance.yml`: Performs scheduled maintenance (e.g., dependency updates).
- `iflow-docs.yml`: Updates documentation on pushes to the `main` branch.
- `iflow-intelijen.yml`: Gathers repository intelligence and creates new issues.
- `iflow-issue.yml`: Attempts to automatically solve new issues.
- `iflow-pr.yml`: Applies suggested changes from PR comments.

The iFlow configuration is defined in `.github/iflow/config.yaml`.

## Recommended Improvements

### 1. Action Pinning

For security reasons, all GitHub Actions should be pinned to their SHA rather than version tags. This prevents unexpected changes when action owners update their code.

The following actions need to be updated:

1. `actions/checkout@v5` → `actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8`
2. `actions/upload-artifact@v5` → `actions/upload-artifact@330a01c490aca151604b8cf639adc76d48f6c5d4`
3. `actions/download-artifact@v6` → `actions/download-artifact@018cc2cf5baa6db3ef3c5f8a56943fffe632ef53`
4. `actions/github-script@v8` → `actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd`
5. `iflow-ai/iflow-cli-action@v2.1.0` → `iflow-ai/iflow-cli-action@5033255d7d73eab7dc4970f1ac8df7a93f30fdbc`
6. `step-security/harden-runner@v2` → `step-security/harden-runner@95d9a5deda9de15063e7595e9719c11c38c90ae2`
7. `google-github-actions/run-gemini-cli@v0.1.14` → `google-github-actions/run-gemini-cli@f7db4b6f82ad0c3725cf4c98bdd93af80e22b4dc`

### 2. Concurrency Settings

To improve efficiency and prevent conflicts, workflows should have appropriate concurrency settings.

The following workflows need concurrency settings:

1. `iflow-docs.yml`:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```

2. `iflow-maintenance.yml`:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}
     cancel-in-progress: false
   ```

3. `iflow-intelijen.yml`:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```

4. `gemini-researcher.yml`:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}
     cancel-in-progress: false
   ```

## Implementation Notes

These changes improve the security, efficiency, and maintainability of the repository's GitHub Actions workflows. They should be implemented manually by updating each workflow file.

The workflow improvements were identified during the repository orchestration process but could not be automatically applied due to GitHub's security restrictions on workflow modifications.