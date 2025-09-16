from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.accommodation_response_failed_item import AccommodationResponseFailedItem
    from ..models.accommodation_response_successful_item import AccommodationResponseSuccessfulItem


T = TypeVar("T", bound="AccommodationResponse")


@_attrs_define
class AccommodationResponse:
    """
    Attributes:
        message (str):
        successful (list['AccommodationResponseSuccessfulItem']):
        failed (list['AccommodationResponseFailedItem']):
    """

    message: str
    successful: list["AccommodationResponseSuccessfulItem"]
    failed: list["AccommodationResponseFailedItem"]
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
        from ..models.accommodation_response_failed_item import AccommodationResponseFailedItem
        from ..models.accommodation_response_successful_item import AccommodationResponseSuccessfulItem

        d = dict(src_dict)
        message = d.pop("message")

        successful = []
        _successful = d.pop("successful")
        for successful_item_data in _successful:
            successful_item = AccommodationResponseSuccessfulItem.from_dict(successful_item_data)

            successful.append(successful_item)

        failed = []
        _failed = d.pop("failed")
        for failed_item_data in _failed:
            failed_item = AccommodationResponseFailedItem.from_dict(failed_item_data)

            failed.append(failed_item)

        accommodation_response = cls(
            message=message,
            successful=successful,
            failed=failed,
        )

        accommodation_response.additional_properties = d
        return accommodation_response

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
