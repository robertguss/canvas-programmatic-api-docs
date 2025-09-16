from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_total_results import PollTotalResults


T = TypeVar("T", bound="Poll")


@_attrs_define
class Poll:
    """
    Attributes:
        id (int):
        question (str):
        description (str):
        created_at (str):
        user_id (int):
        total_results (PollTotalResults):
    """

    id: int
    question: str
    description: str
    created_at: str
    user_id: int
    total_results: "PollTotalResults"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        question = self.question

        description = self.description

        created_at = self.created_at

        user_id = self.user_id

        total_results = self.total_results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "question": question,
                "description": description,
                "created_at": created_at,
                "user_id": user_id,
                "total_results": total_results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_total_results import PollTotalResults

        d = dict(src_dict)
        id = d.pop("id")

        question = d.pop("question")

        description = d.pop("description")

        created_at = d.pop("created_at")

        user_id = d.pop("user_id")

        total_results = PollTotalResults.from_dict(d.pop("total_results"))

        poll = cls(
            id=id,
            question=question,
            description=description,
            created_at=created_at,
            user_id=user_id,
            total_results=total_results,
        )

        poll.additional_properties = d
        return poll

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
