from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.list_courses_response_200_item_blueprint_restrictions import (
        ListCoursesResponse200ItemBlueprintRestrictions,
    )
    from ..models.list_courses_response_200_item_blueprint_restrictions_by_object_type import (
        ListCoursesResponse200ItemBlueprintRestrictionsByObjectType,
    )
    from ..models.list_courses_response_200_item_permissions import ListCoursesResponse200ItemPermissions


T = TypeVar("T", bound="ListCoursesResponse200Item")


@_attrs_define
class ListCoursesResponse200Item:
    """
    Attributes:
        id (int):
        sis_course_id (None):
        uuid (str):
        integration_id (None):
        sis_import_id (int):
        name (str):
        course_code (str):
        original_name (str):
        workflow_state (str):
        account_id (int):
        root_account_id (int):
        enrollment_term_id (int):
        grading_periods (None):
        grading_standard_id (int):
        grade_passback_setting (str):
        created_at (str):
        start_at (str):
        end_at (str):
        locale (str):
        enrollments (None):
        total_students (int):
        calendar (None):
        default_view (str):
        syllabus_body (str):
        needs_grading_count (int):
        term (None):
        course_progress (None):
        apply_assignment_group_weights (bool):
        permissions (ListCoursesResponse200ItemPermissions):
        is_public (bool):
        is_public_to_auth_users (bool):
        public_syllabus (bool):
        public_syllabus_to_auth (bool):
        public_description (str):
        storage_quota_mb (int):
        storage_quota_used_mb (int):
        hide_final_grades (bool):
        license_ (str):
        allow_student_assignment_edits (bool):
        allow_wiki_comments (bool):
        allow_student_forum_attachments (bool):
        open_enrollment (bool):
        self_enrollment (bool):
        restrict_enrollments_to_course_dates (bool):
        course_format (str):
        access_restricted_by_date (bool):
        time_zone (str):
        blueprint (bool):
        blueprint_restrictions (ListCoursesResponse200ItemBlueprintRestrictions):
        blueprint_restrictions_by_object_type (ListCoursesResponse200ItemBlueprintRestrictionsByObjectType):
        template (bool):
    """

    id: int
    sis_course_id: None
    uuid: str
    integration_id: None
    sis_import_id: int
    name: str
    course_code: str
    original_name: str
    workflow_state: str
    account_id: int
    root_account_id: int
    enrollment_term_id: int
    grading_periods: None
    grading_standard_id: int
    grade_passback_setting: str
    created_at: str
    start_at: str
    end_at: str
    locale: str
    enrollments: None
    total_students: int
    calendar: None
    default_view: str
    syllabus_body: str
    needs_grading_count: int
    term: None
    course_progress: None
    apply_assignment_group_weights: bool
    permissions: "ListCoursesResponse200ItemPermissions"
    is_public: bool
    is_public_to_auth_users: bool
    public_syllabus: bool
    public_syllabus_to_auth: bool
    public_description: str
    storage_quota_mb: int
    storage_quota_used_mb: int
    hide_final_grades: bool
    license_: str
    allow_student_assignment_edits: bool
    allow_wiki_comments: bool
    allow_student_forum_attachments: bool
    open_enrollment: bool
    self_enrollment: bool
    restrict_enrollments_to_course_dates: bool
    course_format: str
    access_restricted_by_date: bool
    time_zone: str
    blueprint: bool
    blueprint_restrictions: "ListCoursesResponse200ItemBlueprintRestrictions"
    blueprint_restrictions_by_object_type: "ListCoursesResponse200ItemBlueprintRestrictionsByObjectType"
    template: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sis_course_id = self.sis_course_id

        uuid = self.uuid

        integration_id = self.integration_id

        sis_import_id = self.sis_import_id

        name = self.name

        course_code = self.course_code

        original_name = self.original_name

        workflow_state = self.workflow_state

        account_id = self.account_id

        root_account_id = self.root_account_id

        enrollment_term_id = self.enrollment_term_id

        grading_periods = self.grading_periods

        grading_standard_id = self.grading_standard_id

        grade_passback_setting = self.grade_passback_setting

        created_at = self.created_at

        start_at = self.start_at

        end_at = self.end_at

        locale = self.locale

        enrollments = self.enrollments

        total_students = self.total_students

        calendar = self.calendar

        default_view = self.default_view

        syllabus_body = self.syllabus_body

        needs_grading_count = self.needs_grading_count

        term = self.term

        course_progress = self.course_progress

        apply_assignment_group_weights = self.apply_assignment_group_weights

        permissions = self.permissions.to_dict()

        is_public = self.is_public

        is_public_to_auth_users = self.is_public_to_auth_users

        public_syllabus = self.public_syllabus

        public_syllabus_to_auth = self.public_syllabus_to_auth

        public_description = self.public_description

        storage_quota_mb = self.storage_quota_mb

        storage_quota_used_mb = self.storage_quota_used_mb

        hide_final_grades = self.hide_final_grades

        license_ = self.license_

        allow_student_assignment_edits = self.allow_student_assignment_edits

        allow_wiki_comments = self.allow_wiki_comments

        allow_student_forum_attachments = self.allow_student_forum_attachments

        open_enrollment = self.open_enrollment

        self_enrollment = self.self_enrollment

        restrict_enrollments_to_course_dates = self.restrict_enrollments_to_course_dates

        course_format = self.course_format

        access_restricted_by_date = self.access_restricted_by_date

        time_zone = self.time_zone

        blueprint = self.blueprint

        blueprint_restrictions = self.blueprint_restrictions.to_dict()

        blueprint_restrictions_by_object_type = self.blueprint_restrictions_by_object_type.to_dict()

        template = self.template

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sis_course_id": sis_course_id,
                "uuid": uuid,
                "integration_id": integration_id,
                "sis_import_id": sis_import_id,
                "name": name,
                "course_code": course_code,
                "original_name": original_name,
                "workflow_state": workflow_state,
                "account_id": account_id,
                "root_account_id": root_account_id,
                "enrollment_term_id": enrollment_term_id,
                "grading_periods": grading_periods,
                "grading_standard_id": grading_standard_id,
                "grade_passback_setting": grade_passback_setting,
                "created_at": created_at,
                "start_at": start_at,
                "end_at": end_at,
                "locale": locale,
                "enrollments": enrollments,
                "total_students": total_students,
                "calendar": calendar,
                "default_view": default_view,
                "syllabus_body": syllabus_body,
                "needs_grading_count": needs_grading_count,
                "term": term,
                "course_progress": course_progress,
                "apply_assignment_group_weights": apply_assignment_group_weights,
                "permissions": permissions,
                "is_public": is_public,
                "is_public_to_auth_users": is_public_to_auth_users,
                "public_syllabus": public_syllabus,
                "public_syllabus_to_auth": public_syllabus_to_auth,
                "public_description": public_description,
                "storage_quota_mb": storage_quota_mb,
                "storage_quota_used_mb": storage_quota_used_mb,
                "hide_final_grades": hide_final_grades,
                "license": license_,
                "allow_student_assignment_edits": allow_student_assignment_edits,
                "allow_wiki_comments": allow_wiki_comments,
                "allow_student_forum_attachments": allow_student_forum_attachments,
                "open_enrollment": open_enrollment,
                "self_enrollment": self_enrollment,
                "restrict_enrollments_to_course_dates": restrict_enrollments_to_course_dates,
                "course_format": course_format,
                "access_restricted_by_date": access_restricted_by_date,
                "time_zone": time_zone,
                "blueprint": blueprint,
                "blueprint_restrictions": blueprint_restrictions,
                "blueprint_restrictions_by_object_type": blueprint_restrictions_by_object_type,
                "template": template,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_courses_response_200_item_blueprint_restrictions import (
            ListCoursesResponse200ItemBlueprintRestrictions,
        )
        from ..models.list_courses_response_200_item_blueprint_restrictions_by_object_type import (
            ListCoursesResponse200ItemBlueprintRestrictionsByObjectType,
        )
        from ..models.list_courses_response_200_item_permissions import ListCoursesResponse200ItemPermissions

        d = dict(src_dict)
        id = d.pop("id")

        sis_course_id = d.pop("sis_course_id")

        uuid = d.pop("uuid")

        integration_id = d.pop("integration_id")

        sis_import_id = d.pop("sis_import_id")

        name = d.pop("name")

        course_code = d.pop("course_code")

        original_name = d.pop("original_name")

        workflow_state = d.pop("workflow_state")

        account_id = d.pop("account_id")

        root_account_id = d.pop("root_account_id")

        enrollment_term_id = d.pop("enrollment_term_id")

        grading_periods = d.pop("grading_periods")

        grading_standard_id = d.pop("grading_standard_id")

        grade_passback_setting = d.pop("grade_passback_setting")

        created_at = d.pop("created_at")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        locale = d.pop("locale")

        enrollments = d.pop("enrollments")

        total_students = d.pop("total_students")

        calendar = d.pop("calendar")

        default_view = d.pop("default_view")

        syllabus_body = d.pop("syllabus_body")

        needs_grading_count = d.pop("needs_grading_count")

        term = d.pop("term")

        course_progress = d.pop("course_progress")

        apply_assignment_group_weights = d.pop("apply_assignment_group_weights")

        permissions = ListCoursesResponse200ItemPermissions.from_dict(d.pop("permissions"))

        is_public = d.pop("is_public")

        is_public_to_auth_users = d.pop("is_public_to_auth_users")

        public_syllabus = d.pop("public_syllabus")

        public_syllabus_to_auth = d.pop("public_syllabus_to_auth")

        public_description = d.pop("public_description")

        storage_quota_mb = d.pop("storage_quota_mb")

        storage_quota_used_mb = d.pop("storage_quota_used_mb")

        hide_final_grades = d.pop("hide_final_grades")

        license_ = d.pop("license")

        allow_student_assignment_edits = d.pop("allow_student_assignment_edits")

        allow_wiki_comments = d.pop("allow_wiki_comments")

        allow_student_forum_attachments = d.pop("allow_student_forum_attachments")

        open_enrollment = d.pop("open_enrollment")

        self_enrollment = d.pop("self_enrollment")

        restrict_enrollments_to_course_dates = d.pop("restrict_enrollments_to_course_dates")

        course_format = d.pop("course_format")

        access_restricted_by_date = d.pop("access_restricted_by_date")

        time_zone = d.pop("time_zone")

        blueprint = d.pop("blueprint")

        blueprint_restrictions = ListCoursesResponse200ItemBlueprintRestrictions.from_dict(
            d.pop("blueprint_restrictions")
        )

        blueprint_restrictions_by_object_type = ListCoursesResponse200ItemBlueprintRestrictionsByObjectType.from_dict(
            d.pop("blueprint_restrictions_by_object_type")
        )

        template = d.pop("template")

        list_courses_response_200_item = cls(
            id=id,
            sis_course_id=sis_course_id,
            uuid=uuid,
            integration_id=integration_id,
            sis_import_id=sis_import_id,
            name=name,
            course_code=course_code,
            original_name=original_name,
            workflow_state=workflow_state,
            account_id=account_id,
            root_account_id=root_account_id,
            enrollment_term_id=enrollment_term_id,
            grading_periods=grading_periods,
            grading_standard_id=grading_standard_id,
            grade_passback_setting=grade_passback_setting,
            created_at=created_at,
            start_at=start_at,
            end_at=end_at,
            locale=locale,
            enrollments=enrollments,
            total_students=total_students,
            calendar=calendar,
            default_view=default_view,
            syllabus_body=syllabus_body,
            needs_grading_count=needs_grading_count,
            term=term,
            course_progress=course_progress,
            apply_assignment_group_weights=apply_assignment_group_weights,
            permissions=permissions,
            is_public=is_public,
            is_public_to_auth_users=is_public_to_auth_users,
            public_syllabus=public_syllabus,
            public_syllabus_to_auth=public_syllabus_to_auth,
            public_description=public_description,
            storage_quota_mb=storage_quota_mb,
            storage_quota_used_mb=storage_quota_used_mb,
            hide_final_grades=hide_final_grades,
            license_=license_,
            allow_student_assignment_edits=allow_student_assignment_edits,
            allow_wiki_comments=allow_wiki_comments,
            allow_student_forum_attachments=allow_student_forum_attachments,
            open_enrollment=open_enrollment,
            self_enrollment=self_enrollment,
            restrict_enrollments_to_course_dates=restrict_enrollments_to_course_dates,
            course_format=course_format,
            access_restricted_by_date=access_restricted_by_date,
            time_zone=time_zone,
            blueprint=blueprint,
            blueprint_restrictions=blueprint_restrictions,
            blueprint_restrictions_by_object_type=blueprint_restrictions_by_object_type,
            template=template,
        )

        list_courses_response_200_item.additional_properties = d
        return list_courses_response_200_item

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
