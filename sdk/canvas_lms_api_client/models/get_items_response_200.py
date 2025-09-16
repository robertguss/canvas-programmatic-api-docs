from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetItemsResponse200")


@_attrs_define
class GetItemsResponse200:
    """
    Attributes:
        id (str):
        position (int):
        points_possible (float):
        entry_type (str):
        entry_editable (bool):
        stimulus_quiz_entry_id (str):
        status (str):
        properties (None):
        entry (None):
    """

    id: str
    position: int
    points_possible: float
    entry_type: str
    entry_editable: bool
    stimulus_quiz_entry_id: str
    status: str
    properties: None
    entry: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position

        points_possible = self.points_possible

        entry_type = self.entry_type

        entry_editable = self.entry_editable

        stimulus_quiz_entry_id = self.stimulus_quiz_entry_id

        status = self.status

        properties = self.properties

        entry = self.entry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "position": position,
                "points_possible": points_possible,
                "entry_type": entry_type,
                "entry_editable": entry_editable,
                "stimulus_quiz_entry_id": stimulus_quiz_entry_id,
                "status": status,
                "properties": properties,
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        position = d.pop("position")

        points_possible = d.pop("points_possible")

        entry_type = d.pop("entry_type")

        entry_editable = d.pop("entry_editable")

        stimulus_quiz_entry_id = d.pop("stimulus_quiz_entry_id")

        status = d.pop("status")

        properties = d.pop("properties")

        entry = d.pop("entry")

        get_items_response_200 = cls(
            id=id,
            position=position,
            points_possible=points_possible,
            entry_type=entry_type,
            entry_editable=entry_editable,
            stimulus_quiz_entry_id=stimulus_quiz_entry_id,
            status=status,
            properties=properties,
            entry=entry,
        )

        get_items_response_200.additional_properties = d
        return get_items_response_200

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
