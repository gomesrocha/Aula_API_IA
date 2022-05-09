from pydantic import BaseModel


class UrlResumo(BaseModel):
    url: str
