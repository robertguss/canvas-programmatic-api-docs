from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_conferences_response_200_item_user_settings import GetConferencesResponse200ItemUserSettings


T = TypeVar("T", bound="GetConferencesResponse200Item")


@_attrs_define
class GetConferencesResponse200Item:
    """
    Attributes:
        id (int):
        conference_type (str):
        conference_key (str):
        description (str):
        duration (int):
        ended_at (str):
        started_at (str):
        title (str):
        users (list[int]):
        invitees (list[int]):
        attendees (list[int]):
        has_advanced_settings (bool):
        long_running (bool):
        user_settings (GetConferencesResponse200ItemUserSettings):
        recordings (None):
        url (None):
        join_url (None):
        context_type (None):
        context_id (None):
    """

    id: int
    conference_type: str
    conference_key: str
    description: str
    duration: int
    ended_at: str
    started_at: str
    title: str
    users: list[int]
    invitees: list[int]
    attendees: list[int]
    has_advanced_settings: bool
    long_running: bool
    user_settings: "GetConferencesResponse200ItemUserSettings"
    recordings: None
    url: None
    join_url: None
    context_type: None
    context_id: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        conference_type = self.conference_type

        conference_key = self.conference_key

        description = self.description

        duration = self.duration

        ended_at = self.ended_at

        started_at = self.started_at

        title = self.title

        users = self.users

        invitees = self.invitees

        attendees = self.attendees

        has_advanced_settings = self.has_advanced_settings

        long_running = self.long_running

        user_settings = self.user_settings.to_dict()

        recordings = self.recordings

        url = self.url

        join_url = self.join_url

        context_type = self.context_type

        context_id = self.context_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "conference_type": conference_type,
                "conference_key": conference_key,
                "description": description,
                "duration": duration,
                "ended_at": ended_at,
                "started_at": started_at,
                "title": title,
                "users": users,
                "invitees": invitees,
                "attendees": attendees,
                "has_advanced_settings": has_advanced_settings,
                "long_running": long_running,
                "user_settings": user_settings,
                "recordings": recordings,
                "url": url,
                "join_url": join_url,
                "context_type": context_type,
                "context_id": context_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_conferences_response_200_item_user_settings import GetConferencesResponse200ItemUserSettings

        d = dict(src_dict)
        id = d.pop("id")

        conference_type = d.pop("conference_type")

        conference_key = d.pop("conference_key")

        description = d.pop("description")

        duration = d.pop("duration")

        ended_at = d.pop("ended_at")

        started_at = d.pop("started_at")

        title = d.pop("title")

        users = cast(list[int], d.pop("users"))

        invitees = cast(list[int], d.pop("invitees"))

        attendees = cast(list[int], d.pop("attendees"))

        has_advanced_settings = d.pop("has_advanced_settings")

        long_running = d.pop("long_running")

        user_settings = GetConferencesResponse200ItemUserSettings.from_dict(d.pop("user_settings"))

        recordings = d.pop("recordings")

        url = d.pop("url")

        join_url = d.pop("join_url")

        context_type = d.pop("context_type")

        context_id = d.pop("context_id")

        get_conferences_response_200_item = cls(
            id=id,
            conference_type=conference_type,
            conference_key=conference_key,
            description=description,
            duration=duration,
            ended_at=ended_at,
            started_at=started_at,
            title=title,
            users=users,
            invitees=invitees,
            attendees=attendees,
            has_advanced_settings=has_advanced_settings,
            long_running=long_running,
            user_settings=user_settings,
            recordings=recordings,
            url=url,
            join_url=join_url,
            context_type=context_type,
            context_id=context_id,
        )

        get_conferences_response_200_item.additional_properties = d
        return get_conferences_response_200_item

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
