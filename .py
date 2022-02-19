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
ball = GameSprite(("ball.jpg"),400,win_height - 90,60,90,7)


speed_x = 3
speed_y = 3
font.init()
font1 = font.Font(None,35)
lose1 = font1.render('MAEG 1 LOSE!',True,(180,0,0))

font1 = font.Font(None,35)
lose1 = font1.render('leon 1 LOSE!',True,(180,0,0))
    

while game:
    window.blit(background,(0,0))
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > 420 or ball.rect.y < 0:
                speed_y *= -1
        if sprite.collide_rect(meg,ball) or sprite.collide_rect(leon,ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True 
            window.blit(lose1,(200,200))

        if ball.rect.x > 700:
            finish = True 
            window.blit(lose1,(200,200))
    
        
        # обновляем фон
        
        meg.reset()
        meg.update()
        leon.reset()
        leon.update()
        ball.reset()
       
        
        display.update()
    # цикл срабатывает каждую 0.05 секунд
    clock.tick(fps)





