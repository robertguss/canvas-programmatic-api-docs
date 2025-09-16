from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.context_external_tool_placement_custom_fields import ContextExternalToolPlacementCustomFields
    from ..models.context_external_tool_placement_eula import ContextExternalToolPlacementEula
    from ..models.context_external_tool_placement_labels import ContextExternalToolPlacementLabels


T = TypeVar("T", bound="ContextExternalToolPlacement")


@_attrs_define
class ContextExternalToolPlacement:
    """
    Attributes:
        enabled (bool):
        url (str):
        target_link_uri (str):
        text (str):
        label (str):
        labels (ContextExternalToolPlacementLabels):
        message_type (str):
        selection_width (int):
        selection_height (int):
        launch_width (int):
        launch_height (int):
        icon_url (str):
        canvas_icon_class (str):
        allow_fullscreen (bool):
        custom_fields (ContextExternalToolPlacementCustomFields):
        visibility (str):
        required_permissions (str):
        default (str):
        display_type (str):
        window_target (str):
        accept_media_types (str):
        use_tray (bool):
        icon_svg_path_64 (str):
        root_account_only (bool):
        description (str):
        require_resource_selection (bool):
        prefer_sis_email (bool):
        oauth_compliant (bool):
        eula (ContextExternalToolPlacementEula):
    """

    enabled: bool
    url: str
    target_link_uri: str
    text: str
    label: str
    labels: "ContextExternalToolPlacementLabels"
    message_type: str
    selection_width: int
    selection_height: int
    launch_width: int
    launch_height: int
    icon_url: str
    canvas_icon_class: str
    allow_fullscreen: bool
    custom_fields: "ContextExternalToolPlacementCustomFields"
    visibility: str
    required_permissions: str
    default: str
    display_type: str
    window_target: str
    accept_media_types: str
    use_tray: bool
    icon_svg_path_64: str
    root_account_only: bool
    description: str
    require_resource_selection: bool
    prefer_sis_email: bool
    oauth_compliant: bool
    eula: "ContextExternalToolPlacementEula"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        url = self.url

        target_link_uri = self.target_link_uri

        text = self.text

        label = self.label

        labels = self.labels.to_dict()

        message_type = self.message_type

        selection_width = self.selection_width

        selection_height = self.selection_height

        launch_width = self.launch_width

        launch_height = self.launch_height

        icon_url = self.icon_url

        canvas_icon_class = self.canvas_icon_class

        allow_fullscreen = self.allow_fullscreen

        custom_fields = self.custom_fields.to_dict()

        visibility = self.visibility

        required_permissions = self.required_permissions

        default = self.default

        display_type = self.display_type

        window_target = self.window_target

        accept_media_types = self.accept_media_types

        use_tray = self.use_tray

        icon_svg_path_64 = self.icon_svg_path_64

        root_account_only = self.root_account_only

        description = self.description

        require_resource_selection = self.require_resource_selection

        prefer_sis_email = self.prefer_sis_email

        oauth_compliant = self.oauth_compliant

        eula = self.eula.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "url": url,
                "target_link_uri": target_link_uri,
                "text": text,
                "label": label,
                "labels": labels,
                "message_type": message_type,
                "selection_width": selection_width,
                "selection_height": selection_height,
                "launch_width": launch_width,
                "launch_height": launch_height,
                "icon_url": icon_url,
                "canvas_icon_class": canvas_icon_class,
                "allow_fullscreen": allow_fullscreen,
                "custom_fields": custom_fields,
                "visibility": visibility,
                "required_permissions": required_permissions,
                "default": default,
                "display_type": display_type,
                "windowTarget": window_target,
                "accept_media_types": accept_media_types,
                "use_tray": use_tray,
                "icon_svg_path_64": icon_svg_path_64,
                "root_account_only": root_account_only,
                "description": description,
                "require_resource_selection": require_resource_selection,
                "prefer_sis_email": prefer_sis_email,
                "oauth_compliant": oauth_compliant,
                "eula": eula,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_external_tool_placement_custom_fields import ContextExternalToolPlacementCustomFields
        from ..models.context_external_tool_placement_eula import ContextExternalToolPlacementEula
        from ..models.context_external_tool_placement_labels import ContextExternalToolPlacementLabels

        d = dict(src_dict)
        enabled = d.pop("enabled")

        url = d.pop("url")

        target_link_uri = d.pop("target_link_uri")

        text = d.pop("text")

        label = d.pop("label")

        labels = ContextExternalToolPlacementLabels.from_dict(d.pop("labels"))

        message_type = d.pop("message_type")

        selection_width = d.pop("selection_width")

        selection_height = d.pop("selection_height")

        launch_width = d.pop("launch_width")

        launch_height = d.pop("launch_height")

        icon_url = d.pop("icon_url")

        canvas_icon_class = d.pop("canvas_icon_class")

        allow_fullscreen = d.pop("allow_fullscreen")

        custom_fields = ContextExternalToolPlacementCustomFields.from_dict(d.pop("custom_fields"))

        visibility = d.pop("visibility")

        required_permissions = d.pop("required_permissions")

        default = d.pop("default")

        display_type = d.pop("display_type")

        window_target = d.pop("windowTarget")

        accept_media_types = d.pop("accept_media_types")

        use_tray = d.pop("use_tray")

        icon_svg_path_64 = d.pop("icon_svg_path_64")

        root_account_only = d.pop("root_account_only")

        description = d.pop("description")

        require_resource_selection = d.pop("require_resource_selection")

        prefer_sis_email = d.pop("prefer_sis_email")

        oauth_compliant = d.pop("oauth_compliant")

        eula = ContextExternalToolPlacementEula.from_dict(d.pop("eula"))

        context_external_tool_placement = cls(
            enabled=enabled,
            url=url,
            target_link_uri=target_link_uri,
            text=text,
            label=label,
            labels=labels,
            message_type=message_type,
            selection_width=selection_width,
            selection_height=selection_height,
            launch_width=launch_width,
            launch_height=launch_height,
            icon_url=icon_url,
            canvas_icon_class=canvas_icon_class,
            allow_fullscreen=allow_fullscreen,
            custom_fields=custom_fields,
            visibility=visibility,
            required_permissions=required_permissions,
            default=default,
            display_type=display_type,
            window_target=window_target,
            accept_media_types=accept_media_types,
            use_tray=use_tray,
            icon_svg_path_64=icon_svg_path_64,
            root_account_only=root_account_only,
            description=description,
            require_resource_selection=require_resource_selection,
            prefer_sis_email=prefer_sis_email,
            oauth_compliant=oauth_compliant,
            eula=eula,
        )

        context_external_tool_placement.additional_properties = d
        return context_external_tool_placement

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
