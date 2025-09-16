from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExternalToolsDataBody")


@_attrs_define
class CreateExternalToolsDataBody:
    r"""
    Attributes:
        client_id (Union[Unset, str]): The client id is attached to the developer key. If supplied all other parameters
            are unnecessary and will be ignored
        name (Union[Unset, str]): The name of the tool
        privacy_level (Union[Unset, str]): How much user information to send to the external tool.Allowed values:
            anonymous, name_only, email_only, public
        consumer_key (Union[Unset, str]): The consumer key for the external tool
        shared_secret (Union[Unset, str]): The shared secret with the external tool
        placement_nameplacement_configuration_key (Union[Unset, str]): Set the \ value for a specific placement.
    """

    client_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    privacy_level: Union[Unset, str] = UNSET
    consumer_key: Union[Unset, str] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    placement_nameplacement_configuration_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        name = self.name

        privacy_level = self.privacy_level

        consumer_key = self.consumer_key

        shared_secret = self.shared_secret

        placement_nameplacement_configuration_key = self.placement_nameplacement_configuration_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if name is not UNSET:
            field_dict["name"] = name
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if consumer_key is not UNSET:
            field_dict["consumer_key"] = consumer_key
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if placement_nameplacement_configuration_key is not UNSET:
            field_dict["<placement_name>[<placement_configuration_key>]"] = placement_nameplacement_configuration_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id", UNSET)

        name = d.pop("name", UNSET)

        privacy_level = d.pop("privacy_level", UNSET)

        consumer_key = d.pop("consumer_key", UNSET)

        shared_secret = d.pop("shared_secret", UNSET)

        placement_nameplacement_configuration_key = d.pop("<placement_name>[<placement_configuration_key>]", UNSET)

        create_external_tools_data_body = cls(
            client_id=client_id,
            name=name,
            privacy_level=privacy_level,
            consumer_key=consumer_key,
            shared_secret=shared_secret,
            placement_nameplacement_configuration_key=placement_nameplacement_configuration_key,
        )

        create_external_tools_data_body.additional_properties = d
        return create_external_tools_data_body

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
