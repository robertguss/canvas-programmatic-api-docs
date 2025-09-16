from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_content_shares_response_200_content_export import CreateContentSharesResponse200ContentExport
    from ..models.create_content_shares_response_200_receivers_item import CreateContentSharesResponse200ReceiversItem
    from ..models.create_content_shares_response_200_sender import CreateContentSharesResponse200Sender
    from ..models.create_content_shares_response_200_source_course import CreateContentSharesResponse200SourceCourse


T = TypeVar("T", bound="CreateContentSharesResponse200")


@_attrs_define
class CreateContentSharesResponse200:
    """
    Attributes:
        id (int):
        name (str):
        content_type (str):
        created_at (str):
        updated_at (str):
        user_id (int):
        sender (CreateContentSharesResponse200Sender):
        receivers (list['CreateContentSharesResponse200ReceiversItem']):
        source_course (CreateContentSharesResponse200SourceCourse):
        read_state (str):
        content_export (CreateContentSharesResponse200ContentExport):
    """

    id: int
    name: str
    content_type: str
    created_at: str
    updated_at: str
    user_id: int
    sender: "CreateContentSharesResponse200Sender"
    receivers: list["CreateContentSharesResponse200ReceiversItem"]
    source_course: "CreateContentSharesResponse200SourceCourse"
    read_state: str
    content_export: "CreateContentSharesResponse200ContentExport"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        content_type = self.content_type

        created_at = self.created_at

        updated_at = self.updated_at

        user_id = self.user_id

        sender = self.sender.to_dict()

        receivers = []
        for receivers_item_data in self.receivers:
            receivers_item = receivers_item_data.to_dict()
            receivers.append(receivers_item)

        source_course = self.source_course.to_dict()

        read_state = self.read_state

        content_export = self.content_export.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "content_type": content_type,
                "created_at": created_at,
                "updated_at": updated_at,
                "user_id": user_id,
                "sender": sender,
                "receivers": receivers,
                "source_course": source_course,
                "read_state": read_state,
                "content_export": content_export,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_content_shares_response_200_content_export import (
            CreateContentSharesResponse200ContentExport,
        )
        from ..models.create_content_shares_response_200_receivers_item import (
            CreateContentSharesResponse200ReceiversItem,
        )
        from ..models.create_content_shares_response_200_sender import CreateContentSharesResponse200Sender
        from ..models.create_content_shares_response_200_source_course import CreateContentSharesResponse200SourceCourse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        user_id = d.pop("user_id")

        sender = CreateContentSharesResponse200Sender.from_dict(d.pop("sender"))

        receivers = []
        _receivers = d.pop("receivers")
        for receivers_item_data in _receivers:
            receivers_item = CreateContentSharesResponse200ReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        source_course = CreateContentSharesResponse200SourceCourse.from_dict(d.pop("source_course"))

        read_state = d.pop("read_state")

        content_export = CreateContentSharesResponse200ContentExport.from_dict(d.pop("content_export"))

        create_content_shares_response_200 = cls(
            id=id,
            name=name,
            content_type=content_type,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            sender=sender,
            receivers=receivers,
            source_course=source_course,
            read_state=read_state,
            content_export=content_export,
        )

        create_content_shares_response_200.additional_properties = d
        return create_content_shares_response_200

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
