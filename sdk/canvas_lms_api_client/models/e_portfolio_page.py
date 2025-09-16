from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EPortfolioPage")


@_attrs_define
class EPortfolioPage:
    """
    Attributes:
        id (int):
        eportfolio_id (int):
        position (int):
        name (str):
        content (str):
        created_at (str):
        updated_at (str):
    """

    id: int
    eportfolio_id: int
    position: int
    name: str
    content: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        eportfolio_id = self.eportfolio_id

        position = self.position

        name = self.name

        content = self.content

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "eportfolio_id": eportfolio_id,
                "position": position,
                "name": name,
                "content": content,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        eportfolio_id = d.pop("eportfolio_id")

        position = d.pop("position")

        name = d.pop("name")

        content = d.pop("content")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        e_portfolio_page = cls(
            id=id,
            eportfolio_id=eportfolio_id,
            position=position,
            name=name,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
        )

        e_portfolio_page.additional_properties = d
        return e_portfolio_page

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
