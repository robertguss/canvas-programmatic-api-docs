from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizStatistics")


@_attrs_define
class QuizStatistics:
    """
    Attributes:
        id (int):
        quiz_id (int):
        multiple_attempts_exist (bool):
        includes_all_versions (bool):
        generated_at (str):
        url (str):
        html_url (str):
        question_statistics (None):
        submission_statistics (None):
        links (None):
    """

    id: int
    quiz_id: int
    multiple_attempts_exist: bool
    includes_all_versions: bool
    generated_at: str
    url: str
    html_url: str
    question_statistics: None
    submission_statistics: None
    links: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quiz_id = self.quiz_id

        multiple_attempts_exist = self.multiple_attempts_exist

        includes_all_versions = self.includes_all_versions

        generated_at = self.generated_at

        url = self.url

        html_url = self.html_url

        question_statistics = self.question_statistics

        submission_statistics = self.submission_statistics

        links = self.links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quiz_id": quiz_id,
                "multiple_attempts_exist": multiple_attempts_exist,
                "includes_all_versions": includes_all_versions,
                "generated_at": generated_at,
                "url": url,
                "html_url": html_url,
                "question_statistics": question_statistics,
                "submission_statistics": submission_statistics,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quiz_id = d.pop("quiz_id")

        multiple_attempts_exist = d.pop("multiple_attempts_exist")

        includes_all_versions = d.pop("includes_all_versions")

        generated_at = d.pop("generated_at")

        url = d.pop("url")

        html_url = d.pop("html_url")

        question_statistics = d.pop("question_statistics")

        submission_statistics = d.pop("submission_statistics")

        links = d.pop("links")

        quiz_statistics = cls(
            id=id,
            quiz_id=quiz_id,
            multiple_attempts_exist=multiple_attempts_exist,
            includes_all_versions=includes_all_versions,
            generated_at=generated_at,
            url=url,
            html_url=html_url,
            question_statistics=question_statistics,
            submission_statistics=submission_statistics,
            links=links,
        )

        quiz_statistics.additional_properties = d
        return quiz_statistics

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
