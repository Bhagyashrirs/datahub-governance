# DataHub Governance Automation (Option 3)
 
## Goal
Automatically identify datasets without owners in DataHub and tag them with `needs-owner`.
 
## Approach
- Use DataHub GraphQL Search API to find datasets
- Filter datasets with no owners
- Apply tags using GraphQL mutations
- Run automation as a Kubernetes CronJob
 
## Architecture
- Python script for governance logic
- Kubernetes CronJob for scheduling

 
## Why this approach
- Clear separation of logic and scheduling
- Kubernetes-native automation
- Easily extensible for more governance rules
 
## Limitations
- DataHub deployment was unstable due to AKS quota limits
- Scripts are provided with dry-run logic
- API calls are documented but not executed in this environment
