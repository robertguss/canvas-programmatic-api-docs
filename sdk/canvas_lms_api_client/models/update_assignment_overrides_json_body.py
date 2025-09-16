from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssignmentOverridesJsonBody")


@_attrs_define
class UpdateAssignmentOverridesJsonBody:
    """
    Attributes:
        overrides (Union[Unset, str]): List of overrides to apply to the module. Overrides that already exist should
            include an ID and will be updated if needed. New overrides will be created for overrides in the list without an
            ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the module’s
            overrides. Keys for each override object can include: ‘id’, ‘title’, ‘student_ids’, and ‘course_section_id’.
            ‘group_id’ is accepted if the Differentiation Tags account setting is enabled.
    """

    overrides: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        overrides = self.overrides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if overrides is not UNSET:
            field_dict["overrides[]"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        overrides = d.pop("overrides[]", UNSET)

        update_assignment_overrides_json_body = cls(
            overrides=overrides,
        )

        update_assignment_overrides_json_body.additional_properties = d
        return update_assignment_overrides_json_body

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
