from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_received_response_200_item_content_export import GetReceivedResponse200ItemContentExport
    from ..models.get_received_response_200_item_receivers_item import GetReceivedResponse200ItemReceiversItem
    from ..models.get_received_response_200_item_sender import GetReceivedResponse200ItemSender
    from ..models.get_received_response_200_item_source_course import GetReceivedResponse200ItemSourceCourse


T = TypeVar("T", bound="GetReceivedResponse200Item")


@_attrs_define
class GetReceivedResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        content_type (str):
        created_at (str):
        updated_at (str):
        user_id (int):
        sender (GetReceivedResponse200ItemSender):
        receivers (list['GetReceivedResponse200ItemReceiversItem']):
        source_course (GetReceivedResponse200ItemSourceCourse):
        read_state (str):
        content_export (GetReceivedResponse200ItemContentExport):
    """

    id: int
    name: str
    content_type: str
    created_at: str
    updated_at: str
    user_id: int
    sender: "GetReceivedResponse200ItemSender"
    receivers: list["GetReceivedResponse200ItemReceiversItem"]
    source_course: "GetReceivedResponse200ItemSourceCourse"
    read_state: str
    content_export: "GetReceivedResponse200ItemContentExport"
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
        from ..models.get_received_response_200_item_content_export import GetReceivedResponse200ItemContentExport
        from ..models.get_received_response_200_item_receivers_item import GetReceivedResponse200ItemReceiversItem
        from ..models.get_received_response_200_item_sender import GetReceivedResponse200ItemSender
        from ..models.get_received_response_200_item_source_course import GetReceivedResponse200ItemSourceCourse

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        content_type = d.pop("content_type")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        user_id = d.pop("user_id")

        sender = GetReceivedResponse200ItemSender.from_dict(d.pop("sender"))

        receivers = []
        _receivers = d.pop("receivers")
        for receivers_item_data in _receivers:
            receivers_item = GetReceivedResponse200ItemReceiversItem.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        source_course = GetReceivedResponse200ItemSourceCourse.from_dict(d.pop("source_course"))

        read_state = d.pop("read_state")

        content_export = GetReceivedResponse200ItemContentExport.from_dict(d.pop("content_export"))

        get_received_response_200_item = cls(
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

        get_received_response_200_item.additional_properties = d
        return get_received_response_200_item

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
