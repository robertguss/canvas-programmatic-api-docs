from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.discussion_topic_group_topic_children_item import DiscussionTopicGroupTopicChildrenItem
    from ..models.discussion_topic_permissions import DiscussionTopicPermissions


T = TypeVar("T", bound="DiscussionTopic")


@_attrs_define
class DiscussionTopic:
    """
    Attributes:
        id (int):
        title (str):
        message (str):
        html_url (str):
        posted_at (str):
        last_reply_at (str):
        require_initial_post (bool):
        user_can_see_posts (bool):
        discussion_subentry_count (int):
        read_state (str):
        unread_count (int):
        subscribed (bool):
        subscription_hold (str):
        assignment_id (None):
        delayed_post_at (None):
        published (bool):
        lock_at (None):
        locked (bool):
        pinned (bool):
        locked_for_user (bool):
        lock_info (None):
        lock_explanation (str):
        user_name (str):
        topic_children (list[int]):
        group_topic_children (list['DiscussionTopicGroupTopicChildrenItem']):
        root_topic_id (None):
        podcast_url (str):
        discussion_type (str):
        group_category_id (None):
        attachments (None):
        permissions (DiscussionTopicPermissions):
        allow_rating (bool):
        only_graders_can_rate (bool):
        sort_by_rating (bool):
        sort_order (str):
        sort_order_locked (bool):
        expand (bool):
        expand_locked (bool):
    """

    id: int
    title: str
    message: str
    html_url: str
    posted_at: str
    last_reply_at: str
    require_initial_post: bool
    user_can_see_posts: bool
    discussion_subentry_count: int
    read_state: str
    unread_count: int
    subscribed: bool
    subscription_hold: str
    assignment_id: None
    delayed_post_at: None
    published: bool
    lock_at: None
    locked: bool
    pinned: bool
    locked_for_user: bool
    lock_info: None
    lock_explanation: str
    user_name: str
    topic_children: list[int]
    group_topic_children: list["DiscussionTopicGroupTopicChildrenItem"]
    root_topic_id: None
    podcast_url: str
    discussion_type: str
    group_category_id: None
    attachments: None
    permissions: "DiscussionTopicPermissions"
    allow_rating: bool
    only_graders_can_rate: bool
    sort_by_rating: bool
    sort_order: str
    sort_order_locked: bool
    expand: bool
    expand_locked: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        message = self.message

        html_url = self.html_url

        posted_at = self.posted_at

        last_reply_at = self.last_reply_at

        require_initial_post = self.require_initial_post

        user_can_see_posts = self.user_can_see_posts

        discussion_subentry_count = self.discussion_subentry_count

        read_state = self.read_state

        unread_count = self.unread_count

        subscribed = self.subscribed

        subscription_hold = self.subscription_hold

        assignment_id = self.assignment_id

        delayed_post_at = self.delayed_post_at

        published = self.published

        lock_at = self.lock_at

        locked = self.locked

        pinned = self.pinned

        locked_for_user = self.locked_for_user

        lock_info = self.lock_info

        lock_explanation = self.lock_explanation

        user_name = self.user_name

        topic_children = self.topic_children

        group_topic_children = []
        for group_topic_children_item_data in self.group_topic_children:
            group_topic_children_item = group_topic_children_item_data.to_dict()
            group_topic_children.append(group_topic_children_item)

        root_topic_id = self.root_topic_id

        podcast_url = self.podcast_url

        discussion_type = self.discussion_type

        group_category_id = self.group_category_id

        attachments = self.attachments

        permissions = self.permissions.to_dict()

        allow_rating = self.allow_rating

        only_graders_can_rate = self.only_graders_can_rate

        sort_by_rating = self.sort_by_rating

        sort_order = self.sort_order

        sort_order_locked = self.sort_order_locked

        expand = self.expand

        expand_locked = self.expand_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "message": message,
                "html_url": html_url,
                "posted_at": posted_at,
                "last_reply_at": last_reply_at,
                "require_initial_post": require_initial_post,
                "user_can_see_posts": user_can_see_posts,
                "discussion_subentry_count": discussion_subentry_count,
                "read_state": read_state,
                "unread_count": unread_count,
                "subscribed": subscribed,
                "subscription_hold": subscription_hold,
                "assignment_id": assignment_id,
                "delayed_post_at": delayed_post_at,
                "published": published,
                "lock_at": lock_at,
                "locked": locked,
                "pinned": pinned,
                "locked_for_user": locked_for_user,
                "lock_info": lock_info,
                "lock_explanation": lock_explanation,
                "user_name": user_name,
                "topic_children": topic_children,
                "group_topic_children": group_topic_children,
                "root_topic_id": root_topic_id,
                "podcast_url": podcast_url,
                "discussion_type": discussion_type,
                "group_category_id": group_category_id,
                "attachments": attachments,
                "permissions": permissions,
                "allow_rating": allow_rating,
                "only_graders_can_rate": only_graders_can_rate,
                "sort_by_rating": sort_by_rating,
                "sort_order": sort_order,
                "sort_order_locked": sort_order_locked,
                "expand": expand,
                "expand_locked": expand_locked,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.discussion_topic_group_topic_children_item import DiscussionTopicGroupTopicChildrenItem
        from ..models.discussion_topic_permissions import DiscussionTopicPermissions

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        message = d.pop("message")

        html_url = d.pop("html_url")

        posted_at = d.pop("posted_at")

        last_reply_at = d.pop("last_reply_at")

        require_initial_post = d.pop("require_initial_post")

        user_can_see_posts = d.pop("user_can_see_posts")

        discussion_subentry_count = d.pop("discussion_subentry_count")

        read_state = d.pop("read_state")

        unread_count = d.pop("unread_count")

        subscribed = d.pop("subscribed")

        subscription_hold = d.pop("subscription_hold")

        assignment_id = d.pop("assignment_id")

        delayed_post_at = d.pop("delayed_post_at")

        published = d.pop("published")

        lock_at = d.pop("lock_at")

        locked = d.pop("locked")

        pinned = d.pop("pinned")

        locked_for_user = d.pop("locked_for_user")

        lock_info = d.pop("lock_info")

        lock_explanation = d.pop("lock_explanation")

        user_name = d.pop("user_name")

        topic_children = cast(list[int], d.pop("topic_children"))

        group_topic_children = []
        _group_topic_children = d.pop("group_topic_children")
        for group_topic_children_item_data in _group_topic_children:
            group_topic_children_item = DiscussionTopicGroupTopicChildrenItem.from_dict(group_topic_children_item_data)

            group_topic_children.append(group_topic_children_item)

        root_topic_id = d.pop("root_topic_id")

        podcast_url = d.pop("podcast_url")

        discussion_type = d.pop("discussion_type")

        group_category_id = d.pop("group_category_id")

        attachments = d.pop("attachments")

        permissions = DiscussionTopicPermissions.from_dict(d.pop("permissions"))

        allow_rating = d.pop("allow_rating")

        only_graders_can_rate = d.pop("only_graders_can_rate")

        sort_by_rating = d.pop("sort_by_rating")

        sort_order = d.pop("sort_order")

        sort_order_locked = d.pop("sort_order_locked")

        expand = d.pop("expand")

        expand_locked = d.pop("expand_locked")

        discussion_topic = cls(
            id=id,
            title=title,
            message=message,
            html_url=html_url,
            posted_at=posted_at,
            last_reply_at=last_reply_at,
            require_initial_post=require_initial_post,
            user_can_see_posts=user_can_see_posts,
            discussion_subentry_count=discussion_subentry_count,
            read_state=read_state,
            unread_count=unread_count,
            subscribed=subscribed,
            subscription_hold=subscription_hold,
            assignment_id=assignment_id,
            delayed_post_at=delayed_post_at,
            published=published,
            lock_at=lock_at,
            locked=locked,
            pinned=pinned,
            locked_for_user=locked_for_user,
            lock_info=lock_info,
            lock_explanation=lock_explanation,
            user_name=user_name,
            topic_children=topic_children,
            group_topic_children=group_topic_children,
            root_topic_id=root_topic_id,
            podcast_url=podcast_url,
            discussion_type=discussion_type,
            group_category_id=group_category_id,
            attachments=attachments,
            permissions=permissions,
            allow_rating=allow_rating,
            only_graders_can_rate=only_graders_can_rate,
            sort_by_rating=sort_by_rating,
            sort_order=sort_order,
            sort_order_locked=sort_order_locked,
            expand=expand,
            expand_locked=expand_locked,
        )

        discussion_topic.additional_properties = d
        return discussion_topic

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
