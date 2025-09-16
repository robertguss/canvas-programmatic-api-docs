from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_reports_response_200_parameters import CreateReportsResponse200Parameters


T = TypeVar("T", bound="CreateReportsResponse200")


@_attrs_define
class CreateReportsResponse200:
    """
    Attributes:
        id (int):
        file_url (str):
        attachment (None):
        status (str):
        created_at (str):
        started_at (str):
        ended_at (str):
        parameters (CreateReportsResponse200Parameters):
        progress (int):
    """

    id: int
    file_url: str
    attachment: None
    status: str
    created_at: str
    started_at: str
    ended_at: str
    parameters: "CreateReportsResponse200Parameters"
    progress: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_url = self.file_url

        attachment = self.attachment

        status = self.status

        created_at = self.created_at

        started_at = self.started_at

        ended_at = self.ended_at

        parameters = self.parameters.to_dict()

        progress = self.progress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "file_url": file_url,
                "attachment": attachment,
                "status": status,
                "created_at": created_at,
                "started_at": started_at,
                "ended_at": ended_at,
                "parameters": parameters,
                "progress": progress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_reports_response_200_parameters import CreateReportsResponse200Parameters

        d = dict(src_dict)
        id = d.pop("id")

        file_url = d.pop("file_url")

        attachment = d.pop("attachment")

        status = d.pop("status")

        created_at = d.pop("created_at")

        started_at = d.pop("started_at")

        ended_at = d.pop("ended_at")

        parameters = CreateReportsResponse200Parameters.from_dict(d.pop("parameters"))

        progress = d.pop("progress")

        create_reports_response_200 = cls(
            id=id,
            file_url=file_url,
            attachment=attachment,
            status=status,
            created_at=created_at,
            started_at=started_at,
            ended_at=ended_at,
            parameters=parameters,
            progress=progress,
        )

        create_reports_response_200.additional_properties = d
        return create_reports_response_200

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
