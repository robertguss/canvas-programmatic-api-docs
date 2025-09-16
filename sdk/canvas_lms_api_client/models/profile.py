from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Profile")


@_attrs_define
class Profile:
    """
    Attributes:
        id (int):
        name (str):
        short_name (str):
        sortable_name (str):
        title (None):
        bio (None):
        pronunciation (str):
        primary_email (str):
        login_id (str):
        sis_user_id (str):
        lti_user_id (None):
        avatar_url (str):
        calendar (None):
        time_zone (str):
        locale (None):
        k5_user (bool):
        use_classic_font_in_k5 (bool):
    """

    id: int
    name: str
    short_name: str
    sortable_name: str
    title: None
    bio: None
    pronunciation: str
    primary_email: str
    login_id: str
    sis_user_id: str
    lti_user_id: None
    avatar_url: str
    calendar: None
    time_zone: str
    locale: None
    k5_user: bool
    use_classic_font_in_k5: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        short_name = self.short_name

        sortable_name = self.sortable_name

        title = self.title

        bio = self.bio

        pronunciation = self.pronunciation

        primary_email = self.primary_email

        login_id = self.login_id

        sis_user_id = self.sis_user_id

        lti_user_id = self.lti_user_id

        avatar_url = self.avatar_url

        calendar = self.calendar

        time_zone = self.time_zone

        locale = self.locale

        k5_user = self.k5_user

        use_classic_font_in_k5 = self.use_classic_font_in_k5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "short_name": short_name,
                "sortable_name": sortable_name,
                "title": title,
                "bio": bio,
                "pronunciation": pronunciation,
                "primary_email": primary_email,
                "login_id": login_id,
                "sis_user_id": sis_user_id,
                "lti_user_id": lti_user_id,
                "avatar_url": avatar_url,
                "calendar": calendar,
                "time_zone": time_zone,
                "locale": locale,
                "k5_user": k5_user,
                "use_classic_font_in_k5": use_classic_font_in_k5,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        short_name = d.pop("short_name")

        sortable_name = d.pop("sortable_name")

        title = d.pop("title")

        bio = d.pop("bio")

        pronunciation = d.pop("pronunciation")

        primary_email = d.pop("primary_email")

        login_id = d.pop("login_id")

        sis_user_id = d.pop("sis_user_id")

        lti_user_id = d.pop("lti_user_id")

        avatar_url = d.pop("avatar_url")

        calendar = d.pop("calendar")

        time_zone = d.pop("time_zone")

        locale = d.pop("locale")

        k5_user = d.pop("k5_user")

        use_classic_font_in_k5 = d.pop("use_classic_font_in_k5")

        profile = cls(
            id=id,
            name=name,
            short_name=short_name,
            sortable_name=sortable_name,
            title=title,
            bio=bio,
            pronunciation=pronunciation,
            primary_email=primary_email,
            login_id=login_id,
            sis_user_id=sis_user_id,
            lti_user_id=lti_user_id,
            avatar_url=avatar_url,
            calendar=calendar,
            time_zone=time_zone,
            locale=locale,
            k5_user=k5_user,
            use_classic_font_in_k5=use_classic_font_in_k5,
        )

        profile.additional_properties = d
        return profile

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
