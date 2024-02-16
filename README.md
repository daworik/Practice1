# Practice1
Написано 2 файла python. 

Оба файла в качестве источника используют [стоковое видео](https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm) в формате webm из документации Gstreamer.
# Main.py
Main.py использует `autovideosink` для вывода изображения на экран с возожностью прерывания.

```
pipeline.set_state(Gst.State.PLAYING)
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)

```
# Convert.py
Convert.py переводит видео в формат mp4 используя `x264enc` и сохраняет его в текущую папку через `filesink location=test.mp4`.
