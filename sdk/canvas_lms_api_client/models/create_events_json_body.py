from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEventsJsonBody")


@_attrs_define
class CreateEventsJsonBody:
    """
    Attributes:
        quiz_submission_events (Union[Unset, str]): The submission events to be recorded
    """

    quiz_submission_events: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quiz_submission_events = self.quiz_submission_events

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quiz_submission_events is not UNSET:
            field_dict["quiz_submission_events[]"] = quiz_submission_events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quiz_submission_events = d.pop("quiz_submission_events[]", UNSET)

        create_events_json_body = cls(
            quiz_submission_events=quiz_submission_events,
        )

        create_events_json_body.additional_properties = d
        return create_events_json_body

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
