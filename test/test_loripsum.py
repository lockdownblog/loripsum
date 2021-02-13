from unittest.mock import patch

from loripsum.client import _build_url, ParagraphLength, get_text
import requests_mock
import pytest

@pytest.mark.parametrize(
    ["paragraphs", "length", "kwargs", "expected"],
    [
        (10, "short", {}, "https://loripsum.net/api/10/short"),
        (1, "verylong", {}, "https://loripsum.net/api/1/verylong"),
        (1, "long", {"not":True, "an": True, "attr": True}, "https://loripsum.net/api/1/long"),
        (100, "long", {"link":True, "allcaps": True, "attr": True}, "https://loripsum.net/api/100/long/allcaps/link"),
    ]
)
def test_build_url(paragraphs:int, length:str, kwargs: dict, expected: str):
    paragraph_length = ParagraphLength[length]

    actual = _build_url(paragraphs, paragraph_length, **kwargs)

    assert actual == expected


def test_get_text():
    url = "https://localhost"
    return_text = 'Hello World!'

    with patch("loripsum.client._build_url", return_value=url):
        with requests_mock.Mocker() as request_mocker:
            request_mocker.get(url, text=return_text)
            actual_text = get_text(10, ParagraphLength.short)
            assert actual_text == return_text
