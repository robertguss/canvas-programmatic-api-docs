from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListCalendarEventsResponse200Item")


@_attrs_define
class ListCalendarEventsResponse200Item:
    """
    Attributes:
        id (int):
        title (str):
        start_at (str):
        end_at (str):
        description (str):
        location_name (str):
        location_address (str):
        context_code (str):
        effective_context_code (None):
        context_name (str):
        all_context_codes (str):
        workflow_state (str):
        hidden (bool):
        parent_event_id (None):
        child_events_count (int):
        child_events (None):
        url (str):
        html_url (str):
        all_day_date (str):
        all_day (bool):
        created_at (str):
        updated_at (str):
        appointment_group_id (None):
        appointment_group_url (None):
        own_reservation (bool):
        reserve_url (None):
        reserved (bool):
        participant_type (str):
        participants_per_appointment (None):
        available_slots (None):
        user (None):
        group (None):
        important_dates (bool):
        series_uuid (None):
        rrule (None):
        series_head (None):
        series_natural_language (str):
        blackout_date (bool):
    """

    id: int
    title: str
    start_at: str
    end_at: str
    description: str
    location_name: str
    location_address: str
    context_code: str
    effective_context_code: None
    context_name: str
    all_context_codes: str
    workflow_state: str
    hidden: bool
    parent_event_id: None
    child_events_count: int
    child_events: None
    url: str
    html_url: str
    all_day_date: str
    all_day: bool
    created_at: str
    updated_at: str
    appointment_group_id: None
    appointment_group_url: None
    own_reservation: bool
    reserve_url: None
    reserved: bool
    participant_type: str
    participants_per_appointment: None
    available_slots: None
    user: None
    group: None
    important_dates: bool
    series_uuid: None
    rrule: None
    series_head: None
    series_natural_language: str
    blackout_date: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        start_at = self.start_at

        end_at = self.end_at

        description = self.description

        location_name = self.location_name

        location_address = self.location_address

        context_code = self.context_code

        effective_context_code = self.effective_context_code

        context_name = self.context_name

        all_context_codes = self.all_context_codes

        workflow_state = self.workflow_state

        hidden = self.hidden

        parent_event_id = self.parent_event_id

        child_events_count = self.child_events_count

        child_events = self.child_events

        url = self.url

        html_url = self.html_url

        all_day_date = self.all_day_date

        all_day = self.all_day

        created_at = self.created_at

        updated_at = self.updated_at

        appointment_group_id = self.appointment_group_id

        appointment_group_url = self.appointment_group_url

        own_reservation = self.own_reservation

        reserve_url = self.reserve_url

        reserved = self.reserved

        participant_type = self.participant_type

        participants_per_appointment = self.participants_per_appointment

        available_slots = self.available_slots

        user = self.user

        group = self.group

        important_dates = self.important_dates

        series_uuid = self.series_uuid

        rrule = self.rrule

        series_head = self.series_head

        series_natural_language = self.series_natural_language

        blackout_date = self.blackout_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "start_at": start_at,
                "end_at": end_at,
                "description": description,
                "location_name": location_name,
                "location_address": location_address,
                "context_code": context_code,
                "effective_context_code": effective_context_code,
                "context_name": context_name,
                "all_context_codes": all_context_codes,
                "workflow_state": workflow_state,
                "hidden": hidden,
                "parent_event_id": parent_event_id,
                "child_events_count": child_events_count,
                "child_events": child_events,
                "url": url,
                "html_url": html_url,
                "all_day_date": all_day_date,
                "all_day": all_day,
                "created_at": created_at,
                "updated_at": updated_at,
                "appointment_group_id": appointment_group_id,
                "appointment_group_url": appointment_group_url,
                "own_reservation": own_reservation,
                "reserve_url": reserve_url,
                "reserved": reserved,
                "participant_type": participant_type,
                "participants_per_appointment": participants_per_appointment,
                "available_slots": available_slots,
                "user": user,
                "group": group,
                "important_dates": important_dates,
                "series_uuid": series_uuid,
                "rrule": rrule,
                "series_head": series_head,
                "series_natural_language": series_natural_language,
                "blackout_date": blackout_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        description = d.pop("description")

        location_name = d.pop("location_name")

        location_address = d.pop("location_address")

        context_code = d.pop("context_code")

        effective_context_code = d.pop("effective_context_code")

        context_name = d.pop("context_name")

        all_context_codes = d.pop("all_context_codes")

        workflow_state = d.pop("workflow_state")

        hidden = d.pop("hidden")

        parent_event_id = d.pop("parent_event_id")

        child_events_count = d.pop("child_events_count")

        child_events = d.pop("child_events")

        url = d.pop("url")

        html_url = d.pop("html_url")

        all_day_date = d.pop("all_day_date")

        all_day = d.pop("all_day")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        appointment_group_id = d.pop("appointment_group_id")

        appointment_group_url = d.pop("appointment_group_url")

        own_reservation = d.pop("own_reservation")

        reserve_url = d.pop("reserve_url")

        reserved = d.pop("reserved")

        participant_type = d.pop("participant_type")

        participants_per_appointment = d.pop("participants_per_appointment")

        available_slots = d.pop("available_slots")

        user = d.pop("user")

        group = d.pop("group")

        important_dates = d.pop("important_dates")

        series_uuid = d.pop("series_uuid")

        rrule = d.pop("rrule")

        series_head = d.pop("series_head")

        series_natural_language = d.pop("series_natural_language")

        blackout_date = d.pop("blackout_date")

        list_calendar_events_response_200_item = cls(
            id=id,
            title=title,
            start_at=start_at,
            end_at=end_at,
            description=description,
            location_name=location_name,
            location_address=location_address,
            context_code=context_code,
            effective_context_code=effective_context_code,
            context_name=context_name,
            all_context_codes=all_context_codes,
            workflow_state=workflow_state,
            hidden=hidden,
            parent_event_id=parent_event_id,
            child_events_count=child_events_count,
            child_events=child_events,
            url=url,
            html_url=html_url,
            all_day_date=all_day_date,
            all_day=all_day,
            created_at=created_at,
            updated_at=updated_at,
            appointment_group_id=appointment_group_id,
            appointment_group_url=appointment_group_url,
            own_reservation=own_reservation,
            reserve_url=reserve_url,
            reserved=reserved,
            participant_type=participant_type,
            participants_per_appointment=participants_per_appointment,
            available_slots=available_slots,
            user=user,
            group=group,
            important_dates=important_dates,
            series_uuid=series_uuid,
            rrule=rrule,
            series_head=series_head,
            series_natural_language=series_natural_language,
            blackout_date=blackout_date,
        )

        list_calendar_events_response_200_item.additional_properties = d
        return list_calendar_events_response_200_item

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
