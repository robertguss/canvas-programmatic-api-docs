from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizAssignmentOverride")


@_attrs_define
class QuizAssignmentOverride:
    """
    Attributes:
        id (int):
        due_at (str):
        unlock_at (None):
        lock_at (str):
        title (str):
        base (bool):
    """

    id: int
    due_at: str
    unlock_at: None
    lock_at: str
    title: str
    base: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        title = self.title

        base = self.base

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "due_at": due_at,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
                "title": title,
                "base": base,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        due_at = d.pop("due_at")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        title = d.pop("title")

        base = d.pop("base")

        quiz_assignment_override = cls(
            id=id,
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
            title=title,
            base=base,
        )

        quiz_assignment_override.additional_properties = d
        return quiz_assignment_override

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
