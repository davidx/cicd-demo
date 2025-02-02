# Python FastAPI CICD Pipeline

A FastAPI application with automated deployment pipeline using GitHub Actions and Fly.io.

## Features

FastAPI web application with Jinja2 templating
Health check and time API endpoints
Multi-environment deployment (dev/prod)
Automated testing and preview deployments for PRs
Continuous deployment on merge to main

## Prerequisites

Python 3.x
Fly.io account
GitHub repository

## Local Setup

pip install -r requirements.txt
flyctl auth signup  # if new to Fly.io
flyctl launch      # initial app setup

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
- `FLY_APP`: Application name

## API Endpoints

- `/`: Main page with timestamp
- `/health`: Health check endpoint
- `/api/time`: Current time endpoint

## Contributing

1. Create feature branch
2. Submit PR
3. Automated tests will run
4. Preview deployment available
5. Merge triggers production deployment

## Infrastructure

- GitHub Actions for CI/CD
- Fly.io for hosting
- FastAPI framework
- Jinja2 templating