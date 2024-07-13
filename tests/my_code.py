import os
import simpleaitranslator.translator
from simpleaitranslator.translator import get_text_language, translate


#print(os.environ.get("OPENAI_API_KEY"))

#simpleaitranslator.translator.set_openai_api_key(None)

simpleaitranslator.translator.set_openai_api_key(os.environ.get("OPENAI_API_KEY"))
print(get_text_language("jak ty się nazywasz"))
print(translate("Cześć jak się masz? Meu nome é Adam", "eng"))