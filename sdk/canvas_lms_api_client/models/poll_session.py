from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.poll_session_results import PollSessionResults


T = TypeVar("T", bound="PollSession")


@_attrs_define
class PollSession:
    """
    Attributes:
        id (int):
        poll_id (int):
        course_id (int):
        course_section_id (int):
        is_published (bool):
        has_public_results (bool):
        created_at (str):
        results (PollSessionResults):
        poll_submissions (None):
    """

    id: int
    poll_id: int
    course_id: int
    course_section_id: int
    is_published: bool
    has_public_results: bool
    created_at: str
    results: "PollSessionResults"
    poll_submissions: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        poll_id = self.poll_id

        course_id = self.course_id

        course_section_id = self.course_section_id

        is_published = self.is_published

        has_public_results = self.has_public_results

        created_at = self.created_at

        results = self.results.to_dict()

        poll_submissions = self.poll_submissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "poll_id": poll_id,
                "course_id": course_id,
                "course_section_id": course_section_id,
                "is_published": is_published,
                "has_public_results": has_public_results,
                "created_at": created_at,
                "results": results,
                "poll_submissions": poll_submissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.poll_session_results import PollSessionResults

        d = dict(src_dict)
        id = d.pop("id")

        poll_id = d.pop("poll_id")

        course_id = d.pop("course_id")

        course_section_id = d.pop("course_section_id")

        is_published = d.pop("is_published")

        has_public_results = d.pop("has_public_results")

        created_at = d.pop("created_at")

        results = PollSessionResults.from_dict(d.pop("results"))

        poll_submissions = d.pop("poll_submissions")

        poll_session = cls(
            id=id,
            poll_id=poll_id,
            course_id=course_id,
            course_section_id=course_section_id,
            is_published=is_published,
            has_public_results=has_public_results,
            created_at=created_at,
            results=results,
            poll_submissions=poll_submissions,
        )

        poll_session.additional_properties = d
        return poll_session

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
