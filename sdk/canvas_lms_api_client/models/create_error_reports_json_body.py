from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateErrorReportsJsonBody")


@_attrs_define
class CreateErrorReportsJsonBody:
    """
    Attributes:
        errorsubject (Union[Unset, str]): The summary of the problem
        errorhttp_env (Union[Unset, str]): A collection of metadata about the users’ environment. If not provided,
            canvas will collect it based on information found in the request. (Doesn’t have to be HTTPENV info, could be
            anything JSON object that can be serialized as a hash, a mobile app might include relevant metadata for itself)
    """

    errorsubject: Union[Unset, str] = UNSET
    errorhttp_env: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errorsubject = self.errorsubject

        errorhttp_env = self.errorhttp_env

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errorsubject is not UNSET:
            field_dict["error[subject]"] = errorsubject
        if errorhttp_env is not UNSET:
            field_dict["error[http_env]"] = errorhttp_env

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        errorsubject = d.pop("error[subject]", UNSET)

        errorhttp_env = d.pop("error[http_env]", UNSET)

        create_error_reports_json_body = cls(
            errorsubject=errorsubject,
            errorhttp_env=errorhttp_env,
        )

        create_error_reports_json_body.additional_properties = d
        return create_error_reports_json_body

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
