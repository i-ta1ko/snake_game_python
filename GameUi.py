from tkinter import Tk, Canvas, Button
from SnakeModel import SnakeModel

def key_pressed(e):
    if model.lives > 0: 
        key = e.keysym
        if key == "Down":
            model.move_down()
        elif key == "Up":
            model.move_up()
        elif key == "Left":
            model.move_left()
        elif key == "Right":
            model.move_right()
        canvas.delete("all")
        display_snake()
        canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")


def display_snake():
    for bp in model.body:
        canvas.create_rectangle(bp[0], bp[1], bp[0] + 10, bp[1] + 10, fill="green")

def reset():
    model.lives = 5
    model.body = [
            [200, 200],
            [200, 210],
            [200, 220],
            [200, 230]
                 ]
    model.direction = "Up"
    model.set_fruit_position()
    canvas.delete("all")
    display_snake()
    canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")
        

window = Tk()
model = SnakeModel()

canvas = Canvas(window, bg="white", width=400, height=400)
canvas.grid(row=0, column=0)
restart = Button(window, text ="PLAY AGAIN", command=reset)
restart.grid(row=1, column=0)

display_snake()
canvas.create_rectangle(model.fruit[0], model.fruit[1], model.fruit[0] + 10, model.fruit[1] + 10, fill="red")
window.bind('<KeyRelease>', key_pressed)

window.mainloop()