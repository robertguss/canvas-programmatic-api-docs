from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_details_lock_info import ContentDetailsLockInfo


T = TypeVar("T", bound="ContentDetails")


@_attrs_define
class ContentDetails:
    """
    Attributes:
        points_possible (int):
        due_at (str):
        unlock_at (str):
        lock_at (str):
        locked_for_user (bool):
        lock_explanation (str):
        lock_info (ContentDetailsLockInfo):
    """

    points_possible: int
    due_at: str
    unlock_at: str
    lock_at: str
    locked_for_user: bool
    lock_explanation: str
    lock_info: "ContentDetailsLockInfo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        points_possible = self.points_possible

        due_at = self.due_at

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        locked_for_user = self.locked_for_user

        lock_explanation = self.lock_explanation

        lock_info = self.lock_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "points_possible": points_possible,
                "due_at": due_at,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
                "locked_for_user": locked_for_user,
                "lock_explanation": lock_explanation,
                "lock_info": lock_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_details_lock_info import ContentDetailsLockInfo

        d = dict(src_dict)
        points_possible = d.pop("points_possible")

        due_at = d.pop("due_at")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        locked_for_user = d.pop("locked_for_user")

        lock_explanation = d.pop("lock_explanation")

        lock_info = ContentDetailsLockInfo.from_dict(d.pop("lock_info"))

        content_details = cls(
            points_possible=points_possible,
            due_at=due_at,
            unlock_at=unlock_at,
            lock_at=lock_at,
            locked_for_user=locked_for_user,
            lock_explanation=lock_explanation,
            lock_info=lock_info,
        )

        content_details.additional_properties = d
        return content_details

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
