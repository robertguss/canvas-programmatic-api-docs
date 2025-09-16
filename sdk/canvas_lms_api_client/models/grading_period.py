from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GradingPeriod")


@_attrs_define
class GradingPeriod:
    """
    Attributes:
        id (int):
        title (str):
        start_date (str):
        end_date (str):
        close_date (str):
        weight (float):
        is_closed (bool):
    """

    id: int
    title: str
    start_date: str
    end_date: str
    close_date: str
    weight: float
    is_closed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        start_date = self.start_date

        end_date = self.end_date

        close_date = self.close_date

        weight = self.weight

        is_closed = self.is_closed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "start_date": start_date,
                "end_date": end_date,
                "close_date": close_date,
                "weight": weight,
                "is_closed": is_closed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        close_date = d.pop("close_date")

        weight = d.pop("weight")

        is_closed = d.pop("is_closed")

        grading_period = cls(
            id=id,
            title=title,
            start_date=start_date,
            end_date=end_date,
            close_date=close_date,
            weight=weight,
            is_closed=is_closed,
        )

        grading_period.additional_properties = d
        return grading_period

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
