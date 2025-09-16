from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateMigrationIssuesResponse200")


@_attrs_define
class UpdateMigrationIssuesResponse200:
    """
    Attributes:
        id (int):
        content_migration_url (str):
        description (str):
        workflow_state (str):
        fix_issue_html_url (str):
        issue_type (str):
        error_report_html_url (str):
        error_message (str):
        created_at (str):
        updated_at (str):
    """

    id: int
    content_migration_url: str
    description: str
    workflow_state: str
    fix_issue_html_url: str
    issue_type: str
    error_report_html_url: str
    error_message: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content_migration_url = self.content_migration_url

        description = self.description

        workflow_state = self.workflow_state

        fix_issue_html_url = self.fix_issue_html_url

        issue_type = self.issue_type

        error_report_html_url = self.error_report_html_url

        error_message = self.error_message

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "content_migration_url": content_migration_url,
                "description": description,
                "workflow_state": workflow_state,
                "fix_issue_html_url": fix_issue_html_url,
                "issue_type": issue_type,
                "error_report_html_url": error_report_html_url,
                "error_message": error_message,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        content_migration_url = d.pop("content_migration_url")

        description = d.pop("description")

        workflow_state = d.pop("workflow_state")

        fix_issue_html_url = d.pop("fix_issue_html_url")

        issue_type = d.pop("issue_type")

        error_report_html_url = d.pop("error_report_html_url")

        error_message = d.pop("error_message")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        update_migration_issues_response_200 = cls(
            id=id,
            content_migration_url=content_migration_url,
            description=description,
            workflow_state=workflow_state,
            fix_issue_html_url=fix_issue_html_url,
            issue_type=issue_type,
            error_report_html_url=error_report_html_url,
            error_message=error_message,
            created_at=created_at,
            updated_at=updated_at,
        )

        update_migration_issues_response_200.additional_properties = d
        return update_migration_issues_response_200

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
