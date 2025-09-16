from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConferenceRecording")


@_attrs_define
class ConferenceRecording:
    """
    Attributes:
        duration_minutes (int):
        title (str):
        updated_at (str):
        created_at (str):
        playback_url (str):
    """

    duration_minutes: int
    title: str
    updated_at: str
    created_at: str
    playback_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_minutes = self.duration_minutes

        title = self.title

        updated_at = self.updated_at

        created_at = self.created_at

        playback_url = self.playback_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_minutes": duration_minutes,
                "title": title,
                "updated_at": updated_at,
                "created_at": created_at,
                "playback_url": playback_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_minutes = d.pop("duration_minutes")

        title = d.pop("title")

        updated_at = d.pop("updated_at")

        created_at = d.pop("created_at")

        playback_url = d.pop("playback_url")

        conference_recording = cls(
            duration_minutes=duration_minutes,
            title=title,
            updated_at=updated_at,
            created_at=created_at,
            playback_url=playback_url,
        )

        conference_recording.additional_properties = d
        return conference_recording

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
