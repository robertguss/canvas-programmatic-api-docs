from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSharedBrandConfigsDataBody")


@_attrs_define
class CreateSharedBrandConfigsDataBody:
    """
    Attributes:
        shared_brand_configname (Union[Unset, str]): Name to share this BrandConfig (theme) as.
        shared_brand_configbrand_config_md5 (Union[Unset, str]): MD5 of brand_config to share
    """

    shared_brand_configname: Union[Unset, str] = UNSET
    shared_brand_configbrand_config_md5: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shared_brand_configname = self.shared_brand_configname

        shared_brand_configbrand_config_md5 = self.shared_brand_configbrand_config_md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shared_brand_configname is not UNSET:
            field_dict["shared_brand_config[name]"] = shared_brand_configname
        if shared_brand_configbrand_config_md5 is not UNSET:
            field_dict["shared_brand_config[brand_config_md5]"] = shared_brand_configbrand_config_md5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shared_brand_configname = d.pop("shared_brand_config[name]", UNSET)

        shared_brand_configbrand_config_md5 = d.pop("shared_brand_config[brand_config_md5]", UNSET)

        create_shared_brand_configs_data_body = cls(
            shared_brand_configname=shared_brand_configname,
            shared_brand_configbrand_config_md5=shared_brand_configbrand_config_md5,
        )

        create_shared_brand_configs_data_body.additional_properties = d
        return create_shared_brand_configs_data_body

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
