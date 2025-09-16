from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateActivateResponse200PermissionsReadQuestionBanks")


@_attrs_define
class CreateActivateResponse200PermissionsReadQuestionBanks:
    """
    Attributes:
        enabled (bool):
        locked (bool):
        readonly (bool):
        explicit (bool):
        prior_default (bool):
    """

    enabled: bool
    locked: bool
    readonly: bool
    explicit: bool
    prior_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        locked = self.locked

        readonly = self.readonly

        explicit = self.explicit

        prior_default = self.prior_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "locked": locked,
                "readonly": readonly,
                "explicit": explicit,
                "prior_default": prior_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        locked = d.pop("locked")

        readonly = d.pop("readonly")

        explicit = d.pop("explicit")

        prior_default = d.pop("prior_default")

        create_activate_response_200_permissions_read_question_banks = cls(
            enabled=enabled,
            locked=locked,
            readonly=readonly,
            explicit=explicit,
            prior_default=prior_default,
        )

        create_activate_response_200_permissions_read_question_banks.additional_properties = d
        return create_activate_response_200_permissions_read_question_banks

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
