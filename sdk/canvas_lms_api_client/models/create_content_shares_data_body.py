from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateContentSharesDataBody")


@_attrs_define
class CreateContentSharesDataBody:
    """
    Attributes:
        receiver_ids (Union[Unset, str]): IDs of users to share the content with.
        content_type (Union[Unset, str]): Type of content you are sharing.Allowed values: assignment, discussion_topic,
            page, quiz, module, module_item
        content_id (Union[Unset, str]): The id of the content that you are sharing
    """

    receiver_ids: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    content_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        receiver_ids = self.receiver_ids

        content_type = self.content_type

        content_id = self.content_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if receiver_ids is not UNSET:
            field_dict["receiver_ids"] = receiver_ids
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if content_id is not UNSET:
            field_dict["content_id"] = content_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        receiver_ids = d.pop("receiver_ids", UNSET)

        content_type = d.pop("content_type", UNSET)

        content_id = d.pop("content_id", UNSET)

        create_content_shares_data_body = cls(
            receiver_ids=receiver_ids,
            content_type=content_type,
            content_id=content_id,
        )

        create_content_shares_data_body.additional_properties = d
        return create_content_shares_data_body

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
