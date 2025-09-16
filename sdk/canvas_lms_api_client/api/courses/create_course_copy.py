from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    *,
    source_course: Union[Unset, str] = UNSET,
    except_: Union[Unset, str] = UNSET,
    only: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["source_course"] = source_course

    params["except[]"] = except_

    params["only[]"] = only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/course_copy",
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
    course_id: str,
    *,
    client: AuthenticatedClient,
    source_course: Union[Unset, str] = UNSET,
    except_: Union[Unset, str] = UNSET,
    only: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Course_Copy

     DEPRECATED: Please use the [Content Migrations
    API](../content_migrations#method.content_migrations.create) Copies content from one course into
    another. The default is to copy all course content. You can control specific types to copy by using
    either the ‘except’ option or the ‘only’ option. The response is the same as the course copy status
    endpoint

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/course_copy

    Args:
        course_id (str):
        source_course (Union[Unset, str]):
        except_ (Union[Unset, str]):
        only (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        source_course=source_course,
        except_=except_,
        only=only,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    *,
    client: AuthenticatedClient,
    source_course: Union[Unset, str] = UNSET,
    except_: Union[Unset, str] = UNSET,
    only: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Post Courses Course_Copy

     DEPRECATED: Please use the [Content Migrations
    API](../content_migrations#method.content_migrations.create) Copies content from one course into
    another. The default is to copy all course content. You can control specific types to copy by using
    either the ‘except’ option or the ‘only’ option. The response is the same as the course copy status
    endpoint

    Required OAuth scope: url:POST|/api/v1/courses/:course_id/course_copy

    Args:
        course_id (str):
        source_course (Union[Unset, str]):
        except_ (Union[Unset, str]):
        only (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        source_course=source_course,
        except_=except_,
        only=only,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
