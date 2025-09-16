from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePagesJsonBody")


@_attrs_define
class CreatePagesJsonBody:
    """
    Attributes:
        wiki_pagetitle (Union[Unset, str]): The title for the new page.
        wiki_pagepublish_at (Union[Unset, str]): Schedule a future date/time to publish the page. This will have no
            effect unless the “Scheduled Page Publication” feature is enabled in the account. If a future date is supplied,
            the page will be unpublished and wiki_page[published] will be ignored.
    """

    wiki_pagetitle: Union[Unset, str] = UNSET
    wiki_pagepublish_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wiki_pagetitle = self.wiki_pagetitle

        wiki_pagepublish_at = self.wiki_pagepublish_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wiki_pagetitle is not UNSET:
            field_dict["wiki_page[title]"] = wiki_pagetitle
        if wiki_pagepublish_at is not UNSET:
            field_dict["wiki_page[publish_at]"] = wiki_pagepublish_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        wiki_pagetitle = d.pop("wiki_page[title]", UNSET)

        wiki_pagepublish_at = d.pop("wiki_page[publish_at]", UNSET)

        create_pages_json_body = cls(
            wiki_pagetitle=wiki_pagetitle,
            wiki_pagepublish_at=wiki_pagepublish_at,
        )

        create_pages_json_body.additional_properties = d
        return create_pages_json_body

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
