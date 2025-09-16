from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.feature_feature_flag import FeatureFeatureFlag


T = TypeVar("T", bound="Feature")


@_attrs_define
class Feature:
    """
    Attributes:
        feature (str):
        display_name (str):
        applies_to (str):
        feature_flag (FeatureFeatureFlag):
        root_opt_in (bool):
        beta (bool):
        autoexpand (bool):
        release_notes_url (str):
    """

    feature: str
    display_name: str
    applies_to: str
    feature_flag: "FeatureFeatureFlag"
    root_opt_in: bool
    beta: bool
    autoexpand: bool
    release_notes_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        feature = self.feature

        display_name = self.display_name

        applies_to = self.applies_to

        feature_flag = self.feature_flag.to_dict()

        root_opt_in = self.root_opt_in

        beta = self.beta

        autoexpand = self.autoexpand

        release_notes_url = self.release_notes_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature": feature,
                "display_name": display_name,
                "applies_to": applies_to,
                "feature_flag": feature_flag,
                "root_opt_in": root_opt_in,
                "beta": beta,
                "autoexpand": autoexpand,
                "release_notes_url": release_notes_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_feature_flag import FeatureFeatureFlag

        d = dict(src_dict)
        feature = d.pop("feature")

        display_name = d.pop("display_name")

        applies_to = d.pop("applies_to")

        feature_flag = FeatureFeatureFlag.from_dict(d.pop("feature_flag"))

        root_opt_in = d.pop("root_opt_in")

        beta = d.pop("beta")

        autoexpand = d.pop("autoexpand")

        release_notes_url = d.pop("release_notes_url")

        feature = cls(
            feature=feature,
            display_name=display_name,
            applies_to=applies_to,
            feature_flag=feature_flag,
            root_opt_in=root_opt_in,
            beta=beta,
            autoexpand=autoexpand,
            release_notes_url=release_notes_url,
        )

        feature.additional_properties = d
        return feature

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
