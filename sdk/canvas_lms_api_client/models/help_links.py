from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.help_links_custom_help_links_item import HelpLinksCustomHelpLinksItem
    from ..models.help_links_default_help_links_item import HelpLinksDefaultHelpLinksItem


T = TypeVar("T", bound="HelpLinks")


@_attrs_define
class HelpLinks:
    """
    Attributes:
        help_link_name (str):
        help_link_icon (str):
        custom_help_links (list['HelpLinksCustomHelpLinksItem']):
        default_help_links (list['HelpLinksDefaultHelpLinksItem']):
    """

    help_link_name: str
    help_link_icon: str
    custom_help_links: list["HelpLinksCustomHelpLinksItem"]
    default_help_links: list["HelpLinksDefaultHelpLinksItem"]
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
        from ..models.help_links_custom_help_links_item import HelpLinksCustomHelpLinksItem
        from ..models.help_links_default_help_links_item import HelpLinksDefaultHelpLinksItem

        d = dict(src_dict)
        help_link_name = d.pop("help_link_name")

        help_link_icon = d.pop("help_link_icon")

        custom_help_links = []
        _custom_help_links = d.pop("custom_help_links")
        for custom_help_links_item_data in _custom_help_links:
            custom_help_links_item = HelpLinksCustomHelpLinksItem.from_dict(custom_help_links_item_data)

            custom_help_links.append(custom_help_links_item)

        default_help_links = []
        _default_help_links = d.pop("default_help_links")
        for default_help_links_item_data in _default_help_links:
            default_help_links_item = HelpLinksDefaultHelpLinksItem.from_dict(default_help_links_item_data)

            default_help_links.append(default_help_links_item)

        help_links = cls(
            help_link_name=help_link_name,
            help_link_icon=help_link_icon,
            custom_help_links=custom_help_links,
            default_help_links=default_help_links,
        )

        help_links.additional_properties = d
        return help_links

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
