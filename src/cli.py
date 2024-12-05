import pathlib
import click

from .md_to_pdf_cli_command_handler import MarkdownToPDFClICommandHandler


@click.command
@click.argument("input")
@click.argument("output")
def main(input: click.File, output: click.File):
    MarkdownToPDFClICommandHandler().handle(pathlib.Path(input), pathlib.Path(output))


if __name__ == "__main__":
    main()
