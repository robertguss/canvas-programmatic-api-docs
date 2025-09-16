from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateConversationsDataBody")


@_attrs_define
class UpdateConversationsDataBody:
    """
    Attributes:
        conversation_ids (Union[Unset, str]): List of conversations to update. Limited to 500 conversations.
        event (Union[Unset, str]): The action to take on each conversation.Allowed values: mark_as_read, mark_as_unread,
            star, unstar, archive, destroy
    """

    conversation_ids: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation_ids = self.conversation_ids

        event = self.event

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conversation_ids is not UNSET:
            field_dict["conversation_ids[]"] = conversation_ids
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conversation_ids = d.pop("conversation_ids[]", UNSET)

        event = d.pop("event", UNSET)

        update_conversations_data_body = cls(
            conversation_ids=conversation_ids,
            event=event,
        )

        update_conversations_data_body.additional_properties = d
        return update_conversations_data_body

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
