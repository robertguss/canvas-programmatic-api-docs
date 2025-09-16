from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCommunicationChannelsDataBody")


@_attrs_define
class CreateCommunicationChannelsDataBody:
    """
    Attributes:
        communication_channeladdress (str): An email address or SMS number. Not required for “push” type channels.
        communication_channeltype (Union[Unset, str]): The type of communication channel.In order to enable push
            notification support, the server must be properly configured (via ‘sns_credsin Vault) to communicate with Amazon
            Simple Notification Services, and the developer key used to create the access token from this request must have
            an SNS ARN configured on it.</p> Allowed values:email, sms, push`
    """

    communication_channeladdress: str
    communication_channeltype: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communication_channeladdress = self.communication_channeladdress

        communication_channeltype = self.communication_channeltype

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "communication_channel[address]": communication_channeladdress,
            }
        )
        if communication_channeltype is not UNSET:
            field_dict["communication_channel[type]"] = communication_channeltype

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        communication_channeladdress = d.pop("communication_channel[address]")

        communication_channeltype = d.pop("communication_channel[type]", UNSET)

        create_communication_channels_data_body = cls(
            communication_channeladdress=communication_channeladdress,
            communication_channeltype=communication_channeltype,
        )

        create_communication_channels_data_body.additional_properties = d
        return create_communication_channels_data_body

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
