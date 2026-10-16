#!/usr/bin/env python3
"""Mobile sprites: put a transparent sprite on a solid background and save it as PNG.

Phone chats only show images sent as file cards, and a file card has no transparency, so the
sprite gets a background that matches the chat instead.

  python3 flatten.py <sprite url> <out.png> [--bg "#FAF9F5"]

Prints the PNG path, or nothing if anything went wrong (then skip the sprite). Needs Pillow.
"""
import io, sys, urllib.request


def main():
    a = sys.argv[1:]
    bg = "#FAF9F5"
    if "--bg" in a:
        i = a.index("--bg"); bg = a[i + 1]; del a[i:i + 2]
    try:
        from PIL import Image
        url, out = a[0], a[1]
        data = urllib.request.urlopen(url, timeout=10).read()
        s = Image.open(io.BytesIO(data)).convert("RGBA")
        im = Image.new("RGBA", (s.width + 24, s.height + 24), bg)
        im.alpha_composite(s, (12, 12))
        im.convert("RGB").save(out, "PNG")
        print(out)
    except Exception:
        pass


if __name__ == "__main__":
    main()
