from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PairingCode")


@_attrs_define
class PairingCode:
    """
    Attributes:
        user_id (int):
        code (str):
        expires_at (str):
        workflow_state (str):
    """

    user_id: int
    code: str
    expires_at: str
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        code = self.code

        expires_at = self.expires_at

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "code": code,
                "expires_at": expires_at,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        code = d.pop("code")

        expires_at = d.pop("expires_at")

        workflow_state = d.pop("workflow_state")

        pairing_code = cls(
            user_id=user_id,
            code=code,
            expires_at=expires_at,
            workflow_state=workflow_state,
        )

        pairing_code.additional_properties = d
        return pairing_code

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
