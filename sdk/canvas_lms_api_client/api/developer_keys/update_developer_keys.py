from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_developer_keys_data_body import UpdateDeveloperKeysDataBody
from ...models.update_developer_keys_json_body import UpdateDeveloperKeysJsonBody
from ...models.update_developer_keys_response_200_item import UpdateDeveloperKeysResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: Union[
        UpdateDeveloperKeysJsonBody,
        UpdateDeveloperKeysDataBody,
    ],
    developer_keyauto_expire_tokens: Union[Unset, bool] = UNSET,
    developer_keyemail: Union[Unset, str] = UNSET,
    developer_keyicon_url: Union[Unset, str] = UNSET,
    developer_keyname: Union[Unset, str] = UNSET,
    developer_keynotes: Union[Unset, str] = UNSET,
    developer_keyredirect_uri: Union[Unset, str] = UNSET,
    developer_keyvendor_code: Union[Unset, str] = UNSET,
    developer_keyvisible: Union[Unset, bool] = UNSET,
    developer_keytest_cluster_only: Union[Unset, bool] = UNSET,
    developer_keyclient_credentials_audience: Union[Unset, str] = UNSET,
    developer_keyrequire_scopes: Union[Unset, bool] = UNSET,
    developer_keyallow_includes: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["developer_key[auto_expire_tokens]"] = developer_keyauto_expire_tokens

    params["developer_key[email]"] = developer_keyemail

    params["developer_key[icon_url]"] = developer_keyicon_url

    params["developer_key[name]"] = developer_keyname

    params["developer_key[notes]"] = developer_keynotes

    params["developer_key[redirect_uri]"] = developer_keyredirect_uri

    params["developer_key[vendor_code]"] = developer_keyvendor_code

    params["developer_key[visible]"] = developer_keyvisible

    params["developer_key[test_cluster_only]"] = developer_keytest_cluster_only

    params["developer_key[client_credentials_audience]"] = developer_keyclient_credentials_audience

    params["developer_key[require_scopes]"] = developer_keyrequire_scopes

    params["developer_key[allow_includes]"] = developer_keyallow_includes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/developer_keys/{id}",
        "params": params,
    }

    if isinstance(body, UpdateDeveloperKeysJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateDeveloperKeysDataBody):
        _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UpdateDeveloperKeysResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
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
        UpdateDeveloperKeysJsonBody,
        UpdateDeveloperKeysDataBody,
    ],
    developer_keyauto_expire_tokens: Union[Unset, bool] = UNSET,
    developer_keyemail: Union[Unset, str] = UNSET,
    developer_keyicon_url: Union[Unset, str] = UNSET,
    developer_keyname: Union[Unset, str] = UNSET,
    developer_keynotes: Union[Unset, str] = UNSET,
    developer_keyredirect_uri: Union[Unset, str] = UNSET,
    developer_keyvendor_code: Union[Unset, str] = UNSET,
    developer_keyvisible: Union[Unset, bool] = UNSET,
    developer_keytest_cluster_only: Union[Unset, bool] = UNSET,
    developer_keyclient_credentials_audience: Union[Unset, str] = UNSET,
    developer_keyrequire_scopes: Union[Unset, bool] = UNSET,
    developer_keyallow_includes: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
    """Update Developer_Keys

     Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should
    be done via the LTI Registration API.

    Required OAuth scope: url:PUT|/api/v1/developer_keys/:id

    Args:
        id (str):
        developer_keyauto_expire_tokens (Union[Unset, bool]):
        developer_keyemail (Union[Unset, str]):
        developer_keyicon_url (Union[Unset, str]):
        developer_keyname (Union[Unset, str]):
        developer_keynotes (Union[Unset, str]):
        developer_keyredirect_uri (Union[Unset, str]):
        developer_keyvendor_code (Union[Unset, str]):
        developer_keyvisible (Union[Unset, bool]):
        developer_keytest_cluster_only (Union[Unset, bool]):
        developer_keyclient_credentials_audience (Union[Unset, str]):
        developer_keyrequire_scopes (Union[Unset, bool]):
        developer_keyallow_includes (Union[Unset, bool]):
        body (UpdateDeveloperKeysJsonBody):
        body (UpdateDeveloperKeysDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateDeveloperKeysResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        developer_keyauto_expire_tokens=developer_keyauto_expire_tokens,
        developer_keyemail=developer_keyemail,
        developer_keyicon_url=developer_keyicon_url,
        developer_keyname=developer_keyname,
        developer_keynotes=developer_keynotes,
        developer_keyredirect_uri=developer_keyredirect_uri,
        developer_keyvendor_code=developer_keyvendor_code,
        developer_keyvisible=developer_keyvisible,
        developer_keytest_cluster_only=developer_keytest_cluster_only,
        developer_keyclient_credentials_audience=developer_keyclient_credentials_audience,
        developer_keyrequire_scopes=developer_keyrequire_scopes,
        developer_keyallow_includes=developer_keyallow_includes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDeveloperKeysJsonBody,
        UpdateDeveloperKeysDataBody,
    ],
    developer_keyauto_expire_tokens: Union[Unset, bool] = UNSET,
    developer_keyemail: Union[Unset, str] = UNSET,
    developer_keyicon_url: Union[Unset, str] = UNSET,
    developer_keyname: Union[Unset, str] = UNSET,
    developer_keynotes: Union[Unset, str] = UNSET,
    developer_keyredirect_uri: Union[Unset, str] = UNSET,
    developer_keyvendor_code: Union[Unset, str] = UNSET,
    developer_keyvisible: Union[Unset, bool] = UNSET,
    developer_keytest_cluster_only: Union[Unset, bool] = UNSET,
    developer_keyclient_credentials_audience: Union[Unset, str] = UNSET,
    developer_keyrequire_scopes: Union[Unset, bool] = UNSET,
    developer_keyallow_includes: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
    """Update Developer_Keys

     Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should
    be done via the LTI Registration API.

    Required OAuth scope: url:PUT|/api/v1/developer_keys/:id

    Args:
        id (str):
        developer_keyauto_expire_tokens (Union[Unset, bool]):
        developer_keyemail (Union[Unset, str]):
        developer_keyicon_url (Union[Unset, str]):
        developer_keyname (Union[Unset, str]):
        developer_keynotes (Union[Unset, str]):
        developer_keyredirect_uri (Union[Unset, str]):
        developer_keyvendor_code (Union[Unset, str]):
        developer_keyvisible (Union[Unset, bool]):
        developer_keytest_cluster_only (Union[Unset, bool]):
        developer_keyclient_credentials_audience (Union[Unset, str]):
        developer_keyrequire_scopes (Union[Unset, bool]):
        developer_keyallow_includes (Union[Unset, bool]):
        body (UpdateDeveloperKeysJsonBody):
        body (UpdateDeveloperKeysDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateDeveloperKeysResponse200Item']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        developer_keyauto_expire_tokens=developer_keyauto_expire_tokens,
        developer_keyemail=developer_keyemail,
        developer_keyicon_url=developer_keyicon_url,
        developer_keyname=developer_keyname,
        developer_keynotes=developer_keynotes,
        developer_keyredirect_uri=developer_keyredirect_uri,
        developer_keyvendor_code=developer_keyvendor_code,
        developer_keyvisible=developer_keyvisible,
        developer_keytest_cluster_only=developer_keytest_cluster_only,
        developer_keyclient_credentials_audience=developer_keyclient_credentials_audience,
        developer_keyrequire_scopes=developer_keyrequire_scopes,
        developer_keyallow_includes=developer_keyallow_includes,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDeveloperKeysJsonBody,
        UpdateDeveloperKeysDataBody,
    ],
    developer_keyauto_expire_tokens: Union[Unset, bool] = UNSET,
    developer_keyemail: Union[Unset, str] = UNSET,
    developer_keyicon_url: Union[Unset, str] = UNSET,
    developer_keyname: Union[Unset, str] = UNSET,
    developer_keynotes: Union[Unset, str] = UNSET,
    developer_keyredirect_uri: Union[Unset, str] = UNSET,
    developer_keyvendor_code: Union[Unset, str] = UNSET,
    developer_keyvisible: Union[Unset, bool] = UNSET,
    developer_keytest_cluster_only: Union[Unset, bool] = UNSET,
    developer_keyclient_credentials_audience: Union[Unset, str] = UNSET,
    developer_keyrequire_scopes: Union[Unset, bool] = UNSET,
    developer_keyallow_includes: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
    """Update Developer_Keys

     Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should
    be done via the LTI Registration API.

    Required OAuth scope: url:PUT|/api/v1/developer_keys/:id

    Args:
        id (str):
        developer_keyauto_expire_tokens (Union[Unset, bool]):
        developer_keyemail (Union[Unset, str]):
        developer_keyicon_url (Union[Unset, str]):
        developer_keyname (Union[Unset, str]):
        developer_keynotes (Union[Unset, str]):
        developer_keyredirect_uri (Union[Unset, str]):
        developer_keyvendor_code (Union[Unset, str]):
        developer_keyvisible (Union[Unset, bool]):
        developer_keytest_cluster_only (Union[Unset, bool]):
        developer_keyclient_credentials_audience (Union[Unset, str]):
        developer_keyrequire_scopes (Union[Unset, bool]):
        developer_keyallow_includes (Union[Unset, bool]):
        body (UpdateDeveloperKeysJsonBody):
        body (UpdateDeveloperKeysDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['UpdateDeveloperKeysResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        developer_keyauto_expire_tokens=developer_keyauto_expire_tokens,
        developer_keyemail=developer_keyemail,
        developer_keyicon_url=developer_keyicon_url,
        developer_keyname=developer_keyname,
        developer_keynotes=developer_keynotes,
        developer_keyredirect_uri=developer_keyredirect_uri,
        developer_keyvendor_code=developer_keyvendor_code,
        developer_keyvisible=developer_keyvisible,
        developer_keytest_cluster_only=developer_keytest_cluster_only,
        developer_keyclient_credentials_audience=developer_keyclient_credentials_audience,
        developer_keyrequire_scopes=developer_keyrequire_scopes,
        developer_keyallow_includes=developer_keyallow_includes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateDeveloperKeysJsonBody,
        UpdateDeveloperKeysDataBody,
    ],
    developer_keyauto_expire_tokens: Union[Unset, bool] = UNSET,
    developer_keyemail: Union[Unset, str] = UNSET,
    developer_keyicon_url: Union[Unset, str] = UNSET,
    developer_keyname: Union[Unset, str] = UNSET,
    developer_keynotes: Union[Unset, str] = UNSET,
    developer_keyredirect_uri: Union[Unset, str] = UNSET,
    developer_keyvendor_code: Union[Unset, str] = UNSET,
    developer_keyvisible: Union[Unset, bool] = UNSET,
    developer_keytest_cluster_only: Union[Unset, bool] = UNSET,
    developer_keyclient_credentials_audience: Union[Unset, str] = UNSET,
    developer_keyrequire_scopes: Union[Unset, bool] = UNSET,
    developer_keyallow_includes: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, list["UpdateDeveloperKeysResponse200Item"]]]:
    """Update Developer_Keys

     Update an existing Canvas API key. Updating an LTI 1.3 registration is not supported here and should
    be done via the LTI Registration API.

    Required OAuth scope: url:PUT|/api/v1/developer_keys/:id

    Args:
        id (str):
        developer_keyauto_expire_tokens (Union[Unset, bool]):
        developer_keyemail (Union[Unset, str]):
        developer_keyicon_url (Union[Unset, str]):
        developer_keyname (Union[Unset, str]):
        developer_keynotes (Union[Unset, str]):
        developer_keyredirect_uri (Union[Unset, str]):
        developer_keyvendor_code (Union[Unset, str]):
        developer_keyvisible (Union[Unset, bool]):
        developer_keytest_cluster_only (Union[Unset, bool]):
        developer_keyclient_credentials_audience (Union[Unset, str]):
        developer_keyrequire_scopes (Union[Unset, bool]):
        developer_keyallow_includes (Union[Unset, bool]):
        body (UpdateDeveloperKeysJsonBody):
        body (UpdateDeveloperKeysDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['UpdateDeveloperKeysResponse200Item']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            developer_keyauto_expire_tokens=developer_keyauto_expire_tokens,
            developer_keyemail=developer_keyemail,
            developer_keyicon_url=developer_keyicon_url,
            developer_keyname=developer_keyname,
            developer_keynotes=developer_keynotes,
            developer_keyredirect_uri=developer_keyredirect_uri,
            developer_keyvendor_code=developer_keyvendor_code,
            developer_keyvisible=developer_keyvisible,
            developer_keytest_cluster_only=developer_keytest_cluster_only,
            developer_keyclient_credentials_audience=developer_keyclient_credentials_audience,
            developer_keyrequire_scopes=developer_keyrequire_scopes,
            developer_keyallow_includes=developer_keyallow_includes,
        )
    ).parsed
