from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExtensionsDataBody")


@_attrs_define
class CreateExtensionsDataBody:
    """
    Attributes:
        assignment_extensionsuser_id (Union[Unset, str]): The ID of the user we want to add assignment extensions for.
        assignment_extensionsextra_attempts (Union[Unset, str]): Number of times the student is allowed to re-take the
            assignment over the limit.
    """

    assignment_extensionsuser_id: Union[Unset, str] = UNSET
    assignment_extensionsextra_attempts: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assignment_extensionsuser_id = self.assignment_extensionsuser_id

        assignment_extensionsextra_attempts = self.assignment_extensionsextra_attempts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assignment_extensionsuser_id is not UNSET:
            field_dict["assignment_extensions[][user_id]"] = assignment_extensionsuser_id
        if assignment_extensionsextra_attempts is not UNSET:
            field_dict["assignment_extensions[][extra_attempts]"] = assignment_extensionsextra_attempts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assignment_extensionsuser_id = d.pop("assignment_extensions[][user_id]", UNSET)

        assignment_extensionsextra_attempts = d.pop("assignment_extensions[][extra_attempts]", UNSET)

        create_extensions_data_body = cls(
            assignment_extensionsuser_id=assignment_extensionsuser_id,
            assignment_extensionsextra_attempts=assignment_extensionsextra_attempts,
        )

        create_extensions_data_body.additional_properties = d
        return create_extensions_data_body

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
