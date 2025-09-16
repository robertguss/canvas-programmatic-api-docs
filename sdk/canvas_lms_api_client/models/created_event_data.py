from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreatedEventData")


@_attrs_define
class CreatedEventData:
    """
    Attributes:
        name (list[Union[None, str]]):
        start_at (list[Union[None, str]]):
        conclude_at (list[Union[None, str]]):
        is_public (list[Union[None, bool]]):
        created_source (str):
    """

    name: list[Union[None, str]]
    start_at: list[Union[None, str]]
    conclude_at: list[Union[None, str]]
    is_public: list[Union[None, bool]]
    created_source: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = []
        for name_item_data in self.name:
            name_item: Union[None, str]
            name_item = name_item_data
            name.append(name_item)

        start_at = []
        for start_at_item_data in self.start_at:
            start_at_item: Union[None, str]
            start_at_item = start_at_item_data
            start_at.append(start_at_item)

        conclude_at = []
        for conclude_at_item_data in self.conclude_at:
            conclude_at_item: Union[None, str]
            conclude_at_item = conclude_at_item_data
            conclude_at.append(conclude_at_item)

        is_public = []
        for is_public_item_data in self.is_public:
            is_public_item: Union[None, bool]
            is_public_item = is_public_item_data
            is_public.append(is_public_item)

        created_source = self.created_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "start_at": start_at,
                "conclude_at": conclude_at,
                "is_public": is_public,
                "created_source": created_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = []
        _name = d.pop("name")
        for name_item_data in _name:

            def _parse_name_item(data: object) -> Union[None, str]:
                if data is None:
                    return data
                return cast(Union[None, str], data)

            name_item = _parse_name_item(name_item_data)

            name.append(name_item)

        start_at = []
        _start_at = d.pop("start_at")
        for start_at_item_data in _start_at:

            def _parse_start_at_item(data: object) -> Union[None, str]:
                if data is None:
                    return data
                return cast(Union[None, str], data)

            start_at_item = _parse_start_at_item(start_at_item_data)

            start_at.append(start_at_item)

        conclude_at = []
        _conclude_at = d.pop("conclude_at")
        for conclude_at_item_data in _conclude_at:

            def _parse_conclude_at_item(data: object) -> Union[None, str]:
                if data is None:
                    return data
                return cast(Union[None, str], data)

            conclude_at_item = _parse_conclude_at_item(conclude_at_item_data)

            conclude_at.append(conclude_at_item)

        is_public = []
        _is_public = d.pop("is_public")
        for is_public_item_data in _is_public:

            def _parse_is_public_item(data: object) -> Union[None, bool]:
                if data is None:
                    return data
                return cast(Union[None, bool], data)

            is_public_item = _parse_is_public_item(is_public_item_data)

            is_public.append(is_public_item)

        created_source = d.pop("created_source")

        created_event_data = cls(
            name=name,
            start_at=start_at,
            conclude_at=conclude_at,
            is_public=is_public,
            created_source=created_source,
        )

        created_event_data.additional_properties = d
        return created_event_data

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
