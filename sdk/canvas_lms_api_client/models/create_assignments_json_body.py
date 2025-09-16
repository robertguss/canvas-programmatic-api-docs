from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssignmentsJsonBody")


@_attrs_define
class CreateAssignmentsJsonBody:
    """
    Attributes:
        assignmentname (Union[Unset, str]): The assignment name.
        assignmentpoints_possible (Union[Unset, str]): The maximum points possible on the assignment.
        assignmentdue_at (Union[Unset, str]): The day/time the assignment is due. Must be between the lock dates if
            there are lock dates. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        assignmentlock_at (Union[Unset, str]): The day/time the assignment is locked after. Must be after the due date
            if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        assignmentunlock_at (Union[Unset, str]): The day/time the assignment is unlocked. Must be before the due date if
            there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        assignmentassignment_overrides (Union[Unset, str]): List of overrides for the assignment.
        assignmentpeer_reviewpoints_possible (Union[Unset, str]): The maximum points possible for peer reviews.
        assignmentpeer_reviewdue_at (Union[Unset, str]): The day/time the peer reviews are due. Must be between the lock
            dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z.
        assignmentpeer_reviewlock_at (Union[Unset, str]): The day/time the peer reviews are locked after. Must be after
            the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-25T12:10:00Z.
        assignmentpeer_reviewunlock_at (Union[Unset, str]): The day/time the peer reviews are unlocked. Must be before
            the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-15T12:10:00Z.
    """

    assignmentname: Union[Unset, str] = UNSET
    assignmentpoints_possible: Union[Unset, str] = UNSET
    assignmentdue_at: Union[Unset, str] = UNSET
    assignmentlock_at: Union[Unset, str] = UNSET
    assignmentunlock_at: Union[Unset, str] = UNSET
    assignmentassignment_overrides: Union[Unset, str] = UNSET
    assignmentpeer_reviewpoints_possible: Union[Unset, str] = UNSET
    assignmentpeer_reviewdue_at: Union[Unset, str] = UNSET
    assignmentpeer_reviewlock_at: Union[Unset, str] = UNSET
    assignmentpeer_reviewunlock_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignmentname = self.assignmentname

        assignmentpoints_possible = self.assignmentpoints_possible

        assignmentdue_at = self.assignmentdue_at

        assignmentlock_at = self.assignmentlock_at

        assignmentunlock_at = self.assignmentunlock_at

        assignmentassignment_overrides = self.assignmentassignment_overrides

        assignmentpeer_reviewpoints_possible = self.assignmentpeer_reviewpoints_possible

        assignmentpeer_reviewdue_at = self.assignmentpeer_reviewdue_at

        assignmentpeer_reviewlock_at = self.assignmentpeer_reviewlock_at

        assignmentpeer_reviewunlock_at = self.assignmentpeer_reviewunlock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignmentname is not UNSET:
            field_dict["assignment[name]"] = assignmentname
        if assignmentpoints_possible is not UNSET:
            field_dict["assignment[points_possible]"] = assignmentpoints_possible
        if assignmentdue_at is not UNSET:
            field_dict["assignment[due_at]"] = assignmentdue_at
        if assignmentlock_at is not UNSET:
            field_dict["assignment[lock_at]"] = assignmentlock_at
        if assignmentunlock_at is not UNSET:
            field_dict["assignment[unlock_at]"] = assignmentunlock_at
        if assignmentassignment_overrides is not UNSET:
            field_dict["assignment[assignment_overrides][]"] = assignmentassignment_overrides
        if assignmentpeer_reviewpoints_possible is not UNSET:
            field_dict["assignment[peer_review][points_possible]"] = assignmentpeer_reviewpoints_possible
        if assignmentpeer_reviewdue_at is not UNSET:
            field_dict["assignment[peer_review][due_at]"] = assignmentpeer_reviewdue_at
        if assignmentpeer_reviewlock_at is not UNSET:
            field_dict["assignment[peer_review][lock_at]"] = assignmentpeer_reviewlock_at
        if assignmentpeer_reviewunlock_at is not UNSET:
            field_dict["assignment[peer_review][unlock_at]"] = assignmentpeer_reviewunlock_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignmentname = d.pop("assignment[name]", UNSET)

        assignmentpoints_possible = d.pop("assignment[points_possible]", UNSET)

        assignmentdue_at = d.pop("assignment[due_at]", UNSET)

        assignmentlock_at = d.pop("assignment[lock_at]", UNSET)

        assignmentunlock_at = d.pop("assignment[unlock_at]", UNSET)

        assignmentassignment_overrides = d.pop("assignment[assignment_overrides][]", UNSET)

        assignmentpeer_reviewpoints_possible = d.pop("assignment[peer_review][points_possible]", UNSET)

        assignmentpeer_reviewdue_at = d.pop("assignment[peer_review][due_at]", UNSET)

        assignmentpeer_reviewlock_at = d.pop("assignment[peer_review][lock_at]", UNSET)

        assignmentpeer_reviewunlock_at = d.pop("assignment[peer_review][unlock_at]", UNSET)

        create_assignments_json_body = cls(
            assignmentname=assignmentname,
            assignmentpoints_possible=assignmentpoints_possible,
            assignmentdue_at=assignmentdue_at,
            assignmentlock_at=assignmentlock_at,
            assignmentunlock_at=assignmentunlock_at,
            assignmentassignment_overrides=assignmentassignment_overrides,
            assignmentpeer_reviewpoints_possible=assignmentpeer_reviewpoints_possible,
            assignmentpeer_reviewdue_at=assignmentpeer_reviewdue_at,
            assignmentpeer_reviewlock_at=assignmentpeer_reviewlock_at,
            assignmentpeer_reviewunlock_at=assignmentpeer_reviewunlock_at,
        )

        create_assignments_json_body.additional_properties = d
        return create_assignments_json_body

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
