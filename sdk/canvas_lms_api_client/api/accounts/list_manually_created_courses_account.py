from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_manually_created_courses_account_response_200 import ListManuallyCreatedCoursesAccountResponse200
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/manually_created_courses_account",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    if response.status_code == 200:
        response_200 = ListManuallyCreatedCoursesAccountResponse200.from_dict(response.json())

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
) -> Response[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    r"""List Manually_Created_Courses_Account

     Returns the sub-account that contains manually created courses for the domain root account. Returns
    an [Account](../accounts_-lti#account) object. ### [List active courses in an
    account](#method.accounts.courses_api) <a href=\"#method.accounts.courses_api\"
    id=\"method.accounts.courses_api\"></a>
    [AccountsController#courses\_api](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/accounts_controller.rb)

    Required OAuth scope: url:GET|/api/v1/manually_created_courses_account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    r"""List Manually_Created_Courses_Account

     Returns the sub-account that contains manually created courses for the domain root account. Returns
    an [Account](../accounts_-lti#account) object. ### [List active courses in an
    account](#method.accounts.courses_api) <a href=\"#method.accounts.courses_api\"
    id=\"method.accounts.courses_api\"></a>
    [AccountsController#courses\_api](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/accounts_controller.rb)

    Required OAuth scope: url:GET|/api/v1/manually_created_courses_account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListManuallyCreatedCoursesAccountResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    r"""List Manually_Created_Courses_Account

     Returns the sub-account that contains manually created courses for the domain root account. Returns
    an [Account](../accounts_-lti#account) object. ### [List active courses in an
    account](#method.accounts.courses_api) <a href=\"#method.accounts.courses_api\"
    id=\"method.accounts.courses_api\"></a>
    [AccountsController#courses\_api](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/accounts_controller.rb)

    Required OAuth scope: url:GET|/api/v1/manually_created_courses_account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ListManuallyCreatedCoursesAccountResponse200]]:
    r"""List Manually_Created_Courses_Account

     Returns the sub-account that contains manually created courses for the domain root account. Returns
    an [Account](../accounts_-lti#account) object. ### [List active courses in an
    account](#method.accounts.courses_api) <a href=\"#method.accounts.courses_api\"
    id=\"method.accounts.courses_api\"></a>
    [AccountsController#courses\_api](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/accounts_controller.rb)

    Required OAuth scope: url:GET|/api/v1/manually_created_courses_account

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListManuallyCreatedCoursesAccountResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
