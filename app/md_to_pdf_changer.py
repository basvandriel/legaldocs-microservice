import logging
import pathlib

import markdown
from weasyprint import CSS, HTML

from app.paths import STYLE_PATH


logger = logging.getLogger()


# TODO
# This is not a "changer", this takes in a file and exports a PDF from it
class MarkdownToPDFChanger:
    def write_pdf_from_html(self, html: str, pdf_file: pathlib.Path):
        css = CSS(STYLE_PATH)
        HTML(string=html).write_pdf(
            pdf_file,
            stylesheets=[css],
        )

    def read_markdown_html_from_file(self, markdown_path: pathlib.Path):
        with open(markdown_path) as markdown_file:
            content = markdown_file.read()

        html = markdown.markdown(content)
        return html

    def change(self, markdown_path: pathlib.Path):
        logger.info(
            f"Converting Markdown located at {markdown_path} to PDF... ",
        )
        markdown_html = self.read_markdown_html_from_file(
            markdown_path,
        )

        output = pathlib.Path("./testout.pdf")
        self.write_pdf_from_html(
            markdown_html,
            output,
        )

        logger.info(
            f"File saved at {output}",
        )
