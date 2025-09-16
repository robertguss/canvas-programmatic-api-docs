from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_context_search_response_200_accounts_item import GetContextSearchResponse200AccountsItem
    from ..models.get_context_search_response_200_courses_item import GetContextSearchResponse200CoursesItem


T = TypeVar("T", bound="GetContextSearchResponse200")


@_attrs_define
class GetContextSearchResponse200:
    """
    Attributes:
        accounts (list['GetContextSearchResponse200AccountsItem']):
        courses (list['GetContextSearchResponse200CoursesItem']):
    """

    accounts: list["GetContextSearchResponse200AccountsItem"]
    courses: list["GetContextSearchResponse200CoursesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounts = []
        for accounts_item_data in self.accounts:
            accounts_item = accounts_item_data.to_dict()
            accounts.append(accounts_item)

        courses = []
        for courses_item_data in self.courses:
            courses_item = courses_item_data.to_dict()
            courses.append(courses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
                "courses": courses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_context_search_response_200_accounts_item import GetContextSearchResponse200AccountsItem
        from ..models.get_context_search_response_200_courses_item import GetContextSearchResponse200CoursesItem

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = GetContextSearchResponse200AccountsItem.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        courses = []
        _courses = d.pop("courses")
        for courses_item_data in _courses:
            courses_item = GetContextSearchResponse200CoursesItem.from_dict(courses_item_data)

            courses.append(courses_item)

        get_context_search_response_200 = cls(
            accounts=accounts,
            courses=courses,
        )

        get_context_search_response_200.additional_properties = d
        return get_context_search_response_200

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
