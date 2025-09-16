from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAccountCalendarsResponse200Item")


@_attrs_define
class GetAccountCalendarsResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        parent_account_id (int):
        root_account_id (int):
        visible (bool):
        auto_subscribe (bool):
        sub_account_count (int):
        asset_string (str):
        type_ (str):
        calendar_event_url (str):
        can_create_calendar_events (bool):
        create_calendar_event_url (str):
        new_calendar_event_url (str):
    """

    id: int
    name: str
    parent_account_id: int
    root_account_id: int
    visible: bool
    auto_subscribe: bool
    sub_account_count: int
    asset_string: str
    type_: str
    calendar_event_url: str
    can_create_calendar_events: bool
    create_calendar_event_url: str
    new_calendar_event_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        parent_account_id = self.parent_account_id

        root_account_id = self.root_account_id

        visible = self.visible

        auto_subscribe = self.auto_subscribe

        sub_account_count = self.sub_account_count

        asset_string = self.asset_string

        type_ = self.type_

        calendar_event_url = self.calendar_event_url

        can_create_calendar_events = self.can_create_calendar_events

        create_calendar_event_url = self.create_calendar_event_url

        new_calendar_event_url = self.new_calendar_event_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "parent_account_id": parent_account_id,
                "root_account_id": root_account_id,
                "visible": visible,
                "auto_subscribe": auto_subscribe,
                "sub_account_count": sub_account_count,
                "asset_string": asset_string,
                "type": type_,
                "calendar_event_url": calendar_event_url,
                "can_create_calendar_events": can_create_calendar_events,
                "create_calendar_event_url": create_calendar_event_url,
                "new_calendar_event_url": new_calendar_event_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        parent_account_id = d.pop("parent_account_id")

        root_account_id = d.pop("root_account_id")

        visible = d.pop("visible")

        auto_subscribe = d.pop("auto_subscribe")

        sub_account_count = d.pop("sub_account_count")

        asset_string = d.pop("asset_string")

        type_ = d.pop("type")

        calendar_event_url = d.pop("calendar_event_url")

        can_create_calendar_events = d.pop("can_create_calendar_events")

        create_calendar_event_url = d.pop("create_calendar_event_url")

        new_calendar_event_url = d.pop("new_calendar_event_url")

        get_account_calendars_response_200_item = cls(
            id=id,
            name=name,
            parent_account_id=parent_account_id,
            root_account_id=root_account_id,
            visible=visible,
            auto_subscribe=auto_subscribe,
            sub_account_count=sub_account_count,
            asset_string=asset_string,
            type_=type_,
            calendar_event_url=calendar_event_url,
            can_create_calendar_events=can_create_calendar_events,
            create_calendar_event_url=create_calendar_event_url,
            new_calendar_event_url=new_calendar_event_url,
        )

        get_account_calendars_response_200_item.additional_properties = d
        return get_account_calendars_response_200_item

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
