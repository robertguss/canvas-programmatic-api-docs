from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TemporaryEnrollmentPairing")


@_attrs_define
class TemporaryEnrollmentPairing:
    """
    Attributes:
        id (int):
        workflow_state (str):
    """

    id: int
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        workflow_state = d.pop("workflow_state")

        temporary_enrollment_pairing = cls(
            id=id,
            workflow_state=workflow_state,
        )

        temporary_enrollment_pairing.additional_properties = d
        return temporary_enrollment_pairing

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
