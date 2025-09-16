from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_group_response_200 import CreateGroupResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    course_id: str,
    learning_outcome_group_id: str,
    *,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["import_type"] = import_type

    params["attachment"] = attachment

    params["extension"] = extension

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/courses/{course_id}/outcome_imports(/group/{learning_outcome_group_id})",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreateGroupResponse200]]:
    if response.status_code == 200:
        response_200 = CreateGroupResponse200.from_dict(response.json())

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
) -> Response[Union[Any, CreateGroupResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course_id: str,
    learning_outcome_group_id: str,
    *,
    client: AuthenticatedClient,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateGroupResponse200]]:
    """Post Courses Group

     Import outcomes into Canvas. For more information on the format that’s expected here, please see the
    “Outcomes CSV” section in the API docs.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)

    Args:
        course_id (str):
        learning_outcome_group_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        learning_outcome_group_id=learning_outcome_group_id,
        import_type=import_type,
        attachment=attachment,
        extension=extension,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course_id: str,
    learning_outcome_group_id: str,
    *,
    client: AuthenticatedClient,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateGroupResponse200]]:
    """Post Courses Group

     Import outcomes into Canvas. For more information on the format that’s expected here, please see the
    “Outcomes CSV” section in the API docs.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)

    Args:
        course_id (str):
        learning_outcome_group_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupResponse200]
    """

    return sync_detailed(
        course_id=course_id,
        learning_outcome_group_id=learning_outcome_group_id,
        client=client,
        import_type=import_type,
        attachment=attachment,
        extension=extension,
    ).parsed


async def asyncio_detailed(
    course_id: str,
    learning_outcome_group_id: str,
    *,
    client: AuthenticatedClient,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreateGroupResponse200]]:
    """Post Courses Group

     Import outcomes into Canvas. For more information on the format that’s expected here, please see the
    “Outcomes CSV” section in the API docs.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)

    Args:
        course_id (str):
        learning_outcome_group_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreateGroupResponse200]]
    """

    kwargs = _get_kwargs(
        course_id=course_id,
        learning_outcome_group_id=learning_outcome_group_id,
        import_type=import_type,
        attachment=attachment,
        extension=extension,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course_id: str,
    learning_outcome_group_id: str,
    *,
    client: AuthenticatedClient,
    import_type: Union[Unset, str] = UNSET,
    attachment: str,
    extension: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreateGroupResponse200]]:
    """Post Courses Group

     Import outcomes into Canvas. For more information on the format that’s expected here, please see the
    “Outcomes CSV” section in the API docs.

    Required OAuth scope:
    url:POST|/api/v1/courses/:course_id/outcome_imports(/group/:learning_outcome_group_id)

    Args:
        course_id (str):
        learning_outcome_group_id (str):
        import_type (Union[Unset, str]):
        attachment (str):
        extension (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreateGroupResponse200]
    """

    return (
        await asyncio_detailed(
            course_id=course_id,
            learning_outcome_group_id=learning_outcome_group_id,
            client=client,
            import_type=import_type,
            attachment=attachment,
            extension=extension,
        )
    ).parsed
