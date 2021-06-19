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
    AvailabilityZone: Optional[str]
    ChargeType: Optional[str]
    EngineVersion: Optional[str]
    FirstSlaveZone: Optional[str]
    ForceDelete: Optional[bool]
    Gtid: Optional[float]
    Id: Optional[str]
    InstanceName: Optional[str]
    InternetHost: Optional[str]
    InternetPort: Optional[float]
    InternetService: Optional[float]
    IntranetIp: Optional[str]
    IntranetPort: Optional[float]
    Locked: Optional[float]
    MemSize: Optional[float]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    PayType: Optional[float]
    Period: Optional[float]
    PrepaidPeriod: Optional[float]
    ProjectId: Optional[float]
    RootPassword: Optional[str]
    SecondSlaveZone: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SlaveDeployMode: Optional[float]
    SlaveSyncMode: Optional[float]
    Status: Optional[float]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TaskStatus: Optional[float]
    VolumeSize: Optional[float]
    VpcId: Optional[str]

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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            ChargeType=json_data.get("ChargeType"),
            EngineVersion=json_data.get("EngineVersion"),
            FirstSlaveZone=json_data.get("FirstSlaveZone"),
            ForceDelete=json_data.get("ForceDelete"),
            Gtid=json_data.get("Gtid"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            InternetHost=json_data.get("InternetHost"),
            InternetPort=json_data.get("InternetPort"),
            InternetService=json_data.get("InternetService"),
            IntranetIp=json_data.get("IntranetIp"),
            IntranetPort=json_data.get("IntranetPort"),
            Locked=json_data.get("Locked"),
            MemSize=json_data.get("MemSize"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            PayType=json_data.get("PayType"),
            Period=json_data.get("Period"),
            PrepaidPeriod=json_data.get("PrepaidPeriod"),
            ProjectId=json_data.get("ProjectId"),
            RootPassword=json_data.get("RootPassword"),
            SecondSlaveZone=json_data.get("SecondSlaveZone"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SlaveDeployMode=json_data.get("SlaveDeployMode"),
            SlaveSyncMode=json_data.get("SlaveSyncMode"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TaskStatus=json_data.get("TaskStatus"),
            VolumeSize=json_data.get("VolumeSize"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


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


