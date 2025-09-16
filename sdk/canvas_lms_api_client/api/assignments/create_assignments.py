from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_assignments_data_body import CreateAssignmentsDataBody
from ...models.create_assignments_json_body import CreateAssignmentsJsonBody
from ...models.create_assignments_response_200_item import CreateAssignmentsResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    body: Union[
        CreateAssignmentsJsonBody,
        CreateAssignmentsDataBody,
    ],
    assignmentposition: Union[Unset, int] = UNSET,
    assignmentsubmission_types: Union[Unset, str] = UNSET,
    assignmentallowed_extensions: Union[Unset, str] = UNSET,
    assignmentturnitin_enabled: Union[Unset, bool] = UNSET,
    assignmentvericite_enabled: Union[Unset, bool] = UNSET,
    assignmentturnitin_settings: Union[Unset, str] = UNSET,
    assignmentintegration_data: str,
    assignmentintegration_id: Union[Unset, str] = UNSET,
    assignmentpeer_reviews: Union[Unset, bool] = UNSET,
    assignmentautomatic_peer_reviews: Union[Unset, bool] = UNSET,
    assignmentnotify_of_update: Union[Unset, bool] = UNSET,
    assignmentgroup_category_id: Union[Unset, int] = UNSET,
    assignmentgrade_group_students_individually: Union[Unset, int] = UNSET,
    assignmentexternal_tool_tag_attributes: Union[Unset, str] = UNSET,
    assignmentgrading_type: Union[Unset, str] = UNSET,
    assignmentdescription: Union[Unset, str] = UNSET,
    assignmentassignment_group_id: Union[Unset, int] = UNSET,
    assignmentonly_visible_to_overrides: Union[Unset, bool] = UNSET,
    assignmentpublished: Union[Unset, bool] = UNSET,
    assignmentgrading_standard_id: Union[Unset, int] = UNSET,
    assignmentomit_from_final_grade: Union[Unset, bool] = UNSET,
    assignmenthide_in_gradebook: Union[Unset, bool] = UNSET,
    assignmentquiz_lti: Union[Unset, bool] = UNSET,
    assignmentmoderated_grading: Union[Unset, bool] = UNSET,
    assignmentgrader_count: Union[Unset, int] = UNSET,
    assignmentfinal_grader_id: Union[Unset, int] = UNSET,
    assignmentgrader_comments_visible_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_anonymous_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_names_visible_to_final_grader: Union[Unset, bool] = UNSET,
    assignmentanonymous_grading: Union[Unset, bool] = UNSET,
    assignmentallowed_attempts: Union[Unset, int] = UNSET,
    assignmentannotatable_attachment_id: Union[Unset, int] = UNSET,
    assignmentpeer_reviewgrading_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["assignment[position]"] = assignmentposition

    params["assignment[submission_types][]"] = assignmentsubmission_types

    params["assignment[allowed_extensions][]"] = assignmentallowed_extensions

    params["assignment[turnitin_enabled]"] = assignmentturnitin_enabled

    params["assignment[vericite_enabled]"] = assignmentvericite_enabled

    params["assignment[turnitin_settings]"] = assignmentturnitin_settings

    params["assignment[integration_data]"] = assignmentintegration_data

    params["assignment[integration_id]"] = assignmentintegration_id

    params["assignment[peer_reviews]"] = assignmentpeer_reviews

    params["assignment[automatic_peer_reviews]"] = assignmentautomatic_peer_reviews

    params["assignment[notify_of_update]"] = assignmentnotify_of_update

    params["assignment[group_category_id]"] = assignmentgroup_category_id

    params["assignment[grade_group_students_individually]"] = assignmentgrade_group_students_individually

    params["assignment[external_tool_tag_attributes]"] = assignmentexternal_tool_tag_attributes

    params["assignment[grading_type]"] = assignmentgrading_type

    params["assignment[description]"] = assignmentdescription

    params["assignment[assignment_group_id]"] = assignmentassignment_group_id

    params["assignment[only_visible_to_overrides]"] = assignmentonly_visible_to_overrides

    params["assignment[published]"] = assignmentpublished

    params["assignment[grading_standard_id]"] = assignmentgrading_standard_id

    params["assignment[omit_from_final_grade]"] = assignmentomit_from_final_grade

    params["assignment[hide_in_gradebook]"] = assignmenthide_in_gradebook

    params["assignment[quiz_lti]"] = assignmentquiz_lti

    params["assignment[moderated_grading]"] = assignmentmoderated_grading

    params["assignment[grader_count]"] = assignmentgrader_count

    params["assignment[final_grader_id]"] = assignmentfinal_grader_id

    params["assignment[grader_comments_visible_to_graders]"] = assignmentgrader_comments_visible_to_graders

    params["assignment[graders_anonymous_to_graders]"] = assignmentgraders_anonymous_to_graders

    params["assignment[graders_names_visible_to_final_grader]"] = assignmentgraders_names_visible_to_final_grader

    params["assignment[anonymous_grading]"] = assignmentanonymous_grading

    params["assignment[allowed_attempts]"] = assignmentallowed_attempts

    params["assignment[annotatable_attachment_id]"] = assignmentannotatable_attachment_id

    params["assignment[peer_review][grading_type]"] = assignmentpeer_reviewgrading_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/assignments",
        "params": params,
    }

    if isinstance(body, CreateAssignmentsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateAssignmentsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateAssignmentsResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAssignmentsJsonBody,
        CreateAssignmentsDataBody,
    ],
    assignmentposition: Union[Unset, int] = UNSET,
    assignmentsubmission_types: Union[Unset, str] = UNSET,
    assignmentallowed_extensions: Union[Unset, str] = UNSET,
    assignmentturnitin_enabled: Union[Unset, bool] = UNSET,
    assignmentvericite_enabled: Union[Unset, bool] = UNSET,
    assignmentturnitin_settings: Union[Unset, str] = UNSET,
    assignmentintegration_data: str,
    assignmentintegration_id: Union[Unset, str] = UNSET,
    assignmentpeer_reviews: Union[Unset, bool] = UNSET,
    assignmentautomatic_peer_reviews: Union[Unset, bool] = UNSET,
    assignmentnotify_of_update: Union[Unset, bool] = UNSET,
    assignmentgroup_category_id: Union[Unset, int] = UNSET,
    assignmentgrade_group_students_individually: Union[Unset, int] = UNSET,
    assignmentexternal_tool_tag_attributes: Union[Unset, str] = UNSET,
    assignmentgrading_type: Union[Unset, str] = UNSET,
    assignmentdescription: Union[Unset, str] = UNSET,
    assignmentassignment_group_id: Union[Unset, int] = UNSET,
    assignmentonly_visible_to_overrides: Union[Unset, bool] = UNSET,
    assignmentpublished: Union[Unset, bool] = UNSET,
    assignmentgrading_standard_id: Union[Unset, int] = UNSET,
    assignmentomit_from_final_grade: Union[Unset, bool] = UNSET,
    assignmenthide_in_gradebook: Union[Unset, bool] = UNSET,
    assignmentquiz_lti: Union[Unset, bool] = UNSET,
    assignmentmoderated_grading: Union[Unset, bool] = UNSET,
    assignmentgrader_count: Union[Unset, int] = UNSET,
    assignmentfinal_grader_id: Union[Unset, int] = UNSET,
    assignmentgrader_comments_visible_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_anonymous_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_names_visible_to_final_grader: Union[Unset, bool] = UNSET,
    assignmentanonymous_grading: Union[Unset, bool] = UNSET,
    assignmentallowed_attempts: Union[Unset, int] = UNSET,
    assignmentannotatable_attachment_id: Union[Unset, int] = UNSET,
    assignmentpeer_reviewgrading_type: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    """Post Courses Assignments

     Create a new assignment for this course. The assignment is created in the active state.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments

    Args:
        course_id (str):
        assignmentposition (Union[Unset, int]):
        assignmentsubmission_types (Union[Unset, str]):
        assignmentallowed_extensions (Union[Unset, str]):
        assignmentturnitin_enabled (Union[Unset, bool]):
        assignmentvericite_enabled (Union[Unset, bool]):
        assignmentturnitin_settings (Union[Unset, str]):
        assignmentintegration_data (str):
        assignmentintegration_id (Union[Unset, str]):
        assignmentpeer_reviews (Union[Unset, bool]):
        assignmentautomatic_peer_reviews (Union[Unset, bool]):
        assignmentnotify_of_update (Union[Unset, bool]):
        assignmentgroup_category_id (Union[Unset, int]):
        assignmentgrade_group_students_individually (Union[Unset, int]):
        assignmentexternal_tool_tag_attributes (Union[Unset, str]):
        assignmentgrading_type (Union[Unset, str]):
        assignmentdescription (Union[Unset, str]):
        assignmentassignment_group_id (Union[Unset, int]):
        assignmentonly_visible_to_overrides (Union[Unset, bool]):
        assignmentpublished (Union[Unset, bool]):
        assignmentgrading_standard_id (Union[Unset, int]):
        assignmentomit_from_final_grade (Union[Unset, bool]):
        assignmenthide_in_gradebook (Union[Unset, bool]):
        assignmentquiz_lti (Union[Unset, bool]):
        assignmentmoderated_grading (Union[Unset, bool]):
        assignmentgrader_count (Union[Unset, int]):
        assignmentfinal_grader_id (Union[Unset, int]):
        assignmentgrader_comments_visible_to_graders (Union[Unset, bool]):
        assignmentgraders_anonymous_to_graders (Union[Unset, bool]):
        assignmentgraders_names_visible_to_final_grader (Union[Unset, bool]):
        assignmentanonymous_grading (Union[Unset, bool]):
        assignmentallowed_attempts (Union[Unset, int]):
        assignmentannotatable_attachment_id (Union[Unset, int]):
        assignmentpeer_reviewgrading_type (Union[Unset, str]):
        body (CreateAssignmentsJsonBody):
        body (CreateAssignmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateAssignmentsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        assignmentposition=assignmentposition,
        assignmentsubmission_types=assignmentsubmission_types,
        assignmentallowed_extensions=assignmentallowed_extensions,
        assignmentturnitin_enabled=assignmentturnitin_enabled,
        assignmentvericite_enabled=assignmentvericite_enabled,
        assignmentturnitin_settings=assignmentturnitin_settings,
        assignmentintegration_data=assignmentintegration_data,
        assignmentintegration_id=assignmentintegration_id,
        assignmentpeer_reviews=assignmentpeer_reviews,
        assignmentautomatic_peer_reviews=assignmentautomatic_peer_reviews,
        assignmentnotify_of_update=assignmentnotify_of_update,
        assignmentgroup_category_id=assignmentgroup_category_id,
        assignmentgrade_group_students_individually=assignmentgrade_group_students_individually,
        assignmentexternal_tool_tag_attributes=assignmentexternal_tool_tag_attributes,
        assignmentgrading_type=assignmentgrading_type,
        assignmentdescription=assignmentdescription,
        assignmentassignment_group_id=assignmentassignment_group_id,
        assignmentonly_visible_to_overrides=assignmentonly_visible_to_overrides,
        assignmentpublished=assignmentpublished,
        assignmentgrading_standard_id=assignmentgrading_standard_id,
        assignmentomit_from_final_grade=assignmentomit_from_final_grade,
        assignmenthide_in_gradebook=assignmenthide_in_gradebook,
        assignmentquiz_lti=assignmentquiz_lti,
        assignmentmoderated_grading=assignmentmoderated_grading,
        assignmentgrader_count=assignmentgrader_count,
        assignmentfinal_grader_id=assignmentfinal_grader_id,
        assignmentgrader_comments_visible_to_graders=assignmentgrader_comments_visible_to_graders,
        assignmentgraders_anonymous_to_graders=assignmentgraders_anonymous_to_graders,
        assignmentgraders_names_visible_to_final_grader=assignmentgraders_names_visible_to_final_grader,
        assignmentanonymous_grading=assignmentanonymous_grading,
        assignmentallowed_attempts=assignmentallowed_attempts,
        assignmentannotatable_attachment_id=assignmentannotatable_attachment_id,
        assignmentpeer_reviewgrading_type=assignmentpeer_reviewgrading_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAssignmentsJsonBody,
        CreateAssignmentsDataBody,
    ],
    assignmentposition: Union[Unset, int] = UNSET,
    assignmentsubmission_types: Union[Unset, str] = UNSET,
    assignmentallowed_extensions: Union[Unset, str] = UNSET,
    assignmentturnitin_enabled: Union[Unset, bool] = UNSET,
    assignmentvericite_enabled: Union[Unset, bool] = UNSET,
    assignmentturnitin_settings: Union[Unset, str] = UNSET,
    assignmentintegration_data: str,
    assignmentintegration_id: Union[Unset, str] = UNSET,
    assignmentpeer_reviews: Union[Unset, bool] = UNSET,
    assignmentautomatic_peer_reviews: Union[Unset, bool] = UNSET,
    assignmentnotify_of_update: Union[Unset, bool] = UNSET,
    assignmentgroup_category_id: Union[Unset, int] = UNSET,
    assignmentgrade_group_students_individually: Union[Unset, int] = UNSET,
    assignmentexternal_tool_tag_attributes: Union[Unset, str] = UNSET,
    assignmentgrading_type: Union[Unset, str] = UNSET,
    assignmentdescription: Union[Unset, str] = UNSET,
    assignmentassignment_group_id: Union[Unset, int] = UNSET,
    assignmentonly_visible_to_overrides: Union[Unset, bool] = UNSET,
    assignmentpublished: Union[Unset, bool] = UNSET,
    assignmentgrading_standard_id: Union[Unset, int] = UNSET,
    assignmentomit_from_final_grade: Union[Unset, bool] = UNSET,
    assignmenthide_in_gradebook: Union[Unset, bool] = UNSET,
    assignmentquiz_lti: Union[Unset, bool] = UNSET,
    assignmentmoderated_grading: Union[Unset, bool] = UNSET,
    assignmentgrader_count: Union[Unset, int] = UNSET,
    assignmentfinal_grader_id: Union[Unset, int] = UNSET,
    assignmentgrader_comments_visible_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_anonymous_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_names_visible_to_final_grader: Union[Unset, bool] = UNSET,
    assignmentanonymous_grading: Union[Unset, bool] = UNSET,
    assignmentallowed_attempts: Union[Unset, int] = UNSET,
    assignmentannotatable_attachment_id: Union[Unset, int] = UNSET,
    assignmentpeer_reviewgrading_type: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    """Post Courses Assignments

     Create a new assignment for this course. The assignment is created in the active state.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments

    Args:
        course_id (str):
        assignmentposition (Union[Unset, int]):
        assignmentsubmission_types (Union[Unset, str]):
        assignmentallowed_extensions (Union[Unset, str]):
        assignmentturnitin_enabled (Union[Unset, bool]):
        assignmentvericite_enabled (Union[Unset, bool]):
        assignmentturnitin_settings (Union[Unset, str]):
        assignmentintegration_data (str):
        assignmentintegration_id (Union[Unset, str]):
        assignmentpeer_reviews (Union[Unset, bool]):
        assignmentautomatic_peer_reviews (Union[Unset, bool]):
        assignmentnotify_of_update (Union[Unset, bool]):
        assignmentgroup_category_id (Union[Unset, int]):
        assignmentgrade_group_students_individually (Union[Unset, int]):
        assignmentexternal_tool_tag_attributes (Union[Unset, str]):
        assignmentgrading_type (Union[Unset, str]):
        assignmentdescription (Union[Unset, str]):
        assignmentassignment_group_id (Union[Unset, int]):
        assignmentonly_visible_to_overrides (Union[Unset, bool]):
        assignmentpublished (Union[Unset, bool]):
        assignmentgrading_standard_id (Union[Unset, int]):
        assignmentomit_from_final_grade (Union[Unset, bool]):
        assignmenthide_in_gradebook (Union[Unset, bool]):
        assignmentquiz_lti (Union[Unset, bool]):
        assignmentmoderated_grading (Union[Unset, bool]):
        assignmentgrader_count (Union[Unset, int]):
        assignmentfinal_grader_id (Union[Unset, int]):
        assignmentgrader_comments_visible_to_graders (Union[Unset, bool]):
        assignmentgraders_anonymous_to_graders (Union[Unset, bool]):
        assignmentgraders_names_visible_to_final_grader (Union[Unset, bool]):
        assignmentanonymous_grading (Union[Unset, bool]):
        assignmentallowed_attempts (Union[Unset, int]):
        assignmentannotatable_attachment_id (Union[Unset, int]):
        assignmentpeer_reviewgrading_type (Union[Unset, str]):
        body (CreateAssignmentsJsonBody):
        body (CreateAssignmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateAssignmentsResponse200Item']]
    """

    return sync_detailed(
        course_id=course_id,
        client=client,
        body=body,
        assignmentposition=assignmentposition,
        assignmentsubmission_types=assignmentsubmission_types,
        assignmentallowed_extensions=assignmentallowed_extensions,
        assignmentturnitin_enabled=assignmentturnitin_enabled,
        assignmentvericite_enabled=assignmentvericite_enabled,
        assignmentturnitin_settings=assignmentturnitin_settings,
        assignmentintegration_data=assignmentintegration_data,
        assignmentintegration_id=assignmentintegration_id,
        assignmentpeer_reviews=assignmentpeer_reviews,
        assignmentautomatic_peer_reviews=assignmentautomatic_peer_reviews,
        assignmentnotify_of_update=assignmentnotify_of_update,
        assignmentgroup_category_id=assignmentgroup_category_id,
        assignmentgrade_group_students_individually=assignmentgrade_group_students_individually,
        assignmentexternal_tool_tag_attributes=assignmentexternal_tool_tag_attributes,
        assignmentgrading_type=assignmentgrading_type,
        assignmentdescription=assignmentdescription,
        assignmentassignment_group_id=assignmentassignment_group_id,
        assignmentonly_visible_to_overrides=assignmentonly_visible_to_overrides,
        assignmentpublished=assignmentpublished,
        assignmentgrading_standard_id=assignmentgrading_standard_id,
        assignmentomit_from_final_grade=assignmentomit_from_final_grade,
        assignmenthide_in_gradebook=assignmenthide_in_gradebook,
        assignmentquiz_lti=assignmentquiz_lti,
        assignmentmoderated_grading=assignmentmoderated_grading,
        assignmentgrader_count=assignmentgrader_count,
        assignmentfinal_grader_id=assignmentfinal_grader_id,
        assignmentgrader_comments_visible_to_graders=assignmentgrader_comments_visible_to_graders,
        assignmentgraders_anonymous_to_graders=assignmentgraders_anonymous_to_graders,
        assignmentgraders_names_visible_to_final_grader=assignmentgraders_names_visible_to_final_grader,
        assignmentanonymous_grading=assignmentanonymous_grading,
        assignmentallowed_attempts=assignmentallowed_attempts,
        assignmentannotatable_attachment_id=assignmentannotatable_attachment_id,
        assignmentpeer_reviewgrading_type=assignmentpeer_reviewgrading_type,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAssignmentsJsonBody,
        CreateAssignmentsDataBody,
    ],
    assignmentposition: Union[Unset, int] = UNSET,
    assignmentsubmission_types: Union[Unset, str] = UNSET,
    assignmentallowed_extensions: Union[Unset, str] = UNSET,
    assignmentturnitin_enabled: Union[Unset, bool] = UNSET,
    assignmentvericite_enabled: Union[Unset, bool] = UNSET,
    assignmentturnitin_settings: Union[Unset, str] = UNSET,
    assignmentintegration_data: str,
    assignmentintegration_id: Union[Unset, str] = UNSET,
    assignmentpeer_reviews: Union[Unset, bool] = UNSET,
    assignmentautomatic_peer_reviews: Union[Unset, bool] = UNSET,
    assignmentnotify_of_update: Union[Unset, bool] = UNSET,
    assignmentgroup_category_id: Union[Unset, int] = UNSET,
    assignmentgrade_group_students_individually: Union[Unset, int] = UNSET,
    assignmentexternal_tool_tag_attributes: Union[Unset, str] = UNSET,
    assignmentgrading_type: Union[Unset, str] = UNSET,
    assignmentdescription: Union[Unset, str] = UNSET,
    assignmentassignment_group_id: Union[Unset, int] = UNSET,
    assignmentonly_visible_to_overrides: Union[Unset, bool] = UNSET,
    assignmentpublished: Union[Unset, bool] = UNSET,
    assignmentgrading_standard_id: Union[Unset, int] = UNSET,
    assignmentomit_from_final_grade: Union[Unset, bool] = UNSET,
    assignmenthide_in_gradebook: Union[Unset, bool] = UNSET,
    assignmentquiz_lti: Union[Unset, bool] = UNSET,
    assignmentmoderated_grading: Union[Unset, bool] = UNSET,
    assignmentgrader_count: Union[Unset, int] = UNSET,
    assignmentfinal_grader_id: Union[Unset, int] = UNSET,
    assignmentgrader_comments_visible_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_anonymous_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_names_visible_to_final_grader: Union[Unset, bool] = UNSET,
    assignmentanonymous_grading: Union[Unset, bool] = UNSET,
    assignmentallowed_attempts: Union[Unset, int] = UNSET,
    assignmentannotatable_attachment_id: Union[Unset, int] = UNSET,
    assignmentpeer_reviewgrading_type: Union[Unset, str] = UNSET,
) -> Response[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    """Post Courses Assignments

     Create a new assignment for this course. The assignment is created in the active state.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments

    Args:
        course_id (str):
        assignmentposition (Union[Unset, int]):
        assignmentsubmission_types (Union[Unset, str]):
        assignmentallowed_extensions (Union[Unset, str]):
        assignmentturnitin_enabled (Union[Unset, bool]):
        assignmentvericite_enabled (Union[Unset, bool]):
        assignmentturnitin_settings (Union[Unset, str]):
        assignmentintegration_data (str):
        assignmentintegration_id (Union[Unset, str]):
        assignmentpeer_reviews (Union[Unset, bool]):
        assignmentautomatic_peer_reviews (Union[Unset, bool]):
        assignmentnotify_of_update (Union[Unset, bool]):
        assignmentgroup_category_id (Union[Unset, int]):
        assignmentgrade_group_students_individually (Union[Unset, int]):
        assignmentexternal_tool_tag_attributes (Union[Unset, str]):
        assignmentgrading_type (Union[Unset, str]):
        assignmentdescription (Union[Unset, str]):
        assignmentassignment_group_id (Union[Unset, int]):
        assignmentonly_visible_to_overrides (Union[Unset, bool]):
        assignmentpublished (Union[Unset, bool]):
        assignmentgrading_standard_id (Union[Unset, int]):
        assignmentomit_from_final_grade (Union[Unset, bool]):
        assignmenthide_in_gradebook (Union[Unset, bool]):
        assignmentquiz_lti (Union[Unset, bool]):
        assignmentmoderated_grading (Union[Unset, bool]):
        assignmentgrader_count (Union[Unset, int]):
        assignmentfinal_grader_id (Union[Unset, int]):
        assignmentgrader_comments_visible_to_graders (Union[Unset, bool]):
        assignmentgraders_anonymous_to_graders (Union[Unset, bool]):
        assignmentgraders_names_visible_to_final_grader (Union[Unset, bool]):
        assignmentanonymous_grading (Union[Unset, bool]):
        assignmentallowed_attempts (Union[Unset, int]):
        assignmentannotatable_attachment_id (Union[Unset, int]):
        assignmentpeer_reviewgrading_type (Union[Unset, str]):
        body (CreateAssignmentsJsonBody):
        body (CreateAssignmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateAssignmentsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        body=body,
        assignmentposition=assignmentposition,
        assignmentsubmission_types=assignmentsubmission_types,
        assignmentallowed_extensions=assignmentallowed_extensions,
        assignmentturnitin_enabled=assignmentturnitin_enabled,
        assignmentvericite_enabled=assignmentvericite_enabled,
        assignmentturnitin_settings=assignmentturnitin_settings,
        assignmentintegration_data=assignmentintegration_data,
        assignmentintegration_id=assignmentintegration_id,
        assignmentpeer_reviews=assignmentpeer_reviews,
        assignmentautomatic_peer_reviews=assignmentautomatic_peer_reviews,
        assignmentnotify_of_update=assignmentnotify_of_update,
        assignmentgroup_category_id=assignmentgroup_category_id,
        assignmentgrade_group_students_individually=assignmentgrade_group_students_individually,
        assignmentexternal_tool_tag_attributes=assignmentexternal_tool_tag_attributes,
        assignmentgrading_type=assignmentgrading_type,
        assignmentdescription=assignmentdescription,
        assignmentassignment_group_id=assignmentassignment_group_id,
        assignmentonly_visible_to_overrides=assignmentonly_visible_to_overrides,
        assignmentpublished=assignmentpublished,
        assignmentgrading_standard_id=assignmentgrading_standard_id,
        assignmentomit_from_final_grade=assignmentomit_from_final_grade,
        assignmenthide_in_gradebook=assignmenthide_in_gradebook,
        assignmentquiz_lti=assignmentquiz_lti,
        assignmentmoderated_grading=assignmentmoderated_grading,
        assignmentgrader_count=assignmentgrader_count,
        assignmentfinal_grader_id=assignmentfinal_grader_id,
        assignmentgrader_comments_visible_to_graders=assignmentgrader_comments_visible_to_graders,
        assignmentgraders_anonymous_to_graders=assignmentgraders_anonymous_to_graders,
        assignmentgraders_names_visible_to_final_grader=assignmentgraders_names_visible_to_final_grader,
        assignmentanonymous_grading=assignmentanonymous_grading,
        assignmentallowed_attempts=assignmentallowed_attempts,
        assignmentannotatable_attachment_id=assignmentannotatable_attachment_id,
        assignmentpeer_reviewgrading_type=assignmentpeer_reviewgrading_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAssignmentsJsonBody,
        CreateAssignmentsDataBody,
    ],
    assignmentposition: Union[Unset, int] = UNSET,
    assignmentsubmission_types: Union[Unset, str] = UNSET,
    assignmentallowed_extensions: Union[Unset, str] = UNSET,
    assignmentturnitin_enabled: Union[Unset, bool] = UNSET,
    assignmentvericite_enabled: Union[Unset, bool] = UNSET,
    assignmentturnitin_settings: Union[Unset, str] = UNSET,
    assignmentintegration_data: str,
    assignmentintegration_id: Union[Unset, str] = UNSET,
    assignmentpeer_reviews: Union[Unset, bool] = UNSET,
    assignmentautomatic_peer_reviews: Union[Unset, bool] = UNSET,
    assignmentnotify_of_update: Union[Unset, bool] = UNSET,
    assignmentgroup_category_id: Union[Unset, int] = UNSET,
    assignmentgrade_group_students_individually: Union[Unset, int] = UNSET,
    assignmentexternal_tool_tag_attributes: Union[Unset, str] = UNSET,
    assignmentgrading_type: Union[Unset, str] = UNSET,
    assignmentdescription: Union[Unset, str] = UNSET,
    assignmentassignment_group_id: Union[Unset, int] = UNSET,
    assignmentonly_visible_to_overrides: Union[Unset, bool] = UNSET,
    assignmentpublished: Union[Unset, bool] = UNSET,
    assignmentgrading_standard_id: Union[Unset, int] = UNSET,
    assignmentomit_from_final_grade: Union[Unset, bool] = UNSET,
    assignmenthide_in_gradebook: Union[Unset, bool] = UNSET,
    assignmentquiz_lti: Union[Unset, bool] = UNSET,
    assignmentmoderated_grading: Union[Unset, bool] = UNSET,
    assignmentgrader_count: Union[Unset, int] = UNSET,
    assignmentfinal_grader_id: Union[Unset, int] = UNSET,
    assignmentgrader_comments_visible_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_anonymous_to_graders: Union[Unset, bool] = UNSET,
    assignmentgraders_names_visible_to_final_grader: Union[Unset, bool] = UNSET,
    assignmentanonymous_grading: Union[Unset, bool] = UNSET,
    assignmentallowed_attempts: Union[Unset, int] = UNSET,
    assignmentannotatable_attachment_id: Union[Unset, int] = UNSET,
    assignmentpeer_reviewgrading_type: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, list["CreateAssignmentsResponse200Item"]]]:
    """Post Courses Assignments

     Create a new assignment for this course. The assignment is created in the active state.

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/assignments

    Args:
        course_id (str):
        assignmentposition (Union[Unset, int]):
        assignmentsubmission_types (Union[Unset, str]):
        assignmentallowed_extensions (Union[Unset, str]):
        assignmentturnitin_enabled (Union[Unset, bool]):
        assignmentvericite_enabled (Union[Unset, bool]):
        assignmentturnitin_settings (Union[Unset, str]):
        assignmentintegration_data (str):
        assignmentintegration_id (Union[Unset, str]):
        assignmentpeer_reviews (Union[Unset, bool]):
        assignmentautomatic_peer_reviews (Union[Unset, bool]):
        assignmentnotify_of_update (Union[Unset, bool]):
        assignmentgroup_category_id (Union[Unset, int]):
        assignmentgrade_group_students_individually (Union[Unset, int]):
        assignmentexternal_tool_tag_attributes (Union[Unset, str]):
        assignmentgrading_type (Union[Unset, str]):
        assignmentdescription (Union[Unset, str]):
        assignmentassignment_group_id (Union[Unset, int]):
        assignmentonly_visible_to_overrides (Union[Unset, bool]):
        assignmentpublished (Union[Unset, bool]):
        assignmentgrading_standard_id (Union[Unset, int]):
        assignmentomit_from_final_grade (Union[Unset, bool]):
        assignmenthide_in_gradebook (Union[Unset, bool]):
        assignmentquiz_lti (Union[Unset, bool]):
        assignmentmoderated_grading (Union[Unset, bool]):
        assignmentgrader_count (Union[Unset, int]):
        assignmentfinal_grader_id (Union[Unset, int]):
        assignmentgrader_comments_visible_to_graders (Union[Unset, bool]):
        assignmentgraders_anonymous_to_graders (Union[Unset, bool]):
        assignmentgraders_names_visible_to_final_grader (Union[Unset, bool]):
        assignmentanonymous_grading (Union[Unset, bool]):
        assignmentallowed_attempts (Union[Unset, int]):
        assignmentannotatable_attachment_id (Union[Unset, int]):
        assignmentpeer_reviewgrading_type (Union[Unset, str]):
        body (CreateAssignmentsJsonBody):
        body (CreateAssignmentsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateAssignmentsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            client=client,
            body=body,
            assignmentposition=assignmentposition,
            assignmentsubmission_types=assignmentsubmission_types,
            assignmentallowed_extensions=assignmentallowed_extensions,
            assignmentturnitin_enabled=assignmentturnitin_enabled,
            assignmentvericite_enabled=assignmentvericite_enabled,
            assignmentturnitin_settings=assignmentturnitin_settings,
            assignmentintegration_data=assignmentintegration_data,
            assignmentintegration_id=assignmentintegration_id,
            assignmentpeer_reviews=assignmentpeer_reviews,
            assignmentautomatic_peer_reviews=assignmentautomatic_peer_reviews,
            assignmentnotify_of_update=assignmentnotify_of_update,
            assignmentgroup_category_id=assignmentgroup_category_id,
            assignmentgrade_group_students_individually=assignmentgrade_group_students_individually,
            assignmentexternal_tool_tag_attributes=assignmentexternal_tool_tag_attributes,
            assignmentgrading_type=assignmentgrading_type,
            assignmentdescription=assignmentdescription,
            assignmentassignment_group_id=assignmentassignment_group_id,
            assignmentonly_visible_to_overrides=assignmentonly_visible_to_overrides,
            assignmentpublished=assignmentpublished,
            assignmentgrading_standard_id=assignmentgrading_standard_id,
            assignmentomit_from_final_grade=assignmentomit_from_final_grade,
            assignmenthide_in_gradebook=assignmenthide_in_gradebook,
            assignmentquiz_lti=assignmentquiz_lti,
            assignmentmoderated_grading=assignmentmoderated_grading,
            assignmentgrader_count=assignmentgrader_count,
            assignmentfinal_grader_id=assignmentfinal_grader_id,
            assignmentgrader_comments_visible_to_graders=assignmentgrader_comments_visible_to_graders,
            assignmentgraders_anonymous_to_graders=assignmentgraders_anonymous_to_graders,
            assignmentgraders_names_visible_to_final_grader=assignmentgraders_names_visible_to_final_grader,
            assignmentanonymous_grading=assignmentanonymous_grading,
            assignmentallowed_attempts=assignmentallowed_attempts,
            assignmentannotatable_attachment_id=assignmentannotatable_attachment_id,
            assignmentpeer_reviewgrading_type=assignmentpeer_reviewgrading_type,
        )
    ).parsed
