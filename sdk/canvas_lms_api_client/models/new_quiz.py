from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NewQuiz")


@_attrs_define
class NewQuiz:
    """
    Attributes:
        id (str):
        title (str):
        instructions (str):
        assignment_group_id (str):
        points_possible (int):
        due_at (str):
        lock_at (None):
        unlock_at (str):
        published (bool):
        grading_type (str):
        quiz_settings (None):
    """

    id: str
    title: str
    instructions: str
    assignment_group_id: str
    points_possible: int
    due_at: str
    lock_at: None
    unlock_at: str
    published: bool
    grading_type: str
    quiz_settings: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        instructions = self.instructions

        assignment_group_id = self.assignment_group_id

        points_possible = self.points_possible

        due_at = self.due_at

        lock_at = self.lock_at

        unlock_at = self.unlock_at

        published = self.published

        grading_type = self.grading_type

        quiz_settings = self.quiz_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "instructions": instructions,
                "assignment_group_id": assignment_group_id,
                "points_possible": points_possible,
                "due_at": due_at,
                "lock_at": lock_at,
                "unlock_at": unlock_at,
                "published": published,
                "grading_type": grading_type,
                "quiz_settings": quiz_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        instructions = d.pop("instructions")

        assignment_group_id = d.pop("assignment_group_id")

        points_possible = d.pop("points_possible")

        due_at = d.pop("due_at")

        lock_at = d.pop("lock_at")

        unlock_at = d.pop("unlock_at")

        published = d.pop("published")

        grading_type = d.pop("grading_type")

        quiz_settings = d.pop("quiz_settings")

        new_quiz = cls(
            id=id,
            title=title,
            instructions=instructions,
            assignment_group_id=assignment_group_id,
            points_possible=points_possible,
            due_at=due_at,
            lock_at=lock_at,
            unlock_at=unlock_at,
            published=published,
            grading_type=grading_type,
            quiz_settings=quiz_settings,
        )

        new_quiz.additional_properties = d
        return new_quiz

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
