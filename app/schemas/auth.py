from pydantic import BaseModel


class TokenRequest(BaseModel):
    username: str = None
