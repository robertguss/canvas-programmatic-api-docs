from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_pages_response_200_block_editor_attributes import CreatePagesResponse200BlockEditorAttributes


T = TypeVar("T", bound="CreatePagesResponse200")


@_attrs_define
class CreatePagesResponse200:
    """
    Attributes:
        page_id (int):
        url (str):
        title (str):
        created_at (str):
        updated_at (str):
        hide_from_students (bool):
        editing_roles (str):
        last_edited_by (None):
        body (str):
        published (bool):
        publish_at (str):
        front_page (bool):
        locked_for_user (bool):
        lock_info (None):
        lock_explanation (str):
        editor (str):
        block_editor_attributes (CreatePagesResponse200BlockEditorAttributes):
    """

    page_id: int
    url: str
    title: str
    created_at: str
    updated_at: str
    hide_from_students: bool
    editing_roles: str
    last_edited_by: None
    body: str
    published: bool
    publish_at: str
    front_page: bool
    locked_for_user: bool
    lock_info: None
    lock_explanation: str
    editor: str
    block_editor_attributes: "CreatePagesResponse200BlockEditorAttributes"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_id = self.page_id

        url = self.url

        title = self.title

        created_at = self.created_at

        updated_at = self.updated_at

        hide_from_students = self.hide_from_students

        editing_roles = self.editing_roles

        last_edited_by = self.last_edited_by

        body = self.body

        published = self.published

        publish_at = self.publish_at

        front_page = self.front_page

        locked_for_user = self.locked_for_user

        lock_info = self.lock_info

        lock_explanation = self.lock_explanation

        editor = self.editor

        block_editor_attributes = self.block_editor_attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page_id": page_id,
                "url": url,
                "title": title,
                "created_at": created_at,
                "updated_at": updated_at,
                "hide_from_students": hide_from_students,
                "editing_roles": editing_roles,
                "last_edited_by": last_edited_by,
                "body": body,
                "published": published,
                "publish_at": publish_at,
                "front_page": front_page,
                "locked_for_user": locked_for_user,
                "lock_info": lock_info,
                "lock_explanation": lock_explanation,
                "editor": editor,
                "block_editor_attributes": block_editor_attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_pages_response_200_block_editor_attributes import (
            CreatePagesResponse200BlockEditorAttributes,
        )

        d = dict(src_dict)
        page_id = d.pop("page_id")

        url = d.pop("url")

        title = d.pop("title")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        hide_from_students = d.pop("hide_from_students")

        editing_roles = d.pop("editing_roles")

        last_edited_by = d.pop("last_edited_by")

        body = d.pop("body")

        published = d.pop("published")

        publish_at = d.pop("publish_at")

        front_page = d.pop("front_page")

        locked_for_user = d.pop("locked_for_user")

        lock_info = d.pop("lock_info")

        lock_explanation = d.pop("lock_explanation")

        editor = d.pop("editor")

        block_editor_attributes = CreatePagesResponse200BlockEditorAttributes.from_dict(
            d.pop("block_editor_attributes")
        )

        create_pages_response_200 = cls(
            page_id=page_id,
            url=url,
            title=title,
            created_at=created_at,
            updated_at=updated_at,
            hide_from_students=hide_from_students,
            editing_roles=editing_roles,
            last_edited_by=last_edited_by,
            body=body,
            published=published,
            publish_at=publish_at,
            front_page=front_page,
            locked_for_user=locked_for_user,
            lock_info=lock_info,
            lock_explanation=lock_explanation,
            editor=editor,
            block_editor_attributes=block_editor_attributes,
        )

        create_pages_response_200.additional_properties = d
        return create_pages_response_200

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
