from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlannerNotesJsonBody")


@_attrs_define
class CreatePlannerNotesJsonBody:
    """
    Attributes:
        todo_date (Union[Unset, str]): The date where this planner note should appear in the planner. The value should
            be formatted as: yyyy-mm-dd.
    """

    todo_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        todo_date = self.todo_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if todo_date is not UNSET:
            field_dict["todo_date"] = todo_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        todo_date = d.pop("todo_date", UNSET)

        create_planner_notes_json_body = cls(
            todo_date=todo_date,
        )

        create_planner_notes_json_body.additional_properties = d
        return create_planner_notes_json_body

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
