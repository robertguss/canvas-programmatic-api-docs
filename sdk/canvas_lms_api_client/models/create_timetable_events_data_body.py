from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTimetableEventsDataBody")


@_attrs_define
class CreateTimetableEventsDataBody:
    """
    Attributes:
        events (Union[Unset, str]): An array of event objects to use.
        eventsstart_at (Union[Unset, str]): Start time for the event
        eventsend_at (Union[Unset, str]): End time for the event
    """

    events: Union[Unset, str] = UNSET
    eventsstart_at: Union[Unset, str] = UNSET
    eventsend_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        events = self.events

        eventsstart_at = self.eventsstart_at

        eventsend_at = self.eventsend_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if events is not UNSET:
            field_dict["events[]"] = events
        if eventsstart_at is not UNSET:
            field_dict["events[][start_at]"] = eventsstart_at
        if eventsend_at is not UNSET:
            field_dict["events[][end_at]"] = eventsend_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = d.pop("events[]", UNSET)

        eventsstart_at = d.pop("events[][start_at]", UNSET)

        eventsend_at = d.pop("events[][end_at]", UNSET)

        create_timetable_events_data_body = cls(
            events=events,
            eventsstart_at=eventsstart_at,
            eventsend_at=eventsend_at,
        )

        create_timetable_events_data_body.additional_properties = d
        return create_timetable_events_data_body

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
