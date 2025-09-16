from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCompleteJsonBody")


@_attrs_define
class CreateCompleteJsonBody:
    """
    Attributes:
        attempt (Union[Unset, str]): The attempt number of the quiz submission that should be completed. Note that this
            must be the latest attempt index, as earlier attempts can not be modified.
        validation_token (Union[Unset, str]): The unique validation token you received when this Quiz Submission was
            created.
    """

    attempt: Union[Unset, str] = UNSET
    validation_token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attempt = self.attempt

        validation_token = self.validation_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if validation_token is not UNSET:
            field_dict["validation_token"] = validation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempt = d.pop("attempt", UNSET)

        validation_token = d.pop("validation_token", UNSET)

        create_complete_json_body = cls(
            attempt=attempt,
            validation_token=validation_token,
        )

        create_complete_json_body.additional_properties = d
        return create_complete_json_body

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
