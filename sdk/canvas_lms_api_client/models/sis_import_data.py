from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SisImportData")


@_attrs_define
class SisImportData:
    """
    Attributes:
        import_type (str):
        supplied_batches (list[str]):
        counts (None):
    """

    import_type: str
    supplied_batches: list[str]
    counts: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        import_type = self.import_type

        supplied_batches = self.supplied_batches

        counts = self.counts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "import_type": import_type,
                "supplied_batches": supplied_batches,
                "counts": counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        import_type = d.pop("import_type")

        supplied_batches = cast(list[str], d.pop("supplied_batches"))

        counts = d.pop("counts")

        sis_import_data = cls(
            import_type=import_type,
            supplied_batches=supplied_batches,
            counts=counts,
        )

        sis_import_data.additional_properties = d
        return sis_import_data

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
