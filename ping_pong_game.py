import turtle

#Определение окна программы
window = turtle.Screen()		
window.title('Rocket-Ping Pong Game by pyMa!')
window.setup(width=600, height=600)
window.bgcolor('black')	
window.bgpic('bg.gif')

#Опредление границ игового поля 
borders = turtle.Turtle()
borders.pencolor('lightblue')
borders.speed(0)
borders.pensize(1)
borders.ht()
borders.up()
borders.goto(250, 250)
borders.down()
for x in range(4):
	borders.rt(90), borders.fd(500)

#Опредление объекта счета партии
score = turtle.Turtle()
score.speed(-1)
score.up()
score.pensize(1)
score.pencolor('white')
score.ht()
score.goto(0, 260)
sc = 0
score.write('SCORE : ', True, align = 'center', font = ('Calibri Bold', 20, 'normal'))

#Определение игровой ракетки
rocket = turtle.Turtle(shape = 'square')
rocket.color('black', 'white')
rocket.speed(-1)
rocket.up()
rocket.setpos(0, -200)
rocket.shapesize(stretch_wid = 0.5, stretch_len = 2, outline = 1)  #1 = 20 пикселей 

#Определение игрового мяча
ball = turtle.Turtle(shape = 'circle')
ball.color('black', 'red')
ball.speed(0)
ball.shapesize(1, 1, 1)

#Определение скоросити движения мяча по координатам Y и X
ball.speedY = 8
ball.speedX = 1

#Функции джвижения иговой ракетки
def moveRight(): # функция движения вправо
	rocket.fd(10)
	if rocket.xcor() >= 240:
		rocket.fd(-10)

def moveLeft(): # функция движения влево
	rocket.fd(-10)
	if rocket.xcor() <= -240:
		rocket.fd(10)

#Вызов функций двиения ракетки и опредлениея клавиш движения
window.listen()
window.onkeypress(moveRight, key='Right') #стрелка вправо
window.onkeypress(moveLeft, key='Left') #стрелка влево

#Цикл, который запускает игру
while True:
	window.update()
	window.delay(1)
	
	ball.up()
	#Определение координат-перемещния мяча
	ball.goto(ball.xcor() + ball.speedX, ball.ycor() + ball.speedY)
	
	#Условие столкновения мяча с верхней границей по оси Y
	if ball.ycor() > 240:
		ball.speedY = -ball.speedY
	
	#Условие столкновения мяча с нижней границей по оси Y, если мячь попадает на нижнию границу, то игра останавливается
	if ball.ycor() < -240:
		text = turtle.Turtle()
		text.ht()
		text.pencolor("black")
		text.write('GAME OVER', align = 'center', font = ('Calibri Bold', 60, 'normal'))
		text.pencolor('lightblue')
		text.write('GAME OVER', align = 'center', font = ('Calibri Bold', 58, 'normal'))
		break

	#Условие столкновения мяча с правой и левой границей по оси X
	if ball.xcor() >= 240 or ball.xcor() <= -240:
		ball.speedX = -ball.speedX

	#Условие столкновения мяча с ракеткой
	if (ball.ycor() < rocket.ycor() + 7 and ball.ycor() > rocket.ycor() -7) and (ball.xcor() < rocket.xcor() + 25 and ball.xcor() > rocket.xcor() - 25):
	# if ball.ycor() < -190  and (ball.xcor() < rocket.xcor() + 20 and ball.xcor() > rocket.xcor() - 20): - второе решение
		ball.speedY = -ball.speedY
		#Начисление баллов за отбив мяча
		sc += 1
		score.undo()
		score.write('SCORE : %s' % (sc), True, align = 'center', font = ('Calibri Bold', 20, 'normal'))
	
window.mainloop()