from pydantic import BaseModel, Field
from typing import List, Optional


class RouteCreateRequest(BaseModel):
    """
    Данные при создании нового маршрута.
    """

    start_point: str = Field(..., examples=["Moscow"])
    end_point: str = Field(..., examples=["Saint Petersburg"])
    waypoints: Optional[List[str]] = Field(default=None, examples=[["Tver", "Valdai"]])


class RouteResponse(BaseModel):
    """
    Схема ответа для информации о маршруте.
    """

    route_id: str
    start_point: str
    end_point: str
    waypoints: List[str] = []

    class Config:
        from_attributes = True
