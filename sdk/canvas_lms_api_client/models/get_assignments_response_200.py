from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_assignments_response_200_integration_data import GetAssignmentsResponse200IntegrationData
    from ..models.get_assignments_response_200_needs_grading_count_by_section_item import (
        GetAssignmentsResponse200NeedsGradingCountBySectionItem,
    )
    from ..models.get_assignments_response_200_rubric_settings import GetAssignmentsResponse200RubricSettings


T = TypeVar("T", bound="GetAssignmentsResponse200")


@_attrs_define
class GetAssignmentsResponse200:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        created_at (str):
        updated_at (str):
        due_at (str):
        lock_at (str):
        unlock_at (str):
        has_overrides (bool):
        all_dates (None):
        course_id (int):
        html_url (str):
        submissions_download_url (str):
        assignment_group_id (int):
        due_date_required (bool):
        allowed_extensions (list[str]):
        max_name_length (int):
        turnitin_enabled (bool):
        vericite_enabled (bool):
        turnitin_settings (None):
        grade_group_students_individually (bool):
        external_tool_tag_attributes (None):
        peer_reviews (bool):
        automatic_peer_reviews (bool):
        peer_review_count (int):
        peer_reviews_assign_at (str):
        intra_group_peer_reviews (bool):
        group_category_id (int):
        needs_grading_count (int):
        needs_grading_count_by_section (list['GetAssignmentsResponse200NeedsGradingCountBySectionItem']):
        position (int):
        post_to_sis (bool):
        integration_id (str):
        integration_data (GetAssignmentsResponse200IntegrationData):
        points_possible (float):
        submission_types (list[str]):
        has_submitted_submissions (bool):
        grading_type (str):
        grading_standard_id (None):
        published (bool):
        unpublishable (bool):
        only_visible_to_overrides (bool):
        locked_for_user (bool):
        lock_info (None):
        lock_explanation (str):
        quiz_id (int):
        anonymous_submissions (bool):
        discussion_topic (None):
        freeze_on_copy (bool):
        frozen (bool):
        frozen_attributes (list[str]):
        submission (None):
        use_rubric_for_grading (bool):
        rubric_settings (GetAssignmentsResponse200RubricSettings):
        rubric (None):
        assignment_visibility (list[int]):
        overrides (None):
        omit_from_final_grade (bool):
        hide_in_gradebook (bool):
        moderated_grading (bool):
        grader_count (int):
        final_grader_id (int):
        grader_comments_visible_to_graders (bool):
        graders_anonymous_to_graders (bool):
        grader_names_visible_to_final_grader (bool):
        anonymous_grading (bool):
        allowed_attempts (int):
        post_manually (bool):
        score_statistics (None):
        can_submit (bool):
        ab_guid (list[str]):
        annotatable_attachment_id (None):
        anonymize_students (bool):
        require_lockdown_browser (bool):
        important_dates (bool):
        muted (bool):
        anonymous_peer_reviews (bool):
        anonymous_instructor_annotations (bool):
        graded_submissions_exist (bool):
        is_quiz_assignment (bool):
        in_closed_grading_period (bool):
        can_duplicate (bool):
        original_course_id (int):
        original_assignment_id (int):
        original_lti_resource_link_id (int):
        original_assignment_name (str):
        original_quiz_id (int):
        workflow_state (str):
    """

    id: int
    name: str
    description: str
    created_at: str
    updated_at: str
    due_at: str
    lock_at: str
    unlock_at: str
    has_overrides: bool
    all_dates: None
    course_id: int
    html_url: str
    submissions_download_url: str
    assignment_group_id: int
    due_date_required: bool
    allowed_extensions: list[str]
    max_name_length: int
    turnitin_enabled: bool
    vericite_enabled: bool
    turnitin_settings: None
    grade_group_students_individually: bool
    external_tool_tag_attributes: None
    peer_reviews: bool
    automatic_peer_reviews: bool
    peer_review_count: int
    peer_reviews_assign_at: str
    intra_group_peer_reviews: bool
    group_category_id: int
    needs_grading_count: int
    needs_grading_count_by_section: list["GetAssignmentsResponse200NeedsGradingCountBySectionItem"]
    position: int
    post_to_sis: bool
    integration_id: str
    integration_data: "GetAssignmentsResponse200IntegrationData"
    points_possible: float
    submission_types: list[str]
    has_submitted_submissions: bool
    grading_type: str
    grading_standard_id: None
    published: bool
    unpublishable: bool
    only_visible_to_overrides: bool
    locked_for_user: bool
    lock_info: None
    lock_explanation: str
    quiz_id: int
    anonymous_submissions: bool
    discussion_topic: None
    freeze_on_copy: bool
    frozen: bool
    frozen_attributes: list[str]
    submission: None
    use_rubric_for_grading: bool
    rubric_settings: "GetAssignmentsResponse200RubricSettings"
    rubric: None
    assignment_visibility: list[int]
    overrides: None
    omit_from_final_grade: bool
    hide_in_gradebook: bool
    moderated_grading: bool
    grader_count: int
    final_grader_id: int
    grader_comments_visible_to_graders: bool
    graders_anonymous_to_graders: bool
    grader_names_visible_to_final_grader: bool
    anonymous_grading: bool
    allowed_attempts: int
    post_manually: bool
    score_statistics: None
    can_submit: bool
    ab_guid: list[str]
    annotatable_attachment_id: None
    anonymize_students: bool
    require_lockdown_browser: bool
    important_dates: bool
    muted: bool
    anonymous_peer_reviews: bool
    anonymous_instructor_annotations: bool
    graded_submissions_exist: bool
    is_quiz_assignment: bool
    in_closed_grading_period: bool
    can_duplicate: bool
    original_course_id: int
    original_assignment_id: int
    original_lti_resource_link_id: int
    original_assignment_name: str
    original_quiz_id: int
    workflow_state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        created_at = self.created_at

        updated_at = self.updated_at

        due_at = self.due_at

        lock_at = self.lock_at

        unlock_at = self.unlock_at

        has_overrides = self.has_overrides

        all_dates = self.all_dates

        course_id = self.course_id

        html_url = self.html_url

        submissions_download_url = self.submissions_download_url

        assignment_group_id = self.assignment_group_id

        due_date_required = self.due_date_required

        allowed_extensions = self.allowed_extensions

        max_name_length = self.max_name_length

        turnitin_enabled = self.turnitin_enabled

        vericite_enabled = self.vericite_enabled

        turnitin_settings = self.turnitin_settings

        grade_group_students_individually = self.grade_group_students_individually

        external_tool_tag_attributes = self.external_tool_tag_attributes

        peer_reviews = self.peer_reviews

        automatic_peer_reviews = self.automatic_peer_reviews

        peer_review_count = self.peer_review_count

        peer_reviews_assign_at = self.peer_reviews_assign_at

        intra_group_peer_reviews = self.intra_group_peer_reviews

        group_category_id = self.group_category_id

        needs_grading_count = self.needs_grading_count

        needs_grading_count_by_section = []
        for needs_grading_count_by_section_item_data in self.needs_grading_count_by_section:
            needs_grading_count_by_section_item = needs_grading_count_by_section_item_data.to_dict()
            needs_grading_count_by_section.append(needs_grading_count_by_section_item)

        position = self.position

        post_to_sis = self.post_to_sis

        integration_id = self.integration_id

        integration_data = self.integration_data.to_dict()

        points_possible = self.points_possible

        submission_types = self.submission_types

        has_submitted_submissions = self.has_submitted_submissions

        grading_type = self.grading_type

        grading_standard_id = self.grading_standard_id

        published = self.published

        unpublishable = self.unpublishable

        only_visible_to_overrides = self.only_visible_to_overrides

        locked_for_user = self.locked_for_user

        lock_info = self.lock_info

        lock_explanation = self.lock_explanation

        quiz_id = self.quiz_id

        anonymous_submissions = self.anonymous_submissions

        discussion_topic = self.discussion_topic

        freeze_on_copy = self.freeze_on_copy

        frozen = self.frozen

        frozen_attributes = self.frozen_attributes

        submission = self.submission

        use_rubric_for_grading = self.use_rubric_for_grading

        rubric_settings = self.rubric_settings.to_dict()

        rubric = self.rubric

        assignment_visibility = self.assignment_visibility

        overrides = self.overrides

        omit_from_final_grade = self.omit_from_final_grade

        hide_in_gradebook = self.hide_in_gradebook

        moderated_grading = self.moderated_grading

        grader_count = self.grader_count

        final_grader_id = self.final_grader_id

        grader_comments_visible_to_graders = self.grader_comments_visible_to_graders

        graders_anonymous_to_graders = self.graders_anonymous_to_graders

        grader_names_visible_to_final_grader = self.grader_names_visible_to_final_grader

        anonymous_grading = self.anonymous_grading

        allowed_attempts = self.allowed_attempts

        post_manually = self.post_manually

        score_statistics = self.score_statistics

        can_submit = self.can_submit

        ab_guid = self.ab_guid

        annotatable_attachment_id = self.annotatable_attachment_id

        anonymize_students = self.anonymize_students

        require_lockdown_browser = self.require_lockdown_browser

        important_dates = self.important_dates

        muted = self.muted

        anonymous_peer_reviews = self.anonymous_peer_reviews

        anonymous_instructor_annotations = self.anonymous_instructor_annotations

        graded_submissions_exist = self.graded_submissions_exist

        is_quiz_assignment = self.is_quiz_assignment

        in_closed_grading_period = self.in_closed_grading_period

        can_duplicate = self.can_duplicate

        original_course_id = self.original_course_id

        original_assignment_id = self.original_assignment_id

        original_lti_resource_link_id = self.original_lti_resource_link_id

        original_assignment_name = self.original_assignment_name

        original_quiz_id = self.original_quiz_id

        workflow_state = self.workflow_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "created_at": created_at,
                "updated_at": updated_at,
                "due_at": due_at,
                "lock_at": lock_at,
                "unlock_at": unlock_at,
                "has_overrides": has_overrides,
                "all_dates": all_dates,
                "course_id": course_id,
                "html_url": html_url,
                "submissions_download_url": submissions_download_url,
                "assignment_group_id": assignment_group_id,
                "due_date_required": due_date_required,
                "allowed_extensions": allowed_extensions,
                "max_name_length": max_name_length,
                "turnitin_enabled": turnitin_enabled,
                "vericite_enabled": vericite_enabled,
                "turnitin_settings": turnitin_settings,
                "grade_group_students_individually": grade_group_students_individually,
                "external_tool_tag_attributes": external_tool_tag_attributes,
                "peer_reviews": peer_reviews,
                "automatic_peer_reviews": automatic_peer_reviews,
                "peer_review_count": peer_review_count,
                "peer_reviews_assign_at": peer_reviews_assign_at,
                "intra_group_peer_reviews": intra_group_peer_reviews,
                "group_category_id": group_category_id,
                "needs_grading_count": needs_grading_count,
                "needs_grading_count_by_section": needs_grading_count_by_section,
                "position": position,
                "post_to_sis": post_to_sis,
                "integration_id": integration_id,
                "integration_data": integration_data,
                "points_possible": points_possible,
                "submission_types": submission_types,
                "has_submitted_submissions": has_submitted_submissions,
                "grading_type": grading_type,
                "grading_standard_id": grading_standard_id,
                "published": published,
                "unpublishable": unpublishable,
                "only_visible_to_overrides": only_visible_to_overrides,
                "locked_for_user": locked_for_user,
                "lock_info": lock_info,
                "lock_explanation": lock_explanation,
                "quiz_id": quiz_id,
                "anonymous_submissions": anonymous_submissions,
                "discussion_topic": discussion_topic,
                "freeze_on_copy": freeze_on_copy,
                "frozen": frozen,
                "frozen_attributes": frozen_attributes,
                "submission": submission,
                "use_rubric_for_grading": use_rubric_for_grading,
                "rubric_settings": rubric_settings,
                "rubric": rubric,
                "assignment_visibility": assignment_visibility,
                "overrides": overrides,
                "omit_from_final_grade": omit_from_final_grade,
                "hide_in_gradebook": hide_in_gradebook,
                "moderated_grading": moderated_grading,
                "grader_count": grader_count,
                "final_grader_id": final_grader_id,
                "grader_comments_visible_to_graders": grader_comments_visible_to_graders,
                "graders_anonymous_to_graders": graders_anonymous_to_graders,
                "grader_names_visible_to_final_grader": grader_names_visible_to_final_grader,
                "anonymous_grading": anonymous_grading,
                "allowed_attempts": allowed_attempts,
                "post_manually": post_manually,
                "score_statistics": score_statistics,
                "can_submit": can_submit,
                "ab_guid": ab_guid,
                "annotatable_attachment_id": annotatable_attachment_id,
                "anonymize_students": anonymize_students,
                "require_lockdown_browser": require_lockdown_browser,
                "important_dates": important_dates,
                "muted": muted,
                "anonymous_peer_reviews": anonymous_peer_reviews,
                "anonymous_instructor_annotations": anonymous_instructor_annotations,
                "graded_submissions_exist": graded_submissions_exist,
                "is_quiz_assignment": is_quiz_assignment,
                "in_closed_grading_period": in_closed_grading_period,
                "can_duplicate": can_duplicate,
                "original_course_id": original_course_id,
                "original_assignment_id": original_assignment_id,
                "original_lti_resource_link_id": original_lti_resource_link_id,
                "original_assignment_name": original_assignment_name,
                "original_quiz_id": original_quiz_id,
                "workflow_state": workflow_state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_assignments_response_200_integration_data import GetAssignmentsResponse200IntegrationData
        from ..models.get_assignments_response_200_needs_grading_count_by_section_item import (
            GetAssignmentsResponse200NeedsGradingCountBySectionItem,
        )
        from ..models.get_assignments_response_200_rubric_settings import GetAssignmentsResponse200RubricSettings

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        due_at = d.pop("due_at")

        lock_at = d.pop("lock_at")

        unlock_at = d.pop("unlock_at")

        has_overrides = d.pop("has_overrides")

        all_dates = d.pop("all_dates")

        course_id = d.pop("course_id")

        html_url = d.pop("html_url")

        submissions_download_url = d.pop("submissions_download_url")

        assignment_group_id = d.pop("assignment_group_id")

        due_date_required = d.pop("due_date_required")

        allowed_extensions = cast(list[str], d.pop("allowed_extensions"))

        max_name_length = d.pop("max_name_length")

        turnitin_enabled = d.pop("turnitin_enabled")

        vericite_enabled = d.pop("vericite_enabled")

        turnitin_settings = d.pop("turnitin_settings")

        grade_group_students_individually = d.pop("grade_group_students_individually")

        external_tool_tag_attributes = d.pop("external_tool_tag_attributes")

        peer_reviews = d.pop("peer_reviews")

        automatic_peer_reviews = d.pop("automatic_peer_reviews")

        peer_review_count = d.pop("peer_review_count")

        peer_reviews_assign_at = d.pop("peer_reviews_assign_at")

        intra_group_peer_reviews = d.pop("intra_group_peer_reviews")

        group_category_id = d.pop("group_category_id")

        needs_grading_count = d.pop("needs_grading_count")

        needs_grading_count_by_section = []
        _needs_grading_count_by_section = d.pop("needs_grading_count_by_section")
        for needs_grading_count_by_section_item_data in _needs_grading_count_by_section:
            needs_grading_count_by_section_item = GetAssignmentsResponse200NeedsGradingCountBySectionItem.from_dict(
                needs_grading_count_by_section_item_data
            )

            needs_grading_count_by_section.append(needs_grading_count_by_section_item)

        position = d.pop("position")

        post_to_sis = d.pop("post_to_sis")

        integration_id = d.pop("integration_id")

        integration_data = GetAssignmentsResponse200IntegrationData.from_dict(d.pop("integration_data"))

        points_possible = d.pop("points_possible")

        submission_types = cast(list[str], d.pop("submission_types"))

        has_submitted_submissions = d.pop("has_submitted_submissions")

        grading_type = d.pop("grading_type")

        grading_standard_id = d.pop("grading_standard_id")

        published = d.pop("published")

        unpublishable = d.pop("unpublishable")

        only_visible_to_overrides = d.pop("only_visible_to_overrides")

        locked_for_user = d.pop("locked_for_user")

        lock_info = d.pop("lock_info")

        lock_explanation = d.pop("lock_explanation")

        quiz_id = d.pop("quiz_id")

        anonymous_submissions = d.pop("anonymous_submissions")

        discussion_topic = d.pop("discussion_topic")

        freeze_on_copy = d.pop("freeze_on_copy")

        frozen = d.pop("frozen")

        frozen_attributes = cast(list[str], d.pop("frozen_attributes"))

        submission = d.pop("submission")

        use_rubric_for_grading = d.pop("use_rubric_for_grading")

        rubric_settings = GetAssignmentsResponse200RubricSettings.from_dict(d.pop("rubric_settings"))

        rubric = d.pop("rubric")

        assignment_visibility = cast(list[int], d.pop("assignment_visibility"))

        overrides = d.pop("overrides")

        omit_from_final_grade = d.pop("omit_from_final_grade")

        hide_in_gradebook = d.pop("hide_in_gradebook")

        moderated_grading = d.pop("moderated_grading")

        grader_count = d.pop("grader_count")

        final_grader_id = d.pop("final_grader_id")

        grader_comments_visible_to_graders = d.pop("grader_comments_visible_to_graders")

        graders_anonymous_to_graders = d.pop("graders_anonymous_to_graders")

        grader_names_visible_to_final_grader = d.pop("grader_names_visible_to_final_grader")

        anonymous_grading = d.pop("anonymous_grading")

        allowed_attempts = d.pop("allowed_attempts")

        post_manually = d.pop("post_manually")

        score_statistics = d.pop("score_statistics")

        can_submit = d.pop("can_submit")

        ab_guid = cast(list[str], d.pop("ab_guid"))

        annotatable_attachment_id = d.pop("annotatable_attachment_id")

        anonymize_students = d.pop("anonymize_students")

        require_lockdown_browser = d.pop("require_lockdown_browser")

        important_dates = d.pop("important_dates")

        muted = d.pop("muted")

        anonymous_peer_reviews = d.pop("anonymous_peer_reviews")

        anonymous_instructor_annotations = d.pop("anonymous_instructor_annotations")

        graded_submissions_exist = d.pop("graded_submissions_exist")

        is_quiz_assignment = d.pop("is_quiz_assignment")

        in_closed_grading_period = d.pop("in_closed_grading_period")

        can_duplicate = d.pop("can_duplicate")

        original_course_id = d.pop("original_course_id")

        original_assignment_id = d.pop("original_assignment_id")

        original_lti_resource_link_id = d.pop("original_lti_resource_link_id")

        original_assignment_name = d.pop("original_assignment_name")

        original_quiz_id = d.pop("original_quiz_id")

        workflow_state = d.pop("workflow_state")

        get_assignments_response_200 = cls(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            due_at=due_at,
            lock_at=lock_at,
            unlock_at=unlock_at,
            has_overrides=has_overrides,
            all_dates=all_dates,
            course_id=course_id,
            html_url=html_url,
            submissions_download_url=submissions_download_url,
            assignment_group_id=assignment_group_id,
            due_date_required=due_date_required,
            allowed_extensions=allowed_extensions,
            max_name_length=max_name_length,
            turnitin_enabled=turnitin_enabled,
            vericite_enabled=vericite_enabled,
            turnitin_settings=turnitin_settings,
            grade_group_students_individually=grade_group_students_individually,
            external_tool_tag_attributes=external_tool_tag_attributes,
            peer_reviews=peer_reviews,
            automatic_peer_reviews=automatic_peer_reviews,
            peer_review_count=peer_review_count,
            peer_reviews_assign_at=peer_reviews_assign_at,
            intra_group_peer_reviews=intra_group_peer_reviews,
            group_category_id=group_category_id,
            needs_grading_count=needs_grading_count,
            needs_grading_count_by_section=needs_grading_count_by_section,
            position=position,
            post_to_sis=post_to_sis,
            integration_id=integration_id,
            integration_data=integration_data,
            points_possible=points_possible,
            submission_types=submission_types,
            has_submitted_submissions=has_submitted_submissions,
            grading_type=grading_type,
            grading_standard_id=grading_standard_id,
            published=published,
            unpublishable=unpublishable,
            only_visible_to_overrides=only_visible_to_overrides,
            locked_for_user=locked_for_user,
            lock_info=lock_info,
            lock_explanation=lock_explanation,
            quiz_id=quiz_id,
            anonymous_submissions=anonymous_submissions,
            discussion_topic=discussion_topic,
            freeze_on_copy=freeze_on_copy,
            frozen=frozen,
            frozen_attributes=frozen_attributes,
            submission=submission,
            use_rubric_for_grading=use_rubric_for_grading,
            rubric_settings=rubric_settings,
            rubric=rubric,
            assignment_visibility=assignment_visibility,
            overrides=overrides,
            omit_from_final_grade=omit_from_final_grade,
            hide_in_gradebook=hide_in_gradebook,
            moderated_grading=moderated_grading,
            grader_count=grader_count,
            final_grader_id=final_grader_id,
            grader_comments_visible_to_graders=grader_comments_visible_to_graders,
            graders_anonymous_to_graders=graders_anonymous_to_graders,
            grader_names_visible_to_final_grader=grader_names_visible_to_final_grader,
            anonymous_grading=anonymous_grading,
            allowed_attempts=allowed_attempts,
            post_manually=post_manually,
            score_statistics=score_statistics,
            can_submit=can_submit,
            ab_guid=ab_guid,
            annotatable_attachment_id=annotatable_attachment_id,
            anonymize_students=anonymize_students,
            require_lockdown_browser=require_lockdown_browser,
            important_dates=important_dates,
            muted=muted,
            anonymous_peer_reviews=anonymous_peer_reviews,
            anonymous_instructor_annotations=anonymous_instructor_annotations,
            graded_submissions_exist=graded_submissions_exist,
            is_quiz_assignment=is_quiz_assignment,
            in_closed_grading_period=in_closed_grading_period,
            can_duplicate=can_duplicate,
            original_course_id=original_course_id,
            original_assignment_id=original_assignment_id,
            original_lti_resource_link_id=original_lti_resource_link_id,
            original_assignment_name=original_assignment_name,
            original_quiz_id=original_quiz_id,
            workflow_state=workflow_state,
        )

        get_assignments_response_200.additional_properties = d
        return get_assignments_response_200

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
