from pydantic import BaseModel, Field


class GetWordResponse(BaseModel):
    word: str = Field(
        description="Случайное русское слово из 5 букв в верхнем регистре",
        json_schema_extra={
            "example": "ПИРОГ",
        },
        min_length=5,
        max_length=5,
        pattern="^[А-ЯЁ]{5}$",
    )


class GetHealthResponse(BaseModel):
    status: str = Field(
        description="Статус сервиса",
        json_schema_extra={
            "example": "ok",
        },
    )
