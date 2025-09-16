from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteFilesResponse200")


@_attrs_define
class DeleteFilesResponse200:
    """
    Attributes:
        id (int):
        uuid (str):
        folder_id (int):
        display_name (str):
        filename (str):
        content_type (str):
        url (str):
        size (int):
        created_at (str):
        updated_at (str):
        unlock_at (str):
        locked (bool):
        hidden (bool):
        lock_at (str):
        hidden_for_user (bool):
        visibility_level (str):
        thumbnail_url (None):
        modified_at (str):
        mime_class (str):
        media_entry_id (str):
        locked_for_user (bool):
        lock_info (None):
        lock_explanation (str):
        preview_url (None):
    """

    id: int
    uuid: str
    folder_id: int
    display_name: str
    filename: str
    content_type: str
    url: str
    size: int
    created_at: str
    updated_at: str
    unlock_at: str
    locked: bool
    hidden: bool
    lock_at: str
    hidden_for_user: bool
    visibility_level: str
    thumbnail_url: None
    modified_at: str
    mime_class: str
    media_entry_id: str
    locked_for_user: bool
    lock_info: None
    lock_explanation: str
    preview_url: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        uuid = self.uuid

        folder_id = self.folder_id

        display_name = self.display_name

        filename = self.filename

        content_type = self.content_type

        url = self.url

        size = self.size

        created_at = self.created_at

        updated_at = self.updated_at

        unlock_at = self.unlock_at

        locked = self.locked

        hidden = self.hidden

        lock_at = self.lock_at

        hidden_for_user = self.hidden_for_user

        visibility_level = self.visibility_level

        thumbnail_url = self.thumbnail_url

        modified_at = self.modified_at

        mime_class = self.mime_class

        media_entry_id = self.media_entry_id

        locked_for_user = self.locked_for_user

        lock_info = self.lock_info

        lock_explanation = self.lock_explanation

        preview_url = self.preview_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "folder_id": folder_id,
                "display_name": display_name,
                "filename": filename,
                "content-type": content_type,
                "url": url,
                "size": size,
                "created_at": created_at,
                "updated_at": updated_at,
                "unlock_at": unlock_at,
                "locked": locked,
                "hidden": hidden,
                "lock_at": lock_at,
                "hidden_for_user": hidden_for_user,
                "visibility_level": visibility_level,
                "thumbnail_url": thumbnail_url,
                "modified_at": modified_at,
                "mime_class": mime_class,
                "media_entry_id": media_entry_id,
                "locked_for_user": locked_for_user,
                "lock_info": lock_info,
                "lock_explanation": lock_explanation,
                "preview_url": preview_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        uuid = d.pop("uuid")

        folder_id = d.pop("folder_id")

        display_name = d.pop("display_name")

        filename = d.pop("filename")

        content_type = d.pop("content-type")

        url = d.pop("url")

        size = d.pop("size")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        unlock_at = d.pop("unlock_at")

        locked = d.pop("locked")

        hidden = d.pop("hidden")

        lock_at = d.pop("lock_at")

        hidden_for_user = d.pop("hidden_for_user")

        visibility_level = d.pop("visibility_level")

        thumbnail_url = d.pop("thumbnail_url")

        modified_at = d.pop("modified_at")

        mime_class = d.pop("mime_class")

        media_entry_id = d.pop("media_entry_id")

        locked_for_user = d.pop("locked_for_user")

        lock_info = d.pop("lock_info")

        lock_explanation = d.pop("lock_explanation")

        preview_url = d.pop("preview_url")

        delete_files_response_200 = cls(
            id=id,
            uuid=uuid,
            folder_id=folder_id,
            display_name=display_name,
            filename=filename,
            content_type=content_type,
            url=url,
            size=size,
            created_at=created_at,
            updated_at=updated_at,
            unlock_at=unlock_at,
            locked=locked,
            hidden=hidden,
            lock_at=lock_at,
            hidden_for_user=hidden_for_user,
            visibility_level=visibility_level,
            thumbnail_url=thumbnail_url,
            modified_at=modified_at,
            mime_class=mime_class,
            media_entry_id=media_entry_id,
            locked_for_user=locked_for_user,
            lock_info=lock_info,
            lock_explanation=lock_explanation,
            preview_url=preview_url,
        )

        delete_files_response_200.additional_properties = d
        return delete_files_response_200

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
