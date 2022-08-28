
import sys, argparse, logging

import os
from os import listdir
from os.path import isfile, join

import subprocess

import pygame

os.environ["DISPLAY"] = ":0"
pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.NOFRAME)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

omx_command = ['omxplayer', "-o", "hdmi", "-b"]

def getFullPath(filename):
    return BASE_DIR + '/videos/' + filename

playlist = [getFullPath('dog.mp4'),getFullPath('dog2.mp4')]

# def generatePlaylist(inpath):
#     return [f for f in listdir(inpath) if isfile(join(inpath, f))]
# def main():
    
def main():
    # for f in playlist:
    #     full_command = omx_command +  [f]
    #     stdout = subprocess.PIPE
    #     proc = None
    #     try:
    #         # logging.debug("playing: {0}".format(full_path))
    #         print(f'playing: {f}')
    #         proc = subprocess.run(full_command, check=True, stdin=subprocess.PIPE, stdout=stdout, close_fds=True)
    #     except KeyboardInterrupt:
    #         if proc is not None:
    #             proc.kill()
    #         # logging.info("Keyboard Interrupt")
    #         sys.exit()
    #     except Exception as e:
    #         # logging.exception()

        for f in playlist:
            full_command = omx_command + [f]
            sys.stdout = subprocess.PIPE 
            proc = None 
            try:
                proc = subprocess.run(full_command,check=True,stdin=subprocess.PIPE,stdout=sys.stdout,close_fds=True)
            except KeyboardInterrupt:
                if proc is not None:
                    proc.kill() 
                sys.exit()
            except Exception as e:
                print(e)



running = True

while running:
    main()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: 
                running = False

pygame.quit()



