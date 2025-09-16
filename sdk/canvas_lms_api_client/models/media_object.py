from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.media_object_media_sources_item import MediaObjectMediaSourcesItem
    from ..models.media_object_media_tracks_item import MediaObjectMediaTracksItem


T = TypeVar("T", bound="MediaObject")


@_attrs_define
class MediaObject:
    """
    Attributes:
        can_add_captions (bool):
        user_entered_title (str):
        title (str):
        media_id (str):
        media_type (str):
        media_tracks (list['MediaObjectMediaTracksItem']):
        media_sources (list['MediaObjectMediaSourcesItem']):
    """

    can_add_captions: bool
    user_entered_title: str
    title: str
    media_id: str
    media_type: str
    media_tracks: list["MediaObjectMediaTracksItem"]
    media_sources: list["MediaObjectMediaSourcesItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_add_captions = self.can_add_captions

        user_entered_title = self.user_entered_title

        title = self.title

        media_id = self.media_id

        media_type = self.media_type

        media_tracks = []
        for media_tracks_item_data in self.media_tracks:
            media_tracks_item = media_tracks_item_data.to_dict()
            media_tracks.append(media_tracks_item)

        media_sources = []
        for media_sources_item_data in self.media_sources:
            media_sources_item = media_sources_item_data.to_dict()
            media_sources.append(media_sources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "can_add_captions": can_add_captions,
                "user_entered_title": user_entered_title,
                "title": title,
                "media_id": media_id,
                "media_type": media_type,
                "media_tracks": media_tracks,
                "media_sources": media_sources,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.media_object_media_sources_item import MediaObjectMediaSourcesItem
        from ..models.media_object_media_tracks_item import MediaObjectMediaTracksItem

        d = dict(src_dict)
        can_add_captions = d.pop("can_add_captions")

        user_entered_title = d.pop("user_entered_title")

        title = d.pop("title")

        media_id = d.pop("media_id")

        media_type = d.pop("media_type")

        media_tracks = []
        _media_tracks = d.pop("media_tracks")
        for media_tracks_item_data in _media_tracks:
            media_tracks_item = MediaObjectMediaTracksItem.from_dict(media_tracks_item_data)

            media_tracks.append(media_tracks_item)

        media_sources = []
        _media_sources = d.pop("media_sources")
        for media_sources_item_data in _media_sources:
            media_sources_item = MediaObjectMediaSourcesItem.from_dict(media_sources_item_data)

            media_sources.append(media_sources_item)

        media_object = cls(
            can_add_captions=can_add_captions,
            user_entered_title=user_entered_title,
            title=title,
            media_id=media_id,
            media_type=media_type,
            media_tracks=media_tracks,
            media_sources=media_sources,
        )

        media_object.additional_properties = d
        return media_object

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
