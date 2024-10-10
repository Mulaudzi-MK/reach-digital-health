# Create EKS Node Group
resource "aws_eks_node_group" "example" {
  cluster_name    = aws_eks_cluster.example.name
  node_group_name = "example-node-group"
  instance_types  = "t2.medium"
  node_count      = 3
}
