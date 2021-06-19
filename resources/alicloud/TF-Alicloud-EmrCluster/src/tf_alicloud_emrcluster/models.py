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
    ChargeType: Optional[str]
    ClusterType: Optional[str]
    DepositType: Optional[str]
    EasEnable: Optional[bool]
    EmrVer: Optional[str]
    HighAvailabilityEnable: Optional[bool]
    Id: Optional[str]
    IsOpenPublicIp: Optional[bool]
    KeyPairName: Optional[str]
    MasterPwd: Optional[str]
    Name: Optional[str]
    OptionSoftwareList: Optional[Sequence[str]]
    Period: Optional[float]
    RelatedClusterId: Optional[str]
    SecurityGroupId: Optional[str]
    SshEnable: Optional[bool]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UseLocalMetadb: Optional[bool]
    UserDefinedEmrEcsRole: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    BootstrapAction: Optional[Sequence["_BootstrapActionDefinition"]]
    HostGroup: Optional[Sequence["_HostGroupDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            ChargeType=json_data.get("ChargeType"),
            ClusterType=json_data.get("ClusterType"),
            DepositType=json_data.get("DepositType"),
            EasEnable=json_data.get("EasEnable"),
            EmrVer=json_data.get("EmrVer"),
            HighAvailabilityEnable=json_data.get("HighAvailabilityEnable"),
            Id=json_data.get("Id"),
            IsOpenPublicIp=json_data.get("IsOpenPublicIp"),
            KeyPairName=json_data.get("KeyPairName"),
            MasterPwd=json_data.get("MasterPwd"),
            Name=json_data.get("Name"),
            OptionSoftwareList=json_data.get("OptionSoftwareList"),
            Period=json_data.get("Period"),
            RelatedClusterId=json_data.get("RelatedClusterId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SshEnable=json_data.get("SshEnable"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UseLocalMetadb=json_data.get("UseLocalMetadb"),
            UserDefinedEmrEcsRole=json_data.get("UserDefinedEmrEcsRole"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            BootstrapAction=deserialize_list(json_data.get("BootstrapAction"), BootstrapActionDefinition),
            HostGroup=deserialize_list(json_data.get("HostGroup"), HostGroupDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


@dataclass
class BootstrapActionDefinition(BaseModel):
    Arg: Optional[str]
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Arg=json_data.get("Arg"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapActionDefinition = BootstrapActionDefinition


@dataclass
class HostGroupDefinition(BaseModel):
    AutoRenew: Optional[bool]
    ChargeType: Optional[str]
    DiskCapacity: Optional[str]
    DiskCount: Optional[str]
    DiskType: Optional[str]
    GpuDriver: Optional[str]
    HostGroupName: Optional[str]
    HostGroupType: Optional[str]
    InstanceList: Optional[str]
    InstanceType: Optional[str]
    NodeCount: Optional[str]
    Period: Optional[float]
    SysDiskCapacity: Optional[str]
    SysDiskType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoRenew=json_data.get("AutoRenew"),
            ChargeType=json_data.get("ChargeType"),
            DiskCapacity=json_data.get("DiskCapacity"),
            DiskCount=json_data.get("DiskCount"),
            DiskType=json_data.get("DiskType"),
            GpuDriver=json_data.get("GpuDriver"),
            HostGroupName=json_data.get("HostGroupName"),
            HostGroupType=json_data.get("HostGroupType"),
            InstanceList=json_data.get("InstanceList"),
            InstanceType=json_data.get("InstanceType"),
            NodeCount=json_data.get("NodeCount"),
            Period=json_data.get("Period"),
            SysDiskCapacity=json_data.get("SysDiskCapacity"),
            SysDiskType=json_data.get("SysDiskType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostGroupDefinition = HostGroupDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


