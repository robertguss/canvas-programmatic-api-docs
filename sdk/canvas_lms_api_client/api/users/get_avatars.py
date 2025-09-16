from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_avatars_response_200_item import GetAvatarsResponse200Item
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/users/{user_id}/avatars",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["GetAvatarsResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetAvatarsResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["GetAvatarsResponse200Item"]]]:
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
) -> Response[Union[Any, list["GetAvatarsResponse200Item"]]]:
    r"""Get Users Avatars

     A paginated list of the possible user avatar options that can be set with the user update endpoint.
    The response will be an array of avatar records. If the ‘type’ field is ‘attachment’, the record
    will include all the normal attachment json fields; otherwise it will include only the ‘url’ and
    ‘display\_name’ fields. Additionally, all records will include a ‘type’ field and a ‘token’ field.
    The following explains each field in more detail *   type “gravatar”|“attachment”|“no\_pic” The type
    of avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of
    avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of avatar
    record, for categorization purposes. url The url of the avatar token A unique representation of the
    avatar record which can be used to set the avatar with the user update endpoint. Note: this is an
    internal representation and is subject to change without notice. It should be consumed with this api
    endpoint and used in the user update endpoint, and should not be constructed by the client.
    display\_name A textual description of the avatar record id *   ‘attachment’ type only the internal
    id of the attachment content-type *   ‘attachment’ type only the content-type of the attachment
    filename *   ‘attachment’ type only the filename of the attachment size *   ‘attachment’ type only
    the size of the attachment

    Required OAuth scope: url:GET|/api/v1/users/:user_id/avatars

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetAvatarsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetAvatarsResponse200Item"]]]:
    r"""Get Users Avatars

     A paginated list of the possible user avatar options that can be set with the user update endpoint.
    The response will be an array of avatar records. If the ‘type’ field is ‘attachment’, the record
    will include all the normal attachment json fields; otherwise it will include only the ‘url’ and
    ‘display\_name’ fields. Additionally, all records will include a ‘type’ field and a ‘token’ field.
    The following explains each field in more detail *   type “gravatar”|“attachment”|“no\_pic” The type
    of avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of
    avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of avatar
    record, for categorization purposes. url The url of the avatar token A unique representation of the
    avatar record which can be used to set the avatar with the user update endpoint. Note: this is an
    internal representation and is subject to change without notice. It should be consumed with this api
    endpoint and used in the user update endpoint, and should not be constructed by the client.
    display\_name A textual description of the avatar record id *   ‘attachment’ type only the internal
    id of the attachment content-type *   ‘attachment’ type only the content-type of the attachment
    filename *   ‘attachment’ type only the filename of the attachment size *   ‘attachment’ type only
    the size of the attachment

    Required OAuth scope: url:GET|/api/v1/users/:user_id/avatars

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetAvatarsResponse200Item']]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["GetAvatarsResponse200Item"]]]:
    r"""Get Users Avatars

     A paginated list of the possible user avatar options that can be set with the user update endpoint.
    The response will be an array of avatar records. If the ‘type’ field is ‘attachment’, the record
    will include all the normal attachment json fields; otherwise it will include only the ‘url’ and
    ‘display\_name’ fields. Additionally, all records will include a ‘type’ field and a ‘token’ field.
    The following explains each field in more detail *   type “gravatar”|“attachment”|“no\_pic” The type
    of avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of
    avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of avatar
    record, for categorization purposes. url The url of the avatar token A unique representation of the
    avatar record which can be used to set the avatar with the user update endpoint. Note: this is an
    internal representation and is subject to change without notice. It should be consumed with this api
    endpoint and used in the user update endpoint, and should not be constructed by the client.
    display\_name A textual description of the avatar record id *   ‘attachment’ type only the internal
    id of the attachment content-type *   ‘attachment’ type only the content-type of the attachment
    filename *   ‘attachment’ type only the filename of the attachment size *   ‘attachment’ type only
    the size of the attachment

    Required OAuth scope: url:GET|/api/v1/users/:user_id/avatars

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['GetAvatarsResponse200Item']]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["GetAvatarsResponse200Item"]]]:
    r"""Get Users Avatars

     A paginated list of the possible user avatar options that can be set with the user update endpoint.
    The response will be an array of avatar records. If the ‘type’ field is ‘attachment’, the record
    will include all the normal attachment json fields; otherwise it will include only the ‘url’ and
    ‘display\_name’ fields. Additionally, all records will include a ‘type’ field and a ‘token’ field.
    The following explains each field in more detail *   type “gravatar”|“attachment”|“no\_pic” The type
    of avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of
    avatar record, for categorization purposes. *   “gravatar”|“attachment”|“no\_pic” The type of avatar
    record, for categorization purposes. url The url of the avatar token A unique representation of the
    avatar record which can be used to set the avatar with the user update endpoint. Note: this is an
    internal representation and is subject to change without notice. It should be consumed with this api
    endpoint and used in the user update endpoint, and should not be constructed by the client.
    display\_name A textual description of the avatar record id *   ‘attachment’ type only the internal
    id of the attachment content-type *   ‘attachment’ type only the content-type of the attachment
    filename *   ‘attachment’ type only the filename of the attachment size *   ‘attachment’ type only
    the size of the attachment

    Required OAuth scope: url:GET|/api/v1/users/:user_id/avatars

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['GetAvatarsResponse200Item']]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
