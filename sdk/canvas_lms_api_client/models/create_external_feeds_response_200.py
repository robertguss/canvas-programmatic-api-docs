from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateExternalFeedsResponse200")


@_attrs_define
class CreateExternalFeedsResponse200:
    """
    Attributes:
        id (int):
        display_name (str):
        url (str):
        header_match (str):
        created_at (str):
        verbosity (str):
    """

    id: int
    display_name: str
    url: str
    header_match: str
    created_at: str
    verbosity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        url = self.url

        header_match = self.header_match

        created_at = self.created_at

        verbosity = self.verbosity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "url": url,
                "header_match": header_match,
                "created_at": created_at,
                "verbosity": verbosity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        url = d.pop("url")

        header_match = d.pop("header_match")

        created_at = d.pop("created_at")

        verbosity = d.pop("verbosity")

        create_external_feeds_response_200 = cls(
            id=id,
            display_name=display_name,
            url=url,
            header_match=header_match,
            created_at=created_at,
            verbosity=verbosity,
        )

        create_external_feeds_response_200.additional_properties = d
        return create_external_feeds_response_200

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
