from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.context_external_tool_account_navigation import ContextExternalToolAccountNavigation
    from ..models.context_external_tool_activity_asset_processor import ContextExternalToolActivityAssetProcessor
    from ..models.context_external_tool_activity_asset_processor_contribution import (
        ContextExternalToolActivityAssetProcessorContribution,
    )
    from ..models.context_external_tool_analytics_hub import ContextExternalToolAnalyticsHub
    from ..models.context_external_tool_assignment_edit import ContextExternalToolAssignmentEdit
    from ..models.context_external_tool_assignment_group_menu import ContextExternalToolAssignmentGroupMenu
    from ..models.context_external_tool_assignment_index_menu import ContextExternalToolAssignmentIndexMenu
    from ..models.context_external_tool_assignment_menu import ContextExternalToolAssignmentMenu
    from ..models.context_external_tool_assignment_selection import ContextExternalToolAssignmentSelection
    from ..models.context_external_tool_assignment_view import ContextExternalToolAssignmentView
    from ..models.context_external_tool_collaboration import ContextExternalToolCollaboration
    from ..models.context_external_tool_conference_selection import ContextExternalToolConferenceSelection
    from ..models.context_external_tool_course_assignments_menu import ContextExternalToolCourseAssignmentsMenu
    from ..models.context_external_tool_course_home_sub_navigation import ContextExternalToolCourseHomeSubNavigation
    from ..models.context_external_tool_course_navigation import ContextExternalToolCourseNavigation
    from ..models.context_external_tool_course_settings_sub_navigation import (
        ContextExternalToolCourseSettingsSubNavigation,
    )
    from ..models.context_external_tool_custom_fields import ContextExternalToolCustomFields
    from ..models.context_external_tool_discussion_topic_index_menu import ContextExternalToolDiscussionTopicIndexMenu
    from ..models.context_external_tool_discussion_topic_menu import ContextExternalToolDiscussionTopicMenu
    from ..models.context_external_tool_editor_button import ContextExternalToolEditorButton
    from ..models.context_external_tool_file_index_menu import ContextExternalToolFileIndexMenu
    from ..models.context_external_tool_file_menu import ContextExternalToolFileMenu
    from ..models.context_external_tool_global_navigation import ContextExternalToolGlobalNavigation
    from ..models.context_external_tool_homework_submission import ContextExternalToolHomeworkSubmission
    from ..models.context_external_tool_link_selection import ContextExternalToolLinkSelection
    from ..models.context_external_tool_migration_selection import ContextExternalToolMigrationSelection
    from ..models.context_external_tool_module_group_menu import ContextExternalToolModuleGroupMenu
    from ..models.context_external_tool_module_index_menu import ContextExternalToolModuleIndexMenu
    from ..models.context_external_tool_module_index_menu_modal import ContextExternalToolModuleIndexMenuModal
    from ..models.context_external_tool_module_menu import ContextExternalToolModuleMenu
    from ..models.context_external_tool_module_menu_modal import ContextExternalToolModuleMenuModal
    from ..models.context_external_tool_page_index_menu import ContextExternalToolPageIndexMenu
    from ..models.context_external_tool_page_menu import ContextExternalToolPageMenu
    from ..models.context_external_tool_post_grades import ContextExternalToolPostGrades
    from ..models.context_external_tool_quiz_index_menu import ContextExternalToolQuizIndexMenu
    from ..models.context_external_tool_quiz_menu import ContextExternalToolQuizMenu
    from ..models.context_external_tool_resource_selection import ContextExternalToolResourceSelection
    from ..models.context_external_tool_similarity_detection import ContextExternalToolSimilarityDetection
    from ..models.context_external_tool_student_context_card import ContextExternalToolStudentContextCard
    from ..models.context_external_tool_submission_type_selection import ContextExternalToolSubmissionTypeSelection
    from ..models.context_external_tool_tool_configuration import ContextExternalToolToolConfiguration
    from ..models.context_external_tool_top_navigation import ContextExternalToolTopNavigation
    from ..models.context_external_tool_user_navigation import ContextExternalToolUserNavigation
    from ..models.context_external_tool_wiki_index_menu import ContextExternalToolWikiIndexMenu
    from ..models.context_external_tool_wiki_page_menu import ContextExternalToolWikiPageMenu


T = TypeVar("T", bound="ContextExternalTool")


@_attrs_define
class ContextExternalTool:
    """
    Attributes:
        id (int):
        name (str):
        description (str):
        url (str):
        domain (str):
        consumer_key (str):
        created_at (str):
        updated_at (str):
        privacy_level (str):
        custom_fields (ContextExternalToolCustomFields):
        workflow_state (str):
        is_rce_favorite (bool):
        is_top_nav_favorite (bool):
        selection_width (int):
        selection_height (int):
        icon_url (str):
        not_selectable (bool):
        version (str):
        unified_tool_id (None):
        developer_key_id (int):
        lti_registration_id (int):
        deployment_id (str):
        allow_membership_service_access (bool):
        prefer_sis_email (bool):
        estimated_duration (None):
        account_navigation (ContextExternalToolAccountNavigation):
        analytics_hub (ContextExternalToolAnalyticsHub):
        assignment_edit (ContextExternalToolAssignmentEdit):
        assignment_group_menu (ContextExternalToolAssignmentGroupMenu):
        assignment_index_menu (ContextExternalToolAssignmentIndexMenu):
        assignment_menu (ContextExternalToolAssignmentMenu):
        assignment_selection (ContextExternalToolAssignmentSelection):
        assignment_view (ContextExternalToolAssignmentView):
        collaboration (ContextExternalToolCollaboration):
        conference_selection (ContextExternalToolConferenceSelection):
        course_assignments_menu (ContextExternalToolCourseAssignmentsMenu):
        course_home_sub_navigation (ContextExternalToolCourseHomeSubNavigation):
        course_navigation (ContextExternalToolCourseNavigation):
        course_settings_sub_navigation (ContextExternalToolCourseSettingsSubNavigation):
        discussion_topic_index_menu (ContextExternalToolDiscussionTopicIndexMenu):
        discussion_topic_menu (ContextExternalToolDiscussionTopicMenu):
        editor_button (ContextExternalToolEditorButton):
        file_index_menu (ContextExternalToolFileIndexMenu):
        file_menu (ContextExternalToolFileMenu):
        global_navigation (ContextExternalToolGlobalNavigation):
        homework_submission (ContextExternalToolHomeworkSubmission):
        link_selection (ContextExternalToolLinkSelection):
        migration_selection (ContextExternalToolMigrationSelection):
        module_group_menu (ContextExternalToolModuleGroupMenu):
        module_index_menu (ContextExternalToolModuleIndexMenu):
        module_index_menu_modal (ContextExternalToolModuleIndexMenuModal):
        module_menu_modal (ContextExternalToolModuleMenuModal):
        module_menu (ContextExternalToolModuleMenu):
        page_index_menu (ContextExternalToolPageIndexMenu):
        page_menu (ContextExternalToolPageMenu):
        post_grades (ContextExternalToolPostGrades):
        quiz_index_menu (ContextExternalToolQuizIndexMenu):
        quiz_menu (ContextExternalToolQuizMenu):
        resource_selection (ContextExternalToolResourceSelection):
        similarity_detection (ContextExternalToolSimilarityDetection):
        student_context_card (ContextExternalToolStudentContextCard):
        submission_type_selection (ContextExternalToolSubmissionTypeSelection):
        tool_configuration (ContextExternalToolToolConfiguration):
        top_navigation (ContextExternalToolTopNavigation):
        user_navigation (ContextExternalToolUserNavigation):
        wiki_index_menu (ContextExternalToolWikiIndexMenu):
        wiki_page_menu (ContextExternalToolWikiPageMenu):
        activity_asset_processor (ContextExternalToolActivityAssetProcessor):
        activity_asset_processor_contribution (ContextExternalToolActivityAssetProcessorContribution):
    """

    id: int
    name: str
    description: str
    url: str
    domain: str
    consumer_key: str
    created_at: str
    updated_at: str
    privacy_level: str
    custom_fields: "ContextExternalToolCustomFields"
    workflow_state: str
    is_rce_favorite: bool
    is_top_nav_favorite: bool
    selection_width: int
    selection_height: int
    icon_url: str
    not_selectable: bool
    version: str
    unified_tool_id: None
    developer_key_id: int
    lti_registration_id: int
    deployment_id: str
    allow_membership_service_access: bool
    prefer_sis_email: bool
    estimated_duration: None
    account_navigation: "ContextExternalToolAccountNavigation"
    analytics_hub: "ContextExternalToolAnalyticsHub"
    assignment_edit: "ContextExternalToolAssignmentEdit"
    assignment_group_menu: "ContextExternalToolAssignmentGroupMenu"
    assignment_index_menu: "ContextExternalToolAssignmentIndexMenu"
    assignment_menu: "ContextExternalToolAssignmentMenu"
    assignment_selection: "ContextExternalToolAssignmentSelection"
    assignment_view: "ContextExternalToolAssignmentView"
    collaboration: "ContextExternalToolCollaboration"
    conference_selection: "ContextExternalToolConferenceSelection"
    course_assignments_menu: "ContextExternalToolCourseAssignmentsMenu"
    course_home_sub_navigation: "ContextExternalToolCourseHomeSubNavigation"
    course_navigation: "ContextExternalToolCourseNavigation"
    course_settings_sub_navigation: "ContextExternalToolCourseSettingsSubNavigation"
    discussion_topic_index_menu: "ContextExternalToolDiscussionTopicIndexMenu"
    discussion_topic_menu: "ContextExternalToolDiscussionTopicMenu"
    editor_button: "ContextExternalToolEditorButton"
    file_index_menu: "ContextExternalToolFileIndexMenu"
    file_menu: "ContextExternalToolFileMenu"
    global_navigation: "ContextExternalToolGlobalNavigation"
    homework_submission: "ContextExternalToolHomeworkSubmission"
    link_selection: "ContextExternalToolLinkSelection"
    migration_selection: "ContextExternalToolMigrationSelection"
    module_group_menu: "ContextExternalToolModuleGroupMenu"
    module_index_menu: "ContextExternalToolModuleIndexMenu"
    module_index_menu_modal: "ContextExternalToolModuleIndexMenuModal"
    module_menu_modal: "ContextExternalToolModuleMenuModal"
    module_menu: "ContextExternalToolModuleMenu"
    page_index_menu: "ContextExternalToolPageIndexMenu"
    page_menu: "ContextExternalToolPageMenu"
    post_grades: "ContextExternalToolPostGrades"
    quiz_index_menu: "ContextExternalToolQuizIndexMenu"
    quiz_menu: "ContextExternalToolQuizMenu"
    resource_selection: "ContextExternalToolResourceSelection"
    similarity_detection: "ContextExternalToolSimilarityDetection"
    student_context_card: "ContextExternalToolStudentContextCard"
    submission_type_selection: "ContextExternalToolSubmissionTypeSelection"
    tool_configuration: "ContextExternalToolToolConfiguration"
    top_navigation: "ContextExternalToolTopNavigation"
    user_navigation: "ContextExternalToolUserNavigation"
    wiki_index_menu: "ContextExternalToolWikiIndexMenu"
    wiki_page_menu: "ContextExternalToolWikiPageMenu"
    activity_asset_processor: "ContextExternalToolActivityAssetProcessor"
    activity_asset_processor_contribution: "ContextExternalToolActivityAssetProcessorContribution"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        url = self.url

        domain = self.domain

        consumer_key = self.consumer_key

        created_at = self.created_at

        updated_at = self.updated_at

        privacy_level = self.privacy_level

        custom_fields = self.custom_fields.to_dict()

        workflow_state = self.workflow_state

        is_rce_favorite = self.is_rce_favorite

        is_top_nav_favorite = self.is_top_nav_favorite

        selection_width = self.selection_width

        selection_height = self.selection_height

        icon_url = self.icon_url

        not_selectable = self.not_selectable

        version = self.version

        unified_tool_id = self.unified_tool_id

        developer_key_id = self.developer_key_id

        lti_registration_id = self.lti_registration_id

        deployment_id = self.deployment_id

        allow_membership_service_access = self.allow_membership_service_access

        prefer_sis_email = self.prefer_sis_email

        estimated_duration = self.estimated_duration

        account_navigation = self.account_navigation.to_dict()

        analytics_hub = self.analytics_hub.to_dict()

        assignment_edit = self.assignment_edit.to_dict()

        assignment_group_menu = self.assignment_group_menu.to_dict()

        assignment_index_menu = self.assignment_index_menu.to_dict()

        assignment_menu = self.assignment_menu.to_dict()

        assignment_selection = self.assignment_selection.to_dict()

        assignment_view = self.assignment_view.to_dict()

        collaboration = self.collaboration.to_dict()

        conference_selection = self.conference_selection.to_dict()

        course_assignments_menu = self.course_assignments_menu.to_dict()

        course_home_sub_navigation = self.course_home_sub_navigation.to_dict()

        course_navigation = self.course_navigation.to_dict()

        course_settings_sub_navigation = self.course_settings_sub_navigation.to_dict()

        discussion_topic_index_menu = self.discussion_topic_index_menu.to_dict()

        discussion_topic_menu = self.discussion_topic_menu.to_dict()

        editor_button = self.editor_button.to_dict()

        file_index_menu = self.file_index_menu.to_dict()

        file_menu = self.file_menu.to_dict()

        global_navigation = self.global_navigation.to_dict()

        homework_submission = self.homework_submission.to_dict()

        link_selection = self.link_selection.to_dict()

        migration_selection = self.migration_selection.to_dict()

        module_group_menu = self.module_group_menu.to_dict()

        module_index_menu = self.module_index_menu.to_dict()

        module_index_menu_modal = self.module_index_menu_modal.to_dict()

        module_menu_modal = self.module_menu_modal.to_dict()

        module_menu = self.module_menu.to_dict()

        page_index_menu = self.page_index_menu.to_dict()

        page_menu = self.page_menu.to_dict()

        post_grades = self.post_grades.to_dict()

        quiz_index_menu = self.quiz_index_menu.to_dict()

        quiz_menu = self.quiz_menu.to_dict()

        resource_selection = self.resource_selection.to_dict()

        similarity_detection = self.similarity_detection.to_dict()

        student_context_card = self.student_context_card.to_dict()

        submission_type_selection = self.submission_type_selection.to_dict()

        tool_configuration = self.tool_configuration.to_dict()

        top_navigation = self.top_navigation.to_dict()

        user_navigation = self.user_navigation.to_dict()

        wiki_index_menu = self.wiki_index_menu.to_dict()

        wiki_page_menu = self.wiki_page_menu.to_dict()

        activity_asset_processor = self.activity_asset_processor.to_dict()

        activity_asset_processor_contribution = self.activity_asset_processor_contribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "description": description,
                "url": url,
                "domain": domain,
                "consumer_key": consumer_key,
                "created_at": created_at,
                "updated_at": updated_at,
                "privacy_level": privacy_level,
                "custom_fields": custom_fields,
                "workflow_state": workflow_state,
                "is_rce_favorite": is_rce_favorite,
                "is_top_nav_favorite": is_top_nav_favorite,
                "selection_width": selection_width,
                "selection_height": selection_height,
                "icon_url": icon_url,
                "not_selectable": not_selectable,
                "version": version,
                "unified_tool_id": unified_tool_id,
                "developer_key_id": developer_key_id,
                "lti_registration_id": lti_registration_id,
                "deployment_id": deployment_id,
                "allow_membership_service_access": allow_membership_service_access,
                "prefer_sis_email": prefer_sis_email,
                "estimated_duration": estimated_duration,
                "account_navigation": account_navigation,
                "analytics_hub": analytics_hub,
                "assignment_edit": assignment_edit,
                "assignment_group_menu": assignment_group_menu,
                "assignment_index_menu": assignment_index_menu,
                "assignment_menu": assignment_menu,
                "assignment_selection": assignment_selection,
                "assignment_view": assignment_view,
                "collaboration": collaboration,
                "conference_selection": conference_selection,
                "course_assignments_menu": course_assignments_menu,
                "course_home_sub_navigation": course_home_sub_navigation,
                "course_navigation": course_navigation,
                "course_settings_sub_navigation": course_settings_sub_navigation,
                "discussion_topic_index_menu": discussion_topic_index_menu,
                "discussion_topic_menu": discussion_topic_menu,
                "editor_button": editor_button,
                "file_index_menu": file_index_menu,
                "file_menu": file_menu,
                "global_navigation": global_navigation,
                "homework_submission": homework_submission,
                "link_selection": link_selection,
                "migration_selection": migration_selection,
                "module_group_menu": module_group_menu,
                "module_index_menu": module_index_menu,
                "module_index_menu_modal": module_index_menu_modal,
                "module_menu_modal": module_menu_modal,
                "module_menu": module_menu,
                "page_index_menu": page_index_menu,
                "page_menu": page_menu,
                "post_grades": post_grades,
                "quiz_index_menu": quiz_index_menu,
                "quiz_menu": quiz_menu,
                "resource_selection": resource_selection,
                "similarity_detection": similarity_detection,
                "student_context_card": student_context_card,
                "submission_type_selection": submission_type_selection,
                "tool_configuration": tool_configuration,
                "top_navigation": top_navigation,
                "user_navigation": user_navigation,
                "wiki_index_menu": wiki_index_menu,
                "wiki_page_menu": wiki_page_menu,
                "ActivityAssetProcessor": activity_asset_processor,
                "ActivityAssetProcessorContribution": activity_asset_processor_contribution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_external_tool_account_navigation import ContextExternalToolAccountNavigation
        from ..models.context_external_tool_activity_asset_processor import ContextExternalToolActivityAssetProcessor
        from ..models.context_external_tool_activity_asset_processor_contribution import (
            ContextExternalToolActivityAssetProcessorContribution,
        )
        from ..models.context_external_tool_analytics_hub import ContextExternalToolAnalyticsHub
        from ..models.context_external_tool_assignment_edit import ContextExternalToolAssignmentEdit
        from ..models.context_external_tool_assignment_group_menu import ContextExternalToolAssignmentGroupMenu
        from ..models.context_external_tool_assignment_index_menu import ContextExternalToolAssignmentIndexMenu
        from ..models.context_external_tool_assignment_menu import ContextExternalToolAssignmentMenu
        from ..models.context_external_tool_assignment_selection import ContextExternalToolAssignmentSelection
        from ..models.context_external_tool_assignment_view import ContextExternalToolAssignmentView
        from ..models.context_external_tool_collaboration import ContextExternalToolCollaboration
        from ..models.context_external_tool_conference_selection import ContextExternalToolConferenceSelection
        from ..models.context_external_tool_course_assignments_menu import ContextExternalToolCourseAssignmentsMenu
        from ..models.context_external_tool_course_home_sub_navigation import ContextExternalToolCourseHomeSubNavigation
        from ..models.context_external_tool_course_navigation import ContextExternalToolCourseNavigation
        from ..models.context_external_tool_course_settings_sub_navigation import (
            ContextExternalToolCourseSettingsSubNavigation,
        )
        from ..models.context_external_tool_custom_fields import ContextExternalToolCustomFields
        from ..models.context_external_tool_discussion_topic_index_menu import (
            ContextExternalToolDiscussionTopicIndexMenu,
        )
        from ..models.context_external_tool_discussion_topic_menu import ContextExternalToolDiscussionTopicMenu
        from ..models.context_external_tool_editor_button import ContextExternalToolEditorButton
        from ..models.context_external_tool_file_index_menu import ContextExternalToolFileIndexMenu
        from ..models.context_external_tool_file_menu import ContextExternalToolFileMenu
        from ..models.context_external_tool_global_navigation import ContextExternalToolGlobalNavigation
        from ..models.context_external_tool_homework_submission import ContextExternalToolHomeworkSubmission
        from ..models.context_external_tool_link_selection import ContextExternalToolLinkSelection
        from ..models.context_external_tool_migration_selection import ContextExternalToolMigrationSelection
        from ..models.context_external_tool_module_group_menu import ContextExternalToolModuleGroupMenu
        from ..models.context_external_tool_module_index_menu import ContextExternalToolModuleIndexMenu
        from ..models.context_external_tool_module_index_menu_modal import ContextExternalToolModuleIndexMenuModal
        from ..models.context_external_tool_module_menu import ContextExternalToolModuleMenu
        from ..models.context_external_tool_module_menu_modal import ContextExternalToolModuleMenuModal
        from ..models.context_external_tool_page_index_menu import ContextExternalToolPageIndexMenu
        from ..models.context_external_tool_page_menu import ContextExternalToolPageMenu
        from ..models.context_external_tool_post_grades import ContextExternalToolPostGrades
        from ..models.context_external_tool_quiz_index_menu import ContextExternalToolQuizIndexMenu
        from ..models.context_external_tool_quiz_menu import ContextExternalToolQuizMenu
        from ..models.context_external_tool_resource_selection import ContextExternalToolResourceSelection
        from ..models.context_external_tool_similarity_detection import ContextExternalToolSimilarityDetection
        from ..models.context_external_tool_student_context_card import ContextExternalToolStudentContextCard
        from ..models.context_external_tool_submission_type_selection import ContextExternalToolSubmissionTypeSelection
        from ..models.context_external_tool_tool_configuration import ContextExternalToolToolConfiguration
        from ..models.context_external_tool_top_navigation import ContextExternalToolTopNavigation
        from ..models.context_external_tool_user_navigation import ContextExternalToolUserNavigation
        from ..models.context_external_tool_wiki_index_menu import ContextExternalToolWikiIndexMenu
        from ..models.context_external_tool_wiki_page_menu import ContextExternalToolWikiPageMenu

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        description = d.pop("description")

        url = d.pop("url")

        domain = d.pop("domain")

        consumer_key = d.pop("consumer_key")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        privacy_level = d.pop("privacy_level")

        custom_fields = ContextExternalToolCustomFields.from_dict(d.pop("custom_fields"))

        workflow_state = d.pop("workflow_state")

        is_rce_favorite = d.pop("is_rce_favorite")

        is_top_nav_favorite = d.pop("is_top_nav_favorite")

        selection_width = d.pop("selection_width")

        selection_height = d.pop("selection_height")

        icon_url = d.pop("icon_url")

        not_selectable = d.pop("not_selectable")

        version = d.pop("version")

        unified_tool_id = d.pop("unified_tool_id")

        developer_key_id = d.pop("developer_key_id")

        lti_registration_id = d.pop("lti_registration_id")

        deployment_id = d.pop("deployment_id")

        allow_membership_service_access = d.pop("allow_membership_service_access")

        prefer_sis_email = d.pop("prefer_sis_email")

        estimated_duration = d.pop("estimated_duration")

        account_navigation = ContextExternalToolAccountNavigation.from_dict(d.pop("account_navigation"))

        analytics_hub = ContextExternalToolAnalyticsHub.from_dict(d.pop("analytics_hub"))

        assignment_edit = ContextExternalToolAssignmentEdit.from_dict(d.pop("assignment_edit"))

        assignment_group_menu = ContextExternalToolAssignmentGroupMenu.from_dict(d.pop("assignment_group_menu"))

        assignment_index_menu = ContextExternalToolAssignmentIndexMenu.from_dict(d.pop("assignment_index_menu"))

        assignment_menu = ContextExternalToolAssignmentMenu.from_dict(d.pop("assignment_menu"))

        assignment_selection = ContextExternalToolAssignmentSelection.from_dict(d.pop("assignment_selection"))

        assignment_view = ContextExternalToolAssignmentView.from_dict(d.pop("assignment_view"))

        collaboration = ContextExternalToolCollaboration.from_dict(d.pop("collaboration"))

        conference_selection = ContextExternalToolConferenceSelection.from_dict(d.pop("conference_selection"))

        course_assignments_menu = ContextExternalToolCourseAssignmentsMenu.from_dict(d.pop("course_assignments_menu"))

        course_home_sub_navigation = ContextExternalToolCourseHomeSubNavigation.from_dict(
            d.pop("course_home_sub_navigation")
        )

        course_navigation = ContextExternalToolCourseNavigation.from_dict(d.pop("course_navigation"))

        course_settings_sub_navigation = ContextExternalToolCourseSettingsSubNavigation.from_dict(
            d.pop("course_settings_sub_navigation")
        )

        discussion_topic_index_menu = ContextExternalToolDiscussionTopicIndexMenu.from_dict(
            d.pop("discussion_topic_index_menu")
        )

        discussion_topic_menu = ContextExternalToolDiscussionTopicMenu.from_dict(d.pop("discussion_topic_menu"))

        editor_button = ContextExternalToolEditorButton.from_dict(d.pop("editor_button"))

        file_index_menu = ContextExternalToolFileIndexMenu.from_dict(d.pop("file_index_menu"))

        file_menu = ContextExternalToolFileMenu.from_dict(d.pop("file_menu"))

        global_navigation = ContextExternalToolGlobalNavigation.from_dict(d.pop("global_navigation"))

        homework_submission = ContextExternalToolHomeworkSubmission.from_dict(d.pop("homework_submission"))

        link_selection = ContextExternalToolLinkSelection.from_dict(d.pop("link_selection"))

        migration_selection = ContextExternalToolMigrationSelection.from_dict(d.pop("migration_selection"))

        module_group_menu = ContextExternalToolModuleGroupMenu.from_dict(d.pop("module_group_menu"))

        module_index_menu = ContextExternalToolModuleIndexMenu.from_dict(d.pop("module_index_menu"))

        module_index_menu_modal = ContextExternalToolModuleIndexMenuModal.from_dict(d.pop("module_index_menu_modal"))

        module_menu_modal = ContextExternalToolModuleMenuModal.from_dict(d.pop("module_menu_modal"))

        module_menu = ContextExternalToolModuleMenu.from_dict(d.pop("module_menu"))

        page_index_menu = ContextExternalToolPageIndexMenu.from_dict(d.pop("page_index_menu"))

        page_menu = ContextExternalToolPageMenu.from_dict(d.pop("page_menu"))

        post_grades = ContextExternalToolPostGrades.from_dict(d.pop("post_grades"))

        quiz_index_menu = ContextExternalToolQuizIndexMenu.from_dict(d.pop("quiz_index_menu"))

        quiz_menu = ContextExternalToolQuizMenu.from_dict(d.pop("quiz_menu"))

        resource_selection = ContextExternalToolResourceSelection.from_dict(d.pop("resource_selection"))

        similarity_detection = ContextExternalToolSimilarityDetection.from_dict(d.pop("similarity_detection"))

        student_context_card = ContextExternalToolStudentContextCard.from_dict(d.pop("student_context_card"))

        submission_type_selection = ContextExternalToolSubmissionTypeSelection.from_dict(
            d.pop("submission_type_selection")
        )

        tool_configuration = ContextExternalToolToolConfiguration.from_dict(d.pop("tool_configuration"))

        top_navigation = ContextExternalToolTopNavigation.from_dict(d.pop("top_navigation"))

        user_navigation = ContextExternalToolUserNavigation.from_dict(d.pop("user_navigation"))

        wiki_index_menu = ContextExternalToolWikiIndexMenu.from_dict(d.pop("wiki_index_menu"))

        wiki_page_menu = ContextExternalToolWikiPageMenu.from_dict(d.pop("wiki_page_menu"))

        activity_asset_processor = ContextExternalToolActivityAssetProcessor.from_dict(d.pop("ActivityAssetProcessor"))

        activity_asset_processor_contribution = ContextExternalToolActivityAssetProcessorContribution.from_dict(
            d.pop("ActivityAssetProcessorContribution")
        )

        context_external_tool = cls(
            id=id,
            name=name,
            description=description,
            url=url,
            domain=domain,
            consumer_key=consumer_key,
            created_at=created_at,
            updated_at=updated_at,
            privacy_level=privacy_level,
            custom_fields=custom_fields,
            workflow_state=workflow_state,
            is_rce_favorite=is_rce_favorite,
            is_top_nav_favorite=is_top_nav_favorite,
            selection_width=selection_width,
            selection_height=selection_height,
            icon_url=icon_url,
            not_selectable=not_selectable,
            version=version,
            unified_tool_id=unified_tool_id,
            developer_key_id=developer_key_id,
            lti_registration_id=lti_registration_id,
            deployment_id=deployment_id,
            allow_membership_service_access=allow_membership_service_access,
            prefer_sis_email=prefer_sis_email,
            estimated_duration=estimated_duration,
            account_navigation=account_navigation,
            analytics_hub=analytics_hub,
            assignment_edit=assignment_edit,
            assignment_group_menu=assignment_group_menu,
            assignment_index_menu=assignment_index_menu,
            assignment_menu=assignment_menu,
            assignment_selection=assignment_selection,
            assignment_view=assignment_view,
            collaboration=collaboration,
            conference_selection=conference_selection,
            course_assignments_menu=course_assignments_menu,
            course_home_sub_navigation=course_home_sub_navigation,
            course_navigation=course_navigation,
            course_settings_sub_navigation=course_settings_sub_navigation,
            discussion_topic_index_menu=discussion_topic_index_menu,
            discussion_topic_menu=discussion_topic_menu,
            editor_button=editor_button,
            file_index_menu=file_index_menu,
            file_menu=file_menu,
            global_navigation=global_navigation,
            homework_submission=homework_submission,
            link_selection=link_selection,
            migration_selection=migration_selection,
            module_group_menu=module_group_menu,
            module_index_menu=module_index_menu,
            module_index_menu_modal=module_index_menu_modal,
            module_menu_modal=module_menu_modal,
            module_menu=module_menu,
            page_index_menu=page_index_menu,
            page_menu=page_menu,
            post_grades=post_grades,
            quiz_index_menu=quiz_index_menu,
            quiz_menu=quiz_menu,
            resource_selection=resource_selection,
            similarity_detection=similarity_detection,
            student_context_card=student_context_card,
            submission_type_selection=submission_type_selection,
            tool_configuration=tool_configuration,
            top_navigation=top_navigation,
            user_navigation=user_navigation,
            wiki_index_menu=wiki_index_menu,
            wiki_page_menu=wiki_page_menu,
            activity_asset_processor=activity_asset_processor,
            activity_asset_processor_contribution=activity_asset_processor_contribution,
        )

        context_external_tool.additional_properties = d
        return context_external_tool

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
