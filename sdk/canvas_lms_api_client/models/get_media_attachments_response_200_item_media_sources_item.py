from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetMediaAttachmentsResponse200ItemMediaSourcesItem")


@_attrs_define
class GetMediaAttachmentsResponse200ItemMediaSourcesItem:
    """
    Attributes:
        height (str):
        width (str):
        content_type (str):
        container_format (str):
        url (str):
        bitrate (str):
        size (str):
        is_original (str):
        file_ext (str):
    """

    height: str
    width: str
    content_type: str
    container_format: str
    url: str
    bitrate: str
    size: str
    is_original: str
    file_ext: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        content_type = self.content_type

        container_format = self.container_format

        url = self.url

        bitrate = self.bitrate

        size = self.size

        is_original = self.is_original

        file_ext = self.file_ext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "height": height,
                "width": width,
                "content_type": content_type,
                "containerFormat": container_format,
                "url": url,
                "bitrate": bitrate,
                "size": size,
                "isOriginal": is_original,
                "fileExt": file_ext,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height")

        width = d.pop("width")

        content_type = d.pop("content_type")

        container_format = d.pop("containerFormat")

        url = d.pop("url")

        bitrate = d.pop("bitrate")

        size = d.pop("size")

        is_original = d.pop("isOriginal")

        file_ext = d.pop("fileExt")

        get_media_attachments_response_200_item_media_sources_item = cls(
            height=height,
            width=width,
            content_type=content_type,
            container_format=container_format,
            url=url,
            bitrate=bitrate,
            size=size,
            is_original=is_original,
            file_ext=file_ext,
        )

        get_media_attachments_response_200_item_media_sources_item.additional_properties = d
        return get_media_attachments_response_200_item_media_sources_item

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
