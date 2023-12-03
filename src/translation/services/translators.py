from translation.endpoints.schemas import AvailableLanguages
from translation.data.translations_data import greetings_translations_dict
from translation.services.exceptions import TextNotAllowedException
from translation.endpoints.schemas import (AvailableLanguages, TranslationRequestSchema)

def translate_to_jeringoza(message: str):
    translation = ""
    for x in message.lower():
        translation += x
        if x in "aeiou":
            translation += "p" + x
    
    return translation

def translate_to_language(translation: TranslationRequestSchema):
    if translation.text != greetings_translations_dict[AvailableLanguages.english.value]:
        raise TextNotAllowedException
    else:
        return greetings_translations_dict[translation.language]