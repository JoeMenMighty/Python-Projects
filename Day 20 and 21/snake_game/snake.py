from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake(self):
        start_position = 0
        for _ in range(3):
            mighty = self.create_segment(start_position, 0)
            start_position -= 20
            self.snake.append(mighty)

    def create_segment(self, start_position, y_position):
        mighty_turtle = Turtle('square')
        mighty_turtle.color('white')
        mighty_turtle.penup()
        mighty_turtle.goto(x=start_position, y=y_position)
        return mighty_turtle

    def reset(self):
        for _ in self.snake:
            _.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.snake_head = self.snake[0]

    def extend_snake(self):
        x_place = self.snake[-1].xcor()
        y_place = self.snake[-1].ycor()
        new_segment = self.create_segment(x_place, y_place)
        self.snake.append(new_segment)

    def move(self):
        for m_turtle_pos in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[m_turtle_pos - 1].xcor()
            new_y = self.snake[m_turtle_pos - 1].ycor()
            self.snake[m_turtle_pos].goto(x=new_x, y=new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
