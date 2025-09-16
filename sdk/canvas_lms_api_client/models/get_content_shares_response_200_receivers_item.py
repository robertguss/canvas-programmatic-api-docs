from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetContentSharesResponse200ReceiversItem")


@_attrs_define
class GetContentSharesResponse200ReceiversItem:
    """
    Attributes:
        id (int):
        display_name (str):
        avatar_image_url (str):
        html_url (str):
    """

    id: int
    display_name: str
    avatar_image_url: str
    html_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        avatar_image_url = self.avatar_image_url

        html_url = self.html_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "avatar_image_url": avatar_image_url,
                "html_url": html_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        avatar_image_url = d.pop("avatar_image_url")

        html_url = d.pop("html_url")

        get_content_shares_response_200_receivers_item = cls(
            id=id,
            display_name=display_name,
            avatar_image_url=avatar_image_url,
            html_url=html_url,
        )

        get_content_shares_response_200_receivers_item.additional_properties = d
        return get_content_shares_response_200_receivers_item

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
