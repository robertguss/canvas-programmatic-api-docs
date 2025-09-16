from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_lti_registrations_response_200_data_item import GetLtiRegistrationsResponse200DataItem


T = TypeVar("T", bound="GetLtiRegistrationsResponse200")


@_attrs_define
class GetLtiRegistrationsResponse200:
    """
    Attributes:
        total (int):
        data (list['GetLtiRegistrationsResponse200DataItem']):
    """

    total: int
    data: list["GetLtiRegistrationsResponse200DataItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_lti_registrations_response_200_data_item import GetLtiRegistrationsResponse200DataItem

        d = dict(src_dict)
        total = d.pop("total")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = GetLtiRegistrationsResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        get_lti_registrations_response_200 = cls(
            total=total,
            data=data,
        )

        get_lti_registrations_response_200.additional_properties = d
        return get_lti_registrations_response_200

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
