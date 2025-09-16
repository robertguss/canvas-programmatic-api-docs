from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SubmissionComment")


@_attrs_define
class SubmissionComment:
    """
    Attributes:
        id (int):
        author_id (int):
        author_name (str):
        author (str):
        comment (str):
        created_at (str):
        edited_at (str):
        media_comment (None):
    """

    id: int
    author_id: int
    author_name: str
    author: str
    comment: str
    created_at: str
    edited_at: str
    media_comment: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author_id = self.author_id

        author_name = self.author_name

        author = self.author

        comment = self.comment

        created_at = self.created_at

        edited_at = self.edited_at

        media_comment = self.media_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "author_id": author_id,
                "author_name": author_name,
                "author": author,
                "comment": comment,
                "created_at": created_at,
                "edited_at": edited_at,
                "media_comment": media_comment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author_id = d.pop("author_id")

        author_name = d.pop("author_name")

        author = d.pop("author")

        comment = d.pop("comment")

        created_at = d.pop("created_at")

        edited_at = d.pop("edited_at")

        media_comment = d.pop("media_comment")

        submission_comment = cls(
            id=id,
            author_id=author_id,
            author_name=author_name,
            author=author,
            comment=comment,
            created_at=created_at,
            edited_at=edited_at,
            media_comment=media_comment,
        )

        submission_comment.additional_properties = d
        return submission_comment

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
