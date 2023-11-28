resource "aws_instance" "albfootball" {
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
             mkdir -p  /var/www/html/football/
             echo "this is football" >/var/www/html/football/index.html
       EOF

  tags = {
    Name = "albfootball"
  }
}