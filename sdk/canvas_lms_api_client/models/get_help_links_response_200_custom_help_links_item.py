from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetHelpLinksResponse200CustomHelpLinksItem")


@_attrs_define
class GetHelpLinksResponse200CustomHelpLinksItem:
    """
    Attributes:
        id (str):
        text (str):
        subtext (str):
        url (str):
        type_ (str):
        available_to (list[str]):
        is_featured (bool):
        is_new (bool):
        feature_headline (str):
    """

    id: str
    text: str
    subtext: str
    url: str
    type_: str
    available_to: list[str]
    is_featured: bool
    is_new: bool
    feature_headline: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        text = self.text

        subtext = self.subtext

        url = self.url

        type_ = self.type_

        available_to = self.available_to

        is_featured = self.is_featured

        is_new = self.is_new

        feature_headline = self.feature_headline

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "text": text,
                "subtext": subtext,
                "url": url,
                "type": type_,
                "available_to": available_to,
                "is_featured": is_featured,
                "is_new": is_new,
                "feature_headline": feature_headline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        text = d.pop("text")

        subtext = d.pop("subtext")

        url = d.pop("url")

        type_ = d.pop("type")

        available_to = cast(list[str], d.pop("available_to"))

        is_featured = d.pop("is_featured")

        is_new = d.pop("is_new")

        feature_headline = d.pop("feature_headline")

        get_help_links_response_200_custom_help_links_item = cls(
            id=id,
            text=text,
            subtext=subtext,
            url=url,
            type_=type_,
            available_to=available_to,
            is_featured=is_featured,
            is_new=is_new,
            feature_headline=feature_headline,
        )

        get_help_links_response_200_custom_help_links_item.additional_properties = d
        return get_help_links_response_200_custom_help_links_item

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
