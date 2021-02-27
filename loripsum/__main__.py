import click

from loripsum.client import get_text


@click.command()
@click.argument("paragraphs", type=click.INT)
def main(paragraphs):
    resultado = get_text(paragraphs)
    print(resultado)


if __name__ == "__main__":
    main()
