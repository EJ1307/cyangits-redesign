"""Dev server for site/. Identical to `python -m http.server` apart from two things.

- Cache-Control: no-store, so an edit to assets/site.css reaches the page on
  the next reload instead of sitting behind the browser's heuristic cache.
- .webp and .svg get their real types; Windows' registry has no .webp entry,
  so http.server would otherwise hand every photograph out as octet-stream.

    python serve.py            serves site/ on http://127.0.0.1:8106
"""
import mimetypes
import os
import pathlib
import sys
from http.server import SimpleHTTPRequestHandler, test

mimetypes.add_type('image/webp', '.webp')
mimetypes.add_type('image/svg+xml', '.svg')


class NoStore(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, max-age=0')
        super().end_headers()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8106
    os.chdir(pathlib.Path(__file__).resolve().parent / 'site')
    test(HandlerClass=NoStore, port=port, bind='127.0.0.1')
