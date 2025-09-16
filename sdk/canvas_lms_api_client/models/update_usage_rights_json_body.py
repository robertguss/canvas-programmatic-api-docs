from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUsageRightsJsonBody")


@_attrs_define
class UpdateUsageRightsJsonBody:
    """
    Attributes:
        file_ids (Union[Unset, str]): List of ids of files to set usage rights for.
        usage_rightsuse_justification (Union[Unset, str]): The intellectual property justification for using the files
            in CanvasAllowed values: own_copyright, used_by_permission, fair_use, public_domain, creative_commons
    """

    file_ids: Union[Unset, str] = UNSET
    usage_rightsuse_justification: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_ids = self.file_ids

        usage_rightsuse_justification = self.usage_rightsuse_justification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_ids is not UNSET:
            field_dict["file_ids[]"] = file_ids
        if usage_rightsuse_justification is not UNSET:
            field_dict["usage_rights[use_justification]"] = usage_rightsuse_justification

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_ids = d.pop("file_ids[]", UNSET)

        usage_rightsuse_justification = d.pop("usage_rights[use_justification]", UNSET)

        update_usage_rights_json_body = cls(
            file_ids=file_ids,
            usage_rightsuse_justification=usage_rightsuse_justification,
        )

        update_usage_rights_json_body.additional_properties = d
        return update_usage_rights_json_body

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
