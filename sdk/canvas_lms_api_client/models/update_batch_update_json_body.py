from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBatchUpdateJsonBody")


@_attrs_define
class UpdateBatchUpdateJsonBody:
    """
    Attributes:
        grading_periodstitle (str): The title of the grading period. The title is required for creating a new grading
            period, but not for updating an existing grading period.
        grading_periodsstart_date (str): The date the grading period starts. The start_date is required for creating a
            new grading period, but not for updating an existing grading period.
        grading_periodsend_date (str): The date the grading period ends. The end_date is required for creating a new
            grading period, but not for updating an existing grading period.
        grading_periodsclose_date (str): The date after which grades can no longer be changed for a grading period. The
            close_date is required for creating a new grading period, but not for updating an existing grading period.
        set_id (Union[Unset, str]): The id of the grading period set.
        grading_periodsweight (Union[Unset, str]): A weight value that contributes to the overall weight of a grading
            period set which is used to calculate how much assignments in this period contribute to the total grade
    """

    grading_periodstitle: str
    grading_periodsstart_date: str
    grading_periodsend_date: str
    grading_periodsclose_date: str
    set_id: Union[Unset, str] = UNSET
    grading_periodsweight: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grading_periodstitle = self.grading_periodstitle

        grading_periodsstart_date = self.grading_periodsstart_date

        grading_periodsend_date = self.grading_periodsend_date

        grading_periodsclose_date = self.grading_periodsclose_date

        set_id = self.set_id

        grading_periodsweight = self.grading_periodsweight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grading_periods[][title]": grading_periodstitle,
                "grading_periods[][start_date]": grading_periodsstart_date,
                "grading_periods[][end_date]": grading_periodsend_date,
                "grading_periods[][close_date]": grading_periodsclose_date,
            }
        )
        if set_id is not UNSET:
            field_dict["set_id"] = set_id
        if grading_periodsweight is not UNSET:
            field_dict["grading_periods[][weight]"] = grading_periodsweight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        grading_periodstitle = d.pop("grading_periods[][title]")

        grading_periodsstart_date = d.pop("grading_periods[][start_date]")

        grading_periodsend_date = d.pop("grading_periods[][end_date]")

        grading_periodsclose_date = d.pop("grading_periods[][close_date]")

        set_id = d.pop("set_id", UNSET)

        grading_periodsweight = d.pop("grading_periods[][weight]", UNSET)

        update_batch_update_json_body = cls(
            grading_periodstitle=grading_periodstitle,
            grading_periodsstart_date=grading_periodsstart_date,
            grading_periodsend_date=grading_periodsend_date,
            grading_periodsclose_date=grading_periodsclose_date,
            set_id=set_id,
            grading_periodsweight=grading_periodsweight,
        )

        update_batch_update_json_body.additional_properties = d
        return update_batch_update_json_body

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
