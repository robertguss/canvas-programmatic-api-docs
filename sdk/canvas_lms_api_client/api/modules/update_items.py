from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    module_id: str,
    id: str,
    *,
    module_itemtitle: Union[Unset, str] = UNSET,
    module_itemposition: Union[Unset, int] = UNSET,
    module_itemindent: Union[Unset, int] = UNSET,
    module_itemexternal_url: Union[Unset, str] = UNSET,
    module_itemnew_tab: Union[Unset, bool] = UNSET,
    module_itemcompletion_requirementtype: Union[Unset, str] = UNSET,
    module_itemcompletion_requirementmin_score: int,
    module_itempublished: Union[Unset, bool] = UNSET,
    module_itemmodule_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["module_item[title]"] = module_itemtitle

    params["module_item[position]"] = module_itemposition

    params["module_item[indent]"] = module_itemindent

    params["module_item[external_url]"] = module_itemexternal_url

    params["module_item[new_tab]"] = module_itemnew_tab

    params["module_item[completion_requirement][type]"] = module_itemcompletion_requirementtype

    params["module_item[completion_requirement][min_score]"] = module_itemcompletion_requirementmin_score

    params["module_item[published]"] = module_itempublished

    params["module_item[module_id]"] = module_itemmodule_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/api/v1/courses/{course_id}/modules/{module_id}/items/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
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
    module_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    module_itemtitle: Union[Unset, str] = UNSET,
    module_itemposition: Union[Unset, int] = UNSET,
    module_itemindent: Union[Unset, int] = UNSET,
    module_itemexternal_url: Union[Unset, str] = UNSET,
    module_itemnew_tab: Union[Unset, bool] = UNSET,
    module_itemcompletion_requirementtype: Union[Unset, str] = UNSET,
    module_itemcompletion_requirementmin_score: int,
    module_itempublished: Union[Unset, bool] = UNSET,
    module_itemmodule_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Items

     Update and return an existing module item

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:module_id/items/:id

    Args:
        course_id (str):
        module_id (str):
        id (str):
        module_itemtitle (Union[Unset, str]):
        module_itemposition (Union[Unset, int]):
        module_itemindent (Union[Unset, int]):
        module_itemexternal_url (Union[Unset, str]):
        module_itemnew_tab (Union[Unset, bool]):
        module_itemcompletion_requirementtype (Union[Unset, str]):
        module_itemcompletion_requirementmin_score (int):
        module_itempublished (Union[Unset, bool]):
        module_itemmodule_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        module_id=module_id,
        id=id,
        module_itemtitle=module_itemtitle,
        module_itemposition=module_itemposition,
        module_itemindent=module_itemindent,
        module_itemexternal_url=module_itemexternal_url,
        module_itemnew_tab=module_itemnew_tab,
        module_itemcompletion_requirementtype=module_itemcompletion_requirementtype,
        module_itemcompletion_requirementmin_score=module_itemcompletion_requirementmin_score,
        module_itempublished=module_itempublished,
        module_itemmodule_id=module_itemmodule_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    course_id: str,
    module_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    module_itemtitle: Union[Unset, str] = UNSET,
    module_itemposition: Union[Unset, int] = UNSET,
    module_itemindent: Union[Unset, int] = UNSET,
    module_itemexternal_url: Union[Unset, str] = UNSET,
    module_itemnew_tab: Union[Unset, bool] = UNSET,
    module_itemcompletion_requirementtype: Union[Unset, str] = UNSET,
    module_itemcompletion_requirementmin_score: int,
    module_itempublished: Union[Unset, bool] = UNSET,
    module_itemmodule_id: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Put Courses Items

     Update and return an existing module item

    Required OAuth scope: url:PUT|/api/v1/courses/:course_id/modules/:module_id/items/:id

    Args:
        course_id (str):
        module_id (str):
        id (str):
        module_itemtitle (Union[Unset, str]):
        module_itemposition (Union[Unset, int]):
        module_itemindent (Union[Unset, int]):
        module_itemexternal_url (Union[Unset, str]):
        module_itemnew_tab (Union[Unset, bool]):
        module_itemcompletion_requirementtype (Union[Unset, str]):
        module_itemcompletion_requirementmin_score (int):
        module_itempublished (Union[Unset, bool]):
        module_itemmodule_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        module_id=module_id,
        id=id,
        module_itemtitle=module_itemtitle,
        module_itemposition=module_itemposition,
        module_itemindent=module_itemindent,
        module_itemexternal_url=module_itemexternal_url,
        module_itemnew_tab=module_itemnew_tab,
        module_itemcompletion_requirementtype=module_itemcompletion_requirementtype,
        module_itemcompletion_requirementmin_score=module_itemcompletion_requirementmin_score,
        module_itempublished=module_itempublished,
        module_itemmodule_id=module_itemmodule_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
