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
    Autohealing: Optional[bool]
    Autoscaling: Optional[bool]
    ClusterId: Optional[str]
    ContainerRuntime: Optional[str]
    CreatedAt: Optional[str]
    CurrentSize: Optional[float]
    Id: Optional[str]
    KubeletArgs: Optional[Sequence["_KubeletArgsDefinition"]]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    NodeType: Optional[str]
    Nodes: Optional[Sequence["_NodesDefinition"]]
    PlacementGroupId: Optional[str]
    Region: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    Version: Optional[str]
    WaitForPoolReady: Optional[bool]
    Zone: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpgradePolicy: Optional[Sequence["_UpgradePolicyDefinition"]]

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
            Autohealing=json_data.get("Autohealing"),
            Autoscaling=json_data.get("Autoscaling"),
            ClusterId=json_data.get("ClusterId"),
            ContainerRuntime=json_data.get("ContainerRuntime"),
            CreatedAt=json_data.get("CreatedAt"),
            CurrentSize=json_data.get("CurrentSize"),
            Id=json_data.get("Id"),
            KubeletArgs=deserialize_list(json_data.get("KubeletArgs"), KubeletArgsDefinition),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NodeType=json_data.get("NodeType"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Version=json_data.get("Version"),
            WaitForPoolReady=json_data.get("WaitForPoolReady"),
            Zone=json_data.get("Zone"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpgradePolicy=deserialize_list(json_data.get("UpgradePolicy"), UpgradePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeletArgsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeletArgsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeletArgsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeletArgsDefinition = KubeletArgsDefinition


@dataclass
class NodesDefinition(BaseModel):
    Name: Optional[str]
    PublicIp: Optional[str]
    PublicIpV6: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpV6=json_data.get("PublicIpV6"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UpgradePolicyDefinition(BaseModel):
    MaxSurge: Optional[float]
    MaxUnavailable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_UpgradePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpgradePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxSurge=json_data.get("MaxSurge"),
            MaxUnavailable=json_data.get("MaxUnavailable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpgradePolicyDefinition = UpgradePolicyDefinition


