# Workflow Improvements Needed

This document outlines the improvements that should be made to the GitHub Actions workflows in this repository. These changes were identified during the repository orchestration process but could not be automatically applied due to GitHub's security restrictions on workflow modifications.

## Action Pinning

All GitHub Actions should be pinned to their SHA rather than version tags for security. The following actions need to be updated:

1. `actions/checkout@v5` → `actions/checkout@08c6903cd8c0fde910a37f88322edcfb5dd907a8`
2. `actions/upload-artifact@v5` → `actions/upload-artifact@330a01c490aca151604b8cf639adc76d48f6c5d4`
3. `actions/download-artifact@v6` → `actions/download-artifact@018cc2cf5baa6db3ef3c5f8a56943fffe632ef53`
4. `actions/github-script@v8` → `actions/github-script@ed597411d8f924073f98dfc5c65a23a2325f34cd`
5. `iflow-ai/iflow-cli-action@v2.1.0` → `iflow-ai/iflow-cli-action@5033255d7d73eab7dc4970f1ac8df7a93f30fdbc`
6. `step-security/harden-runner@v2` → `step-security/harden-runner@95d9a5deda9de15063e7595e9719c11c38c90ae2`
7. `google-github-actions/run-gemini-cli@v0.1.14` → `google-github-actions/run-gemini-cli@f7db4b6f82ad0c3725cf4c98bdd93af80e22b4dc`

## Concurrency Settings

The following workflows are missing concurrency settings and should have them added:

1. `iflow-docs.yml` - Add:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```

2. `iflow-maintenance.yml` - Add:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}
     cancel-in-progress: false
   ```

3. `iflow-intelijen.yml` - Add:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```

4. `gemini-researcher.yml` - Add:
   ```yaml
   concurrency:
     group: ${{ github.workflow }}
     cancel-in-progress: false
   ```

## Summary

These changes improve the security, efficiency, and maintainability of the repository's GitHub Actions workflows. They should be implemented manually by updating each workflow file.