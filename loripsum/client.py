from enum import Enum

import requests

BASE_URL = "https://loripsum.net/api/"

VALID_KWARGS = {
    "decorate",
    "link",
    "ul",
    "ol",
    "dl",
    "bq",
    "code",
    "headers",
    "allcaps",
    "prude",
    "plaintext",
}


class ParagraphLength(Enum):
    short = 1
    medium = 2
    long = 3
    verylong = 4


def _build_url(
    paragraphs: int, length: ParagraphLength = ParagraphLength.short, **kwargs
):
    parts = [str(paragraphs), length.name]

    parts.extend(
        sorted(
            [
                arg
                for arg, enabled in kwargs.items()
                if (arg in VALID_KWARGS) and enabled
            ]
        )
    )

    return BASE_URL + ("/".join(parts))


def get_text(
    paragraphs: int, length: ParagraphLength = ParagraphLength.short, **kwargs
):
    url = _build_url(paragraphs, length, **kwargs)

    response = requests.get(url)

    return response.text
