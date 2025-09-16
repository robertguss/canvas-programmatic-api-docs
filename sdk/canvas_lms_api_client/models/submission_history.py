from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmissionHistory")


@_attrs_define
class SubmissionHistory:
    """
    Attributes:
        submission_id (int):
        versions (None):
    """

    submission_id: int
    versions: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        submission_id = self.submission_id

        versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "submission_id": submission_id,
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        submission_id = d.pop("submission_id")

        versions = d.pop("versions")

        submission_history = cls(
            submission_id=submission_id,
            versions=versions,
        )

        submission_history.additional_properties = d
        return submission_history

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
