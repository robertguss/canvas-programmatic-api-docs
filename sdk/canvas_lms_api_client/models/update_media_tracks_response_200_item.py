from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateMediaTracksResponse200Item")


@_attrs_define
class UpdateMediaTracksResponse200Item:
    """
    Attributes:
        id (int):
        user_id (int):
        media_object_id (int):
        kind (str):
        locale (str):
        content (str):
        created_at (str):
        updated_at (str):
        webvtt_content (str):
    """

    id: int
    user_id: int
    media_object_id: int
    kind: str
    locale: str
    content: str
    created_at: str
    updated_at: str
    webvtt_content: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        media_object_id = self.media_object_id

        kind = self.kind

        locale = self.locale

        content = self.content

        created_at = self.created_at

        updated_at = self.updated_at

        webvtt_content = self.webvtt_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "media_object_id": media_object_id,
                "kind": kind,
                "locale": locale,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
                "webvtt_content": webvtt_content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        media_object_id = d.pop("media_object_id")

        kind = d.pop("kind")

        locale = d.pop("locale")

        content = d.pop("content")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        webvtt_content = d.pop("webvtt_content")

        update_media_tracks_response_200_item = cls(
            id=id,
            user_id=user_id,
            media_object_id=media_object_id,
            kind=kind,
            locale=locale,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
            webvtt_content=webvtt_content,
        )

        update_media_tracks_response_200_item.additional_properties = d
        return update_media_tracks_response_200_item

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
