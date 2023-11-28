resource "aws_security_group" "ec24_sg" {
  name        = "ec24_sg"
  description = "Allow TLS inbound traffic"
  vpc_id      = "vpc-015e7f08cb53238e7"

  ingress {
    description      = "alb ip"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    security_groups  = [aws_security_group.al-sg.id]
  }
    ingress {
    description      = "my vpn ip"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["103.110.170.86/32"]
    }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
   
  }

  tags = {
    Name = "ec24_sg"
  }
}