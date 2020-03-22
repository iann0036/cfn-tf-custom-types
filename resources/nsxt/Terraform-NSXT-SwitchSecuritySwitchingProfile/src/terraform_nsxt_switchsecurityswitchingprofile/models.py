# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
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
    RateLimits: Optional[Sequence["_RateLimits"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            RateLimits=json_data.get("RateLimits"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RateLimits:
    Enabled: Optional[bool]
    RxBroadcast: Optional[float]
    RxMulticast: Optional[float]
    TxBroadcast: Optional[float]
    TxMulticast: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RateLimits"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RateLimits"]:
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
_RateLimits = RateLimits


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


