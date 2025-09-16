from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quiz_settings_filters import QuizSettingsFilters


T = TypeVar("T", bound="QuizSettings")


@_attrs_define
class QuizSettings:
    """
    Attributes:
        calculator_type (str):
        filter_ip_address (bool):
        filters (QuizSettingsFilters):
        one_at_a_time_type (str):
        allow_backtracking (bool):
        shuffle_answers (bool):
        shuffle_questions (bool):
        require_student_access_code (bool):
        student_access_code (str):
        has_time_limit (bool):
        session_time_limit_in_seconds (int):
        multiple_attempts (None):
        result_view_settings (None):
    """

    calculator_type: str
    filter_ip_address: bool
    filters: "QuizSettingsFilters"
    one_at_a_time_type: str
    allow_backtracking: bool
    shuffle_answers: bool
    shuffle_questions: bool
    require_student_access_code: bool
    student_access_code: str
    has_time_limit: bool
    session_time_limit_in_seconds: int
    multiple_attempts: None
    result_view_settings: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculator_type = self.calculator_type

        filter_ip_address = self.filter_ip_address

        filters = self.filters.to_dict()

        one_at_a_time_type = self.one_at_a_time_type

        allow_backtracking = self.allow_backtracking

        shuffle_answers = self.shuffle_answers

        shuffle_questions = self.shuffle_questions

        require_student_access_code = self.require_student_access_code

        student_access_code = self.student_access_code

        has_time_limit = self.has_time_limit

        session_time_limit_in_seconds = self.session_time_limit_in_seconds

        multiple_attempts = self.multiple_attempts

        result_view_settings = self.result_view_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculator_type": calculator_type,
                "filter_ip_address": filter_ip_address,
                "filters": filters,
                "one_at_a_time_type": one_at_a_time_type,
                "allow_backtracking": allow_backtracking,
                "shuffle_answers": shuffle_answers,
                "shuffle_questions": shuffle_questions,
                "require_student_access_code": require_student_access_code,
                "student_access_code": student_access_code,
                "has_time_limit": has_time_limit,
                "session_time_limit_in_seconds": session_time_limit_in_seconds,
                "multiple_attempts": multiple_attempts,
                "result_view_settings": result_view_settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quiz_settings_filters import QuizSettingsFilters

        d = dict(src_dict)
        calculator_type = d.pop("calculator_type")

        filter_ip_address = d.pop("filter_ip_address")

        filters = QuizSettingsFilters.from_dict(d.pop("filters"))

        one_at_a_time_type = d.pop("one_at_a_time_type")

        allow_backtracking = d.pop("allow_backtracking")

        shuffle_answers = d.pop("shuffle_answers")

        shuffle_questions = d.pop("shuffle_questions")

        require_student_access_code = d.pop("require_student_access_code")

        student_access_code = d.pop("student_access_code")

        has_time_limit = d.pop("has_time_limit")

        session_time_limit_in_seconds = d.pop("session_time_limit_in_seconds")

        multiple_attempts = d.pop("multiple_attempts")

        result_view_settings = d.pop("result_view_settings")

        quiz_settings = cls(
            calculator_type=calculator_type,
            filter_ip_address=filter_ip_address,
            filters=filters,
            one_at_a_time_type=one_at_a_time_type,
            allow_backtracking=allow_backtracking,
            shuffle_answers=shuffle_answers,
            shuffle_questions=shuffle_questions,
            require_student_access_code=require_student_access_code,
            student_access_code=student_access_code,
            has_time_limit=has_time_limit,
            session_time_limit_in_seconds=session_time_limit_in_seconds,
            multiple_attempts=multiple_attempts,
            result_view_settings=result_view_settings,
        )

        quiz_settings.additional_properties = d
        return quiz_settings

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
