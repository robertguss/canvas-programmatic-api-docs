from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetOriginalityReportResponse200")


@_attrs_define
class GetOriginalityReportResponse200:
    """
    Attributes:
        id (int):
        file_id (int):
        originality_score (float):
        originality_report_file_id (int):
        originality_report_url (str):
        tool_setting (None):
        error_report (None):
        submission_time (None):
        root_account_id (int):
    """

    id: int
    file_id: int
    originality_score: float
    originality_report_file_id: int
    originality_report_url: str
    tool_setting: None
    error_report: None
    submission_time: None
    root_account_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_id = self.file_id

        originality_score = self.originality_score

        originality_report_file_id = self.originality_report_file_id

        originality_report_url = self.originality_report_url

        tool_setting = self.tool_setting

        error_report = self.error_report

        submission_time = self.submission_time

        root_account_id = self.root_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "file_id": file_id,
                "originality_score": originality_score,
                "originality_report_file_id": originality_report_file_id,
                "originality_report_url": originality_report_url,
                "tool_setting": tool_setting,
                "error_report": error_report,
                "submission_time": submission_time,
                "root_account_id": root_account_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        file_id = d.pop("file_id")

        originality_score = d.pop("originality_score")

        originality_report_file_id = d.pop("originality_report_file_id")

        originality_report_url = d.pop("originality_report_url")

        tool_setting = d.pop("tool_setting")

        error_report = d.pop("error_report")

        submission_time = d.pop("submission_time")

        root_account_id = d.pop("root_account_id")

        get_originality_report_response_200 = cls(
            id=id,
            file_id=file_id,
            originality_score=originality_score,
            originality_report_file_id=originality_report_file_id,
            originality_report_url=originality_report_url,
            tool_setting=tool_setting,
            error_report=error_report,
            submission_time=submission_time,
            root_account_id=root_account_id,
        )

        get_originality_report_response_200.additional_properties = d
        return get_originality_report_response_200

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
