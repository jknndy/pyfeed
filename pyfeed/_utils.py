import re


def strip_html(text):
    return re.sub(r"<[^>]+>", "", text) if text else ""
