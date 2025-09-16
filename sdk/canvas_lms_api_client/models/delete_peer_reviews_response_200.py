from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeletePeerReviewsResponse200")


@_attrs_define
class DeletePeerReviewsResponse200:
    """
    Attributes:
        assessor_id (int):
        asset_id (int):
        asset_type (str):
        id (int):
        user_id (int):
        workflow_state (str):
        user (str):
        assessor (str):
        submission_comments (str):
    """

    assessor_id: int
    asset_id: int
    asset_type: str
    id: int
    user_id: int
    workflow_state: str
    user: str
    assessor: str
    submission_comments: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assessor_id = self.assessor_id

        asset_id = self.asset_id

        asset_type = self.asset_type

        id = self.id

        user_id = self.user_id

        workflow_state = self.workflow_state

        user = self.user

        assessor = self.assessor

        submission_comments = self.submission_comments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assessor_id": assessor_id,
                "asset_id": asset_id,
                "asset_type": asset_type,
                "id": id,
                "user_id": user_id,
                "workflow_state": workflow_state,
                "user": user,
                "assessor": assessor,
                "submission_comments": submission_comments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assessor_id = d.pop("assessor_id")

        asset_id = d.pop("asset_id")

        asset_type = d.pop("asset_type")

        id = d.pop("id")

        user_id = d.pop("user_id")

        workflow_state = d.pop("workflow_state")

        user = d.pop("user")

        assessor = d.pop("assessor")

        submission_comments = d.pop("submission_comments")

        delete_peer_reviews_response_200 = cls(
            assessor_id=assessor_id,
            asset_id=asset_id,
            asset_type=asset_type,
            id=id,
            user_id=user_id,
            workflow_state=workflow_state,
            user=user,
            assessor=assessor,
            submission_comments=submission_comments,
        )

        delete_peer_reviews_response_200.additional_properties = d
        return delete_peer_reviews_response_200

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
