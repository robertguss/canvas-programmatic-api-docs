from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_roles_response_200_item_permissions_read_course_content import (
        UpdateRolesResponse200ItemPermissionsReadCourseContent,
    )
    from ..models.update_roles_response_200_item_permissions_read_course_list import (
        UpdateRolesResponse200ItemPermissionsReadCourseList,
    )
    from ..models.update_roles_response_200_item_permissions_read_question_banks import (
        UpdateRolesResponse200ItemPermissionsReadQuestionBanks,
    )
    from ..models.update_roles_response_200_item_permissions_read_reports import (
        UpdateRolesResponse200ItemPermissionsReadReports,
    )


T = TypeVar("T", bound="UpdateRolesResponse200ItemPermissions")


@_attrs_define
class UpdateRolesResponse200ItemPermissions:
    """
    Attributes:
        read_course_content (UpdateRolesResponse200ItemPermissionsReadCourseContent):
        read_course_list (UpdateRolesResponse200ItemPermissionsReadCourseList):
        read_question_banks (UpdateRolesResponse200ItemPermissionsReadQuestionBanks):
        read_reports (UpdateRolesResponse200ItemPermissionsReadReports):
    """

    read_course_content: "UpdateRolesResponse200ItemPermissionsReadCourseContent"
    read_course_list: "UpdateRolesResponse200ItemPermissionsReadCourseList"
    read_question_banks: "UpdateRolesResponse200ItemPermissionsReadQuestionBanks"
    read_reports: "UpdateRolesResponse200ItemPermissionsReadReports"
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
        from ..models.update_roles_response_200_item_permissions_read_course_content import (
            UpdateRolesResponse200ItemPermissionsReadCourseContent,
        )
        from ..models.update_roles_response_200_item_permissions_read_course_list import (
            UpdateRolesResponse200ItemPermissionsReadCourseList,
        )
        from ..models.update_roles_response_200_item_permissions_read_question_banks import (
            UpdateRolesResponse200ItemPermissionsReadQuestionBanks,
        )
        from ..models.update_roles_response_200_item_permissions_read_reports import (
            UpdateRolesResponse200ItemPermissionsReadReports,
        )

        d = dict(src_dict)
        read_course_content = UpdateRolesResponse200ItemPermissionsReadCourseContent.from_dict(
            d.pop("read_course_content")
        )

        read_course_list = UpdateRolesResponse200ItemPermissionsReadCourseList.from_dict(d.pop("read_course_list"))

        read_question_banks = UpdateRolesResponse200ItemPermissionsReadQuestionBanks.from_dict(
            d.pop("read_question_banks")
        )

        read_reports = UpdateRolesResponse200ItemPermissionsReadReports.from_dict(d.pop("read_reports"))

        update_roles_response_200_item_permissions = cls(
            read_course_content=read_course_content,
            read_course_list=read_course_list,
            read_question_banks=read_question_banks,
            read_reports=read_reports,
        )

        update_roles_response_200_item_permissions.additional_properties = d
        return update_roles_response_200_item_permissions

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
