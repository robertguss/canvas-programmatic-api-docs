from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TurnitinSettings")


@_attrs_define
class TurnitinSettings:
    """
    Attributes:
        originality_report_visibility (str):
        s_paper_check (bool):
        internet_check (bool):
        journal_check (bool):
        exclude_biblio (bool):
        exclude_quoted (bool):
        exclude_small_matches_type (str):
        exclude_small_matches_value (int):
    """

    originality_report_visibility: str
    s_paper_check: bool
    internet_check: bool
    journal_check: bool
    exclude_biblio: bool
    exclude_quoted: bool
    exclude_small_matches_type: str
    exclude_small_matches_value: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        originality_report_visibility = self.originality_report_visibility

        s_paper_check = self.s_paper_check

        internet_check = self.internet_check

        journal_check = self.journal_check

        exclude_biblio = self.exclude_biblio

        exclude_quoted = self.exclude_quoted

        exclude_small_matches_type = self.exclude_small_matches_type

        exclude_small_matches_value = self.exclude_small_matches_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "originality_report_visibility": originality_report_visibility,
                "s_paper_check": s_paper_check,
                "internet_check": internet_check,
                "journal_check": journal_check,
                "exclude_biblio": exclude_biblio,
                "exclude_quoted": exclude_quoted,
                "exclude_small_matches_type": exclude_small_matches_type,
                "exclude_small_matches_value": exclude_small_matches_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        originality_report_visibility = d.pop("originality_report_visibility")

        s_paper_check = d.pop("s_paper_check")

        internet_check = d.pop("internet_check")

        journal_check = d.pop("journal_check")

        exclude_biblio = d.pop("exclude_biblio")

        exclude_quoted = d.pop("exclude_quoted")

        exclude_small_matches_type = d.pop("exclude_small_matches_type")

        exclude_small_matches_value = d.pop("exclude_small_matches_value")

        turnitin_settings = cls(
            originality_report_visibility=originality_report_visibility,
            s_paper_check=s_paper_check,
            internet_check=internet_check,
            journal_check=journal_check,
            exclude_biblio=exclude_biblio,
            exclude_quoted=exclude_quoted,
            exclude_small_matches_type=exclude_small_matches_type,
            exclude_small_matches_value=exclude_small_matches_value,
        )

        turnitin_settings.additional_properties = d
        return turnitin_settings

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
