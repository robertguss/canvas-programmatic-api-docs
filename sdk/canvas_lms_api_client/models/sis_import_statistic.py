from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SisImportStatistic")


@_attrs_define
class SisImportStatistic:
    """
    Attributes:
        created (int):
        concluded (int):
        deactivated (int):
        restored (int):
        deleted (int):
    """

    created: int
    concluded: int
    deactivated: int
    restored: int
    deleted: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        concluded = self.concluded

        deactivated = self.deactivated

        restored = self.restored

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "concluded": concluded,
                "deactivated": deactivated,
                "restored": restored,
                "deleted": deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created")

        concluded = d.pop("concluded")

        deactivated = d.pop("deactivated")

        restored = d.pop("restored")

        deleted = d.pop("deleted")

        sis_import_statistic = cls(
            created=created,
            concluded=concluded,
            deactivated=deactivated,
            restored=restored,
            deleted=deleted,
        )

        sis_import_statistic.additional_properties = d
        return sis_import_statistic

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
