from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_external_tools_response_200_account_navigation import (
        UpdateExternalToolsResponse200AccountNavigation,
    )
    from ..models.update_external_tools_response_200_activity_asset_processor import (
        UpdateExternalToolsResponse200ActivityAssetProcessor,
    )
    from ..models.update_external_tools_response_200_activity_asset_processor_contribution import (
        UpdateExternalToolsResponse200ActivityAssetProcessorContribution,
    )
    from ..models.update_external_tools_response_200_analytics_hub import UpdateExternalToolsResponse200AnalyticsHub
    from ..models.update_external_tools_response_200_assignment_edit import UpdateExternalToolsResponse200AssignmentEdit
    from ..models.update_external_tools_response_200_assignment_group_menu import (
        UpdateExternalToolsResponse200AssignmentGroupMenu,
    )
    from ..models.update_external_tools_response_200_assignment_index_menu import (
        UpdateExternalToolsResponse200AssignmentIndexMenu,
    )
    from ..models.update_external_tools_response_200_assignment_menu import UpdateExternalToolsResponse200AssignmentMenu
    from ..models.update_external_tools_response_200_assignment_selection import (
        UpdateExternalToolsResponse200AssignmentSelection,
    )
    from ..models.update_external_tools_response_200_assignment_view import UpdateExternalToolsResponse200AssignmentView
    from ..models.update_external_tools_response_200_collaboration import UpdateExternalToolsResponse200Collaboration
    from ..models.update_external_tools_response_200_conference_selection import (
        UpdateExternalToolsResponse200ConferenceSelection,
    )
    from ..models.update_external_tools_response_200_course_assignments_menu import (
        UpdateExternalToolsResponse200CourseAssignmentsMenu,
    )
    from ..models.update_external_tools_response_200_course_home_sub_navigation import (
        UpdateExternalToolsResponse200CourseHomeSubNavigation,
    )
    from ..models.update_external_tools_response_200_course_navigation import (
        UpdateExternalToolsResponse200CourseNavigation,
    )
    from ..models.update_external_tools_response_200_course_settings_sub_navigation import (
        UpdateExternalToolsResponse200CourseSettingsSubNavigation,
    )
    from ..models.update_external_tools_response_200_custom_fields import UpdateExternalToolsResponse200CustomFields
    from ..models.update_external_tools_response_200_discussion_topic_index_menu import (
        UpdateExternalToolsResponse200DiscussionTopicIndexMenu,
    )
    from ..models.update_external_tools_response_200_discussion_topic_menu import (
        UpdateExternalToolsResponse200DiscussionTopicMenu,
    )
    from ..models.update_external_tools_response_200_editor_button import UpdateExternalToolsResponse200EditorButton
    from ..models.update_external_tools_response_200_file_index_menu import UpdateExternalToolsResponse200FileIndexMenu
    from ..models.update_external_tools_response_200_file_menu import UpdateExternalToolsResponse200FileMenu
    from ..models.update_external_tools_response_200_global_navigation import (
        UpdateExternalToolsResponse200GlobalNavigation,
    )
    from ..models.update_external_tools_response_200_homework_submission import (
        UpdateExternalToolsResponse200HomeworkSubmission,
    )
    from ..models.update_external_tools_response_200_link_selection import UpdateExternalToolsResponse200LinkSelection
    from ..models.update_external_tools_response_200_migration_selection import (
        UpdateExternalToolsResponse200MigrationSelection,
    )
    from ..models.update_external_tools_response_200_module_group_menu import (
        UpdateExternalToolsResponse200ModuleGroupMenu,
    )
    from ..models.update_external_tools_response_200_module_index_menu import (
        UpdateExternalToolsResponse200ModuleIndexMenu,
    )
    from ..models.update_external_tools_response_200_module_index_menu_modal import (
        UpdateExternalToolsResponse200ModuleIndexMenuModal,
    )
    from ..models.update_external_tools_response_200_module_menu import UpdateExternalToolsResponse200ModuleMenu
    from ..models.update_external_tools_response_200_module_menu_modal import (
        UpdateExternalToolsResponse200ModuleMenuModal,
    )
    from ..models.update_external_tools_response_200_page_index_menu import UpdateExternalToolsResponse200PageIndexMenu
    from ..models.update_external_tools_response_200_page_menu import UpdateExternalToolsResponse200PageMenu
    from ..models.update_external_tools_response_200_post_grades import UpdateExternalToolsResponse200PostGrades
    from ..models.update_external_tools_response_200_quiz_index_menu import UpdateExternalToolsResponse200QuizIndexMenu
    from ..models.update_external_tools_response_200_quiz_menu import UpdateExternalToolsResponse200QuizMenu
    from ..models.update_external_tools_response_200_resource_selection import (
        UpdateExternalToolsResponse200ResourceSelection,
    )
    from ..models.update_external_tools_response_200_similarity_detection import (
        UpdateExternalToolsResponse200SimilarityDetection,
    )
    from ..models.update_external_tools_response_200_student_context_card import (
        UpdateExternalToolsResponse200StudentContextCard,
    )
    from ..models.update_external_tools_response_200_submission_type_selection import (
        UpdateExternalToolsResponse200SubmissionTypeSelection,
    )
    from ..models.update_external_tools_response_200_tool_configuration import (
        UpdateExternalToolsResponse200ToolConfiguration,
    )
    from ..models.update_external_tools_response_200_top_navigation import UpdateExternalToolsResponse200TopNavigation
    from ..models.update_external_tools_response_200_user_navigation import UpdateExternalToolsResponse200UserNavigation
    from ..models.update_external_tools_response_200_wiki_index_menu import UpdateExternalToolsResponse200WikiIndexMenu
    from ..models.update_external_tools_response_200_wiki_page_menu import UpdateExternalToolsResponse200WikiPageMenu


T = TypeVar("T", bound="UpdateExternalToolsResponse200")


@_attrs_define
class UpdateExternalToolsResponse200:
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
        custom_fields (UpdateExternalToolsResponse200CustomFields):
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
        account_navigation (UpdateExternalToolsResponse200AccountNavigation):
        analytics_hub (UpdateExternalToolsResponse200AnalyticsHub):
        assignment_edit (UpdateExternalToolsResponse200AssignmentEdit):
        assignment_group_menu (UpdateExternalToolsResponse200AssignmentGroupMenu):
        assignment_index_menu (UpdateExternalToolsResponse200AssignmentIndexMenu):
        assignment_menu (UpdateExternalToolsResponse200AssignmentMenu):
        assignment_selection (UpdateExternalToolsResponse200AssignmentSelection):
        assignment_view (UpdateExternalToolsResponse200AssignmentView):
        collaboration (UpdateExternalToolsResponse200Collaboration):
        conference_selection (UpdateExternalToolsResponse200ConferenceSelection):
        course_assignments_menu (UpdateExternalToolsResponse200CourseAssignmentsMenu):
        course_home_sub_navigation (UpdateExternalToolsResponse200CourseHomeSubNavigation):
        course_navigation (UpdateExternalToolsResponse200CourseNavigation):
        course_settings_sub_navigation (UpdateExternalToolsResponse200CourseSettingsSubNavigation):
        discussion_topic_index_menu (UpdateExternalToolsResponse200DiscussionTopicIndexMenu):
        discussion_topic_menu (UpdateExternalToolsResponse200DiscussionTopicMenu):
        editor_button (UpdateExternalToolsResponse200EditorButton):
        file_index_menu (UpdateExternalToolsResponse200FileIndexMenu):
        file_menu (UpdateExternalToolsResponse200FileMenu):
        global_navigation (UpdateExternalToolsResponse200GlobalNavigation):
        homework_submission (UpdateExternalToolsResponse200HomeworkSubmission):
        link_selection (UpdateExternalToolsResponse200LinkSelection):
        migration_selection (UpdateExternalToolsResponse200MigrationSelection):
        module_group_menu (UpdateExternalToolsResponse200ModuleGroupMenu):
        module_index_menu (UpdateExternalToolsResponse200ModuleIndexMenu):
        module_index_menu_modal (UpdateExternalToolsResponse200ModuleIndexMenuModal):
        module_menu_modal (UpdateExternalToolsResponse200ModuleMenuModal):
        module_menu (UpdateExternalToolsResponse200ModuleMenu):
        page_index_menu (UpdateExternalToolsResponse200PageIndexMenu):
        page_menu (UpdateExternalToolsResponse200PageMenu):
        post_grades (UpdateExternalToolsResponse200PostGrades):
        quiz_index_menu (UpdateExternalToolsResponse200QuizIndexMenu):
        quiz_menu (UpdateExternalToolsResponse200QuizMenu):
        resource_selection (UpdateExternalToolsResponse200ResourceSelection):
        similarity_detection (UpdateExternalToolsResponse200SimilarityDetection):
        student_context_card (UpdateExternalToolsResponse200StudentContextCard):
        submission_type_selection (UpdateExternalToolsResponse200SubmissionTypeSelection):
        tool_configuration (UpdateExternalToolsResponse200ToolConfiguration):
        top_navigation (UpdateExternalToolsResponse200TopNavigation):
        user_navigation (UpdateExternalToolsResponse200UserNavigation):
        wiki_index_menu (UpdateExternalToolsResponse200WikiIndexMenu):
        wiki_page_menu (UpdateExternalToolsResponse200WikiPageMenu):
        activity_asset_processor (UpdateExternalToolsResponse200ActivityAssetProcessor):
        activity_asset_processor_contribution (UpdateExternalToolsResponse200ActivityAssetProcessorContribution):
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
    custom_fields: "UpdateExternalToolsResponse200CustomFields"
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
    account_navigation: "UpdateExternalToolsResponse200AccountNavigation"
    analytics_hub: "UpdateExternalToolsResponse200AnalyticsHub"
    assignment_edit: "UpdateExternalToolsResponse200AssignmentEdit"
    assignment_group_menu: "UpdateExternalToolsResponse200AssignmentGroupMenu"
    assignment_index_menu: "UpdateExternalToolsResponse200AssignmentIndexMenu"
    assignment_menu: "UpdateExternalToolsResponse200AssignmentMenu"
    assignment_selection: "UpdateExternalToolsResponse200AssignmentSelection"
    assignment_view: "UpdateExternalToolsResponse200AssignmentView"
    collaboration: "UpdateExternalToolsResponse200Collaboration"
    conference_selection: "UpdateExternalToolsResponse200ConferenceSelection"
    course_assignments_menu: "UpdateExternalToolsResponse200CourseAssignmentsMenu"
    course_home_sub_navigation: "UpdateExternalToolsResponse200CourseHomeSubNavigation"
    course_navigation: "UpdateExternalToolsResponse200CourseNavigation"
    course_settings_sub_navigation: "UpdateExternalToolsResponse200CourseSettingsSubNavigation"
    discussion_topic_index_menu: "UpdateExternalToolsResponse200DiscussionTopicIndexMenu"
    discussion_topic_menu: "UpdateExternalToolsResponse200DiscussionTopicMenu"
    editor_button: "UpdateExternalToolsResponse200EditorButton"
    file_index_menu: "UpdateExternalToolsResponse200FileIndexMenu"
    file_menu: "UpdateExternalToolsResponse200FileMenu"
    global_navigation: "UpdateExternalToolsResponse200GlobalNavigation"
    homework_submission: "UpdateExternalToolsResponse200HomeworkSubmission"
    link_selection: "UpdateExternalToolsResponse200LinkSelection"
    migration_selection: "UpdateExternalToolsResponse200MigrationSelection"
    module_group_menu: "UpdateExternalToolsResponse200ModuleGroupMenu"
    module_index_menu: "UpdateExternalToolsResponse200ModuleIndexMenu"
    module_index_menu_modal: "UpdateExternalToolsResponse200ModuleIndexMenuModal"
    module_menu_modal: "UpdateExternalToolsResponse200ModuleMenuModal"
    module_menu: "UpdateExternalToolsResponse200ModuleMenu"
    page_index_menu: "UpdateExternalToolsResponse200PageIndexMenu"
    page_menu: "UpdateExternalToolsResponse200PageMenu"
    post_grades: "UpdateExternalToolsResponse200PostGrades"
    quiz_index_menu: "UpdateExternalToolsResponse200QuizIndexMenu"
    quiz_menu: "UpdateExternalToolsResponse200QuizMenu"
    resource_selection: "UpdateExternalToolsResponse200ResourceSelection"
    similarity_detection: "UpdateExternalToolsResponse200SimilarityDetection"
    student_context_card: "UpdateExternalToolsResponse200StudentContextCard"
    submission_type_selection: "UpdateExternalToolsResponse200SubmissionTypeSelection"
    tool_configuration: "UpdateExternalToolsResponse200ToolConfiguration"
    top_navigation: "UpdateExternalToolsResponse200TopNavigation"
    user_navigation: "UpdateExternalToolsResponse200UserNavigation"
    wiki_index_menu: "UpdateExternalToolsResponse200WikiIndexMenu"
    wiki_page_menu: "UpdateExternalToolsResponse200WikiPageMenu"
    activity_asset_processor: "UpdateExternalToolsResponse200ActivityAssetProcessor"
    activity_asset_processor_contribution: "UpdateExternalToolsResponse200ActivityAssetProcessorContribution"
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
        from ..models.update_external_tools_response_200_account_navigation import (
            UpdateExternalToolsResponse200AccountNavigation,
        )
        from ..models.update_external_tools_response_200_activity_asset_processor import (
            UpdateExternalToolsResponse200ActivityAssetProcessor,
        )
        from ..models.update_external_tools_response_200_activity_asset_processor_contribution import (
            UpdateExternalToolsResponse200ActivityAssetProcessorContribution,
        )
        from ..models.update_external_tools_response_200_analytics_hub import UpdateExternalToolsResponse200AnalyticsHub
        from ..models.update_external_tools_response_200_assignment_edit import (
            UpdateExternalToolsResponse200AssignmentEdit,
        )
        from ..models.update_external_tools_response_200_assignment_group_menu import (
            UpdateExternalToolsResponse200AssignmentGroupMenu,
        )
        from ..models.update_external_tools_response_200_assignment_index_menu import (
            UpdateExternalToolsResponse200AssignmentIndexMenu,
        )
        from ..models.update_external_tools_response_200_assignment_menu import (
            UpdateExternalToolsResponse200AssignmentMenu,
        )
        from ..models.update_external_tools_response_200_assignment_selection import (
            UpdateExternalToolsResponse200AssignmentSelection,
        )
        from ..models.update_external_tools_response_200_assignment_view import (
            UpdateExternalToolsResponse200AssignmentView,
        )
        from ..models.update_external_tools_response_200_collaboration import (
            UpdateExternalToolsResponse200Collaboration,
        )
        from ..models.update_external_tools_response_200_conference_selection import (
            UpdateExternalToolsResponse200ConferenceSelection,
        )
        from ..models.update_external_tools_response_200_course_assignments_menu import (
            UpdateExternalToolsResponse200CourseAssignmentsMenu,
        )
        from ..models.update_external_tools_response_200_course_home_sub_navigation import (
            UpdateExternalToolsResponse200CourseHomeSubNavigation,
        )
        from ..models.update_external_tools_response_200_course_navigation import (
            UpdateExternalToolsResponse200CourseNavigation,
        )
        from ..models.update_external_tools_response_200_course_settings_sub_navigation import (
            UpdateExternalToolsResponse200CourseSettingsSubNavigation,
        )
        from ..models.update_external_tools_response_200_custom_fields import UpdateExternalToolsResponse200CustomFields
        from ..models.update_external_tools_response_200_discussion_topic_index_menu import (
            UpdateExternalToolsResponse200DiscussionTopicIndexMenu,
        )
        from ..models.update_external_tools_response_200_discussion_topic_menu import (
            UpdateExternalToolsResponse200DiscussionTopicMenu,
        )
        from ..models.update_external_tools_response_200_editor_button import UpdateExternalToolsResponse200EditorButton
        from ..models.update_external_tools_response_200_file_index_menu import (
            UpdateExternalToolsResponse200FileIndexMenu,
        )
        from ..models.update_external_tools_response_200_file_menu import UpdateExternalToolsResponse200FileMenu
        from ..models.update_external_tools_response_200_global_navigation import (
            UpdateExternalToolsResponse200GlobalNavigation,
        )
        from ..models.update_external_tools_response_200_homework_submission import (
            UpdateExternalToolsResponse200HomeworkSubmission,
        )
        from ..models.update_external_tools_response_200_link_selection import (
            UpdateExternalToolsResponse200LinkSelection,
        )
        from ..models.update_external_tools_response_200_migration_selection import (
            UpdateExternalToolsResponse200MigrationSelection,
        )
        from ..models.update_external_tools_response_200_module_group_menu import (
            UpdateExternalToolsResponse200ModuleGroupMenu,
        )
        from ..models.update_external_tools_response_200_module_index_menu import (
            UpdateExternalToolsResponse200ModuleIndexMenu,
        )
        from ..models.update_external_tools_response_200_module_index_menu_modal import (
            UpdateExternalToolsResponse200ModuleIndexMenuModal,
        )
        from ..models.update_external_tools_response_200_module_menu import UpdateExternalToolsResponse200ModuleMenu
        from ..models.update_external_tools_response_200_module_menu_modal import (
            UpdateExternalToolsResponse200ModuleMenuModal,
        )
        from ..models.update_external_tools_response_200_page_index_menu import (
            UpdateExternalToolsResponse200PageIndexMenu,
        )
        from ..models.update_external_tools_response_200_page_menu import UpdateExternalToolsResponse200PageMenu
        from ..models.update_external_tools_response_200_post_grades import UpdateExternalToolsResponse200PostGrades
        from ..models.update_external_tools_response_200_quiz_index_menu import (
            UpdateExternalToolsResponse200QuizIndexMenu,
        )
        from ..models.update_external_tools_response_200_quiz_menu import UpdateExternalToolsResponse200QuizMenu
        from ..models.update_external_tools_response_200_resource_selection import (
            UpdateExternalToolsResponse200ResourceSelection,
        )
        from ..models.update_external_tools_response_200_similarity_detection import (
            UpdateExternalToolsResponse200SimilarityDetection,
        )
        from ..models.update_external_tools_response_200_student_context_card import (
            UpdateExternalToolsResponse200StudentContextCard,
        )
        from ..models.update_external_tools_response_200_submission_type_selection import (
            UpdateExternalToolsResponse200SubmissionTypeSelection,
        )
        from ..models.update_external_tools_response_200_tool_configuration import (
            UpdateExternalToolsResponse200ToolConfiguration,
        )
        from ..models.update_external_tools_response_200_top_navigation import (
            UpdateExternalToolsResponse200TopNavigation,
        )
        from ..models.update_external_tools_response_200_user_navigation import (
            UpdateExternalToolsResponse200UserNavigation,
        )
        from ..models.update_external_tools_response_200_wiki_index_menu import (
            UpdateExternalToolsResponse200WikiIndexMenu,
        )
        from ..models.update_external_tools_response_200_wiki_page_menu import (
            UpdateExternalToolsResponse200WikiPageMenu,
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

        custom_fields = UpdateExternalToolsResponse200CustomFields.from_dict(d.pop("custom_fields"))

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

        account_navigation = UpdateExternalToolsResponse200AccountNavigation.from_dict(d.pop("account_navigation"))

        analytics_hub = UpdateExternalToolsResponse200AnalyticsHub.from_dict(d.pop("analytics_hub"))

        assignment_edit = UpdateExternalToolsResponse200AssignmentEdit.from_dict(d.pop("assignment_edit"))

        assignment_group_menu = UpdateExternalToolsResponse200AssignmentGroupMenu.from_dict(
            d.pop("assignment_group_menu")
        )

        assignment_index_menu = UpdateExternalToolsResponse200AssignmentIndexMenu.from_dict(
            d.pop("assignment_index_menu")
        )

        assignment_menu = UpdateExternalToolsResponse200AssignmentMenu.from_dict(d.pop("assignment_menu"))

        assignment_selection = UpdateExternalToolsResponse200AssignmentSelection.from_dict(
            d.pop("assignment_selection")
        )

        assignment_view = UpdateExternalToolsResponse200AssignmentView.from_dict(d.pop("assignment_view"))

        collaboration = UpdateExternalToolsResponse200Collaboration.from_dict(d.pop("collaboration"))

        conference_selection = UpdateExternalToolsResponse200ConferenceSelection.from_dict(
            d.pop("conference_selection")
        )

        course_assignments_menu = UpdateExternalToolsResponse200CourseAssignmentsMenu.from_dict(
            d.pop("course_assignments_menu")
        )

        course_home_sub_navigation = UpdateExternalToolsResponse200CourseHomeSubNavigation.from_dict(
            d.pop("course_home_sub_navigation")
        )

        course_navigation = UpdateExternalToolsResponse200CourseNavigation.from_dict(d.pop("course_navigation"))

        course_settings_sub_navigation = UpdateExternalToolsResponse200CourseSettingsSubNavigation.from_dict(
            d.pop("course_settings_sub_navigation")
        )

        discussion_topic_index_menu = UpdateExternalToolsResponse200DiscussionTopicIndexMenu.from_dict(
            d.pop("discussion_topic_index_menu")
        )

        discussion_topic_menu = UpdateExternalToolsResponse200DiscussionTopicMenu.from_dict(
            d.pop("discussion_topic_menu")
        )

        editor_button = UpdateExternalToolsResponse200EditorButton.from_dict(d.pop("editor_button"))

        file_index_menu = UpdateExternalToolsResponse200FileIndexMenu.from_dict(d.pop("file_index_menu"))

        file_menu = UpdateExternalToolsResponse200FileMenu.from_dict(d.pop("file_menu"))

        global_navigation = UpdateExternalToolsResponse200GlobalNavigation.from_dict(d.pop("global_navigation"))

        homework_submission = UpdateExternalToolsResponse200HomeworkSubmission.from_dict(d.pop("homework_submission"))

        link_selection = UpdateExternalToolsResponse200LinkSelection.from_dict(d.pop("link_selection"))

        migration_selection = UpdateExternalToolsResponse200MigrationSelection.from_dict(d.pop("migration_selection"))

        module_group_menu = UpdateExternalToolsResponse200ModuleGroupMenu.from_dict(d.pop("module_group_menu"))

        module_index_menu = UpdateExternalToolsResponse200ModuleIndexMenu.from_dict(d.pop("module_index_menu"))

        module_index_menu_modal = UpdateExternalToolsResponse200ModuleIndexMenuModal.from_dict(
            d.pop("module_index_menu_modal")
        )

        module_menu_modal = UpdateExternalToolsResponse200ModuleMenuModal.from_dict(d.pop("module_menu_modal"))

        module_menu = UpdateExternalToolsResponse200ModuleMenu.from_dict(d.pop("module_menu"))

        page_index_menu = UpdateExternalToolsResponse200PageIndexMenu.from_dict(d.pop("page_index_menu"))

        page_menu = UpdateExternalToolsResponse200PageMenu.from_dict(d.pop("page_menu"))

        post_grades = UpdateExternalToolsResponse200PostGrades.from_dict(d.pop("post_grades"))

        quiz_index_menu = UpdateExternalToolsResponse200QuizIndexMenu.from_dict(d.pop("quiz_index_menu"))

        quiz_menu = UpdateExternalToolsResponse200QuizMenu.from_dict(d.pop("quiz_menu"))

        resource_selection = UpdateExternalToolsResponse200ResourceSelection.from_dict(d.pop("resource_selection"))

        similarity_detection = UpdateExternalToolsResponse200SimilarityDetection.from_dict(
            d.pop("similarity_detection")
        )

        student_context_card = UpdateExternalToolsResponse200StudentContextCard.from_dict(d.pop("student_context_card"))

        submission_type_selection = UpdateExternalToolsResponse200SubmissionTypeSelection.from_dict(
            d.pop("submission_type_selection")
        )

        tool_configuration = UpdateExternalToolsResponse200ToolConfiguration.from_dict(d.pop("tool_configuration"))

        top_navigation = UpdateExternalToolsResponse200TopNavigation.from_dict(d.pop("top_navigation"))

        user_navigation = UpdateExternalToolsResponse200UserNavigation.from_dict(d.pop("user_navigation"))

        wiki_index_menu = UpdateExternalToolsResponse200WikiIndexMenu.from_dict(d.pop("wiki_index_menu"))

        wiki_page_menu = UpdateExternalToolsResponse200WikiPageMenu.from_dict(d.pop("wiki_page_menu"))

        activity_asset_processor = UpdateExternalToolsResponse200ActivityAssetProcessor.from_dict(
            d.pop("ActivityAssetProcessor")
        )

        activity_asset_processor_contribution = (
            UpdateExternalToolsResponse200ActivityAssetProcessorContribution.from_dict(
                d.pop("ActivityAssetProcessorContribution")
            )
        )

        update_external_tools_response_200 = cls(
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

        update_external_tools_response_200.additional_properties = d
        return update_external_tools_response_200

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
