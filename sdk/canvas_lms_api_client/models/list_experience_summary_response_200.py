from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListExperienceSummaryResponse200")


@_attrs_define
class ListExperienceSummaryResponse200:
    """
    Attributes:
        current_app (str):
        available_apps (list[str]):
    """

    current_app: str
    available_apps: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_app = self.current_app

        available_apps = self.available_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "current_app": current_app,
                "available_apps": available_apps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_app = d.pop("current_app")

        available_apps = cast(list[str], d.pop("available_apps"))

        list_experience_summary_response_200 = cls(
            current_app=current_app,
            available_apps=available_apps,
        )

        list_experience_summary_response_200.additional_properties = d
        return list_experience_summary_response_200

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
