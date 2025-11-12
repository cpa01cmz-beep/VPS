# Repository Orchestration Planning

## Current State Analysis

### Workflows
We have several workflows in the repository:
1. Free VPS Research – Simple (gemini-researcher.yml)
2. iFlow - Solve Issue (iflow -issue.yml)
3. Iflow - Intelijen (iflow-intelijen.yml)
4. iFlow - Repository Maintenance (iflow-maintenance.yml)
5. iFlow - Repository Orchestrator (iflow-orchestrator.yml)
6. iFlow - Orchestrator+ (Innovate) (iflow-orchin.yml)
7. iFlow - Apply PR Changes (iflow-pr.yml)

### CI Baseline
From the recent run data, we can see that the "iFlow - Orchestrator+ (Innovate)" workflow has had both successes and failures. The most recent run is still in progress (empty conclusion).

## Proposed Improvements

### 1. CI Optimization
- Split/parallelize long jobs in iflow-orchin.yml
- Extract reusable workflows to .github/workflows/_reusable/
- Add matrix strategies where applicable
- Implement caching keyed by lockfiles

### 2. Experimental Workflows
- Create exp-* workflows to trial new strategies
- Wire them via workflow_call for reusability

### 3. Documentation
- Add CODEOWNERS file
- Create issue templates for different types of issues
- Add SECURITY.md
- Implement labeler configuration
- Set up release-drafter configuration

### 4. Dependency Management
- Implement safe patch bumps with tests

### 5. Innovation
- Create composite actions for common steps
- Implement auto-benchmarking for CI time

## Implementation Plan

1. Create experimental workflows for testing new CI strategies
2. Refactor existing workflows to use reusable components
3. Add caching to speed up builds
4. Implement documentation improvements
5. Set up automated dependency updates
6. Create composite actions for common tasks
7. Validate changes with trial runs
8. Measure and report CI time improvements
9. Update policies and memory with learnings

## Required Permissions
- actions: write
- contents: write
- issues: write
- pull-requests: write
- security-events: write
- workflows: write