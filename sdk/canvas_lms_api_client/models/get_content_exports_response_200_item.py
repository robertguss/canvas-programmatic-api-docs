from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_content_exports_response_200_item_attachment import GetContentExportsResponse200ItemAttachment


T = TypeVar("T", bound="GetContentExportsResponse200Item")


@_attrs_define
class GetContentExportsResponse200Item:
    """
    Attributes:
        id (int):
        created_at (str):
        export_type (str):
        attachment (GetContentExportsResponse200ItemAttachment):
        progress_url (str):
        user_id (int):
        workflow_state (str):
    """

    id: int
    created_at: str
    export_type: str
    attachment: "GetContentExportsResponse200ItemAttachment"
    progress_url: str
    user_id: int
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        export_type = self.export_type

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
                "export_type": export_type,
                "attachment": attachment,
                "progress_url": progress_url,
                "user_id": user_id,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_content_exports_response_200_item_attachment import GetContentExportsResponse200ItemAttachment

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        export_type = d.pop("export_type")

        attachment = GetContentExportsResponse200ItemAttachment.from_dict(d.pop("attachment"))

        progress_url = d.pop("progress_url")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        get_content_exports_response_200_item = cls(
            id=id,
            created_at=created_at,
            export_type=export_type,
            attachment=attachment,
            progress_url=progress_url,
            user_id=user_id,
            workflow_state=workflow_state,
        )

        get_content_exports_response_200_item.additional_properties = d
        return get_content_exports_response_200_item

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
