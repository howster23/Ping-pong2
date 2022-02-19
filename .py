from pygame import *
win_width = 700
win_height = 500
display.set_caption("Ping pong")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load("fon.jpg"),(win_width, win_height))
finish = False

game = True # флаг сбрасывается кнопкой закрытия окна
clock = time.Clock()
fps = 55
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Lol(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

meg = Player(("meg.png"),5,win_height - 100,80,100,10)
leon = Lol(("leon.png"),600,win_height - 100,80,100,10)
ball = Player(("ball.jpg"),400,win_height - 90,60,90,7)

while game:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        # обновляем фон
        window.blit(background,(0,0))
        meg.reset()
        meg.update()
        leon.reset()
        leon.update()
        ball.reset()
       
        
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    clock.tick(fps)





