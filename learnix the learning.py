import pygame
import sys

# Sozlamalar
pygame.init()
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learnix: Robo-Pet Edition")

# Ranglar
WHITE, BG, GREEN, RED, BLUE = (255, 255, 255), (240, 244, 247), (88, 204, 2), (255, 75, 75), (28, 176, 246)
TEXT_COLOR = (75, 75, 75)

# Shriftlar
font_md = pygame.font.SysFont("Segoe UI", 26, bold=True)
font_sm = pygame.font.SysFont("Segoe UI", 20)

# Petni yuklash (Rasm bo'lmasa, doira chizib turadi)
try:
    pet_image = pygame.image.load("pet.png")
    pet_image = pygame.transform.scale(pet_image, (150, 150))
except:
    pet_image = None

def draw_text(text, pos, color=TEXT_COLOR, bold=False):
    f = font_md if bold else font_sm
    img = f.render(text, True, color)
    screen.blit(img, pos)

def run_app():
    clock = pygame.time.Clock()
    state = "NAME" # NAME, GOAL, MAP, QUIZ, RESULT
    user_name = ""
    user_goal = ""
    health = 5
    score = 0
    total_q = 4 # Har bosqichda 4 ta savol
    cur_q_idx = 0
    pet_mood = "HAPPY" # HAPPY, SAD

    # Savollar (Ko'paytirildi)
    questions = [
        {"q": "Python nima?", "o": ["Til", "O'yin", "Ilon"], "c": 0},
        {"q": "Ekranga chiqarish?", "o": ["input", "print", "write"], "c": 1},
        {"q": "Sonli tur?", "o": ["string", "integer", "boolean"], "c": 1},
        {"q": "Izoh qoldirish?", "o": ["//", "/*", "#"], "c": 2}
    ]

    while True:
        m_pos = pygame.mouse.get_pos()
        screen.fill(BG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if state == "NAME":
                    if event.key == pygame.K_RETURN and len(user_name) > 1: state = "GOAL"
                    elif event.key == pygame.K_BACKSPACE: user_name = user_name[:-1]
                    else: user_name += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == "GOAL":
                    # Maqsadni tanlash (Soddalashtirildi)
                    if pygame.Rect(300, 250, 300, 50).collidepoint(m_pos):
                        user_goal = "Dasturchi bo'lish"; state = "MAP"
                
                elif state == "MAP":
                    if health > 0: state = "QUIZ"
                
                elif state == "QUIZ":
                    for i in range(3):
                        if pygame.Rect(100, 250 + i*70, 400, 50).collidepoint(m_pos):
                            if i == questions[cur_q_idx]["c"]:
                                score += 1
                            else:
                                health -= 1 # Xato qilsa quvvat ketadi
                            
                            if cur_q_idx < total_q - 1:
                                cur_q_idx += 1
                            else:
                                # Natijani hisoblash (75% = 3 ta to'g'ri)
                                percentage = (score / total_q) * 100
                                pet_mood = "HAPPY" if percentage >= 75 else "SAD"
                                state = "RESULT"

        # --- CHIZISH ---
        # Petni ko'rsatish
        pet_pos = (650, 150)
        if pet_image:
            screen.blit(pet_image, pet_pos)
        else:
            pygame.draw.circle(screen, BLUE, (750, 250), 50)

        # Holatga qarab Robo-Learnix gapi
        if state == "NAME":
            draw_text("Salom! Men Learnix-man. Isming nima?", (100, 150), bold=True)
            pygame.draw.rect(screen, WHITE, (100, 200, 300, 50), border_radius=10)
            draw_text(user_name + "|", (110, 210), BLUE)

        elif state == "MAP":
            # Quvvat bari
            draw_text(f"Quvvat: {'❤️' * health}", (20, 20), RED)
            draw_text(f"O'quvchi: {user_name}", (20, 60), bold=True)
            pygame.draw.circle(screen, GREEN, (450, 350), 60) # Start tugmasi
            draw_text("BOSHLASH", (400, 340), WHITE, True)

        elif state == "QUIZ":
            q = questions[cur_q_idx]
            draw_text(f"Savol {cur_q_idx+1}/{total_q}", (100, 100), BLUE)
            draw_text(q["q"], (100, 160), bold=True)
            for i, opt in enumerate(q["o"]):
                r = pygame.Rect(100, 250 + i*70, 400, 50)
                pygame.draw.rect(screen, WHITE, r, border_radius=15)
                draw_text(opt, (120, 260 + i*70))

        elif state == "RESULT":
            if pet_mood == "HAPPY":
                draw_text("URRA! Sen 75% dan ko'p topding!", (150, 250), GREEN, True)
                draw_text("Robo-Learnix juda hursand! 😊", (150, 300))
            else:
                draw_text("AFSUS... Natija past.", (150, 250), RED, True)
                draw_text("Robo-Learnix xafa bo'ldi. 😟", (150, 300))
            
            draw_text(f"To'g'ri javoblar: {score}/{total_q}", (150, 350))

        pygame.display.flip()
        clock.tick(60)

run_app()
