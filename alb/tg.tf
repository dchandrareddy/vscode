# for target group 1

resource "aws_lb_target_group" "alb-tg1" {
  name     = "alb-tg1"
  port     = 80
  protocol = "HTTP"
  vpc_id   ="vpc-015e7f08cb53238e7"
}

# for target group 2
resource "aws_lb_target_group" "alb-tg2" {
  name     = "alb-tg2"
  port     = 80
  protocol = "HTTP"
  vpc_id   = "vpc-015e7f08cb53238e7"
}


resource "aws_lb_target_group_attachment" "attach-1" {
  target_group_arn = aws_lb_target_group.alb-tg1.arn
  target_id        = aws_instance.albcricket.id
  port             = 80
}

resource "aws_lb_target_group_attachment" "attach-2" {
  target_group_arn = aws_lb_target_group.alb-tg2.arn
  target_id        = aws_instance.albfootball.id
  port             = 80
}


