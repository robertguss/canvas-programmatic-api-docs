from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetAuthenticationProvidersResponse200Item")


@_attrs_define
class GetAuthenticationProvidersResponse200Item:
    """
    Attributes:
        identifier_format (str):
        auth_type (str):
        id (int):
        log_out_url (str):
        log_in_url (str):
        certificate_fingerprint (str):
        requested_authn_context (None):
        auth_host (str):
        auth_filter (str):
        auth_over_tls (None):
        auth_base (None):
        auth_username (str):
        auth_port (None):
        position (int):
        idp_entity_id (str):
        login_attribute (str):
        sig_alg (str):
        jit_provisioning (None):
        federated_attributes (None):
        mfa_required (None):
    """

    identifier_format: str
    auth_type: str
    id: int
    log_out_url: str
    log_in_url: str
    certificate_fingerprint: str
    requested_authn_context: None
    auth_host: str
    auth_filter: str
    auth_over_tls: None
    auth_base: None
    auth_username: str
    auth_port: None
    position: int
    idp_entity_id: str
    login_attribute: str
    sig_alg: str
    jit_provisioning: None
    federated_attributes: None
    mfa_required: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier_format = self.identifier_format

        auth_type = self.auth_type

        id = self.id

        log_out_url = self.log_out_url

        log_in_url = self.log_in_url

        certificate_fingerprint = self.certificate_fingerprint

        requested_authn_context = self.requested_authn_context

        auth_host = self.auth_host

        auth_filter = self.auth_filter

        auth_over_tls = self.auth_over_tls

        auth_base = self.auth_base

        auth_username = self.auth_username

        auth_port = self.auth_port

        position = self.position

        idp_entity_id = self.idp_entity_id

        login_attribute = self.login_attribute

        sig_alg = self.sig_alg

        jit_provisioning = self.jit_provisioning

        federated_attributes = self.federated_attributes

        mfa_required = self.mfa_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier_format": identifier_format,
                "auth_type": auth_type,
                "id": id,
                "log_out_url": log_out_url,
                "log_in_url": log_in_url,
                "certificate_fingerprint": certificate_fingerprint,
                "requested_authn_context": requested_authn_context,
                "auth_host": auth_host,
                "auth_filter": auth_filter,
                "auth_over_tls": auth_over_tls,
                "auth_base": auth_base,
                "auth_username": auth_username,
                "auth_port": auth_port,
                "position": position,
                "idp_entity_id": idp_entity_id,
                "login_attribute": login_attribute,
                "sig_alg": sig_alg,
                "jit_provisioning": jit_provisioning,
                "federated_attributes": federated_attributes,
                "mfa_required": mfa_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier_format = d.pop("identifier_format")

        auth_type = d.pop("auth_type")

        id = d.pop("id")

        log_out_url = d.pop("log_out_url")

        log_in_url = d.pop("log_in_url")

        certificate_fingerprint = d.pop("certificate_fingerprint")

        requested_authn_context = d.pop("requested_authn_context")

        auth_host = d.pop("auth_host")

        auth_filter = d.pop("auth_filter")

        auth_over_tls = d.pop("auth_over_tls")

        auth_base = d.pop("auth_base")

        auth_username = d.pop("auth_username")

        auth_port = d.pop("auth_port")

        position = d.pop("position")

        idp_entity_id = d.pop("idp_entity_id")

        login_attribute = d.pop("login_attribute")

        sig_alg = d.pop("sig_alg")

        jit_provisioning = d.pop("jit_provisioning")

        federated_attributes = d.pop("federated_attributes")

        mfa_required = d.pop("mfa_required")

        get_authentication_providers_response_200_item = cls(
            identifier_format=identifier_format,
            auth_type=auth_type,
            id=id,
            log_out_url=log_out_url,
            log_in_url=log_in_url,
            certificate_fingerprint=certificate_fingerprint,
            requested_authn_context=requested_authn_context,
            auth_host=auth_host,
            auth_filter=auth_filter,
            auth_over_tls=auth_over_tls,
            auth_base=auth_base,
            auth_username=auth_username,
            auth_port=auth_port,
            position=position,
            idp_entity_id=idp_entity_id,
            login_attribute=login_attribute,
            sig_alg=sig_alg,
            jit_provisioning=jit_provisioning,
            federated_attributes=federated_attributes,
            mfa_required=mfa_required,
        )

        get_authentication_providers_response_200_item.additional_properties = d
        return get_authentication_providers_response_200_item

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
