from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteCommunicationChannelsResponse200")


@_attrs_define
class DeleteCommunicationChannelsResponse200:
    """
    Attributes:
        id (int):
        address (str):
        type_ (str):
        position (int):
        user_id (int):
        bounce_count (int):
        last_bounce_at (str):
        workflow_state (str):
    """

    id: int
    address: str
    type_: str
    position: int
    user_id: int
    bounce_count: int
    last_bounce_at: str
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address

        type_ = self.type_

        position = self.position

        user_id = self.user_id

        bounce_count = self.bounce_count

        last_bounce_at = self.last_bounce_at

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "address": address,
                "type": type_,
                "position": position,
                "user_id": user_id,
                "bounce_count": bounce_count,
                "last_bounce_at": last_bounce_at,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        address = d.pop("address")

        type_ = d.pop("type")

        position = d.pop("position")

        user_id = d.pop("user_id")

        bounce_count = d.pop("bounce_count")

        last_bounce_at = d.pop("last_bounce_at")

        workflow_state = d.pop("workflow_state")

        delete_communication_channels_response_200 = cls(
            id=id,
            address=address,
            type_=type_,
            position=position,
            user_id=user_id,
            bounce_count=bounce_count,
            last_bounce_at=last_bounce_at,
            workflow_state=workflow_state,
        )

        delete_communication_channels_response_200.additional_properties = d
        return delete_communication_channels_response_200

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
