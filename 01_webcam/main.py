import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()
cameras = pygame.camera.list_cameras()
print(cameras)
webcam = pygame.camera.Camera(cameras[0], (32,24))
webcam.start()
screen = pygame.display.set_mode((320,240), 0)


while True:
    stream = webcam.get_image()
    stream = pygame.transform.scale(stream, (320,240))
    screen.blit(stream, (0,0))
    pygame.display.update()