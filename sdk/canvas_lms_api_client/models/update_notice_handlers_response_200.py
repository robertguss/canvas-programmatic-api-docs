from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateNoticeHandlersResponse200")


@_attrs_define
class UpdateNoticeHandlersResponse200:
    """
    Attributes:
        handler (str):
        notice_type (str):
        max_batch_size (int):
    """

    handler: str
    notice_type: str
    max_batch_size: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        handler = self.handler

        notice_type = self.notice_type

        max_batch_size = self.max_batch_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "handler": handler,
                "notice_type": notice_type,
                "max_batch_size": max_batch_size,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        handler = d.pop("handler")

        notice_type = d.pop("notice_type")

        max_batch_size = d.pop("max_batch_size")

        update_notice_handlers_response_200 = cls(
            handler=handler,
            notice_type=notice_type,
            max_batch_size=max_batch_size,
        )

        update_notice_handlers_response_200.additional_properties = d
        return update_notice_handlers_response_200

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
