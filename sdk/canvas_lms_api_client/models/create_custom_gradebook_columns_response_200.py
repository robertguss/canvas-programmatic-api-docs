from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCustomGradebookColumnsResponse200")


@_attrs_define
class CreateCustomGradebookColumnsResponse200:
    """
    Attributes:
        id (int):
        teacher_notes (bool):
        title (str):
        position (int):
        hidden (bool):
        read_only (bool):
    """

    id: int
    teacher_notes: bool
    title: str
    position: int
    hidden: bool
    read_only: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        teacher_notes = self.teacher_notes

        title = self.title

        position = self.position

        hidden = self.hidden

        read_only = self.read_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "teacher_notes": teacher_notes,
                "title": title,
                "position": position,
                "hidden": hidden,
                "read_only": read_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        teacher_notes = d.pop("teacher_notes")

        title = d.pop("title")

        position = d.pop("position")

        hidden = d.pop("hidden")

        read_only = d.pop("read_only")

        create_custom_gradebook_columns_response_200 = cls(
            id=id,
            teacher_notes=teacher_notes,
            title=title,
            position=position,
            hidden=hidden,
            read_only=read_only,
        )

        create_custom_gradebook_columns_response_200.additional_properties = d
        return create_custom_gradebook_columns_response_200

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
