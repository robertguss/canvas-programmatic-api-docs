from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.course_event_links import CourseEventLinks


T = TypeVar("T", bound="CourseEvent")


@_attrs_define
class CourseEvent:
    """
    Attributes:
        id (str):
        created_at (str):
        event_type (str):
        event_data (str):
        event_source (str):
        links (CourseEventLinks):
    """

    id: str
    created_at: str
    event_type: str
    event_data: str
    event_source: str
    links: "CourseEventLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        event_type = self.event_type

        event_data = self.event_data

        event_source = self.event_source

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "event_type": event_type,
                "event_data": event_data,
                "event_source": event_source,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.course_event_links import CourseEventLinks

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        event_data = d.pop("event_data")

        event_source = d.pop("event_source")

        links = CourseEventLinks.from_dict(d.pop("links"))

        course_event = cls(
            id=id,
            created_at=created_at,
            event_type=event_type,
            event_data=event_data,
            event_source=event_source,
            links=links,
        )

        course_event.additional_properties = d
        return course_event

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
