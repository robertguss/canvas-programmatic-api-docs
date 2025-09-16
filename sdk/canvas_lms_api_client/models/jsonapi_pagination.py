from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.jsonapi_pagination_count import JSONAPIPaginationCount
    from ..models.jsonapi_pagination_page import JSONAPIPaginationPage
    from ..models.jsonapi_pagination_page_count import JSONAPIPaginationPageCount
    from ..models.jsonapi_pagination_per_page import JSONAPIPaginationPerPage
    from ..models.jsonapi_pagination_template import JSONAPIPaginationTemplate


T = TypeVar("T", bound="JSONAPIPagination")


@_attrs_define
class JSONAPIPagination:
    """
    Attributes:
        per_page (JSONAPIPaginationPerPage):
        page (JSONAPIPaginationPage):
        template (JSONAPIPaginationTemplate):
        page_count (JSONAPIPaginationPageCount):
        count (JSONAPIPaginationCount):
    """

    per_page: "JSONAPIPaginationPerPage"
    page: "JSONAPIPaginationPage"
    template: "JSONAPIPaginationTemplate"
    page_count: "JSONAPIPaginationPageCount"
    count: "JSONAPIPaginationCount"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per_page = self.per_page.to_dict()

        page = self.page.to_dict()

        template = self.template.to_dict()

        page_count = self.page_count.to_dict()

        count = self.count.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "per_page": per_page,
                "page": page,
                "template": template,
                "page_count": page_count,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jsonapi_pagination_count import JSONAPIPaginationCount
        from ..models.jsonapi_pagination_page import JSONAPIPaginationPage
        from ..models.jsonapi_pagination_page_count import JSONAPIPaginationPageCount
        from ..models.jsonapi_pagination_per_page import JSONAPIPaginationPerPage
        from ..models.jsonapi_pagination_template import JSONAPIPaginationTemplate

        d = dict(src_dict)
        per_page = JSONAPIPaginationPerPage.from_dict(d.pop("per_page"))

        page = JSONAPIPaginationPage.from_dict(d.pop("page"))

        template = JSONAPIPaginationTemplate.from_dict(d.pop("template"))

        page_count = JSONAPIPaginationPageCount.from_dict(d.pop("page_count"))

        count = JSONAPIPaginationCount.from_dict(d.pop("count"))

        jsonapi_pagination = cls(
            per_page=per_page,
            page=page,
            template=template,
            page_count=page_count,
            count=count,
        )

        jsonapi_pagination.additional_properties = d
        return jsonapi_pagination

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
