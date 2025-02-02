# Python FastAPI CICD Pipeline

A FastAPI application with automated deployment pipeline using GitHub Actions and Fly.io.

## Prerequisites

Python 3.x
Fly.io account
GitHub repository

## Local Setup
```
pip install -r requirements.txt
flyctl auth signup  # if new to Fly.io
flyctl launch      # initial app setup
```
## CI/CD Pipeline

### Pull Request Workflow

- Triggers on PR events (open/sync/reopen/close)
- Runs tests in dev environment
- Deploys preview if PR is open
- Uses concurrent job control

### Deployment Workflow

- Triggers on merge to main
- Sequential deployment: dev → prod
- Environment-specific configurations
- Deployment status verification
- Concurrent deployment protection

## Environment Variables

- `FLY_API_TOKEN`: Fly.io authentication token

## API Endpoints

- `/`: Main page with timestamp
- `/health`: Health check endpoint
- `/api/time`: Current time endpoint
