from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Avatar")


@_attrs_define
class Avatar:
    """
    Attributes:
        type_ (str):
        url (str):
        token (str):
        display_name (str):
        id (int):
        content_type (str):
        filename (str):
        size (int):
    """

    type_: str
    url: str
    token: str
    display_name: str
    id: int
    content_type: str
    filename: str
    size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        token = self.token

        display_name = self.display_name

        id = self.id

        content_type = self.content_type

        filename = self.filename

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
                "token": token,
                "display_name": display_name,
                "id": id,
                "content-type": content_type,
                "filename": filename,
                "size": size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        url = d.pop("url")

        token = d.pop("token")

        display_name = d.pop("display_name")

        id = d.pop("id")

        content_type = d.pop("content-type")

        filename = d.pop("filename")

        size = d.pop("size")

        avatar = cls(
            type_=type_,
            url=url,
            token=token,
            display_name=display_name,
            id=id,
            content_type=content_type,
            filename=filename,
            size=size,
        )

        avatar.additional_properties = d
        return avatar

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
