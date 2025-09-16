from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_notice_handlers_response_200_notice_handlers_item import (
        GetNoticeHandlersResponse200NoticeHandlersItem,
    )


T = TypeVar("T", bound="GetNoticeHandlersResponse200")


@_attrs_define
class GetNoticeHandlersResponse200:
    """
    Attributes:
        client_id (str):
        deployment_id (str):
        notice_handlers (list['GetNoticeHandlersResponse200NoticeHandlersItem']):
    """

    client_id: str
    deployment_id: str
    notice_handlers: list["GetNoticeHandlersResponse200NoticeHandlersItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        deployment_id = self.deployment_id

        notice_handlers = []
        for notice_handlers_item_data in self.notice_handlers:
            notice_handlers_item = notice_handlers_item_data.to_dict()
            notice_handlers.append(notice_handlers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "deployment_id": deployment_id,
                "notice_handlers": notice_handlers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_notice_handlers_response_200_notice_handlers_item import (
            GetNoticeHandlersResponse200NoticeHandlersItem,
        )

        d = dict(src_dict)
        client_id = d.pop("client_id")

        deployment_id = d.pop("deployment_id")

        notice_handlers = []
        _notice_handlers = d.pop("notice_handlers")
        for notice_handlers_item_data in _notice_handlers:
            notice_handlers_item = GetNoticeHandlersResponse200NoticeHandlersItem.from_dict(notice_handlers_item_data)

            notice_handlers.append(notice_handlers_item)

        get_notice_handlers_response_200 = cls(
            client_id=client_id,
            deployment_id=deployment_id,
            notice_handlers=notice_handlers,
        )

        get_notice_handlers_response_200.additional_properties = d
        return get_notice_handlers_response_200

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
