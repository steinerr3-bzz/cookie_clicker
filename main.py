import turtle

wn = turtle.Screen()
wn.title('Cookie Clicker Spiel')
wn.bgcolor('black')

wn.register_shape('cookie.gif')
wn.register_shape('oma.gif')

cookie = turtle.Turtle()
cookie.shape('cookie.gif')
cookie.speed(0)

oma = turtle.Turtle()
oma.shape('oma.gif')
oma.speed(0)
oma.penup()
oma.setpos(150, -150)


cookies = 0
auto_clickers = 0
auto_clickers_cost = 50

pen = turtle.Turtle()
pen.hideturtle()
pen.color('white')
pen.penup()
pen.goto(0, 200)
pen.write(f'Cookies: {cookies}', align='center', font=('Arial', 32, 'normal'))

def clicked(x, y):
    global cookies
    cookies += 1
    update_display()

def update_display():
    pen.clear()
    pen.write(f'Cookies: {cookies}', align='center', font=('Arial', 32, 'normal'))

cookie.onclick(clicked)

def buy_auto_clicker(x, y):
    global cookies, auto_clickers, auto_clickers_cost
    if cookies >= auto_clickers_cost:
        cookies -= auto_clickers_cost
        auto_clickers += 1
        update_display()

def update_game_state():
    global cookies, auto_clickers
    cookies += auto_clickers
    update_display()
    wn.ontimer(update_game_state, 1000)

wn.tracer(0)
update_game_state()

oma.onclick(buy_auto_clicker)

wn.update()
wn.mainloop()
