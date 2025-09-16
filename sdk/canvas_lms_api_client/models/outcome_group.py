from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="OutcomeGroup")


@_attrs_define
class OutcomeGroup:
    """
    Attributes:
        id (int):
        url (str):
        parent_outcome_group (None):
        context_id (int):
        context_type (str):
        title (str):
        description (str):
        vendor_guid (str):
        subgroups_url (str):
        outcomes_url (str):
        import_url (str):
        can_edit (bool):
    """

    id: int
    url: str
    parent_outcome_group: None
    context_id: int
    context_type: str
    title: str
    description: str
    vendor_guid: str
    subgroups_url: str
    outcomes_url: str
    import_url: str
    can_edit: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url = self.url

        parent_outcome_group = self.parent_outcome_group

        context_id = self.context_id

        context_type = self.context_type

        title = self.title

        description = self.description

        vendor_guid = self.vendor_guid

        subgroups_url = self.subgroups_url

        outcomes_url = self.outcomes_url

        import_url = self.import_url

        can_edit = self.can_edit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "parent_outcome_group": parent_outcome_group,
                "context_id": context_id,
                "context_type": context_type,
                "title": title,
                "description": description,
                "vendor_guid": vendor_guid,
                "subgroups_url": subgroups_url,
                "outcomes_url": outcomes_url,
                "import_url": import_url,
                "can_edit": can_edit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        url = d.pop("url")

        parent_outcome_group = d.pop("parent_outcome_group")

        context_id = d.pop("context_id")

        context_type = d.pop("context_type")

        title = d.pop("title")

        description = d.pop("description")

        vendor_guid = d.pop("vendor_guid")

        subgroups_url = d.pop("subgroups_url")

        outcomes_url = d.pop("outcomes_url")

        import_url = d.pop("import_url")

        can_edit = d.pop("can_edit")

        outcome_group = cls(
            id=id,
            url=url,
            parent_outcome_group=parent_outcome_group,
            context_id=context_id,
            context_type=context_type,
            title=title,
            description=description,
            vendor_guid=vendor_guid,
            subgroups_url=subgroups_url,
            outcomes_url=outcomes_url,
            import_url=import_url,
            can_edit=can_edit,
        )

        outcome_group.additional_properties = d
        return outcome_group

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
