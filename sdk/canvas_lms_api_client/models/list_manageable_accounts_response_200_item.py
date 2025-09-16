from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListManageableAccountsResponse200Item")


@_attrs_define
class ListManageableAccountsResponse200Item:
    """
    Attributes:
        id (int):
        name (str):
        uuid (str):
        parent_account_id (int):
        root_account_id (int):
        default_storage_quota_mb (int):
        default_user_storage_quota_mb (int):
        default_group_storage_quota_mb (int):
        default_time_zone (str):
        sis_account_id (str):
        integration_id (str):
        sis_import_id (int):
        course_count (int):
        sub_account_count (int):
        lti_guid (str):
        workflow_state (str):
    """

    id: int
    name: str
    uuid: str
    parent_account_id: int
    root_account_id: int
    default_storage_quota_mb: int
    default_user_storage_quota_mb: int
    default_group_storage_quota_mb: int
    default_time_zone: str
    sis_account_id: str
    integration_id: str
    sis_import_id: int
    course_count: int
    sub_account_count: int
    lti_guid: str
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        uuid = self.uuid

        parent_account_id = self.parent_account_id

        root_account_id = self.root_account_id

        default_storage_quota_mb = self.default_storage_quota_mb

        default_user_storage_quota_mb = self.default_user_storage_quota_mb

        default_group_storage_quota_mb = self.default_group_storage_quota_mb

        default_time_zone = self.default_time_zone

        sis_account_id = self.sis_account_id

        integration_id = self.integration_id

        sis_import_id = self.sis_import_id

        course_count = self.course_count

        sub_account_count = self.sub_account_count

        lti_guid = self.lti_guid

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "uuid": uuid,
                "parent_account_id": parent_account_id,
                "root_account_id": root_account_id,
                "default_storage_quota_mb": default_storage_quota_mb,
                "default_user_storage_quota_mb": default_user_storage_quota_mb,
                "default_group_storage_quota_mb": default_group_storage_quota_mb,
                "default_time_zone": default_time_zone,
                "sis_account_id": sis_account_id,
                "integration_id": integration_id,
                "sis_import_id": sis_import_id,
                "course_count": course_count,
                "sub_account_count": sub_account_count,
                "lti_guid": lti_guid,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        uuid = d.pop("uuid")

        parent_account_id = d.pop("parent_account_id")

        root_account_id = d.pop("root_account_id")

        default_storage_quota_mb = d.pop("default_storage_quota_mb")

        default_user_storage_quota_mb = d.pop("default_user_storage_quota_mb")

        default_group_storage_quota_mb = d.pop("default_group_storage_quota_mb")

        default_time_zone = d.pop("default_time_zone")

        sis_account_id = d.pop("sis_account_id")

        integration_id = d.pop("integration_id")

        sis_import_id = d.pop("sis_import_id")

        course_count = d.pop("course_count")

        sub_account_count = d.pop("sub_account_count")

        lti_guid = d.pop("lti_guid")

        workflow_state = d.pop("workflow_state")

        list_manageable_accounts_response_200_item = cls(
            id=id,
            name=name,
            uuid=uuid,
            parent_account_id=parent_account_id,
            root_account_id=root_account_id,
            default_storage_quota_mb=default_storage_quota_mb,
            default_user_storage_quota_mb=default_user_storage_quota_mb,
            default_group_storage_quota_mb=default_group_storage_quota_mb,
            default_time_zone=default_time_zone,
            sis_account_id=sis_account_id,
            integration_id=integration_id,
            sis_import_id=sis_import_id,
            course_count=course_count,
            sub_account_count=sub_account_count,
            lti_guid=lti_guid,
            workflow_state=workflow_state,
        )

        list_manageable_accounts_response_200_item.additional_properties = d
        return list_manageable_accounts_response_200_item

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
