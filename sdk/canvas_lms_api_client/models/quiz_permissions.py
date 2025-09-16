from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QuizPermissions")


@_attrs_define
class QuizPermissions:
    """
    Attributes:
        read (bool):
        submit (bool):
        create (bool):
        manage (bool):
        read_statistics (bool):
        review_grades (bool):
        update (bool):
    """

    read: bool
    submit: bool
    create: bool
    manage: bool
    read_statistics: bool
    review_grades: bool
    update: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read = self.read

        submit = self.submit

        create = self.create

        manage = self.manage

        read_statistics = self.read_statistics

        review_grades = self.review_grades

        update = self.update

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read": read,
                "submit": submit,
                "create": create,
                "manage": manage,
                "read_statistics": read_statistics,
                "review_grades": review_grades,
                "update": update,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read = d.pop("read")

        submit = d.pop("submit")

        create = d.pop("create")

        manage = d.pop("manage")

        read_statistics = d.pop("read_statistics")

        review_grades = d.pop("review_grades")

        update = d.pop("update")

        quiz_permissions = cls(
            read=read,
            submit=submit,
            create=create,
            manage=manage,
            read_statistics=read_statistics,
            review_grades=review_grades,
            update=update,
        )

        quiz_permissions.additional_properties = d
        return quiz_permissions

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
