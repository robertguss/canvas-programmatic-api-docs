from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.progress_results import ProgressResults


T = TypeVar("T", bound="Progress")


@_attrs_define
class Progress:
    """
    Attributes:
        id (int):
        context_id (int):
        context_type (str):
        user_id (int):
        completion (int):
        workflow_state (str):
        created_at (str):
        updated_at (str):
        results (ProgressResults):
        url (str):
    """

    id: int
    context_id: int
    context_type: str
    user_id: int
    completion: int
    workflow_state: str
    created_at: str
    updated_at: str
    results: "ProgressResults"
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        context_id = self.context_id

        context_type = self.context_type

        user_id = self.user_id

        completion = self.completion

        workflow_state = self.workflow_state

        created_at = self.created_at

        updated_at = self.updated_at

        results = self.results.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "context_id": context_id,
                "context_type": context_type,
                "user_id": user_id,
                "completion": completion,
                "workflow_state": workflow_state,
                "created_at": created_at,
                "updated_at": updated_at,
                "results": results,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.progress_results import ProgressResults

        d = dict(src_dict)
        id = d.pop("id")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        user_id = d.pop("user_id")

        completion = d.pop("completion")

        workflow_state = d.pop("workflow_state")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        results = ProgressResults.from_dict(d.pop("results"))

        url = d.pop("url")

        progress = cls(
            id=id,
            context_id=context_id,
            context_type=context_type,
            user_id=user_id,
            completion=completion,
            workflow_state=workflow_state,
            created_at=created_at,
            updated_at=updated_at,
            results=results,
            url=url,
        )

        progress.additional_properties = d
        return progress

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
