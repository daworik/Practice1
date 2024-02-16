from threading import Thread
from time import sleep

import gi
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib, GObject

GST_PLUGIN_PATH = "D:\programs\MSYS2\mingw64\lib\gstreamer-1.0"
Gst.init()

main_loop = GLib.MainLoop()
main_loop_thread = Thread(target=main_loop.run)
main_loop_thread.start()

pipeline = Gst.parse_launch("souphttpsrc location=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm ! decodebin  ! videoconvert ! autovideosink")

pipeline.set_state(Gst.State.PLAYING)
try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()
main_loop_thread.join()