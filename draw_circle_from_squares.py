import turtle

def draw_sq():
	window = turtle.Screen()
	window.bgcolor("red")
	i = 0
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("blue")
	brad.speed(3)
	while i<100:
	 brad.right(i*6)
	 brad.forward(100)
	 brad.right(90)
	 brad.forward(100)
	 brad.right(90)
	 brad.forward(100)
	 brad.right(90)
	 brad.forward(100)
	 brad.right(90)
	 i = i+1


draw_sq()
	

window.exitonclick()