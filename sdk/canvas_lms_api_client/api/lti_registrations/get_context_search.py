from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_context_search_response_200 import GetContextSearchResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    registration_id: str,
    deployment_id: str,
    *,
    only_children_of: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["only_children_of"] = only_children_of

    params["search_term"] = search_term

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{deployment_id}/context_search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetContextSearchResponse200]]:
    if response.status_code == 200:
        response_200 = GetContextSearchResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetContextSearchResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    registration_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    only_children_of: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetContextSearchResponse200]]:
    """Get Accounts Context_Search

     This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases. Search
    for accounts and courses that match the search term on name, SIS id, or course code. Returns all
    matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about
    each account and course, and only up to 20 of each. Used to populate the search dropdowns when
    managing LTI registration availability.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deploy
    ments/:deployment_id/context_search

    Args:
        account_id (str):
        registration_id (str):
        deployment_id (str):
        only_children_of (Union[Unset, str]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContextSearchResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        registration_id=registration_id,
        deployment_id=deployment_id,
        only_children_of=only_children_of,
        search_term=search_term,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    registration_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    only_children_of: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetContextSearchResponse200]]:
    """Get Accounts Context_Search

     This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases. Search
    for accounts and courses that match the search term on name, SIS id, or course code. Returns all
    matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about
    each account and course, and only up to 20 of each. Used to populate the search dropdowns when
    managing LTI registration availability.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deploy
    ments/:deployment_id/context_search

    Args:
        account_id (str):
        registration_id (str):
        deployment_id (str):
        only_children_of (Union[Unset, str]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContextSearchResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        registration_id=registration_id,
        deployment_id=deployment_id,
        client=client,
        only_children_of=only_children_of,
        search_term=search_term,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    registration_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    only_children_of: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetContextSearchResponse200]]:
    """Get Accounts Context_Search

     This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases. Search
    for accounts and courses that match the search term on name, SIS id, or course code. Returns all
    matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about
    each account and course, and only up to 20 of each. Used to populate the search dropdowns when
    managing LTI registration availability.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deploy
    ments/:deployment_id/context_search

    Args:
        account_id (str):
        registration_id (str):
        deployment_id (str):
        only_children_of (Union[Unset, str]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetContextSearchResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        registration_id=registration_id,
        deployment_id=deployment_id,
        only_children_of=only_children_of,
        search_term=search_term,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    registration_id: str,
    deployment_id: str,
    *,
    client: AuthenticatedClient,
    only_children_of: Union[Unset, str] = UNSET,
    search_term: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetContextSearchResponse200]]:
    """Get Accounts Context_Search

     This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases. Search
    for accounts and courses that match the search term on name, SIS id, or course code. Returns all
    matching accounts and courses, including those nested in sub-accounts. Returns bare-bones data about
    each account and course, and only up to 20 of each. Used to populate the search dropdowns when
    managing LTI registration availability.

    Required OAuth scope: url:GET|/api/v1/accounts/:account_id/lti_registrations/:registration_id/deploy
    ments/:deployment_id/context_search

    Args:
        account_id (str):
        registration_id (str):
        deployment_id (str):
        only_children_of (Union[Unset, str]):
        search_term (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetContextSearchResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            registration_id=registration_id,
            deployment_id=deployment_id,
            client=client,
            only_children_of=only_children_of,
            search_term=search_term,
        )
    ).parsed
