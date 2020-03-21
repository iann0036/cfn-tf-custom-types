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
    AllowStoppingForUpdate: Optional[bool]
    AutoRenew: Optional[bool]
    AvailabilityZone: Optional[str]
    BootDiskSize: Optional[float]
    BootDiskType: Optional[str]
    ChargeType: Optional[str]
    Cpu: Optional[float]
    CreateTime: Optional[str]
    DataDiskSize: Optional[float]
    DataDiskType: Optional[str]
    DiskSet: Optional[Sequence["_DiskSet"]]
    Duration: Optional[float]
    ExpireTime: Optional[str]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    IpSet: Optional[Sequence["_IpSet"]]
    IsolationGroup: Optional[str]
    Memory: Optional[float]
    Name: Optional[str]
    PrivateIp: Optional[str]
    Remark: Optional[str]
    RootPassword: Optional[str]
    SecurityGroup: Optional[str]
    Status: Optional[str]
    SubnetId: Optional[str]
    Tag: Optional[str]
    VpcId: Optional[str]
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
            AllowStoppingForUpdate=json_data.get("AllowStoppingForUpdate"),
            AutoRenew=json_data.get("AutoRenew"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BootDiskSize=json_data.get("BootDiskSize"),
            BootDiskType=json_data.get("BootDiskType"),
            ChargeType=json_data.get("ChargeType"),
            Cpu=json_data.get("Cpu"),
            CreateTime=json_data.get("CreateTime"),
            DataDiskSize=json_data.get("DataDiskSize"),
            DataDiskType=json_data.get("DataDiskType"),
            DiskSet=json_data.get("DiskSet"),
            Duration=json_data.get("Duration"),
            ExpireTime=json_data.get("ExpireTime"),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            IpSet=json_data.get("IpSet"),
            IsolationGroup=json_data.get("IsolationGroup"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            Remark=json_data.get("Remark"),
            RootPassword=json_data.get("RootPassword"),
            SecurityGroup=json_data.get("SecurityGroup"),
            Status=json_data.get("Status"),
            SubnetId=json_data.get("SubnetId"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DiskSet:
    Id: Optional[str]
    IsBoot: Optional[bool]
    Size: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DiskSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DiskSet"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IsBoot=json_data.get("IsBoot"),
            Size=json_data.get("Size"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DiskSet = DiskSet


@dataclass
class IpSet:
    InternetType: Optional[str]
    Ip: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpSet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpSet"]:
        if not json_data:
            return None
        return cls(
            InternetType=json_data.get("InternetType"),
            Ip=json_data.get("Ip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpSet = IpSet


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


