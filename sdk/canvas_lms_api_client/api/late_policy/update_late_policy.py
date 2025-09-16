from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_late_policy_data_body import UpdateLatePolicyDataBody
from ...models.update_late_policy_json_body import UpdateLatePolicyJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateLatePolicyJsonBody,
        UpdateLatePolicyDataBody,
    ],
    late_policymissing_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_interval: Union[Unset, str] = UNSET,
    late_policylate_submission_minimum_percent_enabled: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["late_policy[missing_submission_deduction_enabled]"] = late_policymissing_submission_deduction_enabled

    params["late_policy[late_submission_deduction_enabled]"] = late_policylate_submission_deduction_enabled

    params["late_policy[late_submission_interval]"] = late_policylate_submission_interval

    params["late_policy[late_submission_minimum_percent_enabled]"] = late_policylate_submission_minimum_percent_enabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/v1/courses/{id}/late_policy",
        "params": params,
    }

    if isinstance(body, UpdateLatePolicyJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateLatePolicyDataBody):
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
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateLatePolicyJsonBody,
        UpdateLatePolicyDataBody,
    ],
    late_policymissing_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_interval: Union[Unset, str] = UNSET,
    late_policylate_submission_minimum_percent_enabled: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Patch Courses Late_Policy

     Patch a late policy. No body is returned upon success.

    Required OAuth scope: url:PATCH|/api/v1/courses/:id/late_policy

    Args:
        id (str):
        late_policymissing_submission_deduction_enabled (Union[Unset, bool]):
        late_policylate_submission_deduction_enabled (Union[Unset, bool]):
        late_policylate_submission_interval (Union[Unset, str]):
        late_policylate_submission_minimum_percent_enabled (Union[Unset, bool]):
        body (UpdateLatePolicyJsonBody):
        body (UpdateLatePolicyDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        late_policymissing_submission_deduction_enabled=late_policymissing_submission_deduction_enabled,
        late_policylate_submission_deduction_enabled=late_policylate_submission_deduction_enabled,
        late_policylate_submission_interval=late_policylate_submission_interval,
        late_policylate_submission_minimum_percent_enabled=late_policylate_submission_minimum_percent_enabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateLatePolicyJsonBody,
        UpdateLatePolicyDataBody,
    ],
    late_policymissing_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_deduction_enabled: Union[Unset, bool] = UNSET,
    late_policylate_submission_interval: Union[Unset, str] = UNSET,
    late_policylate_submission_minimum_percent_enabled: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Patch Courses Late_Policy

     Patch a late policy. No body is returned upon success.

    Required OAuth scope: url:PATCH|/api/v1/courses/:id/late_policy

    Args:
        id (str):
        late_policymissing_submission_deduction_enabled (Union[Unset, bool]):
        late_policylate_submission_deduction_enabled (Union[Unset, bool]):
        late_policylate_submission_interval (Union[Unset, str]):
        late_policylate_submission_minimum_percent_enabled (Union[Unset, bool]):
        body (UpdateLatePolicyJsonBody):
        body (UpdateLatePolicyDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        late_policymissing_submission_deduction_enabled=late_policymissing_submission_deduction_enabled,
        late_policylate_submission_deduction_enabled=late_policylate_submission_deduction_enabled,
        late_policylate_submission_interval=late_policylate_submission_interval,
        late_policylate_submission_minimum_percent_enabled=late_policylate_submission_minimum_percent_enabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
