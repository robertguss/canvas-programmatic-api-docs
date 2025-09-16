from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.quiz_submission_event_event_data import QuizSubmissionEventEventData


T = TypeVar("T", bound="QuizSubmissionEvent")


@_attrs_define
class QuizSubmissionEvent:
    """
    Attributes:
        created_at (str):
        event_type (str):
        event_data (QuizSubmissionEventEventData):
    """

    created_at: str
    event_type: str
    event_data: "QuizSubmissionEventEventData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        event_type = self.event_type

        event_data = self.event_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "event_type": event_type,
                "event_data": event_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quiz_submission_event_event_data import QuizSubmissionEventEventData

        d = dict(src_dict)
        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        event_data = QuizSubmissionEventEventData.from_dict(d.pop("event_data"))

        quiz_submission_event = cls(
            created_at=created_at,
            event_type=event_type,
            event_data=event_data,
        )

        quiz_submission_event.additional_properties = d
        return quiz_submission_event

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
