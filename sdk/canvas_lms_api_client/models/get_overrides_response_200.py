from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetOverridesResponse200")


@_attrs_define
class GetOverridesResponse200:
    """
    Attributes:
        id (int):
        assignment_id (int):
        quiz_id (int):
        context_module_id (int):
        discussion_topic_id (int):
        wiki_page_id (int):
        attachment_id (int):
        student_ids (list[int]):
        group_id (int):
        course_section_id (int):
        title (str):
        due_at (str):
        all_day (bool):
        all_day_date (str):
        unlock_at (str):
        lock_at (str):
    """

    id: int
    assignment_id: int
    quiz_id: int
    context_module_id: int
    discussion_topic_id: int
    wiki_page_id: int
    attachment_id: int
    student_ids: list[int]
    group_id: int
    course_section_id: int
    title: str
    due_at: str
    all_day: bool
    all_day_date: str
    unlock_at: str
    lock_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        assignment_id = self.assignment_id

        quiz_id = self.quiz_id

        context_module_id = self.context_module_id

        discussion_topic_id = self.discussion_topic_id

        wiki_page_id = self.wiki_page_id

        attachment_id = self.attachment_id

        student_ids = self.student_ids

        group_id = self.group_id

        course_section_id = self.course_section_id

        title = self.title

        due_at = self.due_at

        all_day = self.all_day

        all_day_date = self.all_day_date

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "assignment_id": assignment_id,
                "quiz_id": quiz_id,
                "context_module_id": context_module_id,
                "discussion_topic_id": discussion_topic_id,
                "wiki_page_id": wiki_page_id,
                "attachment_id": attachment_id,
                "student_ids": student_ids,
                "group_id": group_id,
                "course_section_id": course_section_id,
                "title": title,
                "due_at": due_at,
                "all_day": all_day,
                "all_day_date": all_day_date,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        assignment_id = d.pop("assignment_id")

        quiz_id = d.pop("quiz_id")

        context_module_id = d.pop("context_module_id")

        discussion_topic_id = d.pop("discussion_topic_id")

        wiki_page_id = d.pop("wiki_page_id")

        attachment_id = d.pop("attachment_id")

        student_ids = cast(list[int], d.pop("student_ids"))

        group_id = d.pop("group_id")

        course_section_id = d.pop("course_section_id")

        title = d.pop("title")

        due_at = d.pop("due_at")

        all_day = d.pop("all_day")

        all_day_date = d.pop("all_day_date")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        get_overrides_response_200 = cls(
            id=id,
            assignment_id=assignment_id,
            quiz_id=quiz_id,
            context_module_id=context_module_id,
            discussion_topic_id=discussion_topic_id,
            wiki_page_id=wiki_page_id,
            attachment_id=attachment_id,
            student_ids=student_ids,
            group_id=group_id,
            course_section_id=course_section_id,
            title=title,
            due_at=due_at,
            all_day=all_day,
            all_day_date=all_day_date,
            unlock_at=unlock_at,
            lock_at=lock_at,
        )

        get_overrides_response_200.additional_properties = d
        return get_overrides_response_200

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
