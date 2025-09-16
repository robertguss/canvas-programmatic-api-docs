from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateModeratedStudentsDataBody")


@_attrs_define
class CreateModeratedStudentsDataBody:
    """
    Attributes:
        student_ids (Union[Unset, str]): user ids for students to select for moderation
    """

    student_ids: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        student_ids = self.student_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if student_ids is not UNSET:
            field_dict["student_ids[]"] = student_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        student_ids = d.pop("student_ids[]", UNSET)

        create_moderated_students_data_body = cls(
            student_ids=student_ids,
        )

        create_moderated_students_data_body.additional_properties = d
        return create_moderated_students_data_body

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
