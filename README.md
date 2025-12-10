# AI Agent Platform

![Terraform](https://img.shields.io/badge/Terraform-1.13-7B42BC?logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28-326CE5?logo=kubernetes&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EKS-FF9900?logo=amazon-aws&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3-1C3C3C?logo=chainlink&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-latest-2496ED?logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-latest-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-latest-F46800?logo=grafana&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

> Enterprise-grade AI orchestration platform with multi-provider LLM support, intelligent routing, Kubernetes deployment, and complete observability stack.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [API Usage](#api-usage)
- [Design Decisions](#design-decisions)
- [Problems Encountered](#problems-encountered)
- [Known Limitations](#known-limitations)

---

## Overview

Production-ready platform for deploying and managing AI agents with:

- **Multi-provider LLM architecture**: Vendor-agnostic design supporting Claude and Gemini
- **Intelligent query routing**: Complexity-based provider selection
- **Kubernetes orchestration**: Scalable, self-healing infrastructure
- **Vector database**: Qdrant integration for semantic search
- **Full observability**: Prometheus + Grafana monitoring stack
- **Infrastructure as Code**: Terraform-managed AWS EKS deployment

### Value Proposition

Unlike single-provider AI platforms, this architecture enables:
- Zero vendor lock-in (switch providers via configuration)
- Cost optimization through intelligent routing
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
- Claude API - Complex reasoning
- Gemini API - Fast queries
- Qdrant - Vector database
- LangChain Providers - Unified interface

**Infrastructure**
- Terraform - Infrastructure as Code
- Kubernetes 1.28 - Container orchestration
- Docker - Containerization
- AWS EKS - Managed Kubernetes

**Observability**
- Prometheus - Metrics collection
- Grafana - Dashboards
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
│   │   └── eks/                 # Cluster, IAM
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
├── docker-compose.yml           # Local development
├── Dockerfile                   # Container image
├── pyproject.toml              # Dependencies
├── .env.example                # Configuration template
└── README.md                   
```

---

## Getting Started

### Prerequisites

- Python 3.12+
- Docker & Docker Compose
- Poetry
- AWS CLI
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
  -d '{"query": "Hello"}'
```

**6. API documentation**
```
http://localhost:8000/docs
```

---

## AWS Deployment

### Deploy Infrastructure
```bash
cd terraform/environments/dev
terraform init
terraform plan
terraform apply  # ~15 minutes
```

**Resources created:**
- VPC with public subnets (2 AZs)
- Internet Gateway + routing
- EKS cluster (Kubernetes 1.28)
- IAM roles and policies
- Security groups

### Configure kubectl
```bash
aws eks update-kubeconfig \
  --region us-east-1 \
  --name ai-agent-cluster
```

### Deploy Application
```bash
kubectl apply -f k8s/base/
kubectl apply -f k8s/monitoring/

# Verify
kubectl get pods
```

### Access API
```bash
kubectl get svc ai-agent-api-service
# Use LoadBalancer URL to access API
```

### Cleanup
```bash
kubectl delete -f k8s/monitoring/
kubectl delete -f k8s/base/

cd terraform/environments/dev
terraform destroy
```

---

## API Usage

### Health Check
```bash
GET /health
```
**Response:**
```json
{"status": "healthy"}
```

### Chat
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
  "response": "[Claude Response] ...",
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

**Problem:** Vendor lock-in limits flexibility and cost optimization

**Solution:** Provider abstraction layer
- Switch providers via configuration
- Route based on complexity/cost
- A/B test models easily

### Kubernetes

**Why:**
- Auto-scaling for traffic spikes
- Self-healing (automatic restarts)
- Zero-downtime deployments
- Industry-standard orchestration

### Terraform

**Why:**
- Reproducible infrastructure
- Version-controlled changes
- Team collaboration
- Instant resource cleanup

### FastAPI

**Why:**
- Async performance
- Automatic OpenAPI docs
- Type safety with Pydantic
- Modern Python patterns

---

## Problems Encountered

### Issue 1: LLM API Credits

**Problem:**
- Claude API requires separate paid credits
- Gemini model name changed (`gemini-pro` → `gemini-1.5-flash`)

**Solution:**
- Implemented `MockLLMProvider` for demo
- Maintained production-ready architecture
- Clear documentation of demo mode

**Lesson:** Verify API access before development; mocks enable cost-free iteration

### Issue 2: Docker Compose Version Warning

**Problem:**
```
WARN: attribute `version` is obsolete
```

**Solution:**
- Removed deprecated `version` field
- Updated to Docker Compose v2 syntax

**Impact:** Cosmetic only

### Issue 3: Terraform Module Dependencies

**Problem:**
- EKS requires VPC/subnets first

**Solution:**
- Modular Terraform design
- Explicit `depends_on` where needed
- Clear module outputs/inputs

---

## Known Limitations

**Current Implementation:**

1. **Mock LLM Providers**
   - Why: API credits required
   - Impact: Simulated responses only
   - Solution: Add real API keys to enable production mode

2. **Basic Observability**
   - Current: Prometheus/Grafana deployed
   - Missing: Custom LLM metrics (tokens, latency)

3. **Simplified RAG**
   - Current: Qdrant deployed
   - Missing: Document ingestion pipeline

**Production Considerations:**

- No HTTPS (add ALB + ACM)
- No authentication (implement API keys)
- No rate limiting
- Single-region deployment

---

## Author

**Daniel Melo**  
Platform Engineer | Cloud Infrastructure | AI/ML Operations

LinkedIn: [danielaugustormelo](https://linkedin.com/in/danielaugustormelo)  
GitHub: [DanielMelo1](https://github.com/DanielMelo1) 



---

## License

MIT License - See LICENSE file

---

**Related Projects:**
- [k8s-production-platform](https://github.com/DanielMelo1/k8s-production-platform) - Foundation Kubernetes infrastructure
EOF