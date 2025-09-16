from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SisImportStatistics")


@_attrs_define
class SisImportStatistics:
    """
    Attributes:
        total_state_changes (int):
        account (None):
        enrollment_term (None):
        communication_channel (None):
        abstract_course (None):
        course (None):
        course_section (None):
        enrollment (None):
        group_category (None):
        group (None):
        group_membership (None):
        pseudonym (None):
        user_observer (None):
        account_user (None):
    """

    total_state_changes: int
    account: None
    enrollment_term: None
    communication_channel: None
    abstract_course: None
    course: None
    course_section: None
    enrollment: None
    group_category: None
    group: None
    group_membership: None
    pseudonym: None
    user_observer: None
    account_user: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_state_changes = self.total_state_changes

        account = self.account

        enrollment_term = self.enrollment_term

        communication_channel = self.communication_channel

        abstract_course = self.abstract_course

        course = self.course

        course_section = self.course_section

        enrollment = self.enrollment

        group_category = self.group_category

        group = self.group

        group_membership = self.group_membership

        pseudonym = self.pseudonym

        user_observer = self.user_observer

        account_user = self.account_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_state_changes": total_state_changes,
                "Account": account,
                "EnrollmentTerm": enrollment_term,
                "CommunicationChannel": communication_channel,
                "AbstractCourse": abstract_course,
                "Course": course,
                "CourseSection": course_section,
                "Enrollment": enrollment,
                "GroupCategory": group_category,
                "Group": group,
                "GroupMembership": group_membership,
                "Pseudonym": pseudonym,
                "UserObserver": user_observer,
                "AccountUser": account_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_state_changes = d.pop("total_state_changes")

        account = d.pop("Account")

        enrollment_term = d.pop("EnrollmentTerm")

        communication_channel = d.pop("CommunicationChannel")

        abstract_course = d.pop("AbstractCourse")

        course = d.pop("Course")

        course_section = d.pop("CourseSection")

        enrollment = d.pop("Enrollment")

        group_category = d.pop("GroupCategory")

        group = d.pop("Group")

        group_membership = d.pop("GroupMembership")

        pseudonym = d.pop("Pseudonym")

        user_observer = d.pop("UserObserver")

        account_user = d.pop("AccountUser")

        sis_import_statistics = cls(
            total_state_changes=total_state_changes,
            account=account,
            enrollment_term=enrollment_term,
            communication_channel=communication_channel,
            abstract_course=abstract_course,
            course=course,
            course_section=course_section,
            enrollment=enrollment,
            group_category=group_category,
            group=group,
            group_membership=group_membership,
            pseudonym=pseudonym,
            user_observer=user_observer,
            account_user=account_user,
        )

        sis_import_statistics.additional_properties = d
        return sis_import_statistics

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
