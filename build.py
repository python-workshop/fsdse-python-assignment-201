#Draw a line
import turtle
def draw_line(t, sz):
        t.forward(sz)
        return True

wn = turtle.Screen()
wn.title("Draw a Line")
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
draw_line(alex, 100)
wn.mainloop()
