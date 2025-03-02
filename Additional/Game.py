import pygame
import sys

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cyberguy")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Ustawienia piłki
ball_radius = 15
ball_speed = [4, 4]
ball_pos = [WIDTH // 2, HEIGHT // 2]
speed_multiplier = 1.1  # Przyspieszenie piłki po odbiciu
max_speed = 10  # Maksymalna prędkość piłki

# Ustawienia graczy
paddle_width, paddle_height = 20, 100
player1_pos = [30, HEIGHT // 2 - paddle_height // 2]
player2_pos = [WIDTH - 50, HEIGHT // 2 - paddle_height // 2]
paddle_speed = 6

# Punkty graczy
score1, score2 = 0, 0
max_score = 10  # Liczba punktów do wygranej
font = pygame.font.Font(None, 74)
game_over = False  # Flaga końca gry

# Główna pętla gry
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    if game_over:
        # Wyświetlenie napisu GAME OVER
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))

        # Wyświetlenie wyniku końcowego
        winner_text = font.render(f"{score1} : {score2}", True, WHITE)
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()
        pygame.time.delay(3000)  # Pauza na 3 sekundy przed zamknięciem
        break

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ruch graczy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player1_pos[1] < HEIGHT - paddle_height:
        player1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - paddle_height:
        player2_pos[1] += paddle_speed

    # Ruch piłki
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Odbicia od ścian
    if ball_pos[1] <= ball_radius or ball_pos[1] >= HEIGHT - ball_radius:
        ball_speed[1] = -ball_speed[1]

    # Kolizje z paletkami
    def limit_speed(speed):
        """Ogranicza prędkość piłki do wartości max_speed"""
        if speed > 0:
            return min(speed, max_speed)
        else:
            return max(speed, -max_speed)

    if (player1_pos[0] < ball_pos[0] < player1_pos[0] + paddle_width and
            player1_pos[1] < ball_pos[1] < player1_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0] * speed_multiplier
        ball_speed[1] = ball_speed[1] * speed_multiplier
        ball_speed[0] = limit_speed(ball_speed[0])
        ball_speed[1] = limit_speed(ball_speed[1])

    if (player2_pos[0] < ball_pos[0] < player2_pos[0] + paddle_width and
            player2_pos[1] < ball_pos[1] < player2_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0] * speed_multiplier
        ball_speed[1] = ball_speed[1] * speed_multiplier
        ball_speed[0] = limit_speed(ball_speed[0])
        ball_speed[1] = limit_speed(ball_speed[1])

    # Punktacja i reset piłki
    if ball_pos[0] <= 0:
        score2 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [4, 4]

    if ball_pos[0] >= WIDTH:
        score1 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [-4, -4]

    # Sprawdzenie, czy ktoś wygrał
    if score1 >= max_score or score2 >= max_score:
        game_over = True

    # Rysowanie elementów gry
    pygame.draw.circle(screen, WHITE, ball_pos, ball_radius)
    pygame.draw.rect(screen, BLUE, (*player1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, RED, (*player2_pos, paddle_width, paddle_height))

    # Wyświetlanie punktów
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Aktualizacja ekranu i ograniczenie FPS
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
