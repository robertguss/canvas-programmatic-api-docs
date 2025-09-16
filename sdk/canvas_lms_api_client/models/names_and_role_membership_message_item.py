from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.names_and_role_membership_message_item_httpspurl_imsglobal_orgspeclticlaimcustom import (
        NamesAndRoleMembershipMessageItemHttpspurlImsglobalOrgspeclticlaimcustom,
    )


T = TypeVar("T", bound="NamesAndRoleMembershipMessageItem")


@_attrs_define
class NamesAndRoleMembershipMessageItem:
    """
    Attributes:
        httpspurl_imsglobal_orgspeclticlaimmessage_type (str):
        locale (str):
        httpswww_instructure_comcanvas_user_id (int):
        httpswww_instructure_comcanvas_user_login_id (str):
        httpspurl_imsglobal_orgspeclticlaimcustom
            (NamesAndRoleMembershipMessageItemHttpspurlImsglobalOrgspeclticlaimcustom):
    """

    httpspurl_imsglobal_orgspeclticlaimmessage_type: str
    locale: str
    httpswww_instructure_comcanvas_user_id: int
    httpswww_instructure_comcanvas_user_login_id: str
    httpspurl_imsglobal_orgspeclticlaimcustom: (
        "NamesAndRoleMembershipMessageItemHttpspurlImsglobalOrgspeclticlaimcustom"
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        httpspurl_imsglobal_orgspeclticlaimmessage_type = self.httpspurl_imsglobal_orgspeclticlaimmessage_type

        locale = self.locale

        httpswww_instructure_comcanvas_user_id = self.httpswww_instructure_comcanvas_user_id

        httpswww_instructure_comcanvas_user_login_id = self.httpswww_instructure_comcanvas_user_login_id

        httpspurl_imsglobal_orgspeclticlaimcustom = self.httpspurl_imsglobal_orgspeclticlaimcustom.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "https://purl.imsglobal.org/spec/lti/claim/message_type": httpspurl_imsglobal_orgspeclticlaimmessage_type,
                "locale": locale,
                "https://www.instructure.com/canvas_user_id": httpswww_instructure_comcanvas_user_id,
                "https://www.instructure.com/canvas_user_login_id": httpswww_instructure_comcanvas_user_login_id,
                "https://purl.imsglobal.org/spec/lti/claim/custom": httpspurl_imsglobal_orgspeclticlaimcustom,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.names_and_role_membership_message_item_httpspurl_imsglobal_orgspeclticlaimcustom import (
            NamesAndRoleMembershipMessageItemHttpspurlImsglobalOrgspeclticlaimcustom,
        )

        d = dict(src_dict)
        httpspurl_imsglobal_orgspeclticlaimmessage_type = d.pop(
            "https://purl.imsglobal.org/spec/lti/claim/message_type"
        )

        locale = d.pop("locale")

        httpswww_instructure_comcanvas_user_id = d.pop("https://www.instructure.com/canvas_user_id")

        httpswww_instructure_comcanvas_user_login_id = d.pop("https://www.instructure.com/canvas_user_login_id")

        httpspurl_imsglobal_orgspeclticlaimcustom = (
            NamesAndRoleMembershipMessageItemHttpspurlImsglobalOrgspeclticlaimcustom.from_dict(
                d.pop("https://purl.imsglobal.org/spec/lti/claim/custom")
            )
        )

        names_and_role_membership_message_item = cls(
            httpspurl_imsglobal_orgspeclticlaimmessage_type=httpspurl_imsglobal_orgspeclticlaimmessage_type,
            locale=locale,
            httpswww_instructure_comcanvas_user_id=httpswww_instructure_comcanvas_user_id,
            httpswww_instructure_comcanvas_user_login_id=httpswww_instructure_comcanvas_user_login_id,
            httpspurl_imsglobal_orgspeclticlaimcustom=httpspurl_imsglobal_orgspeclticlaimcustom,
        )

        names_and_role_membership_message_item.additional_properties = d
        return names_and_role_membership_message_item

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
