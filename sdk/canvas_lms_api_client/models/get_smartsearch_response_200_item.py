from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSmartsearchResponse200Item")


@_attrs_define
class GetSmartsearchResponse200Item:
    """
    Attributes:
        content_id (int):
        content_type (str):
        title (str):
        body (str):
        html_url (str):
        distance (float):
    """

    content_id: int
    content_type: str
    title: str
    body: str
    html_url: str
    distance: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_id = self.content_id

        content_type = self.content_type

        title = self.title

        body = self.body

        html_url = self.html_url

        distance = self.distance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_id": content_id,
                "content_type": content_type,
                "title": title,
                "body": body,
                "html_url": html_url,
                "distance": distance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_id = d.pop("content_id")

        content_type = d.pop("content_type")

        title = d.pop("title")

        body = d.pop("body")

        html_url = d.pop("html_url")

        distance = d.pop("distance")

        get_smartsearch_response_200_item = cls(
            content_id=content_id,
            content_type=content_type,
            title=title,
            body=body,
            html_url=html_url,
            distance=distance,
        )

        get_smartsearch_response_200_item.additional_properties = d
        return get_smartsearch_response_200_item

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
