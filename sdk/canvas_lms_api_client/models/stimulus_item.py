from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StimulusItem")


@_attrs_define
class StimulusItem:
    """
    Attributes:
        title (str):
        body (str):
        instructions (str):
        source_url (str):
        orientation (str):
        passage (bool):
    """

    title: str
    body: str
    instructions: str
    source_url: str
    orientation: str
    passage: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        body = self.body

        instructions = self.instructions

        source_url = self.source_url

        orientation = self.orientation

        passage = self.passage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "body": body,
                "instructions": instructions,
                "source_url": source_url,
                "orientation": orientation,
                "passage": passage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        body = d.pop("body")

        instructions = d.pop("instructions")

        source_url = d.pop("source_url")

        orientation = d.pop("orientation")

        passage = d.pop("passage")

        stimulus_item = cls(
            title=title,
            body=body,
            instructions=instructions,
            source_url=source_url,
            orientation=orientation,
            passage=passage,
        )

        stimulus_item.additional_properties = d
        return stimulus_item

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
