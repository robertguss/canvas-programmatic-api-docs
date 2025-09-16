from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.change_record_exceptions_item import ChangeRecordExceptionsItem


T = TypeVar("T", bound="ChangeRecord")


@_attrs_define
class ChangeRecord:
    """
    Attributes:
        asset_id (int):
        asset_type (str):
        asset_name (str):
        change_type (str):
        html_url (str):
        locked (bool):
        exceptions (list['ChangeRecordExceptionsItem']):
    """

    asset_id: int
    asset_type: str
    asset_name: str
    change_type: str
    html_url: str
    locked: bool
    exceptions: list["ChangeRecordExceptionsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        asset_type = self.asset_type

        asset_name = self.asset_name

        change_type = self.change_type

        html_url = self.html_url

        locked = self.locked

        exceptions = []
        for exceptions_item_data in self.exceptions:
            exceptions_item = exceptions_item_data.to_dict()
            exceptions.append(exceptions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "asset_type": asset_type,
                "asset_name": asset_name,
                "change_type": change_type,
                "html_url": html_url,
                "locked": locked,
                "exceptions": exceptions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_record_exceptions_item import ChangeRecordExceptionsItem

        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        asset_type = d.pop("asset_type")

        asset_name = d.pop("asset_name")

        change_type = d.pop("change_type")

        html_url = d.pop("html_url")

        locked = d.pop("locked")

        exceptions = []
        _exceptions = d.pop("exceptions")
        for exceptions_item_data in _exceptions:
            exceptions_item = ChangeRecordExceptionsItem.from_dict(exceptions_item_data)

            exceptions.append(exceptions_item)

        change_record = cls(
            asset_id=asset_id,
            asset_type=asset_type,
            asset_name=asset_name,
            change_type=change_type,
            html_url=html_url,
            locked=locked,
            exceptions=exceptions,
        )

        change_record.additional_properties = d
        return change_record

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
