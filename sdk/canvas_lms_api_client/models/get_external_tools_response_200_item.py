from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_external_tools_response_200_item_account_navigation import (
        GetExternalToolsResponse200ItemAccountNavigation,
    )
    from ..models.get_external_tools_response_200_item_activity_asset_processor import (
        GetExternalToolsResponse200ItemActivityAssetProcessor,
    )
    from ..models.get_external_tools_response_200_item_activity_asset_processor_contribution import (
        GetExternalToolsResponse200ItemActivityAssetProcessorContribution,
    )
    from ..models.get_external_tools_response_200_item_analytics_hub import GetExternalToolsResponse200ItemAnalyticsHub
    from ..models.get_external_tools_response_200_item_assignment_edit import (
        GetExternalToolsResponse200ItemAssignmentEdit,
    )
    from ..models.get_external_tools_response_200_item_assignment_group_menu import (
        GetExternalToolsResponse200ItemAssignmentGroupMenu,
    )
    from ..models.get_external_tools_response_200_item_assignment_index_menu import (
        GetExternalToolsResponse200ItemAssignmentIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_assignment_menu import (
        GetExternalToolsResponse200ItemAssignmentMenu,
    )
    from ..models.get_external_tools_response_200_item_assignment_selection import (
        GetExternalToolsResponse200ItemAssignmentSelection,
    )
    from ..models.get_external_tools_response_200_item_assignment_view import (
        GetExternalToolsResponse200ItemAssignmentView,
    )
    from ..models.get_external_tools_response_200_item_collaboration import GetExternalToolsResponse200ItemCollaboration
    from ..models.get_external_tools_response_200_item_conference_selection import (
        GetExternalToolsResponse200ItemConferenceSelection,
    )
    from ..models.get_external_tools_response_200_item_course_assignments_menu import (
        GetExternalToolsResponse200ItemCourseAssignmentsMenu,
    )
    from ..models.get_external_tools_response_200_item_course_home_sub_navigation import (
        GetExternalToolsResponse200ItemCourseHomeSubNavigation,
    )
    from ..models.get_external_tools_response_200_item_course_navigation import (
        GetExternalToolsResponse200ItemCourseNavigation,
    )
    from ..models.get_external_tools_response_200_item_course_settings_sub_navigation import (
        GetExternalToolsResponse200ItemCourseSettingsSubNavigation,
    )
    from ..models.get_external_tools_response_200_item_custom_fields import GetExternalToolsResponse200ItemCustomFields
    from ..models.get_external_tools_response_200_item_discussion_topic_index_menu import (
        GetExternalToolsResponse200ItemDiscussionTopicIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_discussion_topic_menu import (
        GetExternalToolsResponse200ItemDiscussionTopicMenu,
    )
    from ..models.get_external_tools_response_200_item_editor_button import GetExternalToolsResponse200ItemEditorButton
    from ..models.get_external_tools_response_200_item_file_index_menu import (
        GetExternalToolsResponse200ItemFileIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_file_menu import GetExternalToolsResponse200ItemFileMenu
    from ..models.get_external_tools_response_200_item_global_navigation import (
        GetExternalToolsResponse200ItemGlobalNavigation,
    )
    from ..models.get_external_tools_response_200_item_homework_submission import (
        GetExternalToolsResponse200ItemHomeworkSubmission,
    )
    from ..models.get_external_tools_response_200_item_link_selection import (
        GetExternalToolsResponse200ItemLinkSelection,
    )
    from ..models.get_external_tools_response_200_item_migration_selection import (
        GetExternalToolsResponse200ItemMigrationSelection,
    )
    from ..models.get_external_tools_response_200_item_module_group_menu import (
        GetExternalToolsResponse200ItemModuleGroupMenu,
    )
    from ..models.get_external_tools_response_200_item_module_index_menu import (
        GetExternalToolsResponse200ItemModuleIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_module_index_menu_modal import (
        GetExternalToolsResponse200ItemModuleIndexMenuModal,
    )
    from ..models.get_external_tools_response_200_item_module_menu import GetExternalToolsResponse200ItemModuleMenu
    from ..models.get_external_tools_response_200_item_module_menu_modal import (
        GetExternalToolsResponse200ItemModuleMenuModal,
    )
    from ..models.get_external_tools_response_200_item_page_index_menu import (
        GetExternalToolsResponse200ItemPageIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_page_menu import GetExternalToolsResponse200ItemPageMenu
    from ..models.get_external_tools_response_200_item_post_grades import GetExternalToolsResponse200ItemPostGrades
    from ..models.get_external_tools_response_200_item_quiz_index_menu import (
        GetExternalToolsResponse200ItemQuizIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_quiz_menu import GetExternalToolsResponse200ItemQuizMenu
    from ..models.get_external_tools_response_200_item_resource_selection import (
        GetExternalToolsResponse200ItemResourceSelection,
    )
    from ..models.get_external_tools_response_200_item_similarity_detection import (
        GetExternalToolsResponse200ItemSimilarityDetection,
    )
    from ..models.get_external_tools_response_200_item_student_context_card import (
        GetExternalToolsResponse200ItemStudentContextCard,
    )
    from ..models.get_external_tools_response_200_item_submission_type_selection import (
        GetExternalToolsResponse200ItemSubmissionTypeSelection,
    )
    from ..models.get_external_tools_response_200_item_tool_configuration import (
        GetExternalToolsResponse200ItemToolConfiguration,
    )
    from ..models.get_external_tools_response_200_item_top_navigation import (
        GetExternalToolsResponse200ItemTopNavigation,
    )
    from ..models.get_external_tools_response_200_item_user_navigation import (
        GetExternalToolsResponse200ItemUserNavigation,
    )
    from ..models.get_external_tools_response_200_item_wiki_index_menu import (
        GetExternalToolsResponse200ItemWikiIndexMenu,
    )
    from ..models.get_external_tools_response_200_item_wiki_page_menu import GetExternalToolsResponse200ItemWikiPageMenu


T = TypeVar("T", bound="GetExternalToolsResponse200Item")


@_attrs_define
class GetExternalToolsResponse200Item:
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
        custom_fields (GetExternalToolsResponse200ItemCustomFields):
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
        account_navigation (GetExternalToolsResponse200ItemAccountNavigation):
        analytics_hub (GetExternalToolsResponse200ItemAnalyticsHub):
        assignment_edit (GetExternalToolsResponse200ItemAssignmentEdit):
        assignment_group_menu (GetExternalToolsResponse200ItemAssignmentGroupMenu):
        assignment_index_menu (GetExternalToolsResponse200ItemAssignmentIndexMenu):
        assignment_menu (GetExternalToolsResponse200ItemAssignmentMenu):
        assignment_selection (GetExternalToolsResponse200ItemAssignmentSelection):
        assignment_view (GetExternalToolsResponse200ItemAssignmentView):
        collaboration (GetExternalToolsResponse200ItemCollaboration):
        conference_selection (GetExternalToolsResponse200ItemConferenceSelection):
        course_assignments_menu (GetExternalToolsResponse200ItemCourseAssignmentsMenu):
        course_home_sub_navigation (GetExternalToolsResponse200ItemCourseHomeSubNavigation):
        course_navigation (GetExternalToolsResponse200ItemCourseNavigation):
        course_settings_sub_navigation (GetExternalToolsResponse200ItemCourseSettingsSubNavigation):
        discussion_topic_index_menu (GetExternalToolsResponse200ItemDiscussionTopicIndexMenu):
        discussion_topic_menu (GetExternalToolsResponse200ItemDiscussionTopicMenu):
        editor_button (GetExternalToolsResponse200ItemEditorButton):
        file_index_menu (GetExternalToolsResponse200ItemFileIndexMenu):
        file_menu (GetExternalToolsResponse200ItemFileMenu):
        global_navigation (GetExternalToolsResponse200ItemGlobalNavigation):
        homework_submission (GetExternalToolsResponse200ItemHomeworkSubmission):
        link_selection (GetExternalToolsResponse200ItemLinkSelection):
        migration_selection (GetExternalToolsResponse200ItemMigrationSelection):
        module_group_menu (GetExternalToolsResponse200ItemModuleGroupMenu):
        module_index_menu (GetExternalToolsResponse200ItemModuleIndexMenu):
        module_index_menu_modal (GetExternalToolsResponse200ItemModuleIndexMenuModal):
        module_menu_modal (GetExternalToolsResponse200ItemModuleMenuModal):
        module_menu (GetExternalToolsResponse200ItemModuleMenu):
        page_index_menu (GetExternalToolsResponse200ItemPageIndexMenu):
        page_menu (GetExternalToolsResponse200ItemPageMenu):
        post_grades (GetExternalToolsResponse200ItemPostGrades):
        quiz_index_menu (GetExternalToolsResponse200ItemQuizIndexMenu):
        quiz_menu (GetExternalToolsResponse200ItemQuizMenu):
        resource_selection (GetExternalToolsResponse200ItemResourceSelection):
        similarity_detection (GetExternalToolsResponse200ItemSimilarityDetection):
        student_context_card (GetExternalToolsResponse200ItemStudentContextCard):
        submission_type_selection (GetExternalToolsResponse200ItemSubmissionTypeSelection):
        tool_configuration (GetExternalToolsResponse200ItemToolConfiguration):
        top_navigation (GetExternalToolsResponse200ItemTopNavigation):
        user_navigation (GetExternalToolsResponse200ItemUserNavigation):
        wiki_index_menu (GetExternalToolsResponse200ItemWikiIndexMenu):
        wiki_page_menu (GetExternalToolsResponse200ItemWikiPageMenu):
        activity_asset_processor (GetExternalToolsResponse200ItemActivityAssetProcessor):
        activity_asset_processor_contribution (GetExternalToolsResponse200ItemActivityAssetProcessorContribution):
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
    custom_fields: "GetExternalToolsResponse200ItemCustomFields"
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
    account_navigation: "GetExternalToolsResponse200ItemAccountNavigation"
    analytics_hub: "GetExternalToolsResponse200ItemAnalyticsHub"
    assignment_edit: "GetExternalToolsResponse200ItemAssignmentEdit"
    assignment_group_menu: "GetExternalToolsResponse200ItemAssignmentGroupMenu"
    assignment_index_menu: "GetExternalToolsResponse200ItemAssignmentIndexMenu"
    assignment_menu: "GetExternalToolsResponse200ItemAssignmentMenu"
    assignment_selection: "GetExternalToolsResponse200ItemAssignmentSelection"
    assignment_view: "GetExternalToolsResponse200ItemAssignmentView"
    collaboration: "GetExternalToolsResponse200ItemCollaboration"
    conference_selection: "GetExternalToolsResponse200ItemConferenceSelection"
    course_assignments_menu: "GetExternalToolsResponse200ItemCourseAssignmentsMenu"
    course_home_sub_navigation: "GetExternalToolsResponse200ItemCourseHomeSubNavigation"
    course_navigation: "GetExternalToolsResponse200ItemCourseNavigation"
    course_settings_sub_navigation: "GetExternalToolsResponse200ItemCourseSettingsSubNavigation"
    discussion_topic_index_menu: "GetExternalToolsResponse200ItemDiscussionTopicIndexMenu"
    discussion_topic_menu: "GetExternalToolsResponse200ItemDiscussionTopicMenu"
    editor_button: "GetExternalToolsResponse200ItemEditorButton"
    file_index_menu: "GetExternalToolsResponse200ItemFileIndexMenu"
    file_menu: "GetExternalToolsResponse200ItemFileMenu"
    global_navigation: "GetExternalToolsResponse200ItemGlobalNavigation"
    homework_submission: "GetExternalToolsResponse200ItemHomeworkSubmission"
    link_selection: "GetExternalToolsResponse200ItemLinkSelection"
    migration_selection: "GetExternalToolsResponse200ItemMigrationSelection"
    module_group_menu: "GetExternalToolsResponse200ItemModuleGroupMenu"
    module_index_menu: "GetExternalToolsResponse200ItemModuleIndexMenu"
    module_index_menu_modal: "GetExternalToolsResponse200ItemModuleIndexMenuModal"
    module_menu_modal: "GetExternalToolsResponse200ItemModuleMenuModal"
    module_menu: "GetExternalToolsResponse200ItemModuleMenu"
    page_index_menu: "GetExternalToolsResponse200ItemPageIndexMenu"
    page_menu: "GetExternalToolsResponse200ItemPageMenu"
    post_grades: "GetExternalToolsResponse200ItemPostGrades"
    quiz_index_menu: "GetExternalToolsResponse200ItemQuizIndexMenu"
    quiz_menu: "GetExternalToolsResponse200ItemQuizMenu"
    resource_selection: "GetExternalToolsResponse200ItemResourceSelection"
    similarity_detection: "GetExternalToolsResponse200ItemSimilarityDetection"
    student_context_card: "GetExternalToolsResponse200ItemStudentContextCard"
    submission_type_selection: "GetExternalToolsResponse200ItemSubmissionTypeSelection"
    tool_configuration: "GetExternalToolsResponse200ItemToolConfiguration"
    top_navigation: "GetExternalToolsResponse200ItemTopNavigation"
    user_navigation: "GetExternalToolsResponse200ItemUserNavigation"
    wiki_index_menu: "GetExternalToolsResponse200ItemWikiIndexMenu"
    wiki_page_menu: "GetExternalToolsResponse200ItemWikiPageMenu"
    activity_asset_processor: "GetExternalToolsResponse200ItemActivityAssetProcessor"
    activity_asset_processor_contribution: "GetExternalToolsResponse200ItemActivityAssetProcessorContribution"
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
        from ..models.get_external_tools_response_200_item_account_navigation import (
            GetExternalToolsResponse200ItemAccountNavigation,
        )
        from ..models.get_external_tools_response_200_item_activity_asset_processor import (
            GetExternalToolsResponse200ItemActivityAssetProcessor,
        )
        from ..models.get_external_tools_response_200_item_activity_asset_processor_contribution import (
            GetExternalToolsResponse200ItemActivityAssetProcessorContribution,
        )
        from ..models.get_external_tools_response_200_item_analytics_hub import (
            GetExternalToolsResponse200ItemAnalyticsHub,
        )
        from ..models.get_external_tools_response_200_item_assignment_edit import (
            GetExternalToolsResponse200ItemAssignmentEdit,
        )
        from ..models.get_external_tools_response_200_item_assignment_group_menu import (
            GetExternalToolsResponse200ItemAssignmentGroupMenu,
        )
        from ..models.get_external_tools_response_200_item_assignment_index_menu import (
            GetExternalToolsResponse200ItemAssignmentIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_assignment_menu import (
            GetExternalToolsResponse200ItemAssignmentMenu,
        )
        from ..models.get_external_tools_response_200_item_assignment_selection import (
            GetExternalToolsResponse200ItemAssignmentSelection,
        )
        from ..models.get_external_tools_response_200_item_assignment_view import (
            GetExternalToolsResponse200ItemAssignmentView,
        )
        from ..models.get_external_tools_response_200_item_collaboration import (
            GetExternalToolsResponse200ItemCollaboration,
        )
        from ..models.get_external_tools_response_200_item_conference_selection import (
            GetExternalToolsResponse200ItemConferenceSelection,
        )
        from ..models.get_external_tools_response_200_item_course_assignments_menu import (
            GetExternalToolsResponse200ItemCourseAssignmentsMenu,
        )
        from ..models.get_external_tools_response_200_item_course_home_sub_navigation import (
            GetExternalToolsResponse200ItemCourseHomeSubNavigation,
        )
        from ..models.get_external_tools_response_200_item_course_navigation import (
            GetExternalToolsResponse200ItemCourseNavigation,
        )
        from ..models.get_external_tools_response_200_item_course_settings_sub_navigation import (
            GetExternalToolsResponse200ItemCourseSettingsSubNavigation,
        )
        from ..models.get_external_tools_response_200_item_custom_fields import (
            GetExternalToolsResponse200ItemCustomFields,
        )
        from ..models.get_external_tools_response_200_item_discussion_topic_index_menu import (
            GetExternalToolsResponse200ItemDiscussionTopicIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_discussion_topic_menu import (
            GetExternalToolsResponse200ItemDiscussionTopicMenu,
        )
        from ..models.get_external_tools_response_200_item_editor_button import (
            GetExternalToolsResponse200ItemEditorButton,
        )
        from ..models.get_external_tools_response_200_item_file_index_menu import (
            GetExternalToolsResponse200ItemFileIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_file_menu import GetExternalToolsResponse200ItemFileMenu
        from ..models.get_external_tools_response_200_item_global_navigation import (
            GetExternalToolsResponse200ItemGlobalNavigation,
        )
        from ..models.get_external_tools_response_200_item_homework_submission import (
            GetExternalToolsResponse200ItemHomeworkSubmission,
        )
        from ..models.get_external_tools_response_200_item_link_selection import (
            GetExternalToolsResponse200ItemLinkSelection,
        )
        from ..models.get_external_tools_response_200_item_migration_selection import (
            GetExternalToolsResponse200ItemMigrationSelection,
        )
        from ..models.get_external_tools_response_200_item_module_group_menu import (
            GetExternalToolsResponse200ItemModuleGroupMenu,
        )
        from ..models.get_external_tools_response_200_item_module_index_menu import (
            GetExternalToolsResponse200ItemModuleIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_module_index_menu_modal import (
            GetExternalToolsResponse200ItemModuleIndexMenuModal,
        )
        from ..models.get_external_tools_response_200_item_module_menu import GetExternalToolsResponse200ItemModuleMenu
        from ..models.get_external_tools_response_200_item_module_menu_modal import (
            GetExternalToolsResponse200ItemModuleMenuModal,
        )
        from ..models.get_external_tools_response_200_item_page_index_menu import (
            GetExternalToolsResponse200ItemPageIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_page_menu import GetExternalToolsResponse200ItemPageMenu
        from ..models.get_external_tools_response_200_item_post_grades import GetExternalToolsResponse200ItemPostGrades
        from ..models.get_external_tools_response_200_item_quiz_index_menu import (
            GetExternalToolsResponse200ItemQuizIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_quiz_menu import GetExternalToolsResponse200ItemQuizMenu
        from ..models.get_external_tools_response_200_item_resource_selection import (
            GetExternalToolsResponse200ItemResourceSelection,
        )
        from ..models.get_external_tools_response_200_item_similarity_detection import (
            GetExternalToolsResponse200ItemSimilarityDetection,
        )
        from ..models.get_external_tools_response_200_item_student_context_card import (
            GetExternalToolsResponse200ItemStudentContextCard,
        )
        from ..models.get_external_tools_response_200_item_submission_type_selection import (
            GetExternalToolsResponse200ItemSubmissionTypeSelection,
        )
        from ..models.get_external_tools_response_200_item_tool_configuration import (
            GetExternalToolsResponse200ItemToolConfiguration,
        )
        from ..models.get_external_tools_response_200_item_top_navigation import (
            GetExternalToolsResponse200ItemTopNavigation,
        )
        from ..models.get_external_tools_response_200_item_user_navigation import (
            GetExternalToolsResponse200ItemUserNavigation,
        )
        from ..models.get_external_tools_response_200_item_wiki_index_menu import (
            GetExternalToolsResponse200ItemWikiIndexMenu,
        )
        from ..models.get_external_tools_response_200_item_wiki_page_menu import (
            GetExternalToolsResponse200ItemWikiPageMenu,
        )

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

        custom_fields = GetExternalToolsResponse200ItemCustomFields.from_dict(d.pop("custom_fields"))

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

        account_navigation = GetExternalToolsResponse200ItemAccountNavigation.from_dict(d.pop("account_navigation"))

        analytics_hub = GetExternalToolsResponse200ItemAnalyticsHub.from_dict(d.pop("analytics_hub"))

        assignment_edit = GetExternalToolsResponse200ItemAssignmentEdit.from_dict(d.pop("assignment_edit"))

        assignment_group_menu = GetExternalToolsResponse200ItemAssignmentGroupMenu.from_dict(
            d.pop("assignment_group_menu")
        )

        assignment_index_menu = GetExternalToolsResponse200ItemAssignmentIndexMenu.from_dict(
            d.pop("assignment_index_menu")
        )

        assignment_menu = GetExternalToolsResponse200ItemAssignmentMenu.from_dict(d.pop("assignment_menu"))

        assignment_selection = GetExternalToolsResponse200ItemAssignmentSelection.from_dict(
            d.pop("assignment_selection")
        )

        assignment_view = GetExternalToolsResponse200ItemAssignmentView.from_dict(d.pop("assignment_view"))

        collaboration = GetExternalToolsResponse200ItemCollaboration.from_dict(d.pop("collaboration"))

        conference_selection = GetExternalToolsResponse200ItemConferenceSelection.from_dict(
            d.pop("conference_selection")
        )

        course_assignments_menu = GetExternalToolsResponse200ItemCourseAssignmentsMenu.from_dict(
            d.pop("course_assignments_menu")
        )

        course_home_sub_navigation = GetExternalToolsResponse200ItemCourseHomeSubNavigation.from_dict(
            d.pop("course_home_sub_navigation")
        )

        course_navigation = GetExternalToolsResponse200ItemCourseNavigation.from_dict(d.pop("course_navigation"))

        course_settings_sub_navigation = GetExternalToolsResponse200ItemCourseSettingsSubNavigation.from_dict(
            d.pop("course_settings_sub_navigation")
        )

        discussion_topic_index_menu = GetExternalToolsResponse200ItemDiscussionTopicIndexMenu.from_dict(
            d.pop("discussion_topic_index_menu")
        )

        discussion_topic_menu = GetExternalToolsResponse200ItemDiscussionTopicMenu.from_dict(
            d.pop("discussion_topic_menu")
        )

        editor_button = GetExternalToolsResponse200ItemEditorButton.from_dict(d.pop("editor_button"))

        file_index_menu = GetExternalToolsResponse200ItemFileIndexMenu.from_dict(d.pop("file_index_menu"))

        file_menu = GetExternalToolsResponse200ItemFileMenu.from_dict(d.pop("file_menu"))

        global_navigation = GetExternalToolsResponse200ItemGlobalNavigation.from_dict(d.pop("global_navigation"))

        homework_submission = GetExternalToolsResponse200ItemHomeworkSubmission.from_dict(d.pop("homework_submission"))

        link_selection = GetExternalToolsResponse200ItemLinkSelection.from_dict(d.pop("link_selection"))

        migration_selection = GetExternalToolsResponse200ItemMigrationSelection.from_dict(d.pop("migration_selection"))

        module_group_menu = GetExternalToolsResponse200ItemModuleGroupMenu.from_dict(d.pop("module_group_menu"))

        module_index_menu = GetExternalToolsResponse200ItemModuleIndexMenu.from_dict(d.pop("module_index_menu"))

        module_index_menu_modal = GetExternalToolsResponse200ItemModuleIndexMenuModal.from_dict(
            d.pop("module_index_menu_modal")
        )

        module_menu_modal = GetExternalToolsResponse200ItemModuleMenuModal.from_dict(d.pop("module_menu_modal"))

        module_menu = GetExternalToolsResponse200ItemModuleMenu.from_dict(d.pop("module_menu"))

        page_index_menu = GetExternalToolsResponse200ItemPageIndexMenu.from_dict(d.pop("page_index_menu"))

        page_menu = GetExternalToolsResponse200ItemPageMenu.from_dict(d.pop("page_menu"))

        post_grades = GetExternalToolsResponse200ItemPostGrades.from_dict(d.pop("post_grades"))

        quiz_index_menu = GetExternalToolsResponse200ItemQuizIndexMenu.from_dict(d.pop("quiz_index_menu"))

        quiz_menu = GetExternalToolsResponse200ItemQuizMenu.from_dict(d.pop("quiz_menu"))

        resource_selection = GetExternalToolsResponse200ItemResourceSelection.from_dict(d.pop("resource_selection"))

        similarity_detection = GetExternalToolsResponse200ItemSimilarityDetection.from_dict(
            d.pop("similarity_detection")
        )

        student_context_card = GetExternalToolsResponse200ItemStudentContextCard.from_dict(
            d.pop("student_context_card")
        )

        submission_type_selection = GetExternalToolsResponse200ItemSubmissionTypeSelection.from_dict(
            d.pop("submission_type_selection")
        )

        tool_configuration = GetExternalToolsResponse200ItemToolConfiguration.from_dict(d.pop("tool_configuration"))

        top_navigation = GetExternalToolsResponse200ItemTopNavigation.from_dict(d.pop("top_navigation"))

        user_navigation = GetExternalToolsResponse200ItemUserNavigation.from_dict(d.pop("user_navigation"))

        wiki_index_menu = GetExternalToolsResponse200ItemWikiIndexMenu.from_dict(d.pop("wiki_index_menu"))

        wiki_page_menu = GetExternalToolsResponse200ItemWikiPageMenu.from_dict(d.pop("wiki_page_menu"))

        activity_asset_processor = GetExternalToolsResponse200ItemActivityAssetProcessor.from_dict(
            d.pop("ActivityAssetProcessor")
        )

        activity_asset_processor_contribution = (
            GetExternalToolsResponse200ItemActivityAssetProcessorContribution.from_dict(
                d.pop("ActivityAssetProcessorContribution")
            )
        )

        get_external_tools_response_200_item = cls(
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

        get_external_tools_response_200_item.additional_properties = d
        return get_external_tools_response_200_item

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
