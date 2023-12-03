from fastapi import HTTPException, status

class UnavailableTranslationTextHttpException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="The requested text is not available for translation",
        )