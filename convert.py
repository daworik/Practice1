

import gi
gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib

Gst.init()


pipeline = Gst.parse_launch("souphttpsrc location=https://gstreamer.freedesktop.org/data/media/sintel_trailer-480p.webm ! decodebin ! videoconvert ! edgetv ! videoconvert ! x264enc ! mp4mux ! filesink location=test.mp4")

pipeline.set_state(Gst.State.PLAYING)

bus = pipeline.get_bus()

msg = bus.timed_pop_filtered(Gst.CLOCK_TIME_NONE,  
    Gst.MessageType.ERROR | Gst.MessageType.EOS)

pipeline.set_state(Gst.State.NULL)
