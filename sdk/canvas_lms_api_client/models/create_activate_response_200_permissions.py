from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_activate_response_200_permissions_read_course_content import (
        CreateActivateResponse200PermissionsReadCourseContent,
    )
    from ..models.create_activate_response_200_permissions_read_course_list import (
        CreateActivateResponse200PermissionsReadCourseList,
    )
    from ..models.create_activate_response_200_permissions_read_question_banks import (
        CreateActivateResponse200PermissionsReadQuestionBanks,
    )
    from ..models.create_activate_response_200_permissions_read_reports import (
        CreateActivateResponse200PermissionsReadReports,
    )


T = TypeVar("T", bound="CreateActivateResponse200Permissions")


@_attrs_define
class CreateActivateResponse200Permissions:
    """
    Attributes:
        read_course_content (CreateActivateResponse200PermissionsReadCourseContent):
        read_course_list (CreateActivateResponse200PermissionsReadCourseList):
        read_question_banks (CreateActivateResponse200PermissionsReadQuestionBanks):
        read_reports (CreateActivateResponse200PermissionsReadReports):
    """

    read_course_content: "CreateActivateResponse200PermissionsReadCourseContent"
    read_course_list: "CreateActivateResponse200PermissionsReadCourseList"
    read_question_banks: "CreateActivateResponse200PermissionsReadQuestionBanks"
    read_reports: "CreateActivateResponse200PermissionsReadReports"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        read_course_content = self.read_course_content.to_dict()

        read_course_list = self.read_course_list.to_dict()

        read_question_banks = self.read_question_banks.to_dict()

        read_reports = self.read_reports.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "read_course_content": read_course_content,
                "read_course_list": read_course_list,
                "read_question_banks": read_question_banks,
                "read_reports": read_reports,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_activate_response_200_permissions_read_course_content import (
            CreateActivateResponse200PermissionsReadCourseContent,
        )
        from ..models.create_activate_response_200_permissions_read_course_list import (
            CreateActivateResponse200PermissionsReadCourseList,
        )
        from ..models.create_activate_response_200_permissions_read_question_banks import (
            CreateActivateResponse200PermissionsReadQuestionBanks,
        )
        from ..models.create_activate_response_200_permissions_read_reports import (
            CreateActivateResponse200PermissionsReadReports,
        )

        d = dict(src_dict)
        read_course_content = CreateActivateResponse200PermissionsReadCourseContent.from_dict(
            d.pop("read_course_content")
        )

        read_course_list = CreateActivateResponse200PermissionsReadCourseList.from_dict(d.pop("read_course_list"))

        read_question_banks = CreateActivateResponse200PermissionsReadQuestionBanks.from_dict(
            d.pop("read_question_banks")
        )

        read_reports = CreateActivateResponse200PermissionsReadReports.from_dict(d.pop("read_reports"))

        create_activate_response_200_permissions = cls(
            read_course_content=read_course_content,
            read_course_list=read_course_list,
            read_question_banks=read_question_banks,
            read_reports=read_reports,
        )

        create_activate_response_200_permissions.additional_properties = d
        return create_activate_response_200_permissions

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
