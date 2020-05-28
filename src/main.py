import pyaudio
import numpy as np
from . import playback
# import wave
# from datetime import datetime

# 音データフォーマット
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

# 閾値
threshold = 0.01

# 音の取り込み
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=chunk
                    )

cnt = 0

while True:
    # 音データの取得
    data = stream.read(chunk)
    # ndarrayに変換
    x = np.frombuffer(data, dtype="int16") / 32768.0

    # 閾値以上の場合、音楽を再生する
    if x.max() > threshold:
        playback.play()
        cnt += 1

    # 3回検出したら終了
    if cnt > 3:
        break

    '''
    # 閾値以上場合はファイル保存
    if x.max() > threshold:
        filename = datetime.today().strftime("%Y%m%d%H%M%S") + ".wav"
        print(cnt, filename)

        # 2秒間の音データを取り込み
        all = []
        all.append(data)
        for i in range(0, int(RATE / chunk + int(RECORD_SECONDS))):
            data = stream.read(chunk)
            all.append(data)
        data = b''.join(all)

        # 音声ファイルとして出力
        out = wave.open(filename, "w")
        out.setnchannels(CHANNELS)
        out.setsampwidth(2)
        out.setframerate(RATE)
        out.writeframes(data)
        out.close()

        print("Saved.")

        cnt += 1

    # 5回検出したら終了
    if cnt > 5:
        break
    '''

stream.close()
audio.terminate()
