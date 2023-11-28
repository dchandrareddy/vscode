resource "aws_lb" "alb-1" {
  name               = "alb-1"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.al-sg.id]
  subnets            = ["subnet-03c74f81f64b7be6a","subnet-063495464902ee319"]

  # enable_deletion_protection = true

  tags = {
    Name = "alb-1"
  }
}