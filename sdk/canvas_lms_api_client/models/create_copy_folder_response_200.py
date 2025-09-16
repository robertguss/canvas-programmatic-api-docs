from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCopyFolderResponse200")


@_attrs_define
class CreateCopyFolderResponse200:
    """
    Attributes:
        context_type (str):
        context_id (int):
        files_count (int):
        position (int):
        updated_at (str):
        folders_url (str):
        files_url (str):
        full_name (str):
        lock_at (str):
        id (int):
        folders_count (int):
        name (str):
        parent_folder_id (int):
        created_at (str):
        unlock_at (None):
        hidden (bool):
        hidden_for_user (bool):
        locked (bool):
        locked_for_user (bool):
        for_submissions (bool):
    """

    context_type: str
    context_id: int
    files_count: int
    position: int
    updated_at: str
    folders_url: str
    files_url: str
    full_name: str
    lock_at: str
    id: int
    folders_count: int
    name: str
    parent_folder_id: int
    created_at: str
    unlock_at: None
    hidden: bool
    hidden_for_user: bool
    locked: bool
    locked_for_user: bool
    for_submissions: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context_type = self.context_type

        context_id = self.context_id

        files_count = self.files_count

        position = self.position

        updated_at = self.updated_at

        folders_url = self.folders_url

        files_url = self.files_url

        full_name = self.full_name

        lock_at = self.lock_at

        id = self.id

        folders_count = self.folders_count

        name = self.name

        parent_folder_id = self.parent_folder_id

        created_at = self.created_at

        unlock_at = self.unlock_at

        hidden = self.hidden

        hidden_for_user = self.hidden_for_user

        locked = self.locked

        locked_for_user = self.locked_for_user

        for_submissions = self.for_submissions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "context_type": context_type,
                "context_id": context_id,
                "files_count": files_count,
                "position": position,
                "updated_at": updated_at,
                "folders_url": folders_url,
                "files_url": files_url,
                "full_name": full_name,
                "lock_at": lock_at,
                "id": id,
                "folders_count": folders_count,
                "name": name,
                "parent_folder_id": parent_folder_id,
                "created_at": created_at,
                "unlock_at": unlock_at,
                "hidden": hidden,
                "hidden_for_user": hidden_for_user,
                "locked": locked,
                "locked_for_user": locked_for_user,
                "for_submissions": for_submissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        context_type = d.pop("context_type")

        context_id = d.pop("context_id")

        files_count = d.pop("files_count")

        position = d.pop("position")

        updated_at = d.pop("updated_at")

        folders_url = d.pop("folders_url")

        files_url = d.pop("files_url")

        full_name = d.pop("full_name")

        lock_at = d.pop("lock_at")

        id = d.pop("id")

        folders_count = d.pop("folders_count")

        name = d.pop("name")

        parent_folder_id = d.pop("parent_folder_id")

        created_at = d.pop("created_at")

        unlock_at = d.pop("unlock_at")

        hidden = d.pop("hidden")

        hidden_for_user = d.pop("hidden_for_user")

        locked = d.pop("locked")

        locked_for_user = d.pop("locked_for_user")

        for_submissions = d.pop("for_submissions")

        create_copy_folder_response_200 = cls(
            context_type=context_type,
            context_id=context_id,
            files_count=files_count,
            position=position,
            updated_at=updated_at,
            folders_url=folders_url,
            files_url=files_url,
            full_name=full_name,
            lock_at=lock_at,
            id=id,
            folders_count=folders_count,
            name=name,
            parent_folder_id=parent_folder_id,
            created_at=created_at,
            unlock_at=unlock_at,
            hidden=hidden,
            hidden_for_user=hidden_for_user,
            locked=locked,
            locked_for_user=locked_for_user,
            for_submissions=for_submissions,
        )

        create_copy_folder_response_200.additional_properties = d
        return create_copy_folder_response_200

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
