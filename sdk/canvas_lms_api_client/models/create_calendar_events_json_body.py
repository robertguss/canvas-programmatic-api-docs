from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCalendarEventsJsonBody")


@_attrs_define
class CreateCalendarEventsJsonBody:
    """
    Attributes:
        calendar_eventcontext_code (Union[Unset, str]): Context code of the course, group, user, or account whose
            calendar this event should be added to.
        calendar_eventstart_at (Union[Unset, str]): Start date/time of the event.
        calendar_eventend_at (Union[Unset, str]): End date/time of the event.
        calendar_eventchild_event_data_xstart_at (Union[Unset, str]): Section-level start time(s) if this is a course
            event. X can be any identifier, provided that it is consistent across the start_at, end_at and context_code
        calendar_eventchild_event_data_xend_at (Union[Unset, str]): Section-level end time(s) if this is a course event.
        calendar_eventduplicatecount (Union[Unset, str]): Number of times to copy/duplicate the event. Count cannot
            exceed 200.
        calendar_eventduplicateinterval (Union[Unset, str]): Defaults to 1 if duplicate ‘count` is set. The interval
            between the duplicated events.
    """

    calendar_eventcontext_code: Union[Unset, str] = UNSET
    calendar_eventstart_at: Union[Unset, str] = UNSET
    calendar_eventend_at: Union[Unset, str] = UNSET
    calendar_eventchild_event_data_xstart_at: Union[Unset, str] = UNSET
    calendar_eventchild_event_data_xend_at: Union[Unset, str] = UNSET
    calendar_eventduplicatecount: Union[Unset, str] = UNSET
    calendar_eventduplicateinterval: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calendar_eventcontext_code = self.calendar_eventcontext_code

        calendar_eventstart_at = self.calendar_eventstart_at

        calendar_eventend_at = self.calendar_eventend_at

        calendar_eventchild_event_data_xstart_at = self.calendar_eventchild_event_data_xstart_at

        calendar_eventchild_event_data_xend_at = self.calendar_eventchild_event_data_xend_at

        calendar_eventduplicatecount = self.calendar_eventduplicatecount

        calendar_eventduplicateinterval = self.calendar_eventduplicateinterval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if calendar_eventcontext_code is not UNSET:
            field_dict["calendar_event[context_code]"] = calendar_eventcontext_code
        if calendar_eventstart_at is not UNSET:
            field_dict["calendar_event[start_at]"] = calendar_eventstart_at
        if calendar_eventend_at is not UNSET:
            field_dict["calendar_event[end_at]"] = calendar_eventend_at
        if calendar_eventchild_event_data_xstart_at is not UNSET:
            field_dict["calendar_event[child_event_data][X][start_at]"] = calendar_eventchild_event_data_xstart_at
        if calendar_eventchild_event_data_xend_at is not UNSET:
            field_dict["calendar_event[child_event_data][X][end_at]"] = calendar_eventchild_event_data_xend_at
        if calendar_eventduplicatecount is not UNSET:
            field_dict["calendar_event[duplicate][count]"] = calendar_eventduplicatecount
        if calendar_eventduplicateinterval is not UNSET:
            field_dict["calendar_event[duplicate][interval]"] = calendar_eventduplicateinterval

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calendar_eventcontext_code = d.pop("calendar_event[context_code]", UNSET)

        calendar_eventstart_at = d.pop("calendar_event[start_at]", UNSET)

        calendar_eventend_at = d.pop("calendar_event[end_at]", UNSET)

        calendar_eventchild_event_data_xstart_at = d.pop("calendar_event[child_event_data][X][start_at]", UNSET)

        calendar_eventchild_event_data_xend_at = d.pop("calendar_event[child_event_data][X][end_at]", UNSET)

        calendar_eventduplicatecount = d.pop("calendar_event[duplicate][count]", UNSET)

        calendar_eventduplicateinterval = d.pop("calendar_event[duplicate][interval]", UNSET)

        create_calendar_events_json_body = cls(
            calendar_eventcontext_code=calendar_eventcontext_code,
            calendar_eventstart_at=calendar_eventstart_at,
            calendar_eventend_at=calendar_eventend_at,
            calendar_eventchild_event_data_xstart_at=calendar_eventchild_event_data_xstart_at,
            calendar_eventchild_event_data_xend_at=calendar_eventchild_event_data_xend_at,
            calendar_eventduplicatecount=calendar_eventduplicatecount,
            calendar_eventduplicateinterval=calendar_eventduplicateinterval,
        )

        create_calendar_events_json_body.additional_properties = d
        return create_calendar_events_json_body

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
