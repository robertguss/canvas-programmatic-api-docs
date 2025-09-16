from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_page_views_response_200_item_links import GetPageViewsResponse200ItemLinks


T = TypeVar("T", bound="GetPageViewsResponse200Item")


@_attrs_define
class GetPageViewsResponse200Item:
    """
    Attributes:
        id (str):
        app_name (str):
        url (str):
        context_type (str):
        asset_type (str):
        controller (str):
        action (str):
        contributed (bool):
        interaction_seconds (float):
        created_at (str):
        user_request (bool):
        render_time (float):
        user_agent (str):
        participated (bool):
        http_method (str):
        remote_ip (str):
        links (GetPageViewsResponse200ItemLinks):
    """

    id: str
    app_name: str
    url: str
    context_type: str
    asset_type: str
    controller: str
    action: str
    contributed: bool
    interaction_seconds: float
    created_at: str
    user_request: bool
    render_time: float
    user_agent: str
    participated: bool
    http_method: str
    remote_ip: str
    links: "GetPageViewsResponse200ItemLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        app_name = self.app_name

        url = self.url

        context_type = self.context_type

        asset_type = self.asset_type

        controller = self.controller

        action = self.action

        contributed = self.contributed

        interaction_seconds = self.interaction_seconds

        created_at = self.created_at

        user_request = self.user_request

        render_time = self.render_time

        user_agent = self.user_agent

        participated = self.participated

        http_method = self.http_method

        remote_ip = self.remote_ip

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "app_name": app_name,
                "url": url,
                "context_type": context_type,
                "asset_type": asset_type,
                "controller": controller,
                "action": action,
                "contributed": contributed,
                "interaction_seconds": interaction_seconds,
                "created_at": created_at,
                "user_request": user_request,
                "render_time": render_time,
                "user_agent": user_agent,
                "participated": participated,
                "http_method": http_method,
                "remote_ip": remote_ip,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_page_views_response_200_item_links import GetPageViewsResponse200ItemLinks

        d = dict(src_dict)
        id = d.pop("id")

        app_name = d.pop("app_name")

        url = d.pop("url")

        context_type = d.pop("context_type")

        asset_type = d.pop("asset_type")

        controller = d.pop("controller")

        action = d.pop("action")

        contributed = d.pop("contributed")

        interaction_seconds = d.pop("interaction_seconds")

        created_at = d.pop("created_at")

        user_request = d.pop("user_request")

        render_time = d.pop("render_time")

        user_agent = d.pop("user_agent")

        participated = d.pop("participated")

        http_method = d.pop("http_method")

        remote_ip = d.pop("remote_ip")

        links = GetPageViewsResponse200ItemLinks.from_dict(d.pop("links"))

        get_page_views_response_200_item = cls(
            id=id,
            app_name=app_name,
            url=url,
            context_type=context_type,
            asset_type=asset_type,
            controller=controller,
            action=action,
            contributed=contributed,
            interaction_seconds=interaction_seconds,
            created_at=created_at,
            user_request=user_request,
            render_time=render_time,
            user_agent=user_agent,
            participated=participated,
            http_method=http_method,
            remote_ip=remote_ip,
            links=links,
        )

        get_page_views_response_200_item.additional_properties = d
        return get_page_views_response_200_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
