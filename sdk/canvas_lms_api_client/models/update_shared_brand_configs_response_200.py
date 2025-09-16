from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateSharedBrandConfigsResponse200")


@_attrs_define
class UpdateSharedBrandConfigsResponse200:
    """
    Attributes:
        id (int):
        account_id (str):
        brand_config_md5 (str):
        name (str):
        created_at (str):
        updated_at (str):
    """

    id: int
    account_id: str
    brand_config_md5: str
    name: str
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        brand_config_md5 = self.brand_config_md5

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "account_id": account_id,
                "brand_config_md5": brand_config_md5,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        account_id = d.pop("account_id")

        brand_config_md5 = d.pop("brand_config_md5")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        update_shared_brand_configs_response_200 = cls(
            id=id,
            account_id=account_id,
            brand_config_md5=brand_config_md5,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        update_shared_brand_configs_response_200.additional_properties = d
        return update_shared_brand_configs_response_200

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
