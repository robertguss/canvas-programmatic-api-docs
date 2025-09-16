from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTokensDataBody")


@_attrs_define
class CreateTokensDataBody:
    """
    Attributes:
        tokenpurpose (Union[Unset, str]): The purpose of the token.
        tokenexpires_at (Union[Unset, str]): The time at which the token will expire.
        tokenscopes (Union[Unset, str]): The scopes to associate with the token. Ignored if the default developer key
            does not have the “enable scopes” option enabled. In such cases, the token will inherit the user’s permissions
            instead.
    """

    tokenpurpose: Union[Unset, str] = UNSET
    tokenexpires_at: Union[Unset, str] = UNSET
    tokenscopes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tokenpurpose = self.tokenpurpose

        tokenexpires_at = self.tokenexpires_at

        tokenscopes = self.tokenscopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tokenpurpose is not UNSET:
            field_dict["token[purpose]"] = tokenpurpose
        if tokenexpires_at is not UNSET:
            field_dict["token[expires_at]"] = tokenexpires_at
        if tokenscopes is not UNSET:
            field_dict["token[scopes][]"] = tokenscopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        tokenpurpose = d.pop("token[purpose]", UNSET)

        tokenexpires_at = d.pop("token[expires_at]", UNSET)

        tokenscopes = d.pop("token[scopes][]", UNSET)

        create_tokens_data_body = cls(
            tokenpurpose=tokenpurpose,
            tokenexpires_at=tokenexpires_at,
            tokenscopes=tokenscopes,
        )

        create_tokens_data_body.additional_properties = d
        return create_tokens_data_body

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
