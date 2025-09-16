from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MediaComment")


@_attrs_define
class MediaComment:
    """
    Attributes:
        content_type (str):
        display_name (str):
        media_id (str):
        media_type (str):
        url (str):
    """

    content_type: str
    display_name: str
    media_id: str
    media_type: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        display_name = self.display_name

        media_id = self.media_id

        media_type = self.media_type

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content-type": content_type,
                "display_name": display_name,
                "media_id": media_id,
                "media_type": media_type,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content-type")

        display_name = d.pop("display_name")

        media_id = d.pop("media_id")

        media_type = d.pop("media_type")

        url = d.pop("url")

        media_comment = cls(
            content_type=content_type,
            display_name=display_name,
            media_id=media_id,
            media_type=media_type,
            url=url,
        )

        media_comment.additional_properties = d
        return media_comment

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
