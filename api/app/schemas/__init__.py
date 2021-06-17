from typing import Any, Optional

from pydantic import BaseModel


class DefaultResponse(BaseModel):
    count: Optional[int] = 1
    data: Any

    class Config:
        extra = "forbid"
