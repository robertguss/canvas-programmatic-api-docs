from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_share_content_export import ContentShareContentExport
    from ..models.content_share_receivers_item import ContentShareReceiversItem
    from ..models.content_share_sender import ContentShareSender
    from ..models.content_share_source_course import ContentShareSourceCourse


T = TypeVar("T", bound="ContentShare")


@_attrs_define
class ContentShare:
    """
    Attributes:
        id (int):
        name (str):
        content_type (str):
        created_at (str):
        updated_at (str):
        user_id (int):
        sender (ContentShareSender):
        receivers (list['ContentShareReceiversItem']):
        source_course (ContentShareSourceCourse):
        read_state (str):
        content_export (ContentShareContentExport):
    """

    id: int
    name: str
    content_type: str
    created_at: str
    updated_at: str
    user_id: int
    sender: "ContentShareSender"
    receivers: list["ContentShareReceiversItem"]
    source_course: "ContentShareSourceCourse"
    read_state: str
    content_export: "ContentShareContentExport"
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
        from ..models.content_share_content_export import ContentShareContentExport
        from ..models.content_share_receivers_item import ContentShareReceiversItem
        from ..models.content_share_sender import ContentShareSender
        from ..models.content_share_source_course import ContentShareSourceCourse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        user_id = d.pop("user_id")

        sender = ContentShareSender.from_dict(d.pop("sender"))

        receivers = []
        _receivers = d.pop("receivers")
        for receivers_item_data in _receivers:
            receivers_item = ContentShareReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        source_course = ContentShareSourceCourse.from_dict(d.pop("source_course"))

        read_state = d.pop("read_state")

        content_export = ContentShareContentExport.from_dict(d.pop("content_export"))

        content_share = cls(
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

        content_share.additional_properties = d
        return content_share

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
