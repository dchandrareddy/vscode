resource "aws_security_group" "al-sg" {
  name        = "al-sg"
  description = "Allow end user"
  vpc_id      = "vpc-015e7f08cb53238e7"

  ingress {
    description      = "any where"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
   # ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "al-sg"
  }
}