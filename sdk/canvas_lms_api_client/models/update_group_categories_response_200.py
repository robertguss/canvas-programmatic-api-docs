from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateGroupCategoriesResponse200")


@_attrs_define
class UpdateGroupCategoriesResponse200:
    """
    Attributes:
        id (int):
        name (str):
        role (str):
        self_signup (None):
        auto_leader (None):
        context_type (str):
        account_id (int):
        group_limit (None):
        sis_group_category_id (None):
        sis_import_id (None):
        progress (None):
        non_collaborative (None):
    """

    id: int
    name: str
    role: str
    self_signup: None
    auto_leader: None
    context_type: str
    account_id: int
    group_limit: None
    sis_group_category_id: None
    sis_import_id: None
    progress: None
    non_collaborative: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        role = self.role

        self_signup = self.self_signup

        auto_leader = self.auto_leader

        context_type = self.context_type

        account_id = self.account_id

        group_limit = self.group_limit

        sis_group_category_id = self.sis_group_category_id

        sis_import_id = self.sis_import_id

        progress = self.progress

        non_collaborative = self.non_collaborative

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "role": role,
                "self_signup": self_signup,
                "auto_leader": auto_leader,
                "context_type": context_type,
                "account_id": account_id,
                "group_limit": group_limit,
                "sis_group_category_id": sis_group_category_id,
                "sis_import_id": sis_import_id,
                "progress": progress,
                "non_collaborative": non_collaborative,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        role = d.pop("role")

        self_signup = d.pop("self_signup")

        auto_leader = d.pop("auto_leader")

        context_type = d.pop("context_type")

        account_id = d.pop("account_id")

        group_limit = d.pop("group_limit")

        sis_group_category_id = d.pop("sis_group_category_id")

        sis_import_id = d.pop("sis_import_id")

        progress = d.pop("progress")

        non_collaborative = d.pop("non_collaborative")

        update_group_categories_response_200 = cls(
            id=id,
            name=name,
            role=role,
            self_signup=self_signup,
            auto_leader=auto_leader,
            context_type=context_type,
            account_id=account_id,
            group_limit=group_limit,
            sis_group_category_id=sis_group_category_id,
            sis_import_id=sis_import_id,
            progress=progress,
            non_collaborative=non_collaborative,
        )

        update_group_categories_response_200.additional_properties = d
        return update_group_categories_response_200

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
