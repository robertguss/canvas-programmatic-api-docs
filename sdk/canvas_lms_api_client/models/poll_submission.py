from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PollSubmission")


@_attrs_define
class PollSubmission:
    """
    Attributes:
        id (int):
        poll_choice_id (int):
        user_id (int):
        created_at (str):
    """

    id: int
    poll_choice_id: int
    user_id: int
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        poll_choice_id = self.poll_choice_id

        user_id = self.user_id

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "poll_choice_id": poll_choice_id,
                "user_id": user_id,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        poll_choice_id = d.pop("poll_choice_id")

        user_id = d.pop("user_id")

        created_at = d.pop("created_at")

        poll_submission = cls(
            id=id,
            poll_choice_id=poll_choice_id,
            user_id=user_id,
            created_at=created_at,
        )

        poll_submission.additional_properties = d
        return poll_submission

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
