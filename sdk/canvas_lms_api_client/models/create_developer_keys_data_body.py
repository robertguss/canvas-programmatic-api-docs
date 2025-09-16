from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDeveloperKeysDataBody")


@_attrs_define
class CreateDeveloperKeysDataBody:
    """
    Attributes:
        developer_key (Union[Unset, str]): no description
        developer_keyredirect_uris (Union[Unset, str]): List of URLs used during OAuth2 flow to validate given redirect
            URI.
        developer_keyscopes (Union[Unset, str]): List of API endpoints key is allowed to access.
    """

    developer_key: Union[Unset, str] = UNSET
    developer_keyredirect_uris: Union[Unset, str] = UNSET
    developer_keyscopes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        developer_key = self.developer_key

        developer_keyredirect_uris = self.developer_keyredirect_uris

        developer_keyscopes = self.developer_keyscopes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if developer_key is not UNSET:
            field_dict["developer_key"] = developer_key
        if developer_keyredirect_uris is not UNSET:
            field_dict["developer_key[redirect_uris]"] = developer_keyredirect_uris
        if developer_keyscopes is not UNSET:
            field_dict["developer_key[scopes]"] = developer_keyscopes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        developer_key = d.pop("developer_key", UNSET)

        developer_keyredirect_uris = d.pop("developer_key[redirect_uris]", UNSET)

        developer_keyscopes = d.pop("developer_key[scopes]", UNSET)

        create_developer_keys_data_body = cls(
            developer_key=developer_key,
            developer_keyredirect_uris=developer_keyredirect_uris,
            developer_keyscopes=developer_keyscopes,
        )

        create_developer_keys_data_body.additional_properties = d
        return create_developer_keys_data_body

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
