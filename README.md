# AI Agent Platform

![Terraform](https://img.shields.io/badge/Terraform-1.13-7B42BC?logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.31-326CE5?logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EKS-FF9900?logo=amazon-aws&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-latest-2496ED?logo=docker&logoColor=white)
![CI/CD](https://github.com/DanielMelo1/ai-agent-platform/workflows/CI%2FCD%20Pipeline/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

Enterprise-grade AI orchestration platform with multi-provider LLM support, intelligent routing, Kubernetes deployment, and automated CI/CD.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [AWS Deployment](#aws-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Usage](#api-usage)
- [Design Decisions](#design-decisions)
- [Problems Encountered](#problems-encountered)
- [Known Limitations](#known-limitations)
- [Screenshots](#screenshots)

---

## Overview

Production-ready platform for deploying and managing AI agents featuring:

- **Multi-provider LLM architecture**: Vendor-agnostic design (Claude, Gemini)
- **Intelligent query routing**: Complexity-based provider selection
- **Kubernetes orchestration**: Scalable, self-healing infrastructure on AWS EKS
- **CI/CD automation**: GitHub Actions with container registry
- **Vector database**: Qdrant integration for semantic search
- **Infrastructure as Code**: Terraform-managed deployment
- **Observability**: Prometheus + Grafana monitoring stack

### Value Proposition

Unlike single-provider AI platforms, this architecture enables:
- Zero vendor lock-in through provider abstraction
- Cost optimization via intelligent routing
- Automated deployments with GitOps
- Production-grade infrastructure patterns
- Enterprise scalability and reliability

---

## Architecture

### System Design
```
┌─────────────────────────────────────────┐
│          FastAPI REST API               │
│    (Endpoints: /health, /chat)          │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│        LLM Router (Complexity)          │
│   • Simple queries  → Gemini            │
│   • Complex queries → Claude            │
└──────────────┬──────────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
  ┌─────────┐   ┌─────────┐
  │ Claude  │   │ Gemini  │   ← Provider Abstraction
  │Provider │   │Provider │
  └─────────┘   └─────────┘
        │             │
        └──────┬──────┘
               ▼
      ┌────────────────┐
      │ Qdrant Vector  │   ← Semantic Search
      │   Database     │
      └────────────────┘
```

### Infrastructure
```
┌──────────────────────────────────────┐
│         AWS EKS Cluster              │
│  ┌────────────┐  ┌────────────┐     │
│  │  API Pods  │  │   Qdrant   │     │
│  │  (x2)      │  │   Pod      │     │
│  └────────────┘  └────────────┘     │
│                                      │
│  ┌────────────────────────────┐     │
│  │   Monitoring Stack         │     │
│  │  • Prometheus              │     │
│  │  • Grafana                 │     │
│  └────────────────────────────┘     │
└──────────────────────────────────────┘
         │
         ▼
  Terraform-managed
  (VPC, Subnets, IAM)
```

---

## Tech Stack

**Backend & API**
- FastAPI - Async REST framework
- LangChain - LLM orchestration
- Pydantic - Data validation
- Python 3.12 - Type-safe runtime

**AI/ML**
- Claude API - Complex reasoning tasks
- Gemini API - Fast, simple queries
- Qdrant - Vector database
- LangChain Providers - Unified interface

**Infrastructure**
- Terraform - Infrastructure as Code
- Kubernetes 1.31 - Container orchestration
- Docker - Containerization
- AWS EKS - Managed Kubernetes

**CI/CD**
- GitHub Actions - Automated workflows
- GitHub Container Registry - Image storage
- GitOps - Declarative deployments

**Observability**
- Prometheus - Metrics collection
- Grafana - Visualization dashboards
- Kubernetes metrics - Cluster monitoring

**Development**
- Poetry - Dependency management
- Docker Compose - Local environment
- Git - Version control

---

## Project Structure
```
ai-agent-platform/
│
├── src/
│   ├── api/                      # FastAPI endpoints
│   │   └── main.py              # Routes: /health, /chat
│   ├── providers/               # LLM integrations
│   │   ├── claude_provider.py
│   │   ├── gemini_provider.py
│   │   └── mock_provider.py     # Demo mode
│   ├── agents/
│   │   └── router.py            # Query routing logic
│   └── utils/
│
├── terraform/
│   ├── modules/                 # Reusable IaC
│   │   ├── networking/          # VPC, subnets
│   │   └── eks/                 # Cluster, IAM, node group
│   └── environments/
│       └── dev/                 # Development config
│
├── k8s/
│   ├── base/                    # Application workloads
│   │   ├── api-deployment.yaml
│   │   └── qdrant-deployment.yaml
│   └── monitoring/              # Observability
│       ├── prometheus-config.yaml
│       └── grafana-deployment.yaml
│
├── .github/
│   └── workflows/
│       └── deploy.yml           # CI/CD pipeline
│
├── docs/
│   └── screenshots/             # Visual documentation
│
├── docker-compose.yml           # Local development
├── Dockerfile                   # Container image
├── pyproject.toml              # Python dependencies
├── .env.example                # Configuration template
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Poetry
- AWS CLI configured
- kubectl
- Terraform 1.13+

### Local Development

**1. Clone repository**
```bash
git clone https://github.com/DanielMelo1/ai-agent-platform.git
cd ai-agent-platform
```

**2. Configure environment**
```bash
cp .env.example .env
# Edit with your API keys or use demo mode
```

**3. Install dependencies**
```bash
poetry install
```

**4. Start services**
```bash
docker compose up --build
```

**5. Verify**
```bash
# Health check
curl http://localhost:8000/health

# Test chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello world"}'
```

---

## AWS Deployment

### Deploy Infrastructure
```bash
cd terraform/environments/dev

# Initialize Terraform
terraform init

# Review planned changes
terraform plan

# Deploy (~15 minutes)
terraform apply
```

**Resources created:**
- VPC with public subnets (2 AZs)
- Internet Gateway + routing
- EKS cluster (Kubernetes 1.31)
- Node group (2x t3.medium instances)
- IAM roles and policies
- Security groups

### Configure kubectl
```bash
aws eks update-kubeconfig \
  --region us-east-1 \
  --name ai-agent-cluster

# Verify connection
kubectl get nodes
```

### Deploy Application
```bash
# Deploy workloads
kubectl apply -f k8s/base/
kubectl apply -f k8s/monitoring/

# Verify pods
kubectl get pods --all-namespaces
```

### Access Application

Due to AWS LoadBalancer restrictions (see Known Limitations), use port-forward:
```bash
kubectl port-forward svc/ai-agent-api-service 8000:80

# Test (in another terminal)
curl http://localhost:8000
```

### Cleanup
```bash
# Delete Kubernetes resources
kubectl delete -f k8s/monitoring/
kubectl delete -f k8s/base/

# Destroy infrastructure
cd terraform/environments/dev
terraform destroy
```

---

## CI/CD Pipeline

### Overview

Automated continuous integration and deployment using GitHub Actions. Every push to main triggers image build, registry push, and deployment preparation.

**Status:** ![CI/CD](https://github.com/DanielMelo1/ai-agent-platform/workflows/CI%2FCD%20Pipeline/badge.svg)

### Pipeline Stages

**1. Build and Push**
- Checkout code from repository
- Login to GitHub Container Registry (ghcr.io)
- Extract metadata and generate tags
- Build Docker image from Dockerfile
- Push image with version tags

**2. Deploy Preparation**
- Update Kubernetes deployment manifests
- Tag image with commit SHA for traceability
- Display deployment instructions

### Automated Workflow

Triggers on:
- Push to `main` branch
- Pull requests to `main` branch

### Docker Image Registry

Images published to GitHub Container Registry:
```
ghcr.io/danielmelo1/ai-agent-platform:latest
ghcr.io/danielmelo1/ai-agent-platform:main-{commit-sha}
```

### Manual Deployment with CI/CD Image
```bash
# Deploy latest image to EKS
kubectl apply -f k8s/base/api-deployment.yaml

# Verify
kubectl get pods
kubectl describe deployment ai-agent-api
```

### Viewing Workflow Runs

Monitor at: https://github.com/DanielMelo1/ai-agent-platform/actions

### Benefits

- **Automation**: Eliminates manual build steps
- **Consistency**: Same process across environments
- **Traceability**: Commit SHA tagging
- **GitOps**: Version-controlled deployments
- **Reliability**: Automated validation

---

## API Usage

### Endpoints

**Health Check**
```bash
GET /health
```

**Response:**
```json
{"status": "healthy"}
```

**Chat**
```bash
POST /chat
Content-Type: application/json

{
  "query": "Explain quantum computing"
}
```

**Response:**
```json
{
  "provider": "claude",
  "complexity": "complex",
  "response": "[Mock Response] This is a simulated response...",
  "note": "Demo mode - Replace MockLLMProvider with real API keys"
}
```

### Routing Logic

| Query Length | Complexity | Provider |
|-------------|-----------|----------|
| < 15 words  | Simple    | Gemini   |
| ≥ 15 words  | Complex   | Claude   |

---

## Design Decisions

### Multi-Provider Architecture

**Problem:** Single-provider platforms create vendor lock-in and limit cost optimization

**Solution:** Provider abstraction layer enabling:
- Configuration-based provider switching
- Complexity-based routing for cost optimization
- Easy A/B testing of different models

### Kubernetes

**Rationale:**
- Auto-scaling for traffic spikes
- Self-healing via automatic restarts
- Zero-downtime rolling deployments
- Industry-standard orchestration

### Terraform

**Rationale:**
- Reproducible infrastructure
- Version-controlled infrastructure changes
- Team collaboration via code reviews
- Instant cleanup and cost control

### FastAPI

**Rationale:**
- High-performance async capabilities
- Automatic OpenAPI documentation
- Type safety with Pydantic
- Modern Python patterns

### CI/CD with GitHub Actions

**Rationale:**
- Native GitHub integration
- Free for public repositories
- Automated Docker builds
- GitOps workflow support

---

## Problems Encountered

### Issue 1: LLM API Credits

**Problem:**
- Claude API requires paid credits separate from subscription
- Gemini API model naming changed (`gemini-pro` → `gemini-1.5-flash`)

**Solution:**
- Implemented `MockLLMProvider` maintaining production architecture
- Documented demo mode clearly
- Preserved multi-provider code structure

**Lesson:** Verify API access before development; mocks enable cost-free iteration while maintaining architecture integrity

### Issue 2: Kubernetes Version Compatibility

**Problem:**
- Initial deployment used K8s 1.28
- AWS no longer supports AMIs for 1.28

**Solution:**
- Updated to Kubernetes 1.31
- Destroy and recreate cluster (EKS doesn't support multi-version jumps)

**Impact:** No functional changes, demonstrates version management

### Issue 3: Docker Compose Version Warning

**Problem:**
```
WARN: attribute `version` is obsolete
```

**Solution:**
- Removed deprecated `version` field
- Updated to Docker Compose v2 syntax

**Impact:** Cosmetic warning only

---

## Known Limitations

### AWS LoadBalancer Restriction

**Issue:**
AWS account restrictions prevented Elastic Load Balancer creation during deployment.

**Workaround:**
```bash
kubectl port-forward svc/ai-agent-api-service 8000:80
```

**Production Solution:**
AWS Load Balancer Controller with ALB/NLB

---

### Mock LLM Providers

**Current State:**
- LLM responses simulated via `MockLLMProvider`
- Claude API requires paid credits
- Gemini API integration prepared

**Enabling Real APIs:**
```bash
# Add to .env
ANTHROPIC_API_KEY=sk-ant-your-key
GOOGLE_API_KEY=AIza-your-key

# Update src/agents/router.py
from src.providers.claude_provider import ClaudeProvider
from src.providers.gemini_provider import GeminiProvider
```

---

### Basic Observability

**Current State:**
- Prometheus and Grafana deployed
- Standard Kubernetes metrics available

**Future Enhancements:**
- Token usage tracking per provider
- Cost per request dashboards
- Latency distribution by model

---

## Screenshots

Complete visual documentation in `docs/screenshots/`:

1. **01-terraform-complete-and-nodes.png** - Infrastructure provisioning + K8s nodes
2. **02-kubectl-pods-all-running.png** - All pods Running
3. **03-kubectl-port-forward-active.png** - Port-forward workaround
4. **04-curl-nginx-response.png** - Service validation
5. **05-aws-eks-cluster-overview.png** - EKS cluster Active
6. **06-aws-eks-compute-nodes.png** - Node group Ready
7. **07-github-actions-pipeline.png** - CI/CD workflow execution

---

## Author

**Daniel Melo**  
Platform Engineer | Cloud Infrastructure | AI/ML Operations

- LinkedIn: [danielaugustormelo](https://linkedin.com/in/danielaugustormelo)
- GitHub: [DanielMelo1](https://github.com/DanielMelo1)
- Portfolio: [d36ym3gb7903iq.cloudfront.net](http://d36ym3gb7903iq.cloudfront.net)

---

## License

MIT License

---

## Related Projects

- [k8s-production-platform](https://github.com/DanielMelo1/k8s-production-platform) - Foundation Kubernetes infrastructure
