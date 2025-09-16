from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOverridesJsonBody")


@_attrs_define
class CreateOverridesJsonBody:
    """
    Attributes:
        assignment_overridedue_at (Union[Unset, str]): The day/time the overridden assignment is due. Accepts times in
            ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present
            but null to indicate the override removes any previous due date.
        assignment_overrideunlock_at (Union[Unset, str]): The day/time the overridden assignment becomes unlocked.
            Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock
            date. May be present but null to indicate the override removes any previous unlock date.
        assignment_overridelock_at (Union[Unset, str]): The day/time the overridden assignment becomes locked. Accepts
            times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May
            be present but null to indicate the override removes any previous lock date.
    """

    assignment_overridedue_at: Union[Unset, str] = UNSET
    assignment_overrideunlock_at: Union[Unset, str] = UNSET
    assignment_overridelock_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_overridedue_at = self.assignment_overridedue_at

        assignment_overrideunlock_at = self.assignment_overrideunlock_at

        assignment_overridelock_at = self.assignment_overridelock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignment_overridedue_at is not UNSET:
            field_dict["assignment_override[due_at]"] = assignment_overridedue_at
        if assignment_overrideunlock_at is not UNSET:
            field_dict["assignment_override[unlock_at]"] = assignment_overrideunlock_at
        if assignment_overridelock_at is not UNSET:
            field_dict["assignment_override[lock_at]"] = assignment_overridelock_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment_overridedue_at = d.pop("assignment_override[due_at]", UNSET)

        assignment_overrideunlock_at = d.pop("assignment_override[unlock_at]", UNSET)

        assignment_overridelock_at = d.pop("assignment_override[lock_at]", UNSET)

        create_overrides_json_body = cls(
            assignment_overridedue_at=assignment_overridedue_at,
            assignment_overrideunlock_at=assignment_overrideunlock_at,
            assignment_overridelock_at=assignment_overridelock_at,
        )

        create_overrides_json_body.additional_properties = d
        return create_overrides_json_body

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
