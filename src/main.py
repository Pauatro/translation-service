from fastapi import FastAPI
from translation.endpoints.schemas import (available_languages_list, TranslationRequestSchema)
from translation.services.translators import (translate_to_jeringoza, translate_to_language)
from translation.services.exceptions import TextNotAllowedException
from translation.endpoints.exceptions import UnavailableTranslationTextHttpException

app = FastAPI()

translations_prefix = "/translations"

@app.get(translations_prefix + "/languages")
async def get_available_languages():
    return {"message": available_languages_list}

@app.post(translations_prefix + "/jeringoza")
async def post_translate_to_jeringoza(translation: TranslationRequestSchema):
    translation = translate_to_jeringoza(translation.text)
    return {"message": translation}

@app.post(translations_prefix + "/{language}")
async def post_translate_to_language(translation_request: TranslationRequestSchema):
    try: 
        translation = translate_to_language(translation_request)
        return {"message": translation}

    except TextNotAllowedException:
        raise UnavailableTranslationTextHttpException

 # TODO: add logs
 # TODO: add tests