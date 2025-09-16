from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateQuizzesDataBody")


@_attrs_define
class CreateQuizzesDataBody:
    """
    Attributes:
        quizquiz_settingsmultiple_attemptscooling_period_seconds (str): Required waiting period in seconds between
            attempts. If null, there is no required time. Only used if cooling_period is true
        course_id (Union[Unset, str]): no description
        quizpoints_possible (Union[Unset, str]): The total point value given to the quiz. Must be positive.
        quizdue_at (Union[Unset, str]): When the quiz is due.
        quizlock_at (Union[Unset, str]): When to lock the quiz.
        quizunlock_at (Union[Unset, str]): When to unlock the quiz.
        quizquiz_settingsmultiple_attemptsmax_attempts (Union[Unset, str]): The allowed attempts a student can take. If
            null, the allowed attempts are unlimited. Only used if attempt_limit is true.
        quizquiz_settingsresult_view_settingsshow_item_responses_at (Union[Unset, str]): When student responses should
            be shown to them. Only used if display_item_response is true.
        quizquiz_settingsresult_view_settingshide_item_responses_at (Union[Unset, str]): When student responses should
            be hidden from them. Only used if display_item_response is true.
        quizquiz_settingsresult_view_settingsshow_item_response_correctness_at (Union[Unset, str]): When student
            response correctness should be shown to them. Only used if display_item_response_correctness is true.
        quizquiz_settingsresult_view_settingshide_item_response_correctness_at (Union[Unset, str]): When student
            response correctness should be hidden from them. Only used if display_item_response_correctness is true.
        quizquiz_settingssession_time_limit_in_seconds (Union[Unset, str]): Limit the time a student can work on the
            quiz. Should be null if no restriction.
    """

    quizquiz_settingsmultiple_attemptscooling_period_seconds: str
    course_id: Union[Unset, str] = UNSET
    quizpoints_possible: Union[Unset, str] = UNSET
    quizdue_at: Union[Unset, str] = UNSET
    quizlock_at: Union[Unset, str] = UNSET
    quizunlock_at: Union[Unset, str] = UNSET
    quizquiz_settingsmultiple_attemptsmax_attempts: Union[Unset, str] = UNSET
    quizquiz_settingsresult_view_settingsshow_item_responses_at: Union[Unset, str] = UNSET
    quizquiz_settingsresult_view_settingshide_item_responses_at: Union[Unset, str] = UNSET
    quizquiz_settingsresult_view_settingsshow_item_response_correctness_at: Union[Unset, str] = UNSET
    quizquiz_settingsresult_view_settingshide_item_response_correctness_at: Union[Unset, str] = UNSET
    quizquiz_settingssession_time_limit_in_seconds: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quizquiz_settingsmultiple_attemptscooling_period_seconds = (
            self.quizquiz_settingsmultiple_attemptscooling_period_seconds
        )

        course_id = self.course_id

        quizpoints_possible = self.quizpoints_possible

        quizdue_at = self.quizdue_at

        quizlock_at = self.quizlock_at

        quizunlock_at = self.quizunlock_at

        quizquiz_settingsmultiple_attemptsmax_attempts = self.quizquiz_settingsmultiple_attemptsmax_attempts

        quizquiz_settingsresult_view_settingsshow_item_responses_at = (
            self.quizquiz_settingsresult_view_settingsshow_item_responses_at
        )

        quizquiz_settingsresult_view_settingshide_item_responses_at = (
            self.quizquiz_settingsresult_view_settingshide_item_responses_at
        )

        quizquiz_settingsresult_view_settingsshow_item_response_correctness_at = (
            self.quizquiz_settingsresult_view_settingsshow_item_response_correctness_at
        )

        quizquiz_settingsresult_view_settingshide_item_response_correctness_at = (
            self.quizquiz_settingsresult_view_settingshide_item_response_correctness_at
        )

        quizquiz_settingssession_time_limit_in_seconds = self.quizquiz_settingssession_time_limit_in_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quiz[quiz_settings][multiple_attempts][cooling_period_seconds]": quizquiz_settingsmultiple_attemptscooling_period_seconds,
            }
        )
        if course_id is not UNSET:
            field_dict["course_id"] = course_id
        if quizpoints_possible is not UNSET:
            field_dict["quiz[points_possible]"] = quizpoints_possible
        if quizdue_at is not UNSET:
            field_dict["quiz[due_at]"] = quizdue_at
        if quizlock_at is not UNSET:
            field_dict["quiz[lock_at]"] = quizlock_at
        if quizunlock_at is not UNSET:
            field_dict["quiz[unlock_at]"] = quizunlock_at
        if quizquiz_settingsmultiple_attemptsmax_attempts is not UNSET:
            field_dict["quiz[quiz_settings][multiple_attempts][max_attempts]"] = (
                quizquiz_settingsmultiple_attemptsmax_attempts
            )
        if quizquiz_settingsresult_view_settingsshow_item_responses_at is not UNSET:
            field_dict["quiz[quiz_settings][result_view_settings][show_item_responses_at]"] = (
                quizquiz_settingsresult_view_settingsshow_item_responses_at
            )
        if quizquiz_settingsresult_view_settingshide_item_responses_at is not UNSET:
            field_dict["quiz[quiz_settings][result_view_settings][hide_item_responses_at]"] = (
                quizquiz_settingsresult_view_settingshide_item_responses_at
            )
        if quizquiz_settingsresult_view_settingsshow_item_response_correctness_at is not UNSET:
            field_dict["quiz[quiz_settings][result_view_settings][show_item_response_correctness_at]"] = (
                quizquiz_settingsresult_view_settingsshow_item_response_correctness_at
            )
        if quizquiz_settingsresult_view_settingshide_item_response_correctness_at is not UNSET:
            field_dict["quiz[quiz_settings][result_view_settings][hide_item_response_correctness_at]"] = (
                quizquiz_settingsresult_view_settingshide_item_response_correctness_at
            )
        if quizquiz_settingssession_time_limit_in_seconds is not UNSET:
            field_dict["quiz[quiz_settings][session_time_limit_in_seconds]"] = (
                quizquiz_settingssession_time_limit_in_seconds
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quizquiz_settingsmultiple_attemptscooling_period_seconds = d.pop(
            "quiz[quiz_settings][multiple_attempts][cooling_period_seconds]"
        )

        course_id = d.pop("course_id", UNSET)

        quizpoints_possible = d.pop("quiz[points_possible]", UNSET)

        quizdue_at = d.pop("quiz[due_at]", UNSET)

        quizlock_at = d.pop("quiz[lock_at]", UNSET)

        quizunlock_at = d.pop("quiz[unlock_at]", UNSET)

        quizquiz_settingsmultiple_attemptsmax_attempts = d.pop(
            "quiz[quiz_settings][multiple_attempts][max_attempts]", UNSET
        )

        quizquiz_settingsresult_view_settingsshow_item_responses_at = d.pop(
            "quiz[quiz_settings][result_view_settings][show_item_responses_at]", UNSET
        )

        quizquiz_settingsresult_view_settingshide_item_responses_at = d.pop(
            "quiz[quiz_settings][result_view_settings][hide_item_responses_at]", UNSET
        )

        quizquiz_settingsresult_view_settingsshow_item_response_correctness_at = d.pop(
            "quiz[quiz_settings][result_view_settings][show_item_response_correctness_at]", UNSET
        )

        quizquiz_settingsresult_view_settingshide_item_response_correctness_at = d.pop(
            "quiz[quiz_settings][result_view_settings][hide_item_response_correctness_at]", UNSET
        )

        quizquiz_settingssession_time_limit_in_seconds = d.pop(
            "quiz[quiz_settings][session_time_limit_in_seconds]", UNSET
        )

        create_quizzes_data_body = cls(
            quizquiz_settingsmultiple_attemptscooling_period_seconds=quizquiz_settingsmultiple_attemptscooling_period_seconds,
            course_id=course_id,
            quizpoints_possible=quizpoints_possible,
            quizdue_at=quizdue_at,
            quizlock_at=quizlock_at,
            quizunlock_at=quizunlock_at,
            quizquiz_settingsmultiple_attemptsmax_attempts=quizquiz_settingsmultiple_attemptsmax_attempts,
            quizquiz_settingsresult_view_settingsshow_item_responses_at=quizquiz_settingsresult_view_settingsshow_item_responses_at,
            quizquiz_settingsresult_view_settingshide_item_responses_at=quizquiz_settingsresult_view_settingshide_item_responses_at,
            quizquiz_settingsresult_view_settingsshow_item_response_correctness_at=quizquiz_settingsresult_view_settingsshow_item_response_correctness_at,
            quizquiz_settingsresult_view_settingshide_item_response_correctness_at=quizquiz_settingsresult_view_settingshide_item_response_correctness_at,
            quizquiz_settingssession_time_limit_in_seconds=quizquiz_settingssession_time_limit_in_seconds,
        )

        create_quizzes_data_body.additional_properties = d
        return create_quizzes_data_body

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
