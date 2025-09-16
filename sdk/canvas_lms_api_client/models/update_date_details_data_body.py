from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateDateDetailsDataBody")


@_attrs_define
class UpdateDateDetailsDataBody:
    """
    Attributes:
        due_at (Union[Unset, str]): The learning object’s due date. Not applicable for ungraded discussions, pages, and
            files.
        unlock_at (Union[Unset, str]): The learning object’s unlock date. Must be before the due date if there is one.
        lock_at (Union[Unset, str]): The learning object’s lock date. Must be after the due date if there is one.
        assignment_overrides (Union[Unset, str]): List of overrides to apply to the learning object. Overrides that
            already exist should include an ID and will be updated if needed. New overrides will be created for overrides in
            the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete
            all of the object’s overrides. Keys for each override object can include: ‘id’, ‘title’, ‘due_at’, ‘unlock_at’,
            ‘lock_at’, ‘student_ids’, and ‘course_section_id’, ‘course_id’, ‘noop_id’, and ‘unassign_item’.
    """

    due_at: Union[Unset, str] = UNSET
    unlock_at: Union[Unset, str] = UNSET
    lock_at: Union[Unset, str] = UNSET
    assignment_overrides: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        assignment_overrides = self.assignment_overrides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if unlock_at is not UNSET:
            field_dict["unlock_at"] = unlock_at
        if lock_at is not UNSET:
            field_dict["lock_at"] = lock_at
        if assignment_overrides is not UNSET:
            field_dict["assignment_overrides[]"] = assignment_overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        due_at = d.pop("due_at", UNSET)

        unlock_at = d.pop("unlock_at", UNSET)

        lock_at = d.pop("lock_at", UNSET)

        assignment_overrides = d.pop("assignment_overrides[]", UNSET)

        update_date_details_data_body = cls(
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
            assignment_overrides=assignment_overrides,
        )

        update_date_details_data_body.additional_properties = d
        return update_date_details_data_body

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
