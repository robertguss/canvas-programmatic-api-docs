from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBlackoutDatesDataBody")


@_attrs_define
class UpdateBlackoutDatesDataBody:
    """
    Attributes:
        start_date (Union[Unset, str]): The start date of the blackout date.
        end_date (Union[Unset, str]): The end date of the blackout date.
    """

    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_date = self.start_date

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start_date = d.pop("start_date", UNSET)

        end_date = d.pop("end_date", UNSET)

        update_blackout_dates_data_body = cls(
            start_date=start_date,
            end_date=end_date,
        )

        update_blackout_dates_data_body.additional_properties = d
        return update_blackout_dates_data_body

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
