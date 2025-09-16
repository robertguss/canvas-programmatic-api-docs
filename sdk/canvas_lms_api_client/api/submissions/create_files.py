from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    section_id: str,
    assignment_id: str,
    user_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files",
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
    section_id: str,
    assignment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Post Sections Files

     Upload a file to a submission. This API endpoint is the first step in uploading a file to a
    submission as a student. See the [File Upload Documentation](../basics/file.file_uploads) for
    details on the file upload workflow. The final step of the file upload workflow will return the
    attachment data, including the new file id. The caller can then POST to submit the `online_upload`
    assignment with these file ids. ### [Grade or comment on a
    submission](#method.submissions_api.update) <a href=\"#method.submissions_api.update\"
    id=\"method.submissions_api.update\"></a>
    [SubmissionsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/submissions_api_controller.rb)

    Required OAuth scope:
    url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files

    Args:
        section_id (str):
        assignment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    section_id: str,
    assignment_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    r"""Post Sections Files

     Upload a file to a submission. This API endpoint is the first step in uploading a file to a
    submission as a student. See the [File Upload Documentation](../basics/file.file_uploads) for
    details on the file upload workflow. The final step of the file upload workflow will return the
    attachment data, including the new file id. The caller can then POST to submit the `online_upload`
    assignment with these file ids. ### [Grade or comment on a
    submission](#method.submissions_api.update) <a href=\"#method.submissions_api.update\"
    id=\"method.submissions_api.update\"></a>
    [SubmissionsApiController#update](https://github.com/instructure/canvas-
    lms/blob/master/app/controllers/submissions_api_controller.rb)

    Required OAuth scope:
    url:POST|/api/v1/sections/:section_id/assignments/:assignment_id/submissions/:user_id/files

    Args:
        section_id (str):
        assignment_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        section_id=section_id,
        assignment_id=assignment_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
