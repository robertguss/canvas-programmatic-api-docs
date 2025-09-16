from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetRevisionsResponse200")


@_attrs_define
class GetRevisionsResponse200:
    """
    Attributes:
        revision_id (int):
        updated_at (str):
        latest (bool):
        edited_by (None):
        url (str):
        title (str):
        body (str):
    """

    revision_id: int
    updated_at: str
    latest: bool
    edited_by: None
    url: str
    title: str
    body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision_id = self.revision_id

        updated_at = self.updated_at

        latest = self.latest

        edited_by = self.edited_by

        url = self.url

        title = self.title

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision_id": revision_id,
                "updated_at": updated_at,
                "latest": latest,
                "edited_by": edited_by,
                "url": url,
                "title": title,
                "body": body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        revision_id = d.pop("revision_id")

        updated_at = d.pop("updated_at")

        latest = d.pop("latest")

        edited_by = d.pop("edited_by")

        url = d.pop("url")

        title = d.pop("title")

        body = d.pop("body")

        get_revisions_response_200 = cls(
            revision_id=revision_id,
            updated_at=updated_at,
            latest=latest,
            edited_by=edited_by,
            url=url,
            title=title,
            body=body,
        )

        get_revisions_response_200.additional_properties = d
        return get_revisions_response_200

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
