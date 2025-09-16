from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_enrollments_response_200_grades import DeleteEnrollmentsResponse200Grades
    from ..models.delete_enrollments_response_200_user import DeleteEnrollmentsResponse200User


T = TypeVar("T", bound="DeleteEnrollmentsResponse200")


@_attrs_define
class DeleteEnrollmentsResponse200:
    """
    Attributes:
        id (int):
        course_id (int):
        sis_course_id (str):
        course_integration_id (str):
        course_section_id (int):
        section_integration_id (str):
        sis_account_id (str):
        sis_section_id (str):
        sis_user_id (str):
        enrollment_state (str):
        limit_privileges_to_course_section (bool):
        sis_import_id (int):
        root_account_id (int):
        type_ (str):
        user_id (int):
        associated_user_id (None):
        role (str):
        role_id (int):
        created_at (str):
        updated_at (str):
        start_at (str):
        end_at (str):
        last_activity_at (str):
        last_attended_at (str):
        total_activity_time (int):
        html_url (str):
        grades (DeleteEnrollmentsResponse200Grades):
        user (DeleteEnrollmentsResponse200User):
        override_grade (str):
        override_score (float):
        unposted_current_grade (str):
        unposted_final_grade (str):
        unposted_current_score (str):
        unposted_final_score (str):
        has_grading_periods (bool):
        totals_for_all_grading_periods_option (bool):
        current_grading_period_title (str):
        current_grading_period_id (int):
        current_period_override_grade (str):
        current_period_override_score (float):
        current_period_unposted_current_score (float):
        current_period_unposted_final_score (float):
        current_period_unposted_current_grade (str):
        current_period_unposted_final_grade (str):
    """

    id: int
    course_id: int
    sis_course_id: str
    course_integration_id: str
    course_section_id: int
    section_integration_id: str
    sis_account_id: str
    sis_section_id: str
    sis_user_id: str
    enrollment_state: str
    limit_privileges_to_course_section: bool
    sis_import_id: int
    root_account_id: int
    type_: str
    user_id: int
    associated_user_id: None
    role: str
    role_id: int
    created_at: str
    updated_at: str
    start_at: str
    end_at: str
    last_activity_at: str
    last_attended_at: str
    total_activity_time: int
    html_url: str
    grades: "DeleteEnrollmentsResponse200Grades"
    user: "DeleteEnrollmentsResponse200User"
    override_grade: str
    override_score: float
    unposted_current_grade: str
    unposted_final_grade: str
    unposted_current_score: str
    unposted_final_score: str
    has_grading_periods: bool
    totals_for_all_grading_periods_option: bool
    current_grading_period_title: str
    current_grading_period_id: int
    current_period_override_grade: str
    current_period_override_score: float
    current_period_unposted_current_score: float
    current_period_unposted_final_score: float
    current_period_unposted_current_grade: str
    current_period_unposted_final_grade: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        course_id = self.course_id

        sis_course_id = self.sis_course_id

        course_integration_id = self.course_integration_id

        course_section_id = self.course_section_id

        section_integration_id = self.section_integration_id

        sis_account_id = self.sis_account_id

        sis_section_id = self.sis_section_id

        sis_user_id = self.sis_user_id

        enrollment_state = self.enrollment_state

        limit_privileges_to_course_section = self.limit_privileges_to_course_section

        sis_import_id = self.sis_import_id

        root_account_id = self.root_account_id

        type_ = self.type_

        user_id = self.user_id

        associated_user_id = self.associated_user_id

        role = self.role

        role_id = self.role_id

        created_at = self.created_at

        updated_at = self.updated_at

        start_at = self.start_at

        end_at = self.end_at

        last_activity_at = self.last_activity_at

        last_attended_at = self.last_attended_at

        total_activity_time = self.total_activity_time

        html_url = self.html_url

        grades = self.grades.to_dict()

        user = self.user.to_dict()

        override_grade = self.override_grade

        override_score = self.override_score

        unposted_current_grade = self.unposted_current_grade

        unposted_final_grade = self.unposted_final_grade

        unposted_current_score = self.unposted_current_score

        unposted_final_score = self.unposted_final_score

        has_grading_periods = self.has_grading_periods

        totals_for_all_grading_periods_option = self.totals_for_all_grading_periods_option

        current_grading_period_title = self.current_grading_period_title

        current_grading_period_id = self.current_grading_period_id

        current_period_override_grade = self.current_period_override_grade

        current_period_override_score = self.current_period_override_score

        current_period_unposted_current_score = self.current_period_unposted_current_score

        current_period_unposted_final_score = self.current_period_unposted_final_score

        current_period_unposted_current_grade = self.current_period_unposted_current_grade

        current_period_unposted_final_grade = self.current_period_unposted_final_grade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "course_id": course_id,
                "sis_course_id": sis_course_id,
                "course_integration_id": course_integration_id,
                "course_section_id": course_section_id,
                "section_integration_id": section_integration_id,
                "sis_account_id": sis_account_id,
                "sis_section_id": sis_section_id,
                "sis_user_id": sis_user_id,
                "enrollment_state": enrollment_state,
                "limit_privileges_to_course_section": limit_privileges_to_course_section,
                "sis_import_id": sis_import_id,
                "root_account_id": root_account_id,
                "type": type_,
                "user_id": user_id,
                "associated_user_id": associated_user_id,
                "role": role,
                "role_id": role_id,
                "created_at": created_at,
                "updated_at": updated_at,
                "start_at": start_at,
                "end_at": end_at,
                "last_activity_at": last_activity_at,
                "last_attended_at": last_attended_at,
                "total_activity_time": total_activity_time,
                "html_url": html_url,
                "grades": grades,
                "user": user,
                "override_grade": override_grade,
                "override_score": override_score,
                "unposted_current_grade": unposted_current_grade,
                "unposted_final_grade": unposted_final_grade,
                "unposted_current_score": unposted_current_score,
                "unposted_final_score": unposted_final_score,
                "has_grading_periods": has_grading_periods,
                "totals_for_all_grading_periods_option": totals_for_all_grading_periods_option,
                "current_grading_period_title": current_grading_period_title,
                "current_grading_period_id": current_grading_period_id,
                "current_period_override_grade": current_period_override_grade,
                "current_period_override_score": current_period_override_score,
                "current_period_unposted_current_score": current_period_unposted_current_score,
                "current_period_unposted_final_score": current_period_unposted_final_score,
                "current_period_unposted_current_grade": current_period_unposted_current_grade,
                "current_period_unposted_final_grade": current_period_unposted_final_grade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_enrollments_response_200_grades import DeleteEnrollmentsResponse200Grades
        from ..models.delete_enrollments_response_200_user import DeleteEnrollmentsResponse200User

        d = dict(src_dict)
        id = d.pop("id")

        course_id = d.pop("course_id")

        sis_course_id = d.pop("sis_course_id")

        course_integration_id = d.pop("course_integration_id")

        course_section_id = d.pop("course_section_id")

        section_integration_id = d.pop("section_integration_id")

        sis_account_id = d.pop("sis_account_id")

        sis_section_id = d.pop("sis_section_id")

        sis_user_id = d.pop("sis_user_id")

        enrollment_state = d.pop("enrollment_state")

        limit_privileges_to_course_section = d.pop("limit_privileges_to_course_section")

        sis_import_id = d.pop("sis_import_id")

        root_account_id = d.pop("root_account_id")

        type_ = d.pop("type")

        user_id = d.pop("user_id")

        associated_user_id = d.pop("associated_user_id")

        role = d.pop("role")

        role_id = d.pop("role_id")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        last_activity_at = d.pop("last_activity_at")

        last_attended_at = d.pop("last_attended_at")

        total_activity_time = d.pop("total_activity_time")

        html_url = d.pop("html_url")

        grades = DeleteEnrollmentsResponse200Grades.from_dict(d.pop("grades"))

        user = DeleteEnrollmentsResponse200User.from_dict(d.pop("user"))

        override_grade = d.pop("override_grade")

        override_score = d.pop("override_score")

        unposted_current_grade = d.pop("unposted_current_grade")

        unposted_final_grade = d.pop("unposted_final_grade")

        unposted_current_score = d.pop("unposted_current_score")

        unposted_final_score = d.pop("unposted_final_score")

        has_grading_periods = d.pop("has_grading_periods")

        totals_for_all_grading_periods_option = d.pop("totals_for_all_grading_periods_option")

        current_grading_period_title = d.pop("current_grading_period_title")

        current_grading_period_id = d.pop("current_grading_period_id")

        current_period_override_grade = d.pop("current_period_override_grade")

        current_period_override_score = d.pop("current_period_override_score")

        current_period_unposted_current_score = d.pop("current_period_unposted_current_score")

        current_period_unposted_final_score = d.pop("current_period_unposted_final_score")

        current_period_unposted_current_grade = d.pop("current_period_unposted_current_grade")

        current_period_unposted_final_grade = d.pop("current_period_unposted_final_grade")

        delete_enrollments_response_200 = cls(
            id=id,
            course_id=course_id,
            sis_course_id=sis_course_id,
            course_integration_id=course_integration_id,
            course_section_id=course_section_id,
            section_integration_id=section_integration_id,
            sis_account_id=sis_account_id,
            sis_section_id=sis_section_id,
            sis_user_id=sis_user_id,
            enrollment_state=enrollment_state,
            limit_privileges_to_course_section=limit_privileges_to_course_section,
            sis_import_id=sis_import_id,
            root_account_id=root_account_id,
            type_=type_,
            user_id=user_id,
            associated_user_id=associated_user_id,
            role=role,
            role_id=role_id,
            created_at=created_at,
            updated_at=updated_at,
            start_at=start_at,
            end_at=end_at,
            last_activity_at=last_activity_at,
            last_attended_at=last_attended_at,
            total_activity_time=total_activity_time,
            html_url=html_url,
            grades=grades,
            user=user,
            override_grade=override_grade,
            override_score=override_score,
            unposted_current_grade=unposted_current_grade,
            unposted_final_grade=unposted_final_grade,
            unposted_current_score=unposted_current_score,
            unposted_final_score=unposted_final_score,
            has_grading_periods=has_grading_periods,
            totals_for_all_grading_periods_option=totals_for_all_grading_periods_option,
            current_grading_period_title=current_grading_period_title,
            current_grading_period_id=current_grading_period_id,
            current_period_override_grade=current_period_override_grade,
            current_period_override_score=current_period_override_score,
            current_period_unposted_current_score=current_period_unposted_current_score,
            current_period_unposted_final_score=current_period_unposted_final_score,
            current_period_unposted_current_grade=current_period_unposted_current_grade,
            current_period_unposted_final_grade=current_period_unposted_final_grade,
        )

        delete_enrollments_response_200.additional_properties = d
        return delete_enrollments_response_200

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
