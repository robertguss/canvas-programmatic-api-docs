from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Scope")


@_attrs_define
class Scope:
    """
    Attributes:
        resource (str):
        resource_name (str):
        controller (str):
        action (str):
        verb (str):
        scope (str):
    """

    resource: str
    resource_name: str
    controller: str
    action: str
    verb: str
    scope: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource = self.resource

        resource_name = self.resource_name

        controller = self.controller

        action = self.action

        verb = self.verb

        scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resource": resource,
                "resource_name": resource_name,
                "controller": controller,
                "action": action,
                "verb": verb,
                "scope": scope,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        resource = d.pop("resource")

        resource_name = d.pop("resource_name")

        controller = d.pop("controller")

        action = d.pop("action")

        verb = d.pop("verb")

        scope = d.pop("scope")

        scope = cls(
            resource=resource,
            resource_name=resource_name,
            controller=controller,
            action=action,
            verb=verb,
            scope=scope,
        )

        scope.additional_properties = d
        return scope

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
