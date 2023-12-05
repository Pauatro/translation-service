from enum import Enum;
from pydantic import BaseModel

class AvailableLanguages(str, Enum):
    spanish = "spanish"
    german = "german"
    italian = "italian"
    danish = "danish"
    french = "french"
    english = "english"

available_languages_list = [l.value for l in AvailableLanguages]

class TranslationRequestSchema(BaseModel):
    language: AvailableLanguages
    text: str

class JeringozaTranslationRequestSchema(BaseModel):
    text: str