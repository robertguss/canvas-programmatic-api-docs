from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizReport")


@_attrs_define
class QuizReport:
    """
    Attributes:
        id (int):
        quiz_id (int):
        report_type (str):
        readable_type (str):
        includes_all_versions (bool):
        anonymous (bool):
        generatable (bool):
        created_at (str):
        updated_at (str):
        url (str):
        file (None):
        progress_url (None):
        progress (None):
    """

    id: int
    quiz_id: int
    report_type: str
    readable_type: str
    includes_all_versions: bool
    anonymous: bool
    generatable: bool
    created_at: str
    updated_at: str
    url: str
    file: None
    progress_url: None
    progress: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        quiz_id = self.quiz_id

        report_type = self.report_type

        readable_type = self.readable_type

        includes_all_versions = self.includes_all_versions

        anonymous = self.anonymous

        generatable = self.generatable

        created_at = self.created_at

        updated_at = self.updated_at

        url = self.url

        file = self.file

        progress_url = self.progress_url

        progress = self.progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "quiz_id": quiz_id,
                "report_type": report_type,
                "readable_type": readable_type,
                "includes_all_versions": includes_all_versions,
                "anonymous": anonymous,
                "generatable": generatable,
                "created_at": created_at,
                "updated_at": updated_at,
                "url": url,
                "file": file,
                "progress_url": progress_url,
                "progress": progress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        quiz_id = d.pop("quiz_id")

        report_type = d.pop("report_type")

        readable_type = d.pop("readable_type")

        includes_all_versions = d.pop("includes_all_versions")

        anonymous = d.pop("anonymous")

        generatable = d.pop("generatable")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        url = d.pop("url")

        file = d.pop("file")

        progress_url = d.pop("progress_url")

        progress = d.pop("progress")

        quiz_report = cls(
            id=id,
            quiz_id=quiz_id,
            report_type=report_type,
            readable_type=readable_type,
            includes_all_versions=includes_all_versions,
            anonymous=anonymous,
            generatable=generatable,
            created_at=created_at,
            updated_at=updated_at,
            url=url,
            file=file,
            progress_url=progress_url,
            progress=progress,
        )

        quiz_report.additional_properties = d
        return quiz_report

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
