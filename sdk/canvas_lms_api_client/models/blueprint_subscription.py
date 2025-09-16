from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.blueprint_subscription_blueprint_course import BlueprintSubscriptionBlueprintCourse


T = TypeVar("T", bound="BlueprintSubscription")


@_attrs_define
class BlueprintSubscription:
    """
    Attributes:
        id (int):
        template_id (int):
        blueprint_course (BlueprintSubscriptionBlueprintCourse):
    """

    id: int
    template_id: int
    blueprint_course: "BlueprintSubscriptionBlueprintCourse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        blueprint_course = self.blueprint_course.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "template_id": template_id,
                "blueprint_course": blueprint_course,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blueprint_subscription_blueprint_course import BlueprintSubscriptionBlueprintCourse

        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        blueprint_course = BlueprintSubscriptionBlueprintCourse.from_dict(d.pop("blueprint_course"))

        blueprint_subscription = cls(
            id=id,
            template_id=template_id,
            blueprint_course=blueprint_course,
        )

        blueprint_subscription.additional_properties = d
        return blueprint_subscription

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
