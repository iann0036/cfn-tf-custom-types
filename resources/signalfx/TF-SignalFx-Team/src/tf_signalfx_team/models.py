# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Members: Optional[Sequence[str]]
    Name: Optional[str]
    NotificationsCritical: Optional[Sequence[str]]
    NotificationsDefault: Optional[Sequence[str]]
    NotificationsInfo: Optional[Sequence[str]]
    NotificationsMajor: Optional[Sequence[str]]
    NotificationsMinor: Optional[Sequence[str]]
    NotificationsWarning: Optional[Sequence[str]]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Members=json_data.get("Members"),
            Name=json_data.get("Name"),
            NotificationsCritical=json_data.get("NotificationsCritical"),
            NotificationsDefault=json_data.get("NotificationsDefault"),
            NotificationsInfo=json_data.get("NotificationsInfo"),
            NotificationsMajor=json_data.get("NotificationsMajor"),
            NotificationsMinor=json_data.get("NotificationsMinor"),
            NotificationsWarning=json_data.get("NotificationsWarning"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


