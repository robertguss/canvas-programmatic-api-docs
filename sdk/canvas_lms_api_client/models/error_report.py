from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ErrorReport")


@_attrs_define
class ErrorReport:
    """
    Attributes:
        subject (str):
        comments (str):
        user_perceived_severity (str):
        email (str):
        url (str):
        context_asset_string (str):
        user_roles (str):
    """

    subject: str
    comments: str
    user_perceived_severity: str
    email: str
    url: str
    context_asset_string: str
    user_roles: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subject = self.subject

        comments = self.comments

        user_perceived_severity = self.user_perceived_severity

        email = self.email

        url = self.url

        context_asset_string = self.context_asset_string

        user_roles = self.user_roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subject": subject,
                "comments": comments,
                "user_perceived_severity": user_perceived_severity,
                "email": email,
                "url": url,
                "context_asset_string": context_asset_string,
                "user_roles": user_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subject = d.pop("subject")

        comments = d.pop("comments")

        user_perceived_severity = d.pop("user_perceived_severity")

        email = d.pop("email")

        url = d.pop("url")

        context_asset_string = d.pop("context_asset_string")

        user_roles = d.pop("user_roles")

        error_report = cls(
            subject=subject,
            comments=comments,
            user_perceived_severity=user_perceived_severity,
            email=email,
            url=url,
            context_asset_string=context_asset_string,
            user_roles=user_roles,
        )

        error_report.additional_properties = d
        return error_report

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
