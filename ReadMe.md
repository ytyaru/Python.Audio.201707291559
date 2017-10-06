# このソフトウェアについて

サイン波をリアルタイム再生した。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* pyenv
    * Python 3.6.1
        * PyAudio 0.2.11

# 実行

```sh
$ python play.py
```

# 問題

音は再生されたが、以下のエラーが出る。

```sh
$ python play.py 
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2239:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
bt_audio_service_open: connect() failed: Connection refused (111)
```

プログラムが正常終了されないため、Ctrl+Zで強制終了するしかない。

# 参考

* http://www.non-fiction.jp/2015/08/17/sin_wave/
* http://aidiary.hatenablog.com/entry/20110607/1307449007

ほぼ丸パクリした。感謝。

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[pygame](http://www.pygame.org/)|[LGPL](https://www.pygame.org/docs/)|[pygame](http://www.pygame.org/)

