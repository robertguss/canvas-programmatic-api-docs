from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSelfRegistrationJsonBody")


@_attrs_define
class CreateSelfRegistrationJsonBody:
    """
    Attributes:
        username (Union[Unset, str]): The full name of the user. This name will be used by teacher for grading.
        userterms_of_use (Union[Unset, str]): Whether the user accepts the terms of use.
        pseudonymunique_id (Union[Unset, str]): User’s login ID. Must be a valid email address.
    """

    username: Union[Unset, str] = UNSET
    userterms_of_use: Union[Unset, str] = UNSET
    pseudonymunique_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        userterms_of_use = self.userterms_of_use

        pseudonymunique_id = self.pseudonymunique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["user[name]"] = username
        if userterms_of_use is not UNSET:
            field_dict["user[terms_of_use]"] = userterms_of_use
        if pseudonymunique_id is not UNSET:
            field_dict["pseudonym[unique_id]"] = pseudonymunique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("user[name]", UNSET)

        userterms_of_use = d.pop("user[terms_of_use]", UNSET)

        pseudonymunique_id = d.pop("pseudonym[unique_id]", UNSET)

        create_self_registration_json_body = cls(
            username=username,
            userterms_of_use=userterms_of_use,
            pseudonymunique_id=pseudonymunique_id,
        )

        create_self_registration_json_body.additional_properties = d
        return create_self_registration_json_body

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
