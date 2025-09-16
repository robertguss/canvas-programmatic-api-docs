from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDisplay")


@_attrs_define
class UserDisplay:
    """
    Attributes:
        id (int):
        short_name (str):
        avatar_image_url (str):
        html_url (str):
    """

    id: int
    short_name: str
    avatar_image_url: str
    html_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        short_name = self.short_name

        avatar_image_url = self.avatar_image_url

        html_url = self.html_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "short_name": short_name,
                "avatar_image_url": avatar_image_url,
                "html_url": html_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        short_name = d.pop("short_name")

        avatar_image_url = d.pop("avatar_image_url")

        html_url = d.pop("html_url")

        user_display = cls(
            id=id,
            short_name=short_name,
            avatar_image_url=avatar_image_url,
            html_url=html_url,
        )

        user_display.additional_properties = d
        return user_display

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
