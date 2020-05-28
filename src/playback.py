import vlc
import time


def play():
    player = vlc.MediaPlayer()
    player.set_mrl('')  # file path

    player.play()
    time.sleep(60)
    player.stop()
