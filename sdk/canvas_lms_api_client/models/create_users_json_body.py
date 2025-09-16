from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUsersJsonBody")


@_attrs_define
class CreateUsersJsonBody:
    """
    Attributes:
        pseudonymunique_id (Union[Unset, str]): User’s login ID. If this is a self-registration, it must be a valid
            email address.
        destination (Union[Unset, str]): If you’re setting the password for the newly created user, you can provide this
            param with a valid URL pointing into this Canvas installation, and the response will include a destination field
            that’s a URL that you can redirect a browser to and have the newly created user automatically logged in. The URL
            is only valid for a short time, and must match the domain this request is directed to, and be for a well-formed
            path that Canvas can recognize.
    """

    pseudonymunique_id: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pseudonymunique_id = self.pseudonymunique_id

        destination = self.destination

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pseudonymunique_id is not UNSET:
            field_dict["pseudonym[unique_id]"] = pseudonymunique_id
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pseudonymunique_id = d.pop("pseudonym[unique_id]", UNSET)

        destination = d.pop("destination", UNSET)

        create_users_json_body = cls(
            pseudonymunique_id=pseudonymunique_id,
            destination=destination,
        )

        create_users_json_body.additional_properties = d
        return create_users_json_body

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
