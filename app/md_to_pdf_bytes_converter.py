import logging
import pathlib

import markdown
from weasyprint import CSS, HTML

from app.paths import STYLE_PATH
import io


logger = logging.getLogger()


class MarkdownToPDFBytesConverter:
    def read_markdown_html_from_file(self, markdown_path: pathlib.Path):
        with open(markdown_path) as markdown_file:
            content = markdown_file.read()

        return markdown.markdown(content)

    def change(self, markdown_path: pathlib.Path) -> io.BytesIO:
        logger.info(
            f"Converting Markdown located at {markdown_path} to PDF... ",
        )
        markdown_html = self.read_markdown_html_from_file(
            markdown_path,
        )
        css = CSS(
            STYLE_PATH,
        )
        bytes = HTML(string=markdown_html).write_pdf(
            target=None,
            stylesheets=[css],
        )
        return bytes
