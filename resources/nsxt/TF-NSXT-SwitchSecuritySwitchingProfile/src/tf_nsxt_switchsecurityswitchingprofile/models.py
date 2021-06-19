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
    BlockClientDhcp: Optional[bool]
    BlockNonIp: Optional[bool]
    BlockServerDhcp: Optional[bool]
    BpduFilterEnabled: Optional[bool]
    BpduFilterWhitelist: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Revision: Optional[float]
    RateLimits: Optional[Sequence["_RateLimitsDefinition"]]
    Tag: Optional[Sequence["_TagDefinition"]]

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
            BlockClientDhcp=json_data.get("BlockClientDhcp"),
            BlockNonIp=json_data.get("BlockNonIp"),
            BlockServerDhcp=json_data.get("BlockServerDhcp"),
            BpduFilterEnabled=json_data.get("BpduFilterEnabled"),
            BpduFilterWhitelist=json_data.get("BpduFilterWhitelist"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Revision=json_data.get("Revision"),
            RateLimits=deserialize_list(json_data.get("RateLimits"), RateLimitsDefinition),
            Tag=deserialize_list(json_data.get("Tag"), TagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RateLimitsDefinition(BaseModel):
    Enabled: Optional[bool]
    RxBroadcast: Optional[float]
    RxMulticast: Optional[float]
    TxBroadcast: Optional[float]
    TxMulticast: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimitsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimitsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            RxBroadcast=json_data.get("RxBroadcast"),
            RxMulticast=json_data.get("RxMulticast"),
            TxBroadcast=json_data.get("TxBroadcast"),
            TxMulticast=json_data.get("TxMulticast"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RateLimitsDefinition = RateLimitsDefinition


@dataclass
class TagDefinition(BaseModel):
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagDefinition"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagDefinition = TagDefinition


