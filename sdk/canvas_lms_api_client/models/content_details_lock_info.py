from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_details_lock_info_context_module import ContentDetailsLockInfoContextModule


T = TypeVar("T", bound="ContentDetailsLockInfo")


@_attrs_define
class ContentDetailsLockInfo:
    """
    Attributes:
        asset_string (str):
        unlock_at (str):
        lock_at (str):
        context_module (ContentDetailsLockInfoContextModule):
    """

    asset_string: str
    unlock_at: str
    lock_at: str
    context_module: "ContentDetailsLockInfoContextModule"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_string = self.asset_string

        unlock_at = self.unlock_at

        lock_at = self.lock_at

        context_module = self.context_module.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_string": asset_string,
                "unlock_at": unlock_at,
                "lock_at": lock_at,
                "context_module": context_module,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_details_lock_info_context_module import ContentDetailsLockInfoContextModule

        d = dict(src_dict)
        asset_string = d.pop("asset_string")

        unlock_at = d.pop("unlock_at")

        lock_at = d.pop("lock_at")

        context_module = ContentDetailsLockInfoContextModule.from_dict(d.pop("context_module"))

        content_details_lock_info = cls(
            asset_string=asset_string,
            unlock_at=unlock_at,
            lock_at=lock_at,
            context_module=context_module,
        )

        content_details_lock_info.additional_properties = d
        return content_details_lock_info

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
