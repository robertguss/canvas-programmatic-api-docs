from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateUsageRightsResponse200Item")


@_attrs_define
class UpdateUsageRightsResponse200Item:
    """
    Attributes:
        legal_copyright (str):
        use_justification (str):
        license_ (str):
        license_name (str):
        message (str):
        file_ids (list[int]):
    """

    legal_copyright: str
    use_justification: str
    license_: str
    license_name: str
    message: str
    file_ids: list[int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        legal_copyright = self.legal_copyright

        use_justification = self.use_justification

        license_ = self.license_

        license_name = self.license_name

        message = self.message

        file_ids = self.file_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "legal_copyright": legal_copyright,
                "use_justification": use_justification,
                "license": license_,
                "license_name": license_name,
                "message": message,
                "file_ids": file_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        legal_copyright = d.pop("legal_copyright")

        use_justification = d.pop("use_justification")

        license_ = d.pop("license")

        license_name = d.pop("license_name")

        message = d.pop("message")

        file_ids = cast(list[int], d.pop("file_ids"))

        update_usage_rights_response_200_item = cls(
            legal_copyright=legal_copyright,
            use_justification=use_justification,
            license_=license_,
            license_name=license_name,
            message=message,
            file_ids=file_ids,
        )

        update_usage_rights_response_200_item.additional_properties = d
        return update_usage_rights_response_200_item

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
