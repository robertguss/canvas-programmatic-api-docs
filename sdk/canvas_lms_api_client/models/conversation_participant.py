from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConversationParticipant")


@_attrs_define
class ConversationParticipant:
    """
    Attributes:
        id (int):
        name (str):
        full_name (str):
        avatar_url (str):
        uuid (str):
    """

    id: int
    name: str
    full_name: str
    avatar_url: str
    uuid: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        full_name = self.full_name

        avatar_url = self.avatar_url

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "full_name": full_name,
                "avatar_url": avatar_url,
                "uuid": uuid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        full_name = d.pop("full_name")

        avatar_url = d.pop("avatar_url")

        uuid = d.pop("uuid")

        conversation_participant = cls(
            id=id,
            name=name,
            full_name=full_name,
            avatar_url=avatar_url,
            uuid=uuid,
        )

        conversation_participant.additional_properties = d
        return conversation_participant

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
