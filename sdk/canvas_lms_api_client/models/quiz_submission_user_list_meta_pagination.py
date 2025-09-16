from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizSubmissionUserListMetaPagination")


@_attrs_define
class QuizSubmissionUserListMetaPagination:
    """
    Attributes:
        ref (str):
        description (str):
    """

    ref: str
    description: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "$ref": ref,
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ref = d.pop("$ref")

        description = d.pop("description")

        quiz_submission_user_list_meta_pagination = cls(
            ref=ref,
            description=description,
        )

        quiz_submission_user_list_meta_pagination.additional_properties = d
        return quiz_submission_user_list_meta_pagination

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
