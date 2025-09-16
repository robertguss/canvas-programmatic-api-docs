from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLoginsJsonBody")


@_attrs_define
class CreateLoginsJsonBody:
    """
    Attributes:
        userid (Union[Unset, str]): The ID of the user to create the login for.
        loginunique_id (Union[Unset, str]): The unique ID for the new login.
    """

    userid: Union[Unset, str] = UNSET
    loginunique_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        userid = self.userid

        loginunique_id = self.loginunique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if userid is not UNSET:
            field_dict["user[id]"] = userid
        if loginunique_id is not UNSET:
            field_dict["login[unique_id]"] = loginunique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        userid = d.pop("user[id]", UNSET)

        loginunique_id = d.pop("login[unique_id]", UNSET)

        create_logins_json_body = cls(
            userid=userid,
            loginunique_id=loginunique_id,
        )

        create_logins_json_body.additional_properties = d
        return create_logins_json_body

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
