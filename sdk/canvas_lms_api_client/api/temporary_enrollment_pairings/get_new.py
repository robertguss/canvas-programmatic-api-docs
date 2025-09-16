from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_new_response_200 import GetNewResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/temporary_enrollment_pairings/new",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetNewResponse200]]:
    if response.status_code == 200:
        response_200 = GetNewResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetNewResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetNewResponse200]]:
    r"""Get Accounts New

     Initialize an unsaved Temporary Enrollment Pairing. Returns a
    [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object. ### [Create Temporary Enrollment
    Pairing](#method.temporary_enrollment_pairings_api.create) <a
    href=\"#method.temporary_enrollment_pairings_api.create\"
    id=\"method.temporary_enrollment_pairings_api.create\"></a>
    [TemporaryEnrollmentPairingsApiController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNewResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetNewResponse200]]:
    r"""Get Accounts New

     Initialize an unsaved Temporary Enrollment Pairing. Returns a
    [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object. ### [Create Temporary Enrollment
    Pairing](#method.temporary_enrollment_pairings_api.create) <a
    href=\"#method.temporary_enrollment_pairings_api.create\"
    id=\"method.temporary_enrollment_pairings_api.create\"></a>
    [TemporaryEnrollmentPairingsApiController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNewResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, GetNewResponse200]]:
    r"""Get Accounts New

     Initialize an unsaved Temporary Enrollment Pairing. Returns a
    [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object. ### [Create Temporary Enrollment
    Pairing](#method.temporary_enrollment_pairings_api.create) <a
    href=\"#method.temporary_enrollment_pairings_api.create\"
    id=\"method.temporary_enrollment_pairings_api.create\"></a>
    [TemporaryEnrollmentPairingsApiController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetNewResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, GetNewResponse200]]:
    r"""Get Accounts New

     Initialize an unsaved Temporary Enrollment Pairing. Returns a
    [TemporaryEnrollmentPairing](#temporaryenrollmentpairing) object. ### [Create Temporary Enrollment
    Pairing](#method.temporary_enrollment_pairings_api.create) <a
    href=\"#method.temporary_enrollment_pairings_api.create\"
    id=\"method.temporary_enrollment_pairings_api.create\"></a>
    [TemporaryEnrollmentPairingsApiController#create](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new

    Args:
        account_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetNewResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
        )
    ).parsed
