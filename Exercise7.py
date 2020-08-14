import pygame
import datetime
import time

def musiconloop(file, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            pygame.mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()
    watersecs = 5
    exsecs = 10
    eyessecs = 20

    while True:
        if time.time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time.time()
            log_now("Drank Water at")

        if time.time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time.time()
            log_now("Eyes Relaxed at")

        if time.time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('exercise.mp3.mp3', 'donephy')
            init_exercise = time.time()
            log_now("Physical Activity done at")




