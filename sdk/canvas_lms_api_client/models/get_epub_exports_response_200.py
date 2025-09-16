from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_epub_exports_response_200_attachment import GetEpubExportsResponse200Attachment


T = TypeVar("T", bound="GetEpubExportsResponse200")


@_attrs_define
class GetEpubExportsResponse200:
    """
    Attributes:
        id (int):
        created_at (str):
        attachment (GetEpubExportsResponse200Attachment):
        progress_url (str):
        user_id (int):
        workflow_state (str):
    """

    id: int
    created_at: str
    attachment: "GetEpubExportsResponse200Attachment"
    progress_url: str
    user_id: int
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        attachment = self.attachment.to_dict()

        progress_url = self.progress_url

        user_id = self.user_id

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "attachment": attachment,
                "progress_url": progress_url,
                "user_id": user_id,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_epub_exports_response_200_attachment import GetEpubExportsResponse200Attachment

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        attachment = GetEpubExportsResponse200Attachment.from_dict(d.pop("attachment"))

        progress_url = d.pop("progress_url")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        get_epub_exports_response_200 = cls(
            id=id,
            created_at=created_at,
            attachment=attachment,
            progress_url=progress_url,
            user_id=user_id,
            workflow_state=workflow_state,
        )

        get_epub_exports_response_200.additional_properties = d
        return get_epub_exports_response_200

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
