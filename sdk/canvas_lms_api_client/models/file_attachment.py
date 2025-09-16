from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FileAttachment")


@_attrs_define
class FileAttachment:
    """
    Attributes:
        content_type (str):
        url (str):
        filename (str):
        display_name (str):
    """

    content_type: str
    url: str
    filename: str
    display_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        url = self.url

        filename = self.filename

        display_name = self.display_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content-type": content_type,
                "url": url,
                "filename": filename,
                "display_name": display_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("content-type")

        url = d.pop("url")

        filename = d.pop("filename")

        display_name = d.pop("display_name")

        file_attachment = cls(
            content_type=content_type,
            url=url,
            filename=filename,
            display_name=display_name,
        )

        file_attachment.additional_properties = d
        return file_attachment

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
