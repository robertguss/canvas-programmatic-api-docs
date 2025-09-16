from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePollSubmissionsDataBody")


@_attrs_define
class CreatePollSubmissionsDataBody:
    """
    Attributes:
        poll_submissionspoll_choice_id (Union[Unset, str]): The chosen poll choice for this submission.
    """

    poll_submissionspoll_choice_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        poll_submissionspoll_choice_id = self.poll_submissionspoll_choice_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if poll_submissionspoll_choice_id is not UNSET:
            field_dict["poll_submissions[][poll_choice_id]"] = poll_submissionspoll_choice_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        poll_submissionspoll_choice_id = d.pop("poll_submissions[][poll_choice_id]", UNSET)

        create_poll_submissions_data_body = cls(
            poll_submissionspoll_choice_id=poll_submissionspoll_choice_id,
        )

        create_poll_submissions_data_body.additional_properties = d
        return create_poll_submissions_data_body

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
