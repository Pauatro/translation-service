from fastapi import FastAPI
from translation.endpoints.schemas import (
    available_languages_list,
    TranslationRequestSchema,
    JeringozaTranslationRequestSchema,
)
from translation.services.translators import (
    translate_to_jeringoza,
    translate_to_language,
)
from translation.services.exceptions import TextNotAllowedException
from translation.endpoints.exceptions import UnavailableTranslationTextHttpException
from fastapi.middleware.cors import CORSMiddleware
from shared.settings import Settings

app = FastAPI()
app_settings = Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translations_prefix = "/translations"


@app.get(translations_prefix + "/languages")
async def get_available_languages():
    return {"data": available_languages_list}


@app.post(translations_prefix + "/jeringoza")
async def post_translate_to_jeringoza(translation: JeringozaTranslationRequestSchema):
    translation = translate_to_jeringoza(translation.text)
    return {"data": translation}


@app.post(translations_prefix)
async def post_translate_to_language(translation_request: TranslationRequestSchema):
    try:
        translation = translate_to_language(translation_request)
        return {"data": translation}

    except TextNotAllowedException:
        raise UnavailableTranslationTextHttpException


# TODO: add logs
# TODO: add tests
