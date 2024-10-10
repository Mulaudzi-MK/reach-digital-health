terraform
# Configure AWS Provider
provider "aws" {
  region = "us-west-2"
}

# Create EKS Cluster
resource "aws_eks_cluster" "example" {
  name     = "example-cluster"
  role_arn = aws_iam_role.example.arn
}

# Create EKS Node Group
resource "aws_eks_node_group" "example" {
  cluster_name    = aws_eks_cluster.example.name
  node_group_name = "example-node-group"
  instance_types  = ["t2.medium"]
  node_count      = 3
}

# Create IAM Role for EKS
resource "aws_iam_role" "example" {
  name        = "example-eks-role"
  description = "EKS Cluster Role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Principal = {
          Service = "(link unavailable)"
        }
        Effect = "Allow"
      }
    ]
  })
}
