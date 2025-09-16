from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetSisImportErrorsResponse200Item")


@_attrs_define
class GetSisImportErrorsResponse200Item:
    """
    Attributes:
        sis_import_id (int):
        file (str):
        message (str):
        row_info (str):
        row (int):
    """

    sis_import_id: int
    file: str
    message: str
    row_info: str
    row: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sis_import_id = self.sis_import_id

        file = self.file

        message = self.message

        row_info = self.row_info

        row = self.row

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sis_import_id": sis_import_id,
                "file": file,
                "message": message,
                "row_info": row_info,
                "row": row,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sis_import_id = d.pop("sis_import_id")

        file = d.pop("file")

        message = d.pop("message")

        row_info = d.pop("row_info")

        row = d.pop("row")

        get_sis_import_errors_response_200_item = cls(
            sis_import_id=sis_import_id,
            file=file,
            message=message,
            row_info=row_info,
            row=row,
        )

        get_sis_import_errors_response_200_item.additional_properties = d
        return get_sis_import_errors_response_200_item

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
