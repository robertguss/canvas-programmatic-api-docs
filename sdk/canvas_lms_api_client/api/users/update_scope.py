from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_scope_data_body import UpdateScopeDataBody
from ...models.update_scope_json_body import UpdateScopeJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: Union[
        UpdateScopeJsonBody,
        UpdateScopeDataBody,
    ],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{user_id}/custom_data(/*scope)",
    }

    if isinstance(body, UpdateScopeJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, UpdateScopeDataBody):
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
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateScopeJsonBody,
        UpdateScopeDataBody,
    ],
) -> Response[Any]:
    r""" Put Users *Scope)

     Store arbitrary user data as JSON. Arbitrary JSON data can be stored for a User. A typical scenario
    would be an external site/service that registers users in Canvas and wants to capture additional
    info about them. The part of the URL that follows `/custom_data/` defines the scope of the request,
    and it reflects the structure of the JSON data to be stored or retrieved. The value `self` may be
    used for `user_id` to store data associated with the calling user. In order to access another user’s
    custom data, you must be an account administrator with permission to manage users. A namespace
    parameter, `ns`, is used to prevent custom\_data collisions between different apps. This parameter
    is required for all custom\_data requests. A request with Content-Type multipart/form-data or
    Content-Type application/x-www-form-urlencoded can only be used to store strings. Example PUT with
    multipart/form-data data: ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
    -X PUT \ -F 'ns=com.my-organization.canvas-app' \ -F 'data=555-1234' \ -H 'Authorization: Bearer
    <token>' ``` Response: ``` { \"data\": \"555-1234\" } ``` Subscopes (or, generated scopes) can also
    be specified by passing values to `data`\[`subscope`]. Example PUT specifying subscopes: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \ -X PUT \ -F 'ns=com.my-
    organization.canvas-app' \ -F 'data[waist]=32in' \ -F 'data[inseam]=34in' \ -F 'data[chest]=40in' \
    -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"chest\": \"40in\", \"waist\":
    \"32in\", \"inseam\": \"34in\" } } ``` Following such a request, subsets of the stored data to be
    retrieved directly from a subscope. Example [GET](#method.users.get_custom_data) from a generated
    scope ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \ -X
    GET \ -F 'ns=com.my-organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ```
    { \"data\": \"40in\" } ``` If you want to store more than just strings (i.e. numbers, arrays,
    hashes, true, false, and/or null), you must make a request with Content-Type application/json as in
    the following example. Example PUT with JSON data: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -H 'Content-Type: application/json' \ -X PUT
    \ -d '{ \"ns\": \"com.my-organization.canvas-app\", \"data\": { \"a-number\": 6.02e23, \"a-bool\":
    true, \"a-string\": \"true\", \"a-hash\": {\"a\": {\"b\": \"ohai\"}}, \"an-array\": [1, \"two\",
    null, false] } }' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"a-number\":
    6.02e+23, \"a-bool\": true, \"a-string\": \"true\", \"a-hash\": { \"a\": { \"b\": \"ohai\" } },
    \"an-array\": [1, \"two\", null, false] } } ``` If the data is an Object (as it is in the above
    example), then subsets of the data can be accessed by including the object’s (possibly nested) keys
    in the scope of a GET request. Example [GET](#method.users.get_custom_data) with a generated scope:
    ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \ -X GET \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": \"ohai\"
    } ``` On success, this endpoint returns an object containing the data that was stored. Responds with
    status code 200 if the scope already contained data, and it was overwritten by the data specified in
    the request. Responds with status code 201 if the scope was previously empty, and the data specified
    in the request was successfully stored there. Responds with status code 400 if the namespace
    parameter, `ns`, is missing or invalid, or if the `data` parameter is missing. Responds with status
    code 409 if the requested scope caused a conflict and data was not stored. This happens when storing
    data at the requested scope would cause data at an outer scope to be lost. e.g., if `/custom_data`
    was {“fashion\_app”: {“hair”: “blonde”\}}, but you tried to ‘PUT
    /custom\_data/fashion\_app/hair/style -F data=buzz\`, then for the request to succeed,the value of
    `/custom_data/fashion_app/hair` would have to become a hash, and its old string value would be lost.
    In this situation, an error object is returned with the following format: ``` { \"message\": \"write
    conflict for custom_data hash\", \"conflict_scope\": \"fashion_app/hair\", \"type_at_conflict\":
    \"String\", \"value_at_conflict\": \"blonde\" } ```

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/custom_data(/*scope)

    Args:
        user_id (str):
        body (UpdateScopeJsonBody):
        body (UpdateScopeDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: Union[
        UpdateScopeJsonBody,
        UpdateScopeDataBody,
    ],
) -> Response[Any]:
    r""" Put Users *Scope)

     Store arbitrary user data as JSON. Arbitrary JSON data can be stored for a User. A typical scenario
    would be an external site/service that registers users in Canvas and wants to capture additional
    info about them. The part of the URL that follows `/custom_data/` defines the scope of the request,
    and it reflects the structure of the JSON data to be stored or retrieved. The value `self` may be
    used for `user_id` to store data associated with the calling user. In order to access another user’s
    custom data, you must be an account administrator with permission to manage users. A namespace
    parameter, `ns`, is used to prevent custom\_data collisions between different apps. This parameter
    is required for all custom\_data requests. A request with Content-Type multipart/form-data or
    Content-Type application/x-www-form-urlencoded can only be used to store strings. Example PUT with
    multipart/form-data data: ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
    -X PUT \ -F 'ns=com.my-organization.canvas-app' \ -F 'data=555-1234' \ -H 'Authorization: Bearer
    <token>' ``` Response: ``` { \"data\": \"555-1234\" } ``` Subscopes (or, generated scopes) can also
    be specified by passing values to `data`\[`subscope`]. Example PUT specifying subscopes: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \ -X PUT \ -F 'ns=com.my-
    organization.canvas-app' \ -F 'data[waist]=32in' \ -F 'data[inseam]=34in' \ -F 'data[chest]=40in' \
    -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"chest\": \"40in\", \"waist\":
    \"32in\", \"inseam\": \"34in\" } } ``` Following such a request, subsets of the stored data to be
    retrieved directly from a subscope. Example [GET](#method.users.get_custom_data) from a generated
    scope ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \ -X
    GET \ -F 'ns=com.my-organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ```
    { \"data\": \"40in\" } ``` If you want to store more than just strings (i.e. numbers, arrays,
    hashes, true, false, and/or null), you must make a request with Content-Type application/json as in
    the following example. Example PUT with JSON data: ``` curl
    'https://<canvas>/api/v1/users/<user_id>/custom_data' \ -H 'Content-Type: application/json' \ -X PUT
    \ -d '{ \"ns\": \"com.my-organization.canvas-app\", \"data\": { \"a-number\": 6.02e23, \"a-bool\":
    true, \"a-string\": \"true\", \"a-hash\": {\"a\": {\"b\": \"ohai\"}}, \"an-array\": [1, \"two\",
    null, false] } }' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": { \"a-number\":
    6.02e+23, \"a-bool\": true, \"a-string\": \"true\", \"a-hash\": { \"a\": { \"b\": \"ohai\" } },
    \"an-array\": [1, \"two\", null, false] } } ``` If the data is an Object (as it is in the above
    example), then subsets of the data can be accessed by including the object’s (possibly nested) keys
    in the scope of a GET request. Example [GET](#method.users.get_custom_data) with a generated scope:
    ``` curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \ -X GET \ -F 'ns=com.my-
    organization.canvas-app' \ -H 'Authorization: Bearer <token>' ``` Response: ``` { \"data\": \"ohai\"
    } ``` On success, this endpoint returns an object containing the data that was stored. Responds with
    status code 200 if the scope already contained data, and it was overwritten by the data specified in
    the request. Responds with status code 201 if the scope was previously empty, and the data specified
    in the request was successfully stored there. Responds with status code 400 if the namespace
    parameter, `ns`, is missing or invalid, or if the `data` parameter is missing. Responds with status
    code 409 if the requested scope caused a conflict and data was not stored. This happens when storing
    data at the requested scope would cause data at an outer scope to be lost. e.g., if `/custom_data`
    was {“fashion\_app”: {“hair”: “blonde”\}}, but you tried to ‘PUT
    /custom\_data/fashion\_app/hair/style -F data=buzz\`, then for the request to succeed,the value of
    `/custom_data/fashion_app/hair` would have to become a hash, and its old string value would be lost.
    In this situation, an error object is returned with the following format: ``` { \"message\": \"write
    conflict for custom_data hash\", \"conflict_scope\": \"fashion_app/hair\", \"type_at_conflict\":
    \"String\", \"value_at_conflict\": \"blonde\" } ```

    Required OAuth scope: url:PUT|/api/v1/users/:user_id/custom_data(/*scope)

    Args:
        user_id (str):
        body (UpdateScopeJsonBody):
        body (UpdateScopeDataBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
