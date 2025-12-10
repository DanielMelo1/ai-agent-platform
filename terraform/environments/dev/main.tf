terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "networking" {
  source       = "../../modules/networking"
  project_name = "ai-agent-platform"
}

module "eks" {
  source       = "../../modules/eks"
  cluster_name = "ai-agent-cluster"
  subnet_ids   = module.networking.subnet_ids
}

output "cluster_name" {
  value = module.eks.cluster_name
}

output "cluster_endpoint" {
  value = module.eks.cluster_endpoint
}
