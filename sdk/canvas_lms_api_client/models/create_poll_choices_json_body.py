from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePollChoicesJsonBody")


@_attrs_define
class CreatePollChoicesJsonBody:
    """
    Attributes:
        poll_choicestext (Union[Unset, str]): The descriptive text of the poll choice.
    """

    poll_choicestext: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        poll_choicestext = self.poll_choicestext

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if poll_choicestext is not UNSET:
            field_dict["poll_choices[][text]"] = poll_choicestext

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        poll_choicestext = d.pop("poll_choices[][text]", UNSET)

        create_poll_choices_json_body = cls(
            poll_choicestext=poll_choicestext,
        )

        create_poll_choices_json_body.additional_properties = d
        return create_poll_choices_json_body

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
