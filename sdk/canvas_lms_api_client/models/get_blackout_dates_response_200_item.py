from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetBlackoutDatesResponse200Item")


@_attrs_define
class GetBlackoutDatesResponse200Item:
    """
    Attributes:
        id (int):
        context_id (int):
        context_type (str):
        start_date (str):
        end_date (str):
        event_title (str):
    """

    id: int
    context_id: int
    context_type: str
    start_date: str
    end_date: str
    event_title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        context_id = self.context_id

        context_type = self.context_type

        start_date = self.start_date

        end_date = self.end_date

        event_title = self.event_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "context_id": context_id,
                "context_type": context_type,
                "start_date": start_date,
                "end_date": end_date,
                "event_title": event_title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        event_title = d.pop("event_title")

        get_blackout_dates_response_200_item = cls(
            id=id,
            context_id=context_id,
            context_type=context_type,
            start_date=start_date,
            end_date=end_date,
            event_title=event_title,
        )

        get_blackout_dates_response_200_item.additional_properties = d
        return get_blackout_dates_response_200_item

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
