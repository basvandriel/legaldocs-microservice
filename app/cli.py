import pathlib
import click

from app.md_to_pdf_bytes_converter import MarkdownToPDFBytesConverter


@click.command
@click.argument("input")
@click.argument("output")
def main(input: click.File, output: click.File):
    pdfbytes = MarkdownToPDFBytesConverter().change(
        pathlib.Path(input),
    )
    with open(pathlib.Path(output), "wb") as file:
        file.write(pdfbytes)


if __name__ == "__main__":
    main()
