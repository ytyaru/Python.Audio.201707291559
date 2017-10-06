# -*- coding: utf-8 -*-
 
import wave
import numpy as np
from matplotlib import pylab as plt
import struct

# サイン波を生成する
class Sin:
    def __init__(self): self.__wave = []
    @property
    def Wave(self): return self.__wave
    """
    サイン波を生成する。
    a:   振幅
    fs:  サンプリング周波数
    f0:  周波数
    sec: 秒
    """
    def Create(self, a=1, fs=8000, f0=440, sec=5):
#        if fs < 2*f0:
#            print('サンプリング定理によると	、サンプリング周波数は周波数の2倍以上でないと元の信号を再現できない。fs={}をfs={}に強制変換する。'.format(fs, 2*f0))
#            fs = 2*f0
        self.__wave.clear()
        for n in np.arange(fs * sec):
            s = a * np.sin(2.0 * np.pi * f0 * n / fs) # サンプリング(標本化)する
            self.__wave.append(s)
        return self.__wave

#量子化する
class Sampler:
    @staticmethod
    def Sampling(wav, bit=16): #16bit=-32768〜32767
        q = 2**(bit-1)-1 # 符号付きのため-1乗。0で1つ分減るため-1。
        return [int(x * q) for x in wav]

def play (data, fs, bit):
    import pyaudio
    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=int(fs),
                    output= True)
    # チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    sp = 0  # 再生位置ポインタ
    buffer = data[sp:sp+chunk]
    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    p.terminate()

if __name__ == "__main__" :
    s = Sin()
    s.Create(a=1, fs=8000, f0=440, sec=5)
     
    #サイン波を表示
#    plt.plot(s.Wave[0:100])
#    plt.show()
     
    #サイン波を-32768から32767の整数値に変換(signed 16bit pcmへ)
    swav = Sampler.Sampling(s.Wave, bit=16)
     
    #バイナリ化
    binwave = struct.pack("h" * len(swav), *swav)

    play(binwave, 8000, 16)
#    freqList = [262, 294, 330, 349, 392, 440, 494, 523]  # ドレミファソラシド
#    for f in freqList:
#        data = createSineWave(1.0, f, 8000.0, 1.0)
#        play(data, 8000, 16)
