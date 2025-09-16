from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountsJsonBody")


@_attrs_define
class UpdateAccountsJsonBody:
    """
    Attributes:
        accountsettingspassword_policy (str): Hash of optional password policy configuration parameters for a root
            accountallow_login_suspension booleanAllow suspension of user logins upon reaching
            maximum_login_attemptsrequire_number_characters booleanRequire the use of number characters when setting up a
            new passwordrequire_symbol_characters booleanRequire the use of symbol characters when setting up a new
            passwordminimum_character_length integerMinimum number of characters required for a new
            passwordmaximum_login_attempts integerMaximum number of login attempts before a user is locked outRequired
            feature option:Enhance password options
        accountservices (Union[Unset, str]): Give this a set of keys and boolean values to enable or disable services
            matching the keys
    """

    accountsettingspassword_policy: str
    accountservices: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accountsettingspassword_policy = self.accountsettingspassword_policy

        accountservices = self.accountservices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account[settings][password_policy]": accountsettingspassword_policy,
            }
        )
        if accountservices is not UNSET:
            field_dict["account[services]"] = accountservices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accountsettingspassword_policy = d.pop("account[settings][password_policy]")

        accountservices = d.pop("account[services]", UNSET)

        update_accounts_json_body = cls(
            accountsettingspassword_policy=accountsettingspassword_policy,
            accountservices=accountservices,
        )

        update_accounts_json_body.additional_properties = d
        return update_accounts_json_body

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
