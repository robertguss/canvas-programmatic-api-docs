from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    group_id: str,
    topic_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/api/v1/groups/{group_id}/discussion_topics/{topic_id}/view",
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
    group_id: str,
    topic_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Groups View

     Return a cached structure of the discussion topic, containing all entries, their authors, and their
    message bodies. May require (depending on the topic) that the user has posted in the topic. If it is
    required, and the user has not posted, will respond with a 403 Forbidden status and the body
    ‘require\_initial\_post’. In some rare situations, this cached structure may not be available yet.
    In that case, the server will respond with a 503 error, and the caller should try again soon. The
    response is an object containing the following keys: * “participants”: A list of summary information
    on users who have posted to the discussion. Each value is an object containing their id,
    display\_name, and avatar\_url. * “unread\_entries”: A list of entry ids that are unread by the
    current user. this implies that any entry not in this list is read. * “entry\_ratings”: A map of
    entry ids to ratings by the current user. Entries not in this list have no rating. Only populated if
    rating is enabled. * “forced\_entries”: A list of entry ids that have forced\_read\_state set to
    true. This flag is meant to indicate the entry’s read\_state has been manually set to ‘unread’ by
    the user, so the entry should not be automatically marked as read. * “view”: A threaded view of all
    the entries in the discussion, containing the id, user\_id, and message. * “new\_entries”: Because
    this view is eventually consistent, it’s possible that newly created or updated entries won’t yet be
    reflected in the view. If the application wants to also get a flat list of all entries not yet
    reflected in the view, pass include\_new\_entries=1 to the request and this array of entries will be
    returned. These entries are returned in a flat array, in ascending created\_at order.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/view

    Args:
        group_id (str):
        topic_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    group_id: str,
    topic_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Get Groups View

     Return a cached structure of the discussion topic, containing all entries, their authors, and their
    message bodies. May require (depending on the topic) that the user has posted in the topic. If it is
    required, and the user has not posted, will respond with a 403 Forbidden status and the body
    ‘require\_initial\_post’. In some rare situations, this cached structure may not be available yet.
    In that case, the server will respond with a 503 error, and the caller should try again soon. The
    response is an object containing the following keys: * “participants”: A list of summary information
    on users who have posted to the discussion. Each value is an object containing their id,
    display\_name, and avatar\_url. * “unread\_entries”: A list of entry ids that are unread by the
    current user. this implies that any entry not in this list is read. * “entry\_ratings”: A map of
    entry ids to ratings by the current user. Entries not in this list have no rating. Only populated if
    rating is enabled. * “forced\_entries”: A list of entry ids that have forced\_read\_state set to
    true. This flag is meant to indicate the entry’s read\_state has been manually set to ‘unread’ by
    the user, so the entry should not be automatically marked as read. * “view”: A threaded view of all
    the entries in the discussion, containing the id, user\_id, and message. * “new\_entries”: Because
    this view is eventually consistent, it’s possible that newly created or updated entries won’t yet be
    reflected in the view. If the application wants to also get a flat list of all entries not yet
    reflected in the view, pass include\_new\_entries=1 to the request and this array of entries will be
    returned. These entries are returned in a flat array, in ascending created\_at order.

    Required OAuth scope: url:GET|/api/v1/groups/:group_id/discussion_topics/:topic_id/view

    Args:
        group_id (str):
        topic_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        topic_id=topic_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
