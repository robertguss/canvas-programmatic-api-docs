from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (int):
        subject (str):
        workflow_state (str):
        last_message (str):
        start_at (str):
        message_count (int):
        subscribed (bool):
        private (bool):
        starred (bool):
        properties (None):
        audience (None):
        audience_contexts (None):
        avatar_url (str):
        participants (None):
        visible (bool):
        context_name (str):
    """

    id: int
    subject: str
    workflow_state: str
    last_message: str
    start_at: str
    message_count: int
    subscribed: bool
    private: bool
    starred: bool
    properties: None
    audience: None
    audience_contexts: None
    avatar_url: str
    participants: None
    visible: bool
    context_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subject = self.subject

        workflow_state = self.workflow_state

        last_message = self.last_message

        start_at = self.start_at

        message_count = self.message_count

        subscribed = self.subscribed

        private = self.private

        starred = self.starred

        properties = self.properties

        audience = self.audience

        audience_contexts = self.audience_contexts

        avatar_url = self.avatar_url

        participants = self.participants

        visible = self.visible

        context_name = self.context_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subject": subject,
                "workflow_state": workflow_state,
                "last_message": last_message,
                "start_at": start_at,
                "message_count": message_count,
                "subscribed": subscribed,
                "private": private,
                "starred": starred,
                "properties": properties,
                "audience": audience,
                "audience_contexts": audience_contexts,
                "avatar_url": avatar_url,
                "participants": participants,
                "visible": visible,
                "context_name": context_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        subject = d.pop("subject")

        workflow_state = d.pop("workflow_state")

        last_message = d.pop("last_message")

        start_at = d.pop("start_at")

        message_count = d.pop("message_count")

        subscribed = d.pop("subscribed")

        private = d.pop("private")

        starred = d.pop("starred")

        properties = d.pop("properties")

        audience = d.pop("audience")

        audience_contexts = d.pop("audience_contexts")

        avatar_url = d.pop("avatar_url")

        participants = d.pop("participants")

        visible = d.pop("visible")

        context_name = d.pop("context_name")

        conversation = cls(
            id=id,
            subject=subject,
            workflow_state=workflow_state,
            last_message=last_message,
            start_at=start_at,
            message_count=message_count,
            subscribed=subscribed,
            private=private,
            starred=starred,
            properties=properties,
            audience=audience,
            audience_contexts=audience_contexts,
            avatar_url=avatar_url,
            participants=participants,
            visible=visible,
            context_name=context_name,
        )

        conversation.additional_properties = d
        return conversation

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
