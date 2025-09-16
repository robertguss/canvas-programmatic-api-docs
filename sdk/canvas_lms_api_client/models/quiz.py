from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Quiz")


@_attrs_define
class Quiz:
    """
    Attributes:
        id (int):
        title (str):
        html_url (str):
        mobile_url (str):
        preview_url (str):
        description (str):
        quiz_type (str):
        assignment_group_id (int):
        time_limit (int):
        shuffle_answers (bool):
        hide_results (str):
        show_correct_answers (bool):
        show_correct_answers_last_attempt (bool):
        show_correct_answers_at (str):
        hide_correct_answers_at (str):
        one_time_results (bool):
        scoring_policy (str):
        allowed_attempts (int):
        one_question_at_a_time (bool):
        question_count (int):
        points_possible (int):
        cant_go_back (bool):
        access_code (str):
        ip_filter (str):
        due_at (str):
        lock_at (None):
        unlock_at (str):
        published (bool):
        unpublishable (bool):
        locked_for_user (bool):
        lock_info (None):
        lock_explanation (str):
        speedgrader_url (str):
        quiz_extensions_url (str):
        permissions (None):
        all_dates (None):
        version_number (int):
        question_types (list[str]):
        anonymous_submissions (bool):
    """

    id: int
    title: str
    html_url: str
    mobile_url: str
    preview_url: str
    description: str
    quiz_type: str
    assignment_group_id: int
    time_limit: int
    shuffle_answers: bool
    hide_results: str
    show_correct_answers: bool
    show_correct_answers_last_attempt: bool
    show_correct_answers_at: str
    hide_correct_answers_at: str
    one_time_results: bool
    scoring_policy: str
    allowed_attempts: int
    one_question_at_a_time: bool
    question_count: int
    points_possible: int
    cant_go_back: bool
    access_code: str
    ip_filter: str
    due_at: str
    lock_at: None
    unlock_at: str
    published: bool
    unpublishable: bool
    locked_for_user: bool
    lock_info: None
    lock_explanation: str
    speedgrader_url: str
    quiz_extensions_url: str
    permissions: None
    all_dates: None
    version_number: int
    question_types: list[str]
    anonymous_submissions: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        html_url = self.html_url

        mobile_url = self.mobile_url

        preview_url = self.preview_url

        description = self.description

        quiz_type = self.quiz_type

        assignment_group_id = self.assignment_group_id

        time_limit = self.time_limit

        shuffle_answers = self.shuffle_answers

        hide_results = self.hide_results

        show_correct_answers = self.show_correct_answers

        show_correct_answers_last_attempt = self.show_correct_answers_last_attempt

        show_correct_answers_at = self.show_correct_answers_at

        hide_correct_answers_at = self.hide_correct_answers_at

        one_time_results = self.one_time_results

        scoring_policy = self.scoring_policy

        allowed_attempts = self.allowed_attempts

        one_question_at_a_time = self.one_question_at_a_time

        question_count = self.question_count

        points_possible = self.points_possible

        cant_go_back = self.cant_go_back

        access_code = self.access_code

        ip_filter = self.ip_filter

        due_at = self.due_at

        lock_at = self.lock_at

        unlock_at = self.unlock_at

        published = self.published

        unpublishable = self.unpublishable

        locked_for_user = self.locked_for_user

        lock_info = self.lock_info

        lock_explanation = self.lock_explanation

        speedgrader_url = self.speedgrader_url

        quiz_extensions_url = self.quiz_extensions_url

        permissions = self.permissions

        all_dates = self.all_dates

        version_number = self.version_number

        question_types = self.question_types

        anonymous_submissions = self.anonymous_submissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "html_url": html_url,
                "mobile_url": mobile_url,
                "preview_url": preview_url,
                "description": description,
                "quiz_type": quiz_type,
                "assignment_group_id": assignment_group_id,
                "time_limit": time_limit,
                "shuffle_answers": shuffle_answers,
                "hide_results": hide_results,
                "show_correct_answers": show_correct_answers,
                "show_correct_answers_last_attempt": show_correct_answers_last_attempt,
                "show_correct_answers_at": show_correct_answers_at,
                "hide_correct_answers_at": hide_correct_answers_at,
                "one_time_results": one_time_results,
                "scoring_policy": scoring_policy,
                "allowed_attempts": allowed_attempts,
                "one_question_at_a_time": one_question_at_a_time,
                "question_count": question_count,
                "points_possible": points_possible,
                "cant_go_back": cant_go_back,
                "access_code": access_code,
                "ip_filter": ip_filter,
                "due_at": due_at,
                "lock_at": lock_at,
                "unlock_at": unlock_at,
                "published": published,
                "unpublishable": unpublishable,
                "locked_for_user": locked_for_user,
                "lock_info": lock_info,
                "lock_explanation": lock_explanation,
                "speedgrader_url": speedgrader_url,
                "quiz_extensions_url": quiz_extensions_url,
                "permissions": permissions,
                "all_dates": all_dates,
                "version_number": version_number,
                "question_types": question_types,
                "anonymous_submissions": anonymous_submissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        html_url = d.pop("html_url")

        mobile_url = d.pop("mobile_url")

        preview_url = d.pop("preview_url")

        description = d.pop("description")

        quiz_type = d.pop("quiz_type")

        assignment_group_id = d.pop("assignment_group_id")

        time_limit = d.pop("time_limit")

        shuffle_answers = d.pop("shuffle_answers")

        hide_results = d.pop("hide_results")

        show_correct_answers = d.pop("show_correct_answers")

        show_correct_answers_last_attempt = d.pop("show_correct_answers_last_attempt")

        show_correct_answers_at = d.pop("show_correct_answers_at")

        hide_correct_answers_at = d.pop("hide_correct_answers_at")

        one_time_results = d.pop("one_time_results")

        scoring_policy = d.pop("scoring_policy")

        allowed_attempts = d.pop("allowed_attempts")

        one_question_at_a_time = d.pop("one_question_at_a_time")

        question_count = d.pop("question_count")

        points_possible = d.pop("points_possible")

        cant_go_back = d.pop("cant_go_back")

        access_code = d.pop("access_code")

        ip_filter = d.pop("ip_filter")

        due_at = d.pop("due_at")

        lock_at = d.pop("lock_at")

        unlock_at = d.pop("unlock_at")

        published = d.pop("published")

        unpublishable = d.pop("unpublishable")

        locked_for_user = d.pop("locked_for_user")

        lock_info = d.pop("lock_info")

        lock_explanation = d.pop("lock_explanation")

        speedgrader_url = d.pop("speedgrader_url")

        quiz_extensions_url = d.pop("quiz_extensions_url")

        permissions = d.pop("permissions")

        all_dates = d.pop("all_dates")

        version_number = d.pop("version_number")

        question_types = cast(list[str], d.pop("question_types"))

        anonymous_submissions = d.pop("anonymous_submissions")

        quiz = cls(
            id=id,
            title=title,
            html_url=html_url,
            mobile_url=mobile_url,
            preview_url=preview_url,
            description=description,
            quiz_type=quiz_type,
            assignment_group_id=assignment_group_id,
            time_limit=time_limit,
            shuffle_answers=shuffle_answers,
            hide_results=hide_results,
            show_correct_answers=show_correct_answers,
            show_correct_answers_last_attempt=show_correct_answers_last_attempt,
            show_correct_answers_at=show_correct_answers_at,
            hide_correct_answers_at=hide_correct_answers_at,
            one_time_results=one_time_results,
            scoring_policy=scoring_policy,
            allowed_attempts=allowed_attempts,
            one_question_at_a_time=one_question_at_a_time,
            question_count=question_count,
            points_possible=points_possible,
            cant_go_back=cant_go_back,
            access_code=access_code,
            ip_filter=ip_filter,
            due_at=due_at,
            lock_at=lock_at,
            unlock_at=unlock_at,
            published=published,
            unpublishable=unpublishable,
            locked_for_user=locked_for_user,
            lock_info=lock_info,
            lock_explanation=lock_explanation,
            speedgrader_url=speedgrader_url,
            quiz_extensions_url=quiz_extensions_url,
            permissions=permissions,
            all_dates=all_dates,
            version_number=version_number,
            question_types=question_types,
            anonymous_submissions=anonymous_submissions,
        )

        quiz.additional_properties = d
        return quiz

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
