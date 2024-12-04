from app.md_to_pdf_changer import MarkdownToPDFChanger
from app.paths import DATA_PATH

import logging

logging.basicConfig(level=logging.INFO)

english_terms_file_path = DATA_PATH / "terms_en.md"

MarkdownToPDFChanger().change(english_terms_file_path)
