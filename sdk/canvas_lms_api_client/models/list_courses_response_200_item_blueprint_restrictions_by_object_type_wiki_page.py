from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage")


@_attrs_define
class ListCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage:
    """
    Attributes:
        content (bool):
    """

    content: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        list_courses_response_200_item_blueprint_restrictions_by_object_type_wiki_page = cls(
            content=content,
        )

        list_courses_response_200_item_blueprint_restrictions_by_object_type_wiki_page.additional_properties = d
        return list_courses_response_200_item_blueprint_restrictions_by_object_type_wiki_page

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
