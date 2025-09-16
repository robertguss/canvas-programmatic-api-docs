from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.enrollment_term_overrides import EnrollmentTermOverrides


T = TypeVar("T", bound="EnrollmentTerm")


@_attrs_define
class EnrollmentTerm:
    """
    Attributes:
        id (int):
        sis_term_id (str):
        sis_import_id (int):
        name (str):
        start_at (str):
        end_at (str):
        workflow_state (str):
        overrides (EnrollmentTermOverrides):
        course_count (int):
    """

    id: int
    sis_term_id: str
    sis_import_id: int
    name: str
    start_at: str
    end_at: str
    workflow_state: str
    overrides: "EnrollmentTermOverrides"
    course_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sis_term_id = self.sis_term_id

        sis_import_id = self.sis_import_id

        name = self.name

        start_at = self.start_at

        end_at = self.end_at

        workflow_state = self.workflow_state

        overrides = self.overrides.to_dict()

        course_count = self.course_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sis_term_id": sis_term_id,
                "sis_import_id": sis_import_id,
                "name": name,
                "start_at": start_at,
                "end_at": end_at,
                "workflow_state": workflow_state,
                "overrides": overrides,
                "course_count": course_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enrollment_term_overrides import EnrollmentTermOverrides

        d = dict(src_dict)
        id = d.pop("id")

        sis_term_id = d.pop("sis_term_id")

        sis_import_id = d.pop("sis_import_id")

        name = d.pop("name")

        start_at = d.pop("start_at")

        end_at = d.pop("end_at")

        workflow_state = d.pop("workflow_state")

        overrides = EnrollmentTermOverrides.from_dict(d.pop("overrides"))

        course_count = d.pop("course_count")

        enrollment_term = cls(
            id=id,
            sis_term_id=sis_term_id,
            sis_import_id=sis_import_id,
            name=name,
            start_at=start_at,
            end_at=end_at,
            workflow_state=workflow_state,
            overrides=overrides,
            course_count=course_count,
        )

        enrollment_term.additional_properties = d
        return enrollment_term

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
