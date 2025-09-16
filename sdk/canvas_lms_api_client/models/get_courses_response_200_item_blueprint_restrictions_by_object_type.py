from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_courses_response_200_item_blueprint_restrictions_by_object_type_assignment import (
        GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeAssignment,
    )
    from ..models.get_courses_response_200_item_blueprint_restrictions_by_object_type_wiki_page import (
        GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage,
    )


T = TypeVar("T", bound="GetCoursesResponse200ItemBlueprintRestrictionsByObjectType")


@_attrs_define
class GetCoursesResponse200ItemBlueprintRestrictionsByObjectType:
    """
    Attributes:
        assignment (GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeAssignment):
        wiki_page (GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage):
    """

    assignment: "GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeAssignment"
    wiki_page: "GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment = self.assignment.to_dict()

        wiki_page = self.wiki_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assignment": assignment,
                "wiki_page": wiki_page,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_courses_response_200_item_blueprint_restrictions_by_object_type_assignment import (
            GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeAssignment,
        )
        from ..models.get_courses_response_200_item_blueprint_restrictions_by_object_type_wiki_page import (
            GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage,
        )

        d = dict(src_dict)
        assignment = GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeAssignment.from_dict(d.pop("assignment"))

        wiki_page = GetCoursesResponse200ItemBlueprintRestrictionsByObjectTypeWikiPage.from_dict(d.pop("wiki_page"))

        get_courses_response_200_item_blueprint_restrictions_by_object_type = cls(
            assignment=assignment,
            wiki_page=wiki_page,
        )

        get_courses_response_200_item_blueprint_restrictions_by_object_type.additional_properties = d
        return get_courses_response_200_item_blueprint_restrictions_by_object_type

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
