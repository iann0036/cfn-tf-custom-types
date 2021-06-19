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
    AllowMultipleInterfaces: Optional[str]
    BounceQuarantinedLink: Optional[str]
    DefaultVirtualSwitchVlan: Optional[str]
    DynamicSortSubtable: Optional[str]
    HttpsImagePush: Optional[str]
    Id: Optional[str]
    LogMacLimitViolations: Optional[str]
    MacAgingInterval: Optional[float]
    MacEventLogging: Optional[str]
    MacRetentionPeriod: Optional[float]
    MacViolationTimer: Optional[float]
    QuarantineMode: Optional[str]
    SnDnsResolution: Optional[str]
    UpdateUserDevice: Optional[str]
    Vdomparam: Optional[str]
    VlanAllMode: Optional[str]
    VlanOptimization: Optional[str]
    CustomCommand: Optional[Sequence["_CustomCommandDefinition"]]
    DisableDiscovery: Optional[Sequence["_DisableDiscoveryDefinition"]]

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
            AllowMultipleInterfaces=json_data.get("AllowMultipleInterfaces"),
            BounceQuarantinedLink=json_data.get("BounceQuarantinedLink"),
            DefaultVirtualSwitchVlan=json_data.get("DefaultVirtualSwitchVlan"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            HttpsImagePush=json_data.get("HttpsImagePush"),
            Id=json_data.get("Id"),
            LogMacLimitViolations=json_data.get("LogMacLimitViolations"),
            MacAgingInterval=json_data.get("MacAgingInterval"),
            MacEventLogging=json_data.get("MacEventLogging"),
            MacRetentionPeriod=json_data.get("MacRetentionPeriod"),
            MacViolationTimer=json_data.get("MacViolationTimer"),
            QuarantineMode=json_data.get("QuarantineMode"),
            SnDnsResolution=json_data.get("SnDnsResolution"),
            UpdateUserDevice=json_data.get("UpdateUserDevice"),
            Vdomparam=json_data.get("Vdomparam"),
            VlanAllMode=json_data.get("VlanAllMode"),
            VlanOptimization=json_data.get("VlanOptimization"),
            CustomCommand=deserialize_list(json_data.get("CustomCommand"), CustomCommandDefinition),
            DisableDiscovery=deserialize_list(json_data.get("DisableDiscovery"), DisableDiscoveryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomCommandDefinition(BaseModel):
    CommandEntry: Optional[str]
    CommandName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCommandDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCommandDefinition"]:
        if not json_data:
            return None
        return cls(
            CommandEntry=json_data.get("CommandEntry"),
            CommandName=json_data.get("CommandName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCommandDefinition = CustomCommandDefinition


@dataclass
class DisableDiscoveryDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DisableDiscoveryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DisableDiscoveryDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DisableDiscoveryDefinition = DisableDiscoveryDefinition


