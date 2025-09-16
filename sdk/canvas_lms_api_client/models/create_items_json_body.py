from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateItemsJsonBody")


@_attrs_define
class CreateItemsJsonBody:
    """
    Attributes:
        course_id (Union[Unset, str]): no description
        assignment_id (Union[Unset, str]): The id of the assignment associated with the quiz.
        itempoints_possible (Union[Unset, str]): The number of points available to score on this item. Must be positive.
        itementry_type (Union[Unset, str]): The type of the item.Allowed values: Item
        itementryitem_body (Union[Unset, str]): The question stem (rich content).
        itementryinteraction_type_slug (Union[Unset, str]): The type of question. One of ‘multi-answer’, ‘matching’,
            ‘categorization’, ‘file-upload’, ‘formula’, ‘ordering’, ‘rich-fill-blank’, ‘hot-spot’, ‘choice’, ‘numeric’,
            ‘true-false’, or ‘essay’. See Appendix: Question Types for more info about each type.
        itementryinteraction_data (Union[Unset, str]): An object that contains the question data. See Appendix: Question
            Types for more info about this field.
        itementryproperties (Union[Unset, str]): An object that contains additional properties for some question types.
            See Appendix: Question Types for more info about this field.
        itementryscoring_data (Union[Unset, str]): An object that describes how to score the question. See Appendix:
            Question Types for more info about this field.
        itementryanswer_feedback (Union[Unset, str]): Feedback provided for each answer (rich content, only available on
            ‘choice’ question types).
        itementryscoring_algorithm (Union[Unset, str]): The algorithm used to score the question. See Appendix: Question
            Types for more info about this field.
    """

    course_id: Union[Unset, str] = UNSET
    assignment_id: Union[Unset, str] = UNSET
    itempoints_possible: Union[Unset, str] = UNSET
    itementry_type: Union[Unset, str] = UNSET
    itementryitem_body: Union[Unset, str] = UNSET
    itementryinteraction_type_slug: Union[Unset, str] = UNSET
    itementryinteraction_data: Union[Unset, str] = UNSET
    itementryproperties: Union[Unset, str] = UNSET
    itementryscoring_data: Union[Unset, str] = UNSET
    itementryanswer_feedback: Union[Unset, str] = UNSET
    itementryscoring_algorithm: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        course_id = self.course_id

        assignment_id = self.assignment_id

        itempoints_possible = self.itempoints_possible

        itementry_type = self.itementry_type

        itementryitem_body = self.itementryitem_body

        itementryinteraction_type_slug = self.itementryinteraction_type_slug

        itementryinteraction_data = self.itementryinteraction_data

        itementryproperties = self.itementryproperties

        itementryscoring_data = self.itementryscoring_data

        itementryanswer_feedback = self.itementryanswer_feedback

        itementryscoring_algorithm = self.itementryscoring_algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_id is not UNSET:
            field_dict["course_id"] = course_id
        if assignment_id is not UNSET:
            field_dict["assignment_id"] = assignment_id
        if itempoints_possible is not UNSET:
            field_dict["item[points_possible]"] = itempoints_possible
        if itementry_type is not UNSET:
            field_dict["item[entry_type]"] = itementry_type
        if itementryitem_body is not UNSET:
            field_dict["item[entry][item_body]"] = itementryitem_body
        if itementryinteraction_type_slug is not UNSET:
            field_dict["item[entry][interaction_type_slug]"] = itementryinteraction_type_slug
        if itementryinteraction_data is not UNSET:
            field_dict["item[entry][interaction_data]"] = itementryinteraction_data
        if itementryproperties is not UNSET:
            field_dict["item[entry][properties]"] = itementryproperties
        if itementryscoring_data is not UNSET:
            field_dict["item[entry][scoring_data]"] = itementryscoring_data
        if itementryanswer_feedback is not UNSET:
            field_dict["item[entry][answer_feedback]"] = itementryanswer_feedback
        if itementryscoring_algorithm is not UNSET:
            field_dict["item[entry][scoring_algorithm]"] = itementryscoring_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        course_id = d.pop("course_id", UNSET)

        assignment_id = d.pop("assignment_id", UNSET)

        itempoints_possible = d.pop("item[points_possible]", UNSET)

        itementry_type = d.pop("item[entry_type]", UNSET)

        itementryitem_body = d.pop("item[entry][item_body]", UNSET)

        itementryinteraction_type_slug = d.pop("item[entry][interaction_type_slug]", UNSET)

        itementryinteraction_data = d.pop("item[entry][interaction_data]", UNSET)

        itementryproperties = d.pop("item[entry][properties]", UNSET)

        itementryscoring_data = d.pop("item[entry][scoring_data]", UNSET)

        itementryanswer_feedback = d.pop("item[entry][answer_feedback]", UNSET)

        itementryscoring_algorithm = d.pop("item[entry][scoring_algorithm]", UNSET)

        create_items_json_body = cls(
            course_id=course_id,
            assignment_id=assignment_id,
            itempoints_possible=itempoints_possible,
            itementry_type=itementry_type,
            itementryitem_body=itementryitem_body,
            itementryinteraction_type_slug=itementryinteraction_type_slug,
            itementryinteraction_data=itementryinteraction_data,
            itementryproperties=itementryproperties,
            itementryscoring_data=itementryscoring_data,
            itementryanswer_feedback=itementryanswer_feedback,
            itementryscoring_algorithm=itementryscoring_algorithm,
        )

        create_items_json_body.additional_properties = d
        return create_items_json_body

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
