from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetCollaborationsResponse200Item")


@_attrs_define
class GetCollaborationsResponse200Item:
    """
    Attributes:
        id (int):
        collaboration_type (str):
        document_id (str):
        user_id (int):
        context_id (int):
        context_type (str):
        url (None):
        created_at (str):
        updated_at (str):
        description (None):
        title (None):
        type_ (str):
        update_url (None):
        user_name (str):
    """

    id: int
    collaboration_type: str
    document_id: str
    user_id: int
    context_id: int
    context_type: str
    url: None
    created_at: str
    updated_at: str
    description: None
    title: None
    type_: str
    update_url: None
    user_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        collaboration_type = self.collaboration_type

        document_id = self.document_id

        user_id = self.user_id

        context_id = self.context_id

        context_type = self.context_type

        url = self.url

        created_at = self.created_at

        updated_at = self.updated_at

        description = self.description

        title = self.title

        type_ = self.type_

        update_url = self.update_url

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "collaboration_type": collaboration_type,
                "document_id": document_id,
                "user_id": user_id,
                "context_id": context_id,
                "context_type": context_type,
                "url": url,
                "created_at": created_at,
                "updated_at": updated_at,
                "description": description,
                "title": title,
                "type": type_,
                "update_url": update_url,
                "user_name": user_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        collaboration_type = d.pop("collaboration_type")

        document_id = d.pop("document_id")

        user_id = d.pop("user_id")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        url = d.pop("url")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        description = d.pop("description")

        title = d.pop("title")

        type_ = d.pop("type")

        update_url = d.pop("update_url")

        user_name = d.pop("user_name")

        get_collaborations_response_200_item = cls(
            id=id,
            collaboration_type=collaboration_type,
            document_id=document_id,
            user_id=user_id,
            context_id=context_id,
            context_type=context_type,
            url=url,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            title=title,
            type_=type_,
            update_url=update_url,
            user_name=user_name,
        )

        get_collaborations_response_200_item.additional_properties = d
        return get_collaborations_response_200_item

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
