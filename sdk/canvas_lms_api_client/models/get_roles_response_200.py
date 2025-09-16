from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_roles_response_200_account import GetRolesResponse200Account
    from ..models.get_roles_response_200_permissions import GetRolesResponse200Permissions


T = TypeVar("T", bound="GetRolesResponse200")


@_attrs_define
class GetRolesResponse200:
    """
    Attributes:
        id (int):
        label (str):
        role (str):
        base_role_type (str):
        is_account_role (bool):
        account (GetRolesResponse200Account):
        workflow_state (str):
        created_at (str):
        last_updated_at (str):
        permissions (GetRolesResponse200Permissions):
    """

    id: int
    label: str
    role: str
    base_role_type: str
    is_account_role: bool
    account: "GetRolesResponse200Account"
    workflow_state: str
    created_at: str
    last_updated_at: str
    permissions: "GetRolesResponse200Permissions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label = self.label

        role = self.role

        base_role_type = self.base_role_type

        is_account_role = self.is_account_role

        account = self.account.to_dict()

        workflow_state = self.workflow_state

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        permissions = self.permissions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "role": role,
                "base_role_type": base_role_type,
                "is_account_role": is_account_role,
                "account": account,
                "workflow_state": workflow_state,
                "created_at": created_at,
                "last_updated_at": last_updated_at,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_roles_response_200_account import GetRolesResponse200Account
        from ..models.get_roles_response_200_permissions import GetRolesResponse200Permissions

        d = dict(src_dict)
        id = d.pop("id")

        label = d.pop("label")

        role = d.pop("role")

        base_role_type = d.pop("base_role_type")

        is_account_role = d.pop("is_account_role")

        account = GetRolesResponse200Account.from_dict(d.pop("account"))

        workflow_state = d.pop("workflow_state")

        created_at = d.pop("created_at")

        last_updated_at = d.pop("last_updated_at")

        permissions = GetRolesResponse200Permissions.from_dict(d.pop("permissions"))

        get_roles_response_200 = cls(
            id=id,
            label=label,
            role=role,
            base_role_type=base_role_type,
            is_account_role=is_account_role,
            account=account,
            workflow_state=workflow_state,
            created_at=created_at,
            last_updated_at=last_updated_at,
            permissions=permissions,
        )

        get_roles_response_200.additional_properties = d
        return get_roles_response_200

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
