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
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv6: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    LoadBalancerType: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[float]
    NetworkIp: Optional[str]
    NetworkZone: Optional[str]
    Algorithm: Optional[Sequence["_AlgorithmDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]

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
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            LoadBalancerType=json_data.get("LoadBalancerType"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NetworkIp=json_data.get("NetworkIp"),
            NetworkZone=json_data.get("NetworkZone"),
            Algorithm=deserialize_list(json_data.get("Algorithm"), AlgorithmDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AlgorithmDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlgorithmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlgorithmDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlgorithmDefinition = AlgorithmDefinition


@dataclass
class TargetDefinition(BaseModel):
    ServerId: Optional[float]
    Type: Optional[str]
    UsePrivateIp: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            ServerId=json_data.get("ServerId"),
            Type=json_data.get("Type"),
            UsePrivateIp=json_data.get("UsePrivateIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


