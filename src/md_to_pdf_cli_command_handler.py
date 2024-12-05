import pathlib

from .md_to_pdf_bytes_converter import MarkdownToPDFBytesConverter


class MarkdownToPDFClICommandHandler:
    def handle(self, input: pathlib.Path, output: pathlib.Path):
        pdfbytes = MarkdownToPDFBytesConverter().change(
            input,
        )
        with open(output, "wb") as file:
            file.write(pdfbytes)
