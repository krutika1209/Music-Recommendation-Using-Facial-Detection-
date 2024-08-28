import os
import random
import pygame

directory = 'C:\\Users\\korde\\OneDrive\\Desktop\\sem6_project\\Song-Recommendation-using-Facial-Emotion-Recognition-main\\musics\\Neutral'
play_list = [f for f in os.listdir(directory) if f.endswith('.mp3')]
print(play_list)
current_list = []

pygame.init()
window = pygame.display.set_mode((1000, 500))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

window_center = window.get_rect().center
title_surf = None

run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if not pygame.mixer.music.get_busy():
        if not current_list:
           current_list = play_list[:]
           random.shuffle(current_list)
        current_song = current_list.pop(0)
        pygame.mixer.music.load(os.path.join(directory, current_song))
        pygame.mixer.music.play()
        title_surf = font.render(current_song, True, (255, 255, 0))

    window.fill(0)
    if title_surf:
        window.blit(title_surf, title_surf.get_rect(center = window_center))
    pygame.display.flip()
    
pygame.quit()
exit()