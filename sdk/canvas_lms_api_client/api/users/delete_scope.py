from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    ns: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["ns"] = ns

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v1/users/{user_id}/custom_data(/*scope)",
        "params": params,
    }

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
    user_id: str,
    *,
    client: AuthenticatedClient,
    ns: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Delete Users *Scope)

     Delete custom user data. Arbitrary JSON data can be stored for a User. This API call deletes that
    data for a given scope. Without a scope, all custom\_data is deleted. See [Store Custom
    Data](#method.users.set_custom_data) for details and examples of storage and retrieval. As an
    example, we’ll store some data, then delete a subset of it. Example
    [PUT](#method.users.set_custom_data) with valid JSON data: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X PUT \ -F 'ns=com.my-organization.canvas-
    app' \ -F 'data[fruit][apple]=so tasty' \ -F 'data[fruit][kiwi]=a bit sour' \ -F
    'data[veggies][root][onion]=tear-jerking' \ -H 'Authorization: Bearer <token>' ``` Response: ``` {
    \"data\": { \"fruit\": { \"apple\": \"so tasty\", \"kiwi\": \"a bit sour\" }, \"veggies\": {
    \"root\": { \"onion\": \"tear-jerking\" } } } } ``` Example DELETE: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \ -X DELETE \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": \"a bit
    sour\" } ``` Example [GET](#method.users.get_custom_data) following the above DELETE: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X GET \ -F 'ns=com.my-organization.canvas-
    app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"fruit\": { \"apple\":
    \"so tasty\" }, \"veggies\": { \"root\": { \"onion\": \"tear-jerking\" } } } } ``` Note that hashes
    left empty after a DELETE will get removed from the custom\_data store. For example, following the
    previous commands, if we delete /custom\_data/veggies/root/onion, then the entire
    /custom\_data/veggies scope will be removed. Example DELETE that empties a parent scope: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \ -X DELETE \ -F
    'ns=com.my-organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` {
    \"data\": \"tear-jerking\" } ``` Example [GET](#method.users.get_custom_data) following the above
    DELETE: ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X GET \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": {
    \"fruit\": { \"apple\": \"so tasty\" } } } ``` On success, this endpoint returns an object
    containing the data that was deleted. Responds with status code 400 if the namespace parameter,
    `ns`, is missing or invalid, or if the specified scope does not contain any data.

    Required OAuth scope: url:DELETE|/api/v1/users/:user_id/custom_data(/*scope)

    Args:
        user_id (str):
        ns (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        ns=ns,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    ns: Union[Unset, str] = UNSET,
) -> Response[Any]:
    r"""Delete Users *Scope)

     Delete custom user data. Arbitrary JSON data can be stored for a User. This API call deletes that
    data for a given scope. Without a scope, all custom\_data is deleted. See [Store Custom
    Data](#method.users.set_custom_data) for details and examples of storage and retrieval. As an
    example, we’ll store some data, then delete a subset of it. Example
    [PUT](#method.users.set_custom_data) with valid JSON data: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X PUT \ -F 'ns=com.my-organization.canvas-
    app' \ -F 'data[fruit][apple]=so tasty' \ -F 'data[fruit][kiwi]=a bit sour' \ -F
    'data[veggies][root][onion]=tear-jerking' \ -H 'Authorization: Bearer <token>' ``` Response: ``` {
    \"data\": { \"fruit\": { \"apple\": \"so tasty\", \"kiwi\": \"a bit sour\" }, \"veggies\": {
    \"root\": { \"onion\": \"tear-jerking\" } } } } ``` Example DELETE: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \ -X DELETE \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": \"a bit
    sour\" } ``` Example [GET](#method.users.get_custom_data) following the above DELETE: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X GET \ -F 'ns=com.my-organization.canvas-
    app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"fruit\": { \"apple\":
    \"so tasty\" }, \"veggies\": { \"root\": { \"onion\": \"tear-jerking\" } } } } ``` Note that hashes
    left empty after a DELETE will get removed from the custom\_data store. For example, following the
    previous commands, if we delete /custom\_data/veggies/root/onion, then the entire
    /custom\_data/veggies scope will be removed. Example DELETE that empties a parent scope: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \ -X DELETE \ -F
    'ns=com.my-organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` {
    \"data\": \"tear-jerking\" } ``` Example [GET](#method.users.get_custom_data) following the above
    DELETE: ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -X GET \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": {
    \"fruit\": { \"apple\": \"so tasty\" } } } ``` On success, this endpoint returns an object
    containing the data that was deleted. Responds with status code 400 if the namespace parameter,
    `ns`, is missing or invalid, or if the specified scope does not contain any data.

    Required OAuth scope: url:DELETE|/api/v1/users/:user_id/custom_data(/*scope)

    Args:
        user_id (str):
        ns (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        ns=ns,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
