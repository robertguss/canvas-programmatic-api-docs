from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SisImportCounts")


@_attrs_define
class SisImportCounts:
    """
    Attributes:
        accounts (int):
        terms (int):
        abstract_courses (int):
        courses (int):
        sections (int):
        xlists (int):
        users (int):
        enrollments (int):
        groups (int):
        group_memberships (int):
        grade_publishing_results (int):
        batch_courses_deleted (int):
        batch_sections_deleted (int):
        batch_enrollments_deleted (int):
        error_count (int):
        warning_count (int):
    """

    accounts: int
    terms: int
    abstract_courses: int
    courses: int
    sections: int
    xlists: int
    users: int
    enrollments: int
    groups: int
    group_memberships: int
    grade_publishing_results: int
    batch_courses_deleted: int
    batch_sections_deleted: int
    batch_enrollments_deleted: int
    error_count: int
    warning_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = self.accounts

        terms = self.terms

        abstract_courses = self.abstract_courses

        courses = self.courses

        sections = self.sections

        xlists = self.xlists

        users = self.users

        enrollments = self.enrollments

        groups = self.groups

        group_memberships = self.group_memberships

        grade_publishing_results = self.grade_publishing_results

        batch_courses_deleted = self.batch_courses_deleted

        batch_sections_deleted = self.batch_sections_deleted

        batch_enrollments_deleted = self.batch_enrollments_deleted

        error_count = self.error_count

        warning_count = self.warning_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "terms": terms,
                "abstract_courses": abstract_courses,
                "courses": courses,
                "sections": sections,
                "xlists": xlists,
                "users": users,
                "enrollments": enrollments,
                "groups": groups,
                "group_memberships": group_memberships,
                "grade_publishing_results": grade_publishing_results,
                "batch_courses_deleted": batch_courses_deleted,
                "batch_sections_deleted": batch_sections_deleted,
                "batch_enrollments_deleted": batch_enrollments_deleted,
                "error_count": error_count,
                "warning_count": warning_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        accounts = d.pop("accounts")

        terms = d.pop("terms")

        abstract_courses = d.pop("abstract_courses")

        courses = d.pop("courses")

        sections = d.pop("sections")

        xlists = d.pop("xlists")

        users = d.pop("users")

        enrollments = d.pop("enrollments")

        groups = d.pop("groups")

        group_memberships = d.pop("group_memberships")

        grade_publishing_results = d.pop("grade_publishing_results")

        batch_courses_deleted = d.pop("batch_courses_deleted")

        batch_sections_deleted = d.pop("batch_sections_deleted")

        batch_enrollments_deleted = d.pop("batch_enrollments_deleted")

        error_count = d.pop("error_count")

        warning_count = d.pop("warning_count")

        sis_import_counts = cls(
            accounts=accounts,
            terms=terms,
            abstract_courses=abstract_courses,
            courses=courses,
            sections=sections,
            xlists=xlists,
            users=users,
            enrollments=enrollments,
            groups=groups,
            group_memberships=group_memberships,
            grade_publishing_results=grade_publishing_results,
            batch_courses_deleted=batch_courses_deleted,
            batch_sections_deleted=batch_sections_deleted,
            batch_enrollments_deleted=batch_enrollments_deleted,
            error_count=error_count,
            warning_count=warning_count,
        )

        sis_import_counts.additional_properties = d
        return sis_import_counts

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
