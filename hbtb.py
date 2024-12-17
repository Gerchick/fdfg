import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Параметры окна
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Forza Horizon 6")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Загрузка изображений
car_image = pygame.image.load("car.png").convert_alpha()  # Убедитесь, что файл car.png существует
car_image = pygame.transform.scale(car_image, (60, 100)) # Масштабирование изображения машины
game_over_image = pygame.image.load("game_over.png").convert_alpha() # Убедитесь, что файл game_over.png существует
game_over_image = pygame.transform.scale(game_over_image, (400, 300)) # Масштабирование изображения Game Over

# Автомобиль
car_x = 350
car_y = 500
car_width = 60
car_height = 120
car_speed = 10

# Препятствия
obstacle_width = 50
obstacle_height = 50
obstacles = []
for i in range(5):
    obstacles.append([random.randint(50, width - obstacle_width - 50), -i * 100 - 50, obstacle_width, obstacle_height])

# Счетчик очков и времени
score = 0
start_time = time.time()

# Шрифт
font = pygame.font.Font(None, 36)

# Цикл игры
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление автомобилем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < width - car_width:
        car_x += car_speed

    # Движение препятствий
    for obstacle in obstacles:
        obstacle[1] += 5
        if obstacle[1] > height:
            obstacle[1] = -obstacle_height
            obstacle[0] = random.randint(50, width - obstacle_width - 50)
            score += 10 # Добавляем очки за прошедшее препятствие


    # Проверка столкновений
    for obstacle in obstacles:
        if car_x < obstacle[0] + obstacle_width and \
           car_x + car_width > obstacle[0] and \
           car_y < obstacle[1] + obstacle_height and \
           car_y + car_height > obstacle[1]:
            running = False
            break

    # Отрисовка
    screen.fill(white)
    screen.blit(car_image, (car_x, car_y)) # Отрисовка изображения машины
    for obstacle in obstacles:
        pygame.draw.rect(screen, black, obstacle)

    # Отображение счета и времени
    elapsed_time = int(time.time() - start_time)
    score_text = font.render(f"Счет: {score}  Время: {elapsed_time}", True, black)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

# Экран Game Over
screen.fill(white)
screen.blit(game_over_image, (width//2 - game_over_image.get_width()//2, height//2 - game_over_image.get_height()//2))
score_text = font.render(f"Ваш счет: {score}", True, black)
screen.blit(score_text,(width//2 - score_text.get_width()//2, height//2 + game_over_image.get_height()//2 + 20))
pygame.display.update()
time.sleep(3) # Экран Game Over показывается 3 секунды

pygame.quit()


