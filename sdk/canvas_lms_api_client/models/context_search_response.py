from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.context_search_response_accounts_item import ContextSearchResponseAccountsItem
    from ..models.context_search_response_courses_item import ContextSearchResponseCoursesItem


T = TypeVar("T", bound="ContextSearchResponse")


@_attrs_define
class ContextSearchResponse:
    """
    Attributes:
        accounts (list['ContextSearchResponseAccountsItem']):
        courses (list['ContextSearchResponseCoursesItem']):
    """

    accounts: list["ContextSearchResponseAccountsItem"]
    courses: list["ContextSearchResponseCoursesItem"]
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
        from ..models.context_search_response_accounts_item import ContextSearchResponseAccountsItem
        from ..models.context_search_response_courses_item import ContextSearchResponseCoursesItem

        d = dict(src_dict)
        accounts = []
        _accounts = d.pop("accounts")
        for accounts_item_data in _accounts:
            accounts_item = ContextSearchResponseAccountsItem.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        courses = []
        _courses = d.pop("courses")
        for courses_item_data in _courses:
            courses_item = ContextSearchResponseCoursesItem.from_dict(courses_item_data)

            courses.append(courses_item)

        context_search_response = cls(
            accounts=accounts,
            courses=courses,
        )

        context_search_response.additional_properties = d
        return context_search_response

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
