from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDiscussionTopicsDataBody")


@_attrs_define
class CreateDiscussionTopicsDataBody:
    """
    Attributes:
        delayed_post_at (Union[Unset, str]): If a timestamp is given, the topic will not be published until that time.
        lock_at (Union[Unset, str]): If a timestamp is given, the topic will be scheduled to lock at the provided
            timestamp. If the timestamp is in the past, the topic will be locked.
        assignment (Union[Unset, str]): To create an assignment discussion, pass the assignment parameters as a sub-
            object. See the Create an Assignment API for the available parameters. The name parameter will be ignored, as
            it’s taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment,
            pass set_assignment = false as part of the assignment object
        attachment (Union[Unset, str]): A multipart/form-data form-field-style attachment. Attachments larger than 1
            kilobyte are subject to quota restrictions.
    """

    delayed_post_at: Union[Unset, str] = UNSET
    lock_at: Union[Unset, str] = UNSET
    assignment: Union[Unset, str] = UNSET
    attachment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delayed_post_at = self.delayed_post_at

        lock_at = self.lock_at

        assignment = self.assignment

        attachment = self.attachment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delayed_post_at is not UNSET:
            field_dict["delayed_post_at"] = delayed_post_at
        if lock_at is not UNSET:
            field_dict["lock_at"] = lock_at
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if attachment is not UNSET:
            field_dict["attachment"] = attachment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        delayed_post_at = d.pop("delayed_post_at", UNSET)

        lock_at = d.pop("lock_at", UNSET)

        assignment = d.pop("assignment", UNSET)

        attachment = d.pop("attachment", UNSET)

        create_discussion_topics_data_body = cls(
            delayed_post_at=delayed_post_at,
            lock_at=lock_at,
            assignment=assignment,
            attachment=attachment,
        )

        create_discussion_topics_data_body.additional_properties = d
        return create_discussion_topics_data_body

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
