from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAddRecipientsDataBody")


@_attrs_define
class CreateAddRecipientsDataBody:
    r"""
    Attributes:
        recipients (Union[Unset, str]): An array of recipient ids. These may be user ids or course/group ids prefixed
            with “course_” or “group_” respectively, e.g. recipients[]=1\&recipients=2\&recipients[]=course_3
    """

    recipients: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        recipients = self.recipients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipients is not UNSET:
            field_dict["recipients[]"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipients = d.pop("recipients[]", UNSET)

        create_add_recipients_data_body = cls(
            recipients=recipients,
        )

        create_add_recipients_data_body.additional_properties = d
        return create_add_recipients_data_body

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
