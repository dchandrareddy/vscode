resource "aws_instance" "albcricket" {
  ami           = "ami-052cef05d01020f1d"
  instance_type = "t2.micro"
  key_name = "ntr"
  vpc_security_group_ids = [aws_security_group.ec24_sg.id]
  user_data = <<EOF
             #!/bin/bash
             yum update -y
             yum install httpd -y 
             systemctl enable httpd
             systemctl start httpd
             mkdir -p  /var/www/html/cricket/
             echo "this is cricket" >/var/www/html/cricket/index.html
       EOF

  tags = {
    Name = "albcricket"
  }
}