from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_appointment_groups_data_body import CreateAppointmentGroupsDataBody
from ...models.create_appointment_groups_json_body import CreateAppointmentGroupsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Union[
        CreateAppointmentGroupsJsonBody,
        CreateAppointmentGroupsDataBody,
    ],
    appointment_groupsub_context_codes: Union[Unset, str] = UNSET,
    appointment_groupdescription: Union[Unset, str] = UNSET,
    appointment_grouplocation_name: Union[Unset, str] = UNSET,
    appointment_grouplocation_address: Union[Unset, str] = UNSET,
    appointment_grouppublish: Union[Unset, bool] = UNSET,
    appointment_groupparticipants_per_appointment: Union[Unset, int] = UNSET,
    appointment_groupmin_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupmax_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupnew_appointments_x: Union[Unset, str] = UNSET,
    appointment_groupparticipant_visibility: Union[Unset, str] = UNSET,
    appointment_groupallow_observer_signup: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["appointment_group[sub_context_codes][]"] = appointment_groupsub_context_codes

    params["appointment_group[description]"] = appointment_groupdescription

    params["appointment_group[location_name]"] = appointment_grouplocation_name

    params["appointment_group[location_address]"] = appointment_grouplocation_address

    params["appointment_group[publish]"] = appointment_grouppublish

    params["appointment_group[participants_per_appointment]"] = appointment_groupparticipants_per_appointment

    params["appointment_group[min_appointments_per_participant]"] = appointment_groupmin_appointments_per_participant

    params["appointment_group[max_appointments_per_participant]"] = appointment_groupmax_appointments_per_participant

    params["appointment_group[new_appointments][X][]"] = appointment_groupnew_appointments_x

    params["appointment_group[participant_visibility]"] = appointment_groupparticipant_visibility

    params["appointment_group[allow_observer_signup]"] = appointment_groupallow_observer_signup

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/appointment_groups",
        "params": params,
    }

    if isinstance(body, CreateAppointmentGroupsJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, CreateAppointmentGroupsDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 500:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAppointmentGroupsJsonBody,
        CreateAppointmentGroupsDataBody,
    ],
    appointment_groupsub_context_codes: Union[Unset, str] = UNSET,
    appointment_groupdescription: Union[Unset, str] = UNSET,
    appointment_grouplocation_name: Union[Unset, str] = UNSET,
    appointment_grouplocation_address: Union[Unset, str] = UNSET,
    appointment_grouppublish: Union[Unset, bool] = UNSET,
    appointment_groupparticipants_per_appointment: Union[Unset, int] = UNSET,
    appointment_groupmin_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupmax_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupnew_appointments_x: Union[Unset, str] = UNSET,
    appointment_groupparticipant_visibility: Union[Unset, str] = UNSET,
    appointment_groupallow_observer_signup: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Create Appointment_Groups

     Create and return a new appointment group. If new\_appointments are specified, the response will
    return a new\_appointments array (same format as appointments array, see “List appointment groups”
    action)

    Required OAuth scope: url:POST|/api/v1/appointment_groups

    Args:
        appointment_groupsub_context_codes (Union[Unset, str]):
        appointment_groupdescription (Union[Unset, str]):
        appointment_grouplocation_name (Union[Unset, str]):
        appointment_grouplocation_address (Union[Unset, str]):
        appointment_grouppublish (Union[Unset, bool]):
        appointment_groupparticipants_per_appointment (Union[Unset, int]):
        appointment_groupmin_appointments_per_participant (Union[Unset, int]):
        appointment_groupmax_appointments_per_participant (Union[Unset, int]):
        appointment_groupnew_appointments_x (Union[Unset, str]):
        appointment_groupparticipant_visibility (Union[Unset, str]):
        appointment_groupallow_observer_signup (Union[Unset, bool]):
        body (CreateAppointmentGroupsJsonBody):
        body (CreateAppointmentGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        appointment_groupsub_context_codes=appointment_groupsub_context_codes,
        appointment_groupdescription=appointment_groupdescription,
        appointment_grouplocation_name=appointment_grouplocation_name,
        appointment_grouplocation_address=appointment_grouplocation_address,
        appointment_grouppublish=appointment_grouppublish,
        appointment_groupparticipants_per_appointment=appointment_groupparticipants_per_appointment,
        appointment_groupmin_appointments_per_participant=appointment_groupmin_appointments_per_participant,
        appointment_groupmax_appointments_per_participant=appointment_groupmax_appointments_per_participant,
        appointment_groupnew_appointments_x=appointment_groupnew_appointments_x,
        appointment_groupparticipant_visibility=appointment_groupparticipant_visibility,
        appointment_groupallow_observer_signup=appointment_groupallow_observer_signup,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        CreateAppointmentGroupsJsonBody,
        CreateAppointmentGroupsDataBody,
    ],
    appointment_groupsub_context_codes: Union[Unset, str] = UNSET,
    appointment_groupdescription: Union[Unset, str] = UNSET,
    appointment_grouplocation_name: Union[Unset, str] = UNSET,
    appointment_grouplocation_address: Union[Unset, str] = UNSET,
    appointment_grouppublish: Union[Unset, bool] = UNSET,
    appointment_groupparticipants_per_appointment: Union[Unset, int] = UNSET,
    appointment_groupmin_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupmax_appointments_per_participant: Union[Unset, int] = UNSET,
    appointment_groupnew_appointments_x: Union[Unset, str] = UNSET,
    appointment_groupparticipant_visibility: Union[Unset, str] = UNSET,
    appointment_groupallow_observer_signup: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    r"""Create Appointment_Groups

     Create and return a new appointment group. If new\_appointments are specified, the response will
    return a new\_appointments array (same format as appointments array, see “List appointment groups”
    action)

    Required OAuth scope: url:POST|/api/v1/appointment_groups

    Args:
        appointment_groupsub_context_codes (Union[Unset, str]):
        appointment_groupdescription (Union[Unset, str]):
        appointment_grouplocation_name (Union[Unset, str]):
        appointment_grouplocation_address (Union[Unset, str]):
        appointment_grouppublish (Union[Unset, bool]):
        appointment_groupparticipants_per_appointment (Union[Unset, int]):
        appointment_groupmin_appointments_per_participant (Union[Unset, int]):
        appointment_groupmax_appointments_per_participant (Union[Unset, int]):
        appointment_groupnew_appointments_x (Union[Unset, str]):
        appointment_groupparticipant_visibility (Union[Unset, str]):
        appointment_groupallow_observer_signup (Union[Unset, bool]):
        body (CreateAppointmentGroupsJsonBody):
        body (CreateAppointmentGroupsDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        appointment_groupsub_context_codes=appointment_groupsub_context_codes,
        appointment_groupdescription=appointment_groupdescription,
        appointment_grouplocation_name=appointment_grouplocation_name,
        appointment_grouplocation_address=appointment_grouplocation_address,
        appointment_grouppublish=appointment_grouppublish,
        appointment_groupparticipants_per_appointment=appointment_groupparticipants_per_appointment,
        appointment_groupmin_appointments_per_participant=appointment_groupmin_appointments_per_participant,
        appointment_groupmax_appointments_per_participant=appointment_groupmax_appointments_per_participant,
        appointment_groupnew_appointments_x=appointment_groupnew_appointments_x,
        appointment_groupparticipant_visibility=appointment_groupparticipant_visibility,
        appointment_groupallow_observer_signup=appointment_groupallow_observer_signup,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
