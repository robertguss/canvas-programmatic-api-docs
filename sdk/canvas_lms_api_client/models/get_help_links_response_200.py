from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_help_links_response_200_custom_help_links_item import GetHelpLinksResponse200CustomHelpLinksItem
    from ..models.get_help_links_response_200_default_help_links_item import GetHelpLinksResponse200DefaultHelpLinksItem


T = TypeVar("T", bound="GetHelpLinksResponse200")


@_attrs_define
class GetHelpLinksResponse200:
    """
    Attributes:
        help_link_name (str):
        help_link_icon (str):
        custom_help_links (list['GetHelpLinksResponse200CustomHelpLinksItem']):
        default_help_links (list['GetHelpLinksResponse200DefaultHelpLinksItem']):
    """

    help_link_name: str
    help_link_icon: str
    custom_help_links: list["GetHelpLinksResponse200CustomHelpLinksItem"]
    default_help_links: list["GetHelpLinksResponse200DefaultHelpLinksItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        help_link_name = self.help_link_name

        help_link_icon = self.help_link_icon

        custom_help_links = []
        for custom_help_links_item_data in self.custom_help_links:
            custom_help_links_item = custom_help_links_item_data.to_dict()
            custom_help_links.append(custom_help_links_item)

        default_help_links = []
        for default_help_links_item_data in self.default_help_links:
            default_help_links_item = default_help_links_item_data.to_dict()
            default_help_links.append(default_help_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "help_link_name": help_link_name,
                "help_link_icon": help_link_icon,
                "custom_help_links": custom_help_links,
                "default_help_links": default_help_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_help_links_response_200_custom_help_links_item import (
            GetHelpLinksResponse200CustomHelpLinksItem,
        )
        from ..models.get_help_links_response_200_default_help_links_item import (
            GetHelpLinksResponse200DefaultHelpLinksItem,
        )

        d = dict(src_dict)
        help_link_name = d.pop("help_link_name")

        help_link_icon = d.pop("help_link_icon")

        custom_help_links = []
        _custom_help_links = d.pop("custom_help_links")
        for custom_help_links_item_data in _custom_help_links:
            custom_help_links_item = GetHelpLinksResponse200CustomHelpLinksItem.from_dict(custom_help_links_item_data)

            custom_help_links.append(custom_help_links_item)

        default_help_links = []
        _default_help_links = d.pop("default_help_links")
        for default_help_links_item_data in _default_help_links:
            default_help_links_item = GetHelpLinksResponse200DefaultHelpLinksItem.from_dict(
                default_help_links_item_data
            )

            default_help_links.append(default_help_links_item)

        get_help_links_response_200 = cls(
            help_link_name=help_link_name,
            help_link_icon=help_link_icon,
            custom_help_links=custom_help_links,
            default_help_links=default_help_links,
        )

        get_help_links_response_200.additional_properties = d
        return get_help_links_response_200

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
