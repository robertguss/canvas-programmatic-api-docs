from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.developer_key_lti_registration import DeveloperKeyLtiRegistration
    from ..models.developer_key_public_jwk import DeveloperKeyPublicJwk
    from ..models.developer_key_tool_configuration import DeveloperKeyToolConfiguration


T = TypeVar("T", bound="DeveloperKey")


@_attrs_define
class DeveloperKey:
    """
    Attributes:
        id (int):
        name (str):
        created_at (str):
        updated_at (str):
        workflow_state (str):
        is_lti_key (bool):
        email (str):
        icon_url (str):
        notes (str):
        vendor_code (str):
        account_name (str):
        visible (bool):
        scopes (list[str]):
        redirect_uri (str):
        redirect_uris (list[str]):
        access_token_count (int):
        last_used_at (str):
        test_cluster_only (bool):
        allow_includes (bool):
        require_scopes (bool):
        client_credentials_audience (str):
        api_key (str):
        tool_configuration (DeveloperKeyToolConfiguration):
        public_jwk (DeveloperKeyPublicJwk):
        public_jwk_url (str):
        lti_registration (DeveloperKeyLtiRegistration):
        is_lti_registration (bool):
        user_name (str):
        user_id (str):
    """

    id: int
    name: str
    created_at: str
    updated_at: str
    workflow_state: str
    is_lti_key: bool
    email: str
    icon_url: str
    notes: str
    vendor_code: str
    account_name: str
    visible: bool
    scopes: list[str]
    redirect_uri: str
    redirect_uris: list[str]
    access_token_count: int
    last_used_at: str
    test_cluster_only: bool
    allow_includes: bool
    require_scopes: bool
    client_credentials_audience: str
    api_key: str
    tool_configuration: "DeveloperKeyToolConfiguration"
    public_jwk: "DeveloperKeyPublicJwk"
    public_jwk_url: str
    lti_registration: "DeveloperKeyLtiRegistration"
    is_lti_registration: bool
    user_name: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        created_at = self.created_at

        updated_at = self.updated_at

        workflow_state = self.workflow_state

        is_lti_key = self.is_lti_key

        email = self.email

        icon_url = self.icon_url

        notes = self.notes

        vendor_code = self.vendor_code

        account_name = self.account_name

        visible = self.visible

        scopes = self.scopes

        redirect_uri = self.redirect_uri

        redirect_uris = self.redirect_uris

        access_token_count = self.access_token_count

        last_used_at = self.last_used_at

        test_cluster_only = self.test_cluster_only

        allow_includes = self.allow_includes

        require_scopes = self.require_scopes

        client_credentials_audience = self.client_credentials_audience

        api_key = self.api_key

        tool_configuration = self.tool_configuration.to_dict()

        public_jwk = self.public_jwk.to_dict()

        public_jwk_url = self.public_jwk_url

        lti_registration = self.lti_registration.to_dict()

        is_lti_registration = self.is_lti_registration

        user_name = self.user_name

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "workflow_state": workflow_state,
                "is_lti_key": is_lti_key,
                "email": email,
                "icon_url": icon_url,
                "notes": notes,
                "vendor_code": vendor_code,
                "account_name": account_name,
                "visible": visible,
                "scopes": scopes,
                "redirect_uri": redirect_uri,
                "redirect_uris": redirect_uris,
                "access_token_count": access_token_count,
                "last_used_at": last_used_at,
                "test_cluster_only": test_cluster_only,
                "allow_includes": allow_includes,
                "require_scopes": require_scopes,
                "client_credentials_audience": client_credentials_audience,
                "api_key": api_key,
                "tool_configuration": tool_configuration,
                "public_jwk": public_jwk,
                "public_jwk_url": public_jwk_url,
                "lti_registration": lti_registration,
                "is_lti_registration": is_lti_registration,
                "user_name": user_name,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.developer_key_lti_registration import DeveloperKeyLtiRegistration
        from ..models.developer_key_public_jwk import DeveloperKeyPublicJwk
        from ..models.developer_key_tool_configuration import DeveloperKeyToolConfiguration

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        workflow_state = d.pop("workflow_state")

        is_lti_key = d.pop("is_lti_key")

        email = d.pop("email")

        icon_url = d.pop("icon_url")

        notes = d.pop("notes")

        vendor_code = d.pop("vendor_code")

        account_name = d.pop("account_name")

        visible = d.pop("visible")

        scopes = cast(list[str], d.pop("scopes"))

        redirect_uri = d.pop("redirect_uri")

        redirect_uris = cast(list[str], d.pop("redirect_uris"))

        access_token_count = d.pop("access_token_count")

        last_used_at = d.pop("last_used_at")

        test_cluster_only = d.pop("test_cluster_only")

        allow_includes = d.pop("allow_includes")

        require_scopes = d.pop("require_scopes")

        client_credentials_audience = d.pop("client_credentials_audience")

        api_key = d.pop("api_key")

        tool_configuration = DeveloperKeyToolConfiguration.from_dict(d.pop("tool_configuration"))

        public_jwk = DeveloperKeyPublicJwk.from_dict(d.pop("public_jwk"))

        public_jwk_url = d.pop("public_jwk_url")

        lti_registration = DeveloperKeyLtiRegistration.from_dict(d.pop("lti_registration"))

        is_lti_registration = d.pop("is_lti_registration")

        user_name = d.pop("user_name")

        user_id = d.pop("user_id")

        developer_key = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            workflow_state=workflow_state,
            is_lti_key=is_lti_key,
            email=email,
            icon_url=icon_url,
            notes=notes,
            vendor_code=vendor_code,
            account_name=account_name,
            visible=visible,
            scopes=scopes,
            redirect_uri=redirect_uri,
            redirect_uris=redirect_uris,
            access_token_count=access_token_count,
            last_used_at=last_used_at,
            test_cluster_only=test_cluster_only,
            allow_includes=allow_includes,
            require_scopes=require_scopes,
            client_credentials_audience=client_credentials_audience,
            api_key=api_key,
            tool_configuration=tool_configuration,
            public_jwk=public_jwk,
            public_jwk_url=public_jwk_url,
            lti_registration=lti_registration,
            is_lti_registration=is_lti_registration,
            user_name=user_name,
            user_id=user_id,
        )

        developer_key.additional_properties = d
        return developer_key

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
