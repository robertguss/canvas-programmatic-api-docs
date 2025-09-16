from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBindDataBody")


@_attrs_define
class CreateBindDataBody:
    """
    Attributes:
        workflow_state (Union[Unset, str]): The desired state for this registration/account binding. “allow” is only
            valid for Site Admin registrations.Allowed values: on, off, allow
    """

    workflow_state: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_state is not UNSET:
            field_dict["workflow_state"] = workflow_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_state = d.pop("workflow_state", UNSET)

        create_bind_data_body = cls(
            workflow_state=workflow_state,
        )

        create_bind_data_body.additional_properties = d
        return create_bind_data_body

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
