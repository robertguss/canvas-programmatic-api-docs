from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_users_response_200 import UpdateUsersResponse200
from ...types import Response


def _get_kwargs(
    id: str,
    destination_account_id: str,
    destination_user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateUsersResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateUsersResponse200.from_dict(response.json())

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
) -> Response[Union[Any, UpdateUsersResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    destination_account_id: str,
    destination_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateUsersResponse200]]:
    r"""Put Users Users

     Merge a user into another user. To merge users, the caller must have permissions to manage both
    users. This should be considered irreversible. This will delete the user and move all the data into
    the destination user. User merge details and caveats: The from\_user is the user that was deleted in
    the user\_merge process. The destination\_user is the user that remains, that is being split.
    Avatars: When both users have avatars, only the destination\_users avatar will remain. When one user
    has an avatar, it will end up on the destination\_user. Terms of Use: If either user has accepted
    terms of use, it will be be left as accepted. Communication Channels: All unique communication
    channels moved to the destination\_user. All notification preferences are moved to the
    destination\_user. Enrollments: All unique enrollments are moved to the destination\_user. When
    there is an enrollment that would end up making it so that a user would be observing themselves, the
    enrollment is not moved over. Everything that is tied to the from\_user at the course level relating
    to the enrollment is also moved to the destination\_user. Submissions: All submissions are moved to
    the destination\_user. If there are enrollments for both users in the same course, we prefer
    submissions that have grades then submissions that have work in them, and if there are no grades or
    no work, they are not moved. Other notes: Access Tokens are moved on merge. Conversations are moved
    on merge. Favorites are moved on merge. Courses will commonly use LTI tools. LTI tools reference the
    user with IDs that are stored on a user object. Merging users deletes one user and moves all records
    from the deleted user to the destination\_user. These IDs are kept for all enrollments,
    group\_membership, and account\_users for the from\_user at the time of the merge. When the
    destination\_user launches an LTI tool from a course that used to be the from\_user’s, it doesn’t
    appear as a new user to the tool provider. Instead it will send the stored ids. The
    destination\_user’s LTI IDs remain as they were for the courses that they originally had. Future
    enrollments for the destination\_user will use the IDs that are on the destination\_user object. LTI
    IDs that are kept and tracked per context include lti\_context\_id, lti\_id and uuid. APIs that
    return the LTI ids will return the one for the context that it is called for, except for the user
    uuid. The user UUID will display the destination\_users uuid, and when getting the uuid from an api
    that is in a context that was recorded from a merge event, an additional attribute is added as
    past\_uuid. When finding users by SIS ids in different accounts the destination\_account\_id is
    required. The account can also be identified by passing the domain in destination\_account\_id.

    Required OAuth scope:
    url:PUT|/api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id

    Args:
        id (str):
        destination_account_id (str):
        destination_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateUsersResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        destination_account_id=destination_account_id,
        destination_user_id=destination_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    destination_account_id: str,
    destination_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateUsersResponse200]]:
    r"""Put Users Users

     Merge a user into another user. To merge users, the caller must have permissions to manage both
    users. This should be considered irreversible. This will delete the user and move all the data into
    the destination user. User merge details and caveats: The from\_user is the user that was deleted in
    the user\_merge process. The destination\_user is the user that remains, that is being split.
    Avatars: When both users have avatars, only the destination\_users avatar will remain. When one user
    has an avatar, it will end up on the destination\_user. Terms of Use: If either user has accepted
    terms of use, it will be be left as accepted. Communication Channels: All unique communication
    channels moved to the destination\_user. All notification preferences are moved to the
    destination\_user. Enrollments: All unique enrollments are moved to the destination\_user. When
    there is an enrollment that would end up making it so that a user would be observing themselves, the
    enrollment is not moved over. Everything that is tied to the from\_user at the course level relating
    to the enrollment is also moved to the destination\_user. Submissions: All submissions are moved to
    the destination\_user. If there are enrollments for both users in the same course, we prefer
    submissions that have grades then submissions that have work in them, and if there are no grades or
    no work, they are not moved. Other notes: Access Tokens are moved on merge. Conversations are moved
    on merge. Favorites are moved on merge. Courses will commonly use LTI tools. LTI tools reference the
    user with IDs that are stored on a user object. Merging users deletes one user and moves all records
    from the deleted user to the destination\_user. These IDs are kept for all enrollments,
    group\_membership, and account\_users for the from\_user at the time of the merge. When the
    destination\_user launches an LTI tool from a course that used to be the from\_user’s, it doesn’t
    appear as a new user to the tool provider. Instead it will send the stored ids. The
    destination\_user’s LTI IDs remain as they were for the courses that they originally had. Future
    enrollments for the destination\_user will use the IDs that are on the destination\_user object. LTI
    IDs that are kept and tracked per context include lti\_context\_id, lti\_id and uuid. APIs that
    return the LTI ids will return the one for the context that it is called for, except for the user
    uuid. The user UUID will display the destination\_users uuid, and when getting the uuid from an api
    that is in a context that was recorded from a merge event, an additional attribute is added as
    past\_uuid. When finding users by SIS ids in different accounts the destination\_account\_id is
    required. The account can also be identified by passing the domain in destination\_account\_id.

    Required OAuth scope:
    url:PUT|/api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id

    Args:
        id (str):
        destination_account_id (str):
        destination_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateUsersResponse200]
    """

    return sync_detailed(
        id=id,
        destination_account_id=destination_account_id,
        destination_user_id=destination_user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    destination_account_id: str,
    destination_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, UpdateUsersResponse200]]:
    r"""Put Users Users

     Merge a user into another user. To merge users, the caller must have permissions to manage both
    users. This should be considered irreversible. This will delete the user and move all the data into
    the destination user. User merge details and caveats: The from\_user is the user that was deleted in
    the user\_merge process. The destination\_user is the user that remains, that is being split.
    Avatars: When both users have avatars, only the destination\_users avatar will remain. When one user
    has an avatar, it will end up on the destination\_user. Terms of Use: If either user has accepted
    terms of use, it will be be left as accepted. Communication Channels: All unique communication
    channels moved to the destination\_user. All notification preferences are moved to the
    destination\_user. Enrollments: All unique enrollments are moved to the destination\_user. When
    there is an enrollment that would end up making it so that a user would be observing themselves, the
    enrollment is not moved over. Everything that is tied to the from\_user at the course level relating
    to the enrollment is also moved to the destination\_user. Submissions: All submissions are moved to
    the destination\_user. If there are enrollments for both users in the same course, we prefer
    submissions that have grades then submissions that have work in them, and if there are no grades or
    no work, they are not moved. Other notes: Access Tokens are moved on merge. Conversations are moved
    on merge. Favorites are moved on merge. Courses will commonly use LTI tools. LTI tools reference the
    user with IDs that are stored on a user object. Merging users deletes one user and moves all records
    from the deleted user to the destination\_user. These IDs are kept for all enrollments,
    group\_membership, and account\_users for the from\_user at the time of the merge. When the
    destination\_user launches an LTI tool from a course that used to be the from\_user’s, it doesn’t
    appear as a new user to the tool provider. Instead it will send the stored ids. The
    destination\_user’s LTI IDs remain as they were for the courses that they originally had. Future
    enrollments for the destination\_user will use the IDs that are on the destination\_user object. LTI
    IDs that are kept and tracked per context include lti\_context\_id, lti\_id and uuid. APIs that
    return the LTI ids will return the one for the context that it is called for, except for the user
    uuid. The user UUID will display the destination\_users uuid, and when getting the uuid from an api
    that is in a context that was recorded from a merge event, an additional attribute is added as
    past\_uuid. When finding users by SIS ids in different accounts the destination\_account\_id is
    required. The account can also be identified by passing the domain in destination\_account\_id.

    Required OAuth scope:
    url:PUT|/api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id

    Args:
        id (str):
        destination_account_id (str):
        destination_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateUsersResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        destination_account_id=destination_account_id,
        destination_user_id=destination_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    destination_account_id: str,
    destination_user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, UpdateUsersResponse200]]:
    r"""Put Users Users

     Merge a user into another user. To merge users, the caller must have permissions to manage both
    users. This should be considered irreversible. This will delete the user and move all the data into
    the destination user. User merge details and caveats: The from\_user is the user that was deleted in
    the user\_merge process. The destination\_user is the user that remains, that is being split.
    Avatars: When both users have avatars, only the destination\_users avatar will remain. When one user
    has an avatar, it will end up on the destination\_user. Terms of Use: If either user has accepted
    terms of use, it will be be left as accepted. Communication Channels: All unique communication
    channels moved to the destination\_user. All notification preferences are moved to the
    destination\_user. Enrollments: All unique enrollments are moved to the destination\_user. When
    there is an enrollment that would end up making it so that a user would be observing themselves, the
    enrollment is not moved over. Everything that is tied to the from\_user at the course level relating
    to the enrollment is also moved to the destination\_user. Submissions: All submissions are moved to
    the destination\_user. If there are enrollments for both users in the same course, we prefer
    submissions that have grades then submissions that have work in them, and if there are no grades or
    no work, they are not moved. Other notes: Access Tokens are moved on merge. Conversations are moved
    on merge. Favorites are moved on merge. Courses will commonly use LTI tools. LTI tools reference the
    user with IDs that are stored on a user object. Merging users deletes one user and moves all records
    from the deleted user to the destination\_user. These IDs are kept for all enrollments,
    group\_membership, and account\_users for the from\_user at the time of the merge. When the
    destination\_user launches an LTI tool from a course that used to be the from\_user’s, it doesn’t
    appear as a new user to the tool provider. Instead it will send the stored ids. The
    destination\_user’s LTI IDs remain as they were for the courses that they originally had. Future
    enrollments for the destination\_user will use the IDs that are on the destination\_user object. LTI
    IDs that are kept and tracked per context include lti\_context\_id, lti\_id and uuid. APIs that
    return the LTI ids will return the one for the context that it is called for, except for the user
    uuid. The user UUID will display the destination\_users uuid, and when getting the uuid from an api
    that is in a context that was recorded from a merge event, an additional attribute is added as
    past\_uuid. When finding users by SIS ids in different accounts the destination\_account\_id is
    required. The account can also be identified by passing the domain in destination\_account\_id.

    Required OAuth scope:
    url:PUT|/api/v1/users/:id/merge_into/accounts/:destination_account_id/users/:destination_user_id

    Args:
        id (str):
        destination_account_id (str):
        destination_user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateUsersResponse200]
    """

    return (
        await asyncio_detailed(
            id=id,
            destination_account_id=destination_account_id,
            destination_user_id=destination_user_id,
            client=client,
        )
    ).parsed
