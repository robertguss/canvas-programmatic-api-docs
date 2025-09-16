from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateGroupResponse200")


@_attrs_define
class CreateGroupResponse200:
    """
    Attributes:
        id (int):
        learning_outcome_group_id (int):
        created_at (str):
        ended_at (str):
        updated_at (str):
        workflow_state (str):
        data (None):
        progress (str):
        user (None):
        processing_errors (list[list[Union[int, str]]]):
    """

    id: int
    learning_outcome_group_id: int
    created_at: str
    ended_at: str
    updated_at: str
    workflow_state: str
    data: None
    progress: str
    user: None
    processing_errors: list[list[Union[int, str]]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        learning_outcome_group_id = self.learning_outcome_group_id

        created_at = self.created_at

        ended_at = self.ended_at

        updated_at = self.updated_at

        workflow_state = self.workflow_state

        data = self.data

        progress = self.progress

        user = self.user

        processing_errors = []
        for processing_errors_item_data in self.processing_errors:
            processing_errors_item = []
            for processing_errors_item_item_data in processing_errors_item_data:
                processing_errors_item_item: Union[int, str]
                processing_errors_item_item = processing_errors_item_item_data
                processing_errors_item.append(processing_errors_item_item)

            processing_errors.append(processing_errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "learning_outcome_group_id": learning_outcome_group_id,
                "created_at": created_at,
                "ended_at": ended_at,
                "updated_at": updated_at,
                "workflow_state": workflow_state,
                "data": data,
                "progress": progress,
                "user": user,
                "processing_errors": processing_errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        learning_outcome_group_id = d.pop("learning_outcome_group_id")

        created_at = d.pop("created_at")

        ended_at = d.pop("ended_at")

        updated_at = d.pop("updated_at")

        workflow_state = d.pop("workflow_state")

        data = d.pop("data")

        progress = d.pop("progress")

        user = d.pop("user")

        processing_errors = []
        _processing_errors = d.pop("processing_errors")
        for processing_errors_item_data in _processing_errors:
            processing_errors_item = []
            _processing_errors_item = processing_errors_item_data
            for processing_errors_item_item_data in _processing_errors_item:

                def _parse_processing_errors_item_item(data: object) -> Union[int, str]:
                    return cast(Union[int, str], data)

                processing_errors_item_item = _parse_processing_errors_item_item(processing_errors_item_item_data)

                processing_errors_item.append(processing_errors_item_item)

            processing_errors.append(processing_errors_item)

        create_group_response_200 = cls(
            id=id,
            learning_outcome_group_id=learning_outcome_group_id,
            created_at=created_at,
            ended_at=ended_at,
            updated_at=updated_at,
            workflow_state=workflow_state,
            data=data,
            progress=progress,
            user=user,
            processing_errors=processing_errors,
        )

        create_group_response_200.additional_properties = d
        return create_group_response_200

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
