from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_pieces = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_piece(position)
            self.head = self.body_pieces[0]


    def move(self):
        for body_num in range(len(self.body_pieces) - 1, 0, -1):
            new_x = self.body_pieces[body_num-1].xcor()
            new_y = self.body_pieces[body_num - 1].ycor()
            self.body_pieces[body_num].goto(new_x, new_y)
        self.body_pieces[0].forward(MOVE_DISTANCE)

    def add_body_piece(self, position):
        body = Turtle(shape="square")
        body.color('white')
        body.pu()
        body.goto(position)
        self.body_pieces.append(body)

    def reset(self):
        for bodies in self.body_pieces:
            bodies.goto(1000, 1000)
        self.body_pieces.clear()
        self.create_snake()
        self.head = self.body_pieces[0]

    def extend(self):
        self.add_body_piece(self.body_pieces[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
