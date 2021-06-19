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
    AutoRenewFlag: Optional[float]
    AvailableZone: Optional[str]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    MachineType: Optional[str]
    Memory: Optional[float]
    Password: Optional[str]
    PrepaidPeriod: Optional[float]
    ProjectId: Optional[float]
    SecurityGroups: Optional[Sequence[str]]
    StandbyInstanceList: Optional[Sequence["_StandbyInstanceListDefinition"]]
    Status: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Vip: Optional[str]
    Volume: Optional[float]
    VpcId: Optional[str]
    Vport: Optional[float]

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
            AutoRenewFlag=json_data.get("AutoRenewFlag"),
            AvailableZone=json_data.get("AvailableZone"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            MachineType=json_data.get("MachineType"),
            Memory=json_data.get("Memory"),
            Password=json_data.get("Password"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            ProjectId=json_data.get("ProjectId"),
            SecurityGroups=json_data.get("SecurityGroups"),
            StandbyInstanceList=deserialize_list(json_data.get("StandbyInstanceList"), StandbyInstanceListDefinition),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Vip=json_data.get("Vip"),
            Volume=json_data.get("Volume"),
            VpcId=json_data.get("VpcId"),
            Vport=json_data.get("Vport"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StandbyInstanceListDefinition(BaseModel):
    StandbyInstanceId: Optional[str]
    StandbyInstanceRegion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StandbyInstanceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StandbyInstanceListDefinition"]:
        if not json_data:
            return None
        return cls(
            StandbyInstanceId=json_data.get("StandbyInstanceId"),
            StandbyInstanceRegion=json_data.get("StandbyInstanceRegion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StandbyInstanceListDefinition = StandbyInstanceListDefinition


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


