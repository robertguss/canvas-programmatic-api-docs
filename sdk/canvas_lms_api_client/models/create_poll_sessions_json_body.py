from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePollSessionsJsonBody")


@_attrs_define
class CreatePollSessionsJsonBody:
    """
    Attributes:
        poll_sessionscourse_id (Union[Unset, str]): The id of the course this session is associated with.
    """

    poll_sessionscourse_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        poll_sessionscourse_id = self.poll_sessionscourse_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if poll_sessionscourse_id is not UNSET:
            field_dict["poll_sessions[][course_id]"] = poll_sessionscourse_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        poll_sessionscourse_id = d.pop("poll_sessions[][course_id]", UNSET)

        create_poll_sessions_json_body = cls(
            poll_sessionscourse_id=poll_sessionscourse_id,
        )

        create_poll_sessions_json_body.additional_properties = d
        return create_poll_sessions_json_body

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
