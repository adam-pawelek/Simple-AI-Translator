import re

import pytest
from unittest.mock import patch

from simpleaitranslator.translator import translate, get_text_language


# Assuming the translate function is in a module named 'translator_module'


def test_translate_api_key_not_set():
    text = "Hello, world!"
    to_language = "Spanish"

    expected_message = (
        "OpenAI API key is not set. Please set the API key in simpleaitranslator.translator.OPENAI_API_KEY. "
        "See documentation: https://github.com/adam-pawelek/SimpleAITranslator/tree/main?tab=readme-ov-file#setting-up"
    )

    with patch('simpleaitranslator.translator.OPENAI_API_KEY', None):
        with pytest.raises(ValueError, match=re.escape(expected_message)):
            translate(text, to_language)





def test_get_text_language_api_key_not_set():
    text = "Hello, world!"

    expected_message = (
        "OpenAI API key is not set. Please set the API key in simpleaitranslator.translator.OPENAI_API_KEY. "
        "See documentation: https://github.com/adam-pawelek/SimpleAITranslator/tree/main?tab=readme-ov-file#setting-up"
    )

    with patch('simpleaitranslator.translator.OPENAI_API_KEY', None):
        with pytest.raises(ValueError, match=re.escape(expected_message)):
            get_text_language(text)
