from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetNoticeHandlersResponse200NoticeHandlersItem")


@_attrs_define
class GetNoticeHandlersResponse200NoticeHandlersItem:
    """
    Attributes:
        handler (str):
        notice_type (str):
    """

    handler: str
    notice_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handler = self.handler

        notice_type = self.notice_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handler": handler,
                "notice_type": notice_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handler = d.pop("handler")

        notice_type = d.pop("notice_type")

        get_notice_handlers_response_200_notice_handlers_item = cls(
            handler=handler,
            notice_type=notice_type,
        )

        get_notice_handlers_response_200_notice_handlers_item.additional_properties = d
        return get_notice_handlers_response_200_notice_handlers_item

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
