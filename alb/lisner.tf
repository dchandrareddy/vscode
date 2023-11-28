# for default listener

resource "aws_lb_listener" "l-1" {
  load_balancer_arn = aws_lb.alb-1.arn
  port              = "80"
  protocol          = "HTTP"
  # ssl_policy        = "ELBSecurityPolicy-2016-08"
  # certificate_arn   = "arn:aws:iam::187416307283:server-certificate/test_cert_rab3wuqwgja25ct3n4jdj2tzu4"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.alb-tg1.arn
  }
}


# for listener rule 1

resource "aws_lb_listener_rule" "lr1" {
  listener_arn = aws_lb_listener.l-1.arn
  # priority     = 100

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.alb-tg1.arn
  }

  condition {
    path_pattern {
      values = ["/cricket/*"]
    }
  }
}

# for listener rule 2

resource "aws_lb_listener_rule" "lr2" {
  listener_arn = aws_lb_listener.l-1.arn
  # priority     = 100

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.alb-tg2.arn
  }

  condition {
    path_pattern {
      values = ["/football/*"]
    }
  }
}

