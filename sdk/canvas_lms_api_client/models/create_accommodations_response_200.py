from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_accommodations_response_200_failed_item import CreateAccommodationsResponse200FailedItem
    from ..models.create_accommodations_response_200_successful_item import (
        CreateAccommodationsResponse200SuccessfulItem,
    )


T = TypeVar("T", bound="CreateAccommodationsResponse200")


@_attrs_define
class CreateAccommodationsResponse200:
    """
    Attributes:
        message (str):
        successful (list['CreateAccommodationsResponse200SuccessfulItem']):
        failed (list['CreateAccommodationsResponse200FailedItem']):
    """

    message: str
    successful: list["CreateAccommodationsResponse200SuccessfulItem"]
    failed: list["CreateAccommodationsResponse200FailedItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        successful = []
        for successful_item_data in self.successful:
            successful_item = successful_item_data.to_dict()
            successful.append(successful_item)

        failed = []
        for failed_item_data in self.failed:
            failed_item = failed_item_data.to_dict()
            failed.append(failed_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "successful": successful,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_accommodations_response_200_failed_item import CreateAccommodationsResponse200FailedItem
        from ..models.create_accommodations_response_200_successful_item import (
            CreateAccommodationsResponse200SuccessfulItem,
        )

        d = dict(src_dict)
        message = d.pop("message")

        successful = []
        _successful = d.pop("successful")
        for successful_item_data in _successful:
            successful_item = CreateAccommodationsResponse200SuccessfulItem.from_dict(successful_item_data)

            successful.append(successful_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = CreateAccommodationsResponse200FailedItem.from_dict(failed_item_data)

            failed.append(failed_item)

        create_accommodations_response_200 = cls(
            message=message,
            successful=successful,
            failed=failed,
        )

        create_accommodations_response_200.additional_properties = d
        return create_accommodations_response_200

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
