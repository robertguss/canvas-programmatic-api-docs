from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SectionAttributes")


@_attrs_define
class SectionAttributes:
    """
    Attributes:
        id (int):
        name (str):
        sis_id (str):
        integration_id (str):
        origin_course (None):
        xlist_course (None):
        override (None):
    """

    id: int
    name: str
    sis_id: str
    integration_id: str
    origin_course: None
    xlist_course: None
    override: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sis_id = self.sis_id

        integration_id = self.integration_id

        origin_course = self.origin_course

        xlist_course = self.xlist_course

        override = self.override

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sis_id": sis_id,
                "integration_id": integration_id,
                "origin_course": origin_course,
                "xlist_course": xlist_course,
                "override": override,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sis_id = d.pop("sis_id")

        integration_id = d.pop("integration_id")

        origin_course = d.pop("origin_course")

        xlist_course = d.pop("xlist_course")

        override = d.pop("override")

        section_attributes = cls(
            id=id,
            name=name,
            sis_id=sis_id,
            integration_id=integration_id,
            origin_course=origin_course,
            xlist_course=xlist_course,
            override=override,
        )

        section_attributes.additional_properties = d
        return section_attributes

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
