from pygame import *
win_width = 700
win_height = 500
display.set_caption("Ping pong")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load("fon.jpg"),(win_width, win_height))
finish = False
# Основной цикл игры:
game = True # флаг сбрасывается кнопкой закрытия окна
while game:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False
        

 
    if finish != True:
        # обновляем фон
        window.blit(background,(0,0))
        
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)





