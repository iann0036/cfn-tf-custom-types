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
    RelatedClusterId: Optional[str]
    SecurityGroupId: Optional[str]
    SshEnable: Optional[bool]
    Tags: Optional[Sequence["_Tags"]]
    UseLocalMetadb: Optional[bool]
    UserDefinedEmrEcsRole: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    BootstrapAction: Optional[Sequence["_BootstrapAction"]]
    HostGroup: Optional[Sequence["_HostGroup"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
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
            RelatedClusterId=json_data.get("RelatedClusterId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SshEnable=json_data.get("SshEnable"),
            Tags=json_data.get("Tags"),
            UseLocalMetadb=json_data.get("UseLocalMetadb"),
            UserDefinedEmrEcsRole=json_data.get("UserDefinedEmrEcsRole"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            BootstrapAction=json_data.get("BootstrapAction"),
            HostGroup=json_data.get("HostGroup"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class BootstrapAction:
    Arg: Optional[str]
    Name: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BootstrapAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BootstrapAction"]:
        if not json_data:
            return None
        return cls(
            Arg=json_data.get("Arg"),
            Name=json_data.get("Name"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BootstrapAction = BootstrapAction


@dataclass
class HostGroup:
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
        cls: Type["_HostGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostGroup"]:
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
_HostGroup = HostGroup


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


