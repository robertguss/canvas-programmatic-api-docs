from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDateDetailsResponse200Item")


@_attrs_define
class GetDateDetailsResponse200Item:
    """
    Attributes:
        id (int):
        due_at (str):
        lock_at (str):
        reply_to_topic_due_at (str):
        required_replies_due_at (str):
        unlock_at (str):
        only_visible_to_overrides (bool):
        graded (bool):
        blueprint_date_locks (list[str]):
        visible_to_everyone (bool):
        overrides (None):
        checkpoints (None):
        tag (str):
    """

    id: int
    due_at: str
    lock_at: str
    reply_to_topic_due_at: str
    required_replies_due_at: str
    unlock_at: str
    only_visible_to_overrides: bool
    graded: bool
    blueprint_date_locks: list[str]
    visible_to_everyone: bool
    overrides: None
    checkpoints: None
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        due_at = self.due_at

        lock_at = self.lock_at

        reply_to_topic_due_at = self.reply_to_topic_due_at

        required_replies_due_at = self.required_replies_due_at

        unlock_at = self.unlock_at

        only_visible_to_overrides = self.only_visible_to_overrides

        graded = self.graded

        blueprint_date_locks = self.blueprint_date_locks

        visible_to_everyone = self.visible_to_everyone

        overrides = self.overrides

        checkpoints = self.checkpoints

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "due_at": due_at,
                "lock_at": lock_at,
                "reply_to_topic_due_at": reply_to_topic_due_at,
                "required_replies_due_at": required_replies_due_at,
                "unlock_at": unlock_at,
                "only_visible_to_overrides": only_visible_to_overrides,
                "graded": graded,
                "blueprint_date_locks": blueprint_date_locks,
                "visible_to_everyone": visible_to_everyone,
                "overrides": overrides,
                "checkpoints": checkpoints,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        due_at = d.pop("due_at")

        lock_at = d.pop("lock_at")

        reply_to_topic_due_at = d.pop("reply_to_topic_due_at")

        required_replies_due_at = d.pop("required_replies_due_at")

        unlock_at = d.pop("unlock_at")

        only_visible_to_overrides = d.pop("only_visible_to_overrides")

        graded = d.pop("graded")

        blueprint_date_locks = cast(list[str], d.pop("blueprint_date_locks"))

        visible_to_everyone = d.pop("visible_to_everyone")

        overrides = d.pop("overrides")

        checkpoints = d.pop("checkpoints")

        tag = d.pop("tag")

        get_date_details_response_200_item = cls(
            id=id,
            due_at=due_at,
            lock_at=lock_at,
            reply_to_topic_due_at=reply_to_topic_due_at,
            required_replies_due_at=required_replies_due_at,
            unlock_at=unlock_at,
            only_visible_to_overrides=only_visible_to_overrides,
            graded=graded,
            blueprint_date_locks=blueprint_date_locks,
            visible_to_everyone=visible_to_everyone,
            overrides=overrides,
            checkpoints=checkpoints,
            tag=tag,
        )

        get_date_details_response_200_item.additional_properties = d
        return get_date_details_response_200_item

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
