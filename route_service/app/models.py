from typing import Optional, List


class Route:
    """
    Доменная модель маршрута.
    """

    def __init__(
        self, route_id: str, start_point: str, end_point: str, waypoints: Optional[List[str]]
    ):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.waypoints = waypoints or []

    def dict(self) -> dict:
        return {
            "route_id": self.route_id,
            "start_point": self.start_point,
            "end_point": self.end_point,
            "waypoints": self.waypoints,
        }

    def __repr__(self):
        return f"Route(id={self.route_id}, from={self.start_point}, to={self.end_point})"
