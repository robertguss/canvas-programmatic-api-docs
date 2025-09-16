from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUpdateAssociationsDataBody")


@_attrs_define
class UpdateUpdateAssociationsDataBody:
    """
    Attributes:
        course_ids_to_add (Union[Unset, str]): Courses to add as associated courses
        course_ids_to_remove (Union[Unset, str]): Courses to remove as associated courses
    """

    course_ids_to_add: Union[Unset, str] = UNSET
    course_ids_to_remove: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_ids_to_add = self.course_ids_to_add

        course_ids_to_remove = self.course_ids_to_remove

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_ids_to_add is not UNSET:
            field_dict["course_ids_to_add"] = course_ids_to_add
        if course_ids_to_remove is not UNSET:
            field_dict["course_ids_to_remove"] = course_ids_to_remove

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_ids_to_add = d.pop("course_ids_to_add", UNSET)

        course_ids_to_remove = d.pop("course_ids_to_remove", UNSET)

        update_update_associations_data_body = cls(
            course_ids_to_add=course_ids_to_add,
            course_ids_to_remove=course_ids_to_remove,
        )

        update_update_associations_data_body.additional_properties = d
        return update_update_associations_data_body

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
