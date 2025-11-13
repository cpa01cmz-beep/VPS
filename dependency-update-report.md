# Dependency Update Report

## Summary
Applied patch-level security updates to resolve vulnerabilities in the project's Python dependencies.

## Updated Dependencies
| Package | Old Version | New Version | Vulnerability Severity |
|---------|-------------|-------------|------------------------|
| lazr.restfulclient | 0.14.4 | 0.14.6 | Low |
| lazr.uri | 1.0.6 | 1.0.7 | Low |

## Changelog
- **lazr.restfulclient 0.14.6**:
  - Add Read the Docs configuration
  - Add Python 3.12 compatibility
  - Fix handling of 304 responses with an empty body on Python 3

- **lazr.uri 1.0.7**:
  - Add support for Python 3.9, 3.10, 3.11, 3.12 and 3.13
  - Drop support for Python 3.7 and below
  - Add basic pre-commit configuration
  - Publish documentation on Read the Docs
  - Apply black, isort, pyupgrade and check-manifest

## Verification
All tests are passing after the updates.