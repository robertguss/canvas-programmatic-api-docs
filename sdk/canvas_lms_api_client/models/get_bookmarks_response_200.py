from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_bookmarks_response_200_data import GetBookmarksResponse200Data


T = TypeVar("T", bound="GetBookmarksResponse200")


@_attrs_define
class GetBookmarksResponse200:
    """
    Attributes:
        id (int):
        name (str):
        url (str):
        position (int):
        data (GetBookmarksResponse200Data):
    """

    id: int
    name: str
    url: str
    position: int
    data: "GetBookmarksResponse200Data"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        url = self.url

        position = self.position

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "url": url,
                "position": position,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bookmarks_response_200_data import GetBookmarksResponse200Data

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        url = d.pop("url")

        position = d.pop("position")

        data = GetBookmarksResponse200Data.from_dict(d.pop("data"))

        get_bookmarks_response_200 = cls(
            id=id,
            name=name,
            url=url,
            position=position,
            data=data,
        )

        get_bookmarks_response_200.additional_properties = d
        return get_bookmarks_response_200

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
