from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollChoice")


@_attrs_define
class PollChoice:
    """
    Attributes:
        id (int):
        poll_id (int):
        is_correct (bool):
        text (str):
        position (int):
    """

    id: int
    poll_id: int
    is_correct: bool
    text: str
    position: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        poll_id = self.poll_id

        is_correct = self.is_correct

        text = self.text

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "poll_id": poll_id,
                "is_correct": is_correct,
                "text": text,
                "position": position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        poll_id = d.pop("poll_id")

        is_correct = d.pop("is_correct")

        text = d.pop("text")

        position = d.pop("position")

        poll_choice = cls(
            id=id,
            poll_id=poll_id,
            is_correct=is_correct,
            text=text,
            position=position,
        )

        poll_choice.additional_properties = d
        return poll_choice

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
