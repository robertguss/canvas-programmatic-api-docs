from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CommMessage")


@_attrs_define
class CommMessage:
    """
    Attributes:
        id (int):
        created_at (str):
        sent_at (str):
        workflow_state (str):
        from_ (str):
        from_name (str):
        to (str):
        reply_to (str):
        subject (str):
        body (str):
        html_body (str):
    """

    id: int
    created_at: str
    sent_at: str
    workflow_state: str
    from_: str
    from_name: str
    to: str
    reply_to: str
    subject: str
    body: str
    html_body: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        sent_at = self.sent_at

        workflow_state = self.workflow_state

        from_ = self.from_

        from_name = self.from_name

        to = self.to

        reply_to = self.reply_to

        subject = self.subject

        body = self.body

        html_body = self.html_body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "created_at": created_at,
                "sent_at": sent_at,
                "workflow_state": workflow_state,
                "from": from_,
                "from_name": from_name,
                "to": to,
                "reply_to": reply_to,
                "subject": subject,
                "body": body,
                "html_body": html_body,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        sent_at = d.pop("sent_at")

        workflow_state = d.pop("workflow_state")

        from_ = d.pop("from")

        from_name = d.pop("from_name")

        to = d.pop("to")

        reply_to = d.pop("reply_to")

        subject = d.pop("subject")

        body = d.pop("body")

        html_body = d.pop("html_body")

        comm_message = cls(
            id=id,
            created_at=created_at,
            sent_at=sent_at,
            workflow_state=workflow_state,
            from_=from_,
            from_name=from_name,
            to=to,
            reply_to=reply_to,
            subject=subject,
            body=body,
            html_body=html_body,
        )

        comm_message.additional_properties = d
        return comm_message

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
