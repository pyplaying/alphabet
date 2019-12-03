import turtle
import vector
import bitmap

class TurtleDraw:

    def __init__(self, font, scale=32):
        self.font = font
        self.scale = scale
        self.commands = {
            "[": turtle.pendown,
            "]": turtle.penup,
            "L": lambda: turtle.left(90),
            "R": lambda: turtle.right(90),
            "S": lambda: turtle.forward(self.scale),
            " ": lambda: None,
        }
        turtle.shape("turtle")
        turtle.penup()
        turtle.hideturtle()

    def draw_text(self, text):
        turtle.showturtle()
        for char in text:
            for c in self.font[char]:
                command = self.commands[c]
                command()
        turtle.hideturtle()
        turtle.done()

if __name__ == "__main__":
    tool = TurtleDraw(vector.font)
    tool.draw_text("ABC")
