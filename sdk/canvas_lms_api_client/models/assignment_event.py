from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignmentEvent")


@_attrs_define
class AssignmentEvent:
    """
    Attributes:
        id (str):
        title (str):
        start_at (str):
        end_at (str):
        description (str):
        context_code (str):
        workflow_state (str):
        url (str):
        html_url (str):
        all_day_date (str):
        all_day (bool):
        created_at (str):
        updated_at (str):
        assignment (None):
        assignment_overrides (None):
        important_dates (bool):
        rrule (str):
        series_head (None):
        series_natural_language (str):
    """

    id: str
    title: str
    start_at: str
    end_at: str
    description: str
    context_code: str
    workflow_state: str
    url: str
    html_url: str
    all_day_date: str
    all_day: bool
    created_at: str
    updated_at: str
    assignment: None
    assignment_overrides: None
    important_dates: bool
    rrule: str
    series_head: None
    series_natural_language: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        start_at = self.start_at

        end_at = self.end_at

        description = self.description

        context_code = self.context_code

        workflow_state = self.workflow_state

        url = self.url

        html_url = self.html_url

        all_day_date = self.all_day_date

        all_day = self.all_day

        created_at = self.created_at

        updated_at = self.updated_at

        assignment = self.assignment

        assignment_overrides = self.assignment_overrides

        important_dates = self.important_dates

        rrule = self.rrule

        series_head = self.series_head

        series_natural_language = self.series_natural_language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "start_at": start_at,
                "end_at": end_at,
                "description": description,
                "context_code": context_code,
                "workflow_state": workflow_state,
                "url": url,
                "html_url": html_url,
                "all_day_date": all_day_date,
                "all_day": all_day,
                "created_at": created_at,
                "updated_at": updated_at,
                "assignment": assignment,
                "assignment_overrides": assignment_overrides,
                "important_dates": important_dates,
                "rrule": rrule,
                "series_head": series_head,
                "series_natural_language": series_natural_language,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        description = d.pop("description")

        context_code = d.pop("context_code")

        workflow_state = d.pop("workflow_state")

        url = d.pop("url")

        html_url = d.pop("html_url")

        all_day_date = d.pop("all_day_date")

        all_day = d.pop("all_day")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        assignment = d.pop("assignment")

        assignment_overrides = d.pop("assignment_overrides")

        important_dates = d.pop("important_dates")

        rrule = d.pop("rrule")

        series_head = d.pop("series_head")

        series_natural_language = d.pop("series_natural_language")

        assignment_event = cls(
            id=id,
            title=title,
            start_at=start_at,
            end_at=end_at,
            description=description,
            context_code=context_code,
            workflow_state=workflow_state,
            url=url,
            html_url=html_url,
            all_day_date=all_day_date,
            all_day=all_day,
            created_at=created_at,
            updated_at=updated_at,
            assignment=assignment,
            assignment_overrides=assignment_overrides,
            important_dates=important_dates,
            rrule=rrule,
            series_head=series_head,
            series_natural_language=series_natural_language,
        )

        assignment_event.additional_properties = d
        return assignment_event

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
