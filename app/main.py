from urllib.request import Request
from app.md_to_pdf_bytes_converter import MarkdownToPDFBytesConverter
from app.paths import DATA_PATH

import logging

from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route

logging.basicConfig(level=logging.INFO)


async def generate_terms_response(request: Request):
    english_terms_file_path = DATA_PATH / "terms_en.md"

    bytes = MarkdownToPDFBytesConverter().change(
        english_terms_file_path,
    )
    return Response(bytes)


app = Starlette(debug=True, routes=[Route("/", generate_terms_response)])
