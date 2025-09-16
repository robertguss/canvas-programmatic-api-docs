from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetGradersResponse200Item")


@_attrs_define
class GetGradersResponse200Item:
    """
    Attributes:
        id (str):
        created_at (str):
        event_type (str):
        excused_after (bool):
        excused_before (bool):
        grade_after (str):
        grade_before (str):
        graded_anonymously (bool):
        version_number (str):
        request_id (str):
        links (None):
    """

    id: str
    created_at: str
    event_type: str
    excused_after: bool
    excused_before: bool
    grade_after: str
    grade_before: str
    graded_anonymously: bool
    version_number: str
    request_id: str
    links: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        event_type = self.event_type

        excused_after = self.excused_after

        excused_before = self.excused_before

        grade_after = self.grade_after

        grade_before = self.grade_before

        graded_anonymously = self.graded_anonymously

        version_number = self.version_number

        request_id = self.request_id

        links = self.links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "event_type": event_type,
                "excused_after": excused_after,
                "excused_before": excused_before,
                "grade_after": grade_after,
                "grade_before": grade_before,
                "graded_anonymously": graded_anonymously,
                "version_number": version_number,
                "request_id": request_id,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        excused_after = d.pop("excused_after")

        excused_before = d.pop("excused_before")

        grade_after = d.pop("grade_after")

        grade_before = d.pop("grade_before")

        graded_anonymously = d.pop("graded_anonymously")

        version_number = d.pop("version_number")

        request_id = d.pop("request_id")

        links = d.pop("links")

        get_graders_response_200_item = cls(
            id=id,
            created_at=created_at,
            event_type=event_type,
            excused_after=excused_after,
            excused_before=excused_before,
            grade_after=grade_after,
            grade_before=grade_before,
            graded_anonymously=graded_anonymously,
            version_number=version_number,
            request_id=request_id,
            links=links,
        )

        get_graders_response_200_item.additional_properties = d
        return get_graders_response_200_item

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
