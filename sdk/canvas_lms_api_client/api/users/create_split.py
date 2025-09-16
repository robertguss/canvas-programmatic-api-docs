from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_split_response_200_item import CreateSplitResponse200Item
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/users/{id}/split",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CreateSplitResponse200Item"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CreateSplitResponse200Item.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CreateSplitResponse200Item"]]]:
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
) -> Response[Union[Any, list["CreateSplitResponse200Item"]]]:
    r"""Post Users Split

     Merged users cannot be fully restored to their previous state, but this will attempt to split as
    much as possible to the previous state. To split a merged user, the caller must have permissions to
    manage all of the users logins. If there are multiple users that have been merged into one user it
    will split each merge into a separate user. A split can only happen within 180 days of a user merge.
    A user merge deletes the previous user and may be permanently deleted. In this scenario we create a
    new user object and proceed to move as much as possible to the new user. The user object will not
    have preserved the name or settings from the previous user. Some items may have been deleted during
    a user\_merge that cannot be restored, and/or the data has become stale because of other changes to
    the objects since the time of the user\_merge. Split users details and caveats: The from\_user is
    the user that was deleted in the user\_merge process. The destination\_user is the user that
    remains, that is being split. Avatars: When both users had avatars, both will be remain. When
    from\_user had an avatar and destination\_user did not have an avatar, the destination\_user’s
    avatar will be deleted if it still matches what was there are the time of the merge. If the
    destination\_user’s avatar was changed at anytime after the merge, it will remain on the destination
    user. If the from\_user had an avatar it will be there after split. Terms of Use: If from\_user had
    not accepted terms of use, they will be prompted again to accept terms of use after the split. If
    the destination\_user had not accepted terms of use, hey will be prompted again to accept terms of
    use after the split. If neither user had accepted the terms of use, but since the time of the merge
    had accepted, both will be prompted to accept terms of use. If both had accepted terms of use, this
    will remain. Communication Channels: All communication channels are restored to what they were prior
    to the merge. If a communication channel was added after the merge, it will remain on the
    destination\_user. Notification preferences remain with the communication channels. Enrollments: All
    enrollments from the time of the merge will be moved back to where they were. Enrollments created
    since the time of the merge that were created by sis\_import will go to the user that owns that
    sis\_id used for the import. Other new enrollments will remain on the destination\_user. Everything
    that is tied to the destination\_user at the course level relating to an enrollment is moved to the
    from\_user. When both users are in the same course prior to merge this can cause some unexpected
    items to move. Submissions: Unlike other items tied to a course, submissions are explicitly recorded
    to avoid problems with grades. All submissions were moved are restored to the spot prior to merge.
    All submission that were created in a course that was moved in enrollments are moved over to the
    from\_user. Other notes: Access Tokens are moved back on split. Conversations are moved back on
    split. Favorites that existing at the time of merge are moved back on split. LTI ids are restored to
    how they were prior to merge.

    Required OAuth scope: url:POST|/api/v1/users/:id/split

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateSplitResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["CreateSplitResponse200Item"]]]:
    r"""Post Users Split

     Merged users cannot be fully restored to their previous state, but this will attempt to split as
    much as possible to the previous state. To split a merged user, the caller must have permissions to
    manage all of the users logins. If there are multiple users that have been merged into one user it
    will split each merge into a separate user. A split can only happen within 180 days of a user merge.
    A user merge deletes the previous user and may be permanently deleted. In this scenario we create a
    new user object and proceed to move as much as possible to the new user. The user object will not
    have preserved the name or settings from the previous user. Some items may have been deleted during
    a user\_merge that cannot be restored, and/or the data has become stale because of other changes to
    the objects since the time of the user\_merge. Split users details and caveats: The from\_user is
    the user that was deleted in the user\_merge process. The destination\_user is the user that
    remains, that is being split. Avatars: When both users had avatars, both will be remain. When
    from\_user had an avatar and destination\_user did not have an avatar, the destination\_user’s
    avatar will be deleted if it still matches what was there are the time of the merge. If the
    destination\_user’s avatar was changed at anytime after the merge, it will remain on the destination
    user. If the from\_user had an avatar it will be there after split. Terms of Use: If from\_user had
    not accepted terms of use, they will be prompted again to accept terms of use after the split. If
    the destination\_user had not accepted terms of use, hey will be prompted again to accept terms of
    use after the split. If neither user had accepted the terms of use, but since the time of the merge
    had accepted, both will be prompted to accept terms of use. If both had accepted terms of use, this
    will remain. Communication Channels: All communication channels are restored to what they were prior
    to the merge. If a communication channel was added after the merge, it will remain on the
    destination\_user. Notification preferences remain with the communication channels. Enrollments: All
    enrollments from the time of the merge will be moved back to where they were. Enrollments created
    since the time of the merge that were created by sis\_import will go to the user that owns that
    sis\_id used for the import. Other new enrollments will remain on the destination\_user. Everything
    that is tied to the destination\_user at the course level relating to an enrollment is moved to the
    from\_user. When both users are in the same course prior to merge this can cause some unexpected
    items to move. Submissions: Unlike other items tied to a course, submissions are explicitly recorded
    to avoid problems with grades. All submissions were moved are restored to the spot prior to merge.
    All submission that were created in a course that was moved in enrollments are moved over to the
    from\_user. Other notes: Access Tokens are moved back on split. Conversations are moved back on
    split. Favorites that existing at the time of merge are moved back on split. LTI ids are restored to
    how they were prior to merge.

    Required OAuth scope: url:POST|/api/v1/users/:id/split

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateSplitResponse200Item']]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, list["CreateSplitResponse200Item"]]]:
    r"""Post Users Split

     Merged users cannot be fully restored to their previous state, but this will attempt to split as
    much as possible to the previous state. To split a merged user, the caller must have permissions to
    manage all of the users logins. If there are multiple users that have been merged into one user it
    will split each merge into a separate user. A split can only happen within 180 days of a user merge.
    A user merge deletes the previous user and may be permanently deleted. In this scenario we create a
    new user object and proceed to move as much as possible to the new user. The user object will not
    have preserved the name or settings from the previous user. Some items may have been deleted during
    a user\_merge that cannot be restored, and/or the data has become stale because of other changes to
    the objects since the time of the user\_merge. Split users details and caveats: The from\_user is
    the user that was deleted in the user\_merge process. The destination\_user is the user that
    remains, that is being split. Avatars: When both users had avatars, both will be remain. When
    from\_user had an avatar and destination\_user did not have an avatar, the destination\_user’s
    avatar will be deleted if it still matches what was there are the time of the merge. If the
    destination\_user’s avatar was changed at anytime after the merge, it will remain on the destination
    user. If the from\_user had an avatar it will be there after split. Terms of Use: If from\_user had
    not accepted terms of use, they will be prompted again to accept terms of use after the split. If
    the destination\_user had not accepted terms of use, hey will be prompted again to accept terms of
    use after the split. If neither user had accepted the terms of use, but since the time of the merge
    had accepted, both will be prompted to accept terms of use. If both had accepted terms of use, this
    will remain. Communication Channels: All communication channels are restored to what they were prior
    to the merge. If a communication channel was added after the merge, it will remain on the
    destination\_user. Notification preferences remain with the communication channels. Enrollments: All
    enrollments from the time of the merge will be moved back to where they were. Enrollments created
    since the time of the merge that were created by sis\_import will go to the user that owns that
    sis\_id used for the import. Other new enrollments will remain on the destination\_user. Everything
    that is tied to the destination\_user at the course level relating to an enrollment is moved to the
    from\_user. When both users are in the same course prior to merge this can cause some unexpected
    items to move. Submissions: Unlike other items tied to a course, submissions are explicitly recorded
    to avoid problems with grades. All submissions were moved are restored to the spot prior to merge.
    All submission that were created in a course that was moved in enrollments are moved over to the
    from\_user. Other notes: Access Tokens are moved back on split. Conversations are moved back on
    split. Favorites that existing at the time of merge are moved back on split. LTI ids are restored to
    how they were prior to merge.

    Required OAuth scope: url:POST|/api/v1/users/:id/split

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CreateSplitResponse200Item']]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, list["CreateSplitResponse200Item"]]]:
    r"""Post Users Split

     Merged users cannot be fully restored to their previous state, but this will attempt to split as
    much as possible to the previous state. To split a merged user, the caller must have permissions to
    manage all of the users logins. If there are multiple users that have been merged into one user it
    will split each merge into a separate user. A split can only happen within 180 days of a user merge.
    A user merge deletes the previous user and may be permanently deleted. In this scenario we create a
    new user object and proceed to move as much as possible to the new user. The user object will not
    have preserved the name or settings from the previous user. Some items may have been deleted during
    a user\_merge that cannot be restored, and/or the data has become stale because of other changes to
    the objects since the time of the user\_merge. Split users details and caveats: The from\_user is
    the user that was deleted in the user\_merge process. The destination\_user is the user that
    remains, that is being split. Avatars: When both users had avatars, both will be remain. When
    from\_user had an avatar and destination\_user did not have an avatar, the destination\_user’s
    avatar will be deleted if it still matches what was there are the time of the merge. If the
    destination\_user’s avatar was changed at anytime after the merge, it will remain on the destination
    user. If the from\_user had an avatar it will be there after split. Terms of Use: If from\_user had
    not accepted terms of use, they will be prompted again to accept terms of use after the split. If
    the destination\_user had not accepted terms of use, hey will be prompted again to accept terms of
    use after the split. If neither user had accepted the terms of use, but since the time of the merge
    had accepted, both will be prompted to accept terms of use. If both had accepted terms of use, this
    will remain. Communication Channels: All communication channels are restored to what they were prior
    to the merge. If a communication channel was added after the merge, it will remain on the
    destination\_user. Notification preferences remain with the communication channels. Enrollments: All
    enrollments from the time of the merge will be moved back to where they were. Enrollments created
    since the time of the merge that were created by sis\_import will go to the user that owns that
    sis\_id used for the import. Other new enrollments will remain on the destination\_user. Everything
    that is tied to the destination\_user at the course level relating to an enrollment is moved to the
    from\_user. When both users are in the same course prior to merge this can cause some unexpected
    items to move. Submissions: Unlike other items tied to a course, submissions are explicitly recorded
    to avoid problems with grades. All submissions were moved are restored to the spot prior to merge.
    All submission that were created in a course that was moved in enrollments are moved over to the
    from\_user. Other notes: Access Tokens are moved back on split. Conversations are moved back on
    split. Favorites that existing at the time of merge are moved back on split. LTI ids are restored to
    how they were prior to merge.

    Required OAuth scope: url:POST|/api/v1/users/:id/split

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CreateSplitResponse200Item']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
