import vlc
import time

player = vlc.MediaPlayer()
player.set_mrl('')  # file path

player.play()
time.sleep(60)
player.stop()
