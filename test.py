
import sys, argparse, logging

import os
from os import listdir
from os.path import isfile, join

import subprocess

omx_command = ['omxplayer', "-o", "hdmi", "-b"]

def getFullPath(filename):
    return BASE_DIR + '/videos/' + filename

playlist = [getFullPath('dog.mp4'),getFullPath('dog2.mp4')]

# def generatePlaylist(inpath):
#     return [f for f in listdir(inpath) if isfile(join(inpath, f))]

def main(args, loglevel):
    logging.basicConfig(format="%(levelname)s: %(message)s", level=loglevel)

    #[omx_command.append(f) for f in args.remaining] # add extra OMX commands to end, sort of janky
    # playlist = generatePlaylist(args.directory)

    for f in playlist:
        full_path = args.directory + "/" + f
        full_command = omx_command + args.remaining + [full_path]

        stdout = subprocess.PIPE
        if args.debug:
            stdout = False

        proc = None
        try:
            logging.debug("playing: {0}".format(full_path))
            proc = subprocess.run(full_command, check=True, stdin=subprocess.PIPE, stdout=stdout, close_fds=True)
        except KeyboardInterrupt:
            if proc is not None:
                proc.kill()
            logging.info("Keyboard Interrupt")
            sys.exit()
        except Exception as e:
            logging.exception()

