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
    Action: Optional[str]
    ArpRetry: Optional[float]
    DeadTimer: Optional[float]
    DeviceId: Optional[float]
    DisableDefaultVrid: Optional[float]
    ForwardL4PacketOnStandby: Optional[float]
    GetReadyTime: Optional[float]
    HelloInterval: Optional[float]
    Id: Optional[str]
    PreemptionDelay: Optional[float]
    RestartTime: Optional[float]
    SetId: Optional[float]
    TrackEventDelay: Optional[float]
    Uuid: Optional[str]
    HostidAppendToVrid: Optional[Sequence["_HostidAppendToVridDefinition"]]
    InlineModeCfg: Optional[Sequence["_InlineModeCfgDefinition"]]

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
            Action=json_data.get("Action"),
            ArpRetry=json_data.get("ArpRetry"),
            DeadTimer=json_data.get("DeadTimer"),
            DeviceId=json_data.get("DeviceId"),
            DisableDefaultVrid=json_data.get("DisableDefaultVrid"),
            ForwardL4PacketOnStandby=json_data.get("ForwardL4PacketOnStandby"),
            GetReadyTime=json_data.get("GetReadyTime"),
            HelloInterval=json_data.get("HelloInterval"),
            Id=json_data.get("Id"),
            PreemptionDelay=json_data.get("PreemptionDelay"),
            RestartTime=json_data.get("RestartTime"),
            SetId=json_data.get("SetId"),
            TrackEventDelay=json_data.get("TrackEventDelay"),
            Uuid=json_data.get("Uuid"),
            HostidAppendToVrid=deserialize_list(json_data.get("HostidAppendToVrid"), HostidAppendToVridDefinition),
            InlineModeCfg=deserialize_list(json_data.get("InlineModeCfg"), InlineModeCfgDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HostidAppendToVridDefinition(BaseModel):
    HostidAppendToVridDefault: Optional[float]
    HostidAppendToVridValue: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HostidAppendToVridDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostidAppendToVridDefinition"]:
        if not json_data:
            return None
        return cls(
            HostidAppendToVridDefault=json_data.get("HostidAppendToVridDefault"),
            HostidAppendToVridValue=json_data.get("HostidAppendToVridValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostidAppendToVridDefinition = HostidAppendToVridDefinition


@dataclass
class InlineModeCfgDefinition(BaseModel):
    InlineMode: Optional[float]
    PreferredPort: Optional[float]
    PreferredTrunk: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_InlineModeCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InlineModeCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            InlineMode=json_data.get("InlineMode"),
            PreferredPort=json_data.get("PreferredPort"),
            PreferredTrunk=json_data.get("PreferredTrunk"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InlineModeCfgDefinition = InlineModeCfgDefinition


