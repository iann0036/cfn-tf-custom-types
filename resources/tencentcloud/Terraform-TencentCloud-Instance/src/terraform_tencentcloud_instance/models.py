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
    AllocatePublicIp: Optional[bool]
    AvailabilityZone: Optional[str]
    CreateTime: Optional[str]
    DisableMonitorService: Optional[bool]
    DisableSecurityService: Optional[bool]
    ExpiredTime: Optional[str]
    Hostname: Optional[str]
    ImageId: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceChargeTypePrepaidPeriod: Optional[float]
    InstanceChargeTypePrepaidRenewFlag: Optional[str]
    InstanceName: Optional[str]
    InstanceStatus: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthOut: Optional[float]
    KeyName: Optional[str]
    Password: Optional[str]
    PlacementGroupId: Optional[str]
    PrivateIp: Optional[str]
    ProjectId: Optional[float]
    PublicIp: Optional[str]
    RunningFlag: Optional[bool]
    SecurityGroups: Optional[Sequence[str]]
    SpotInstanceType: Optional[str]
    SpotMaxPrice: Optional[str]
    SubnetId: Optional[str]
    SystemDiskId: Optional[str]
    SystemDiskSize: Optional[float]
    SystemDiskType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    UserData: Optional[str]
    UserDataRaw: Optional[str]
    VpcId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisks"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllocatePublicIp=json_data.get("AllocatePublicIp"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            CreateTime=json_data.get("CreateTime"),
            DisableMonitorService=json_data.get("DisableMonitorService"),
            DisableSecurityService=json_data.get("DisableSecurityService"),
            ExpiredTime=json_data.get("ExpiredTime"),
            Hostname=json_data.get("Hostname"),
            ImageId=json_data.get("ImageId"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceChargeTypePrepaidPeriod=json_data.get("InstanceChargeTypePrepaidPeriod"),
            InstanceChargeTypePrepaidRenewFlag=json_data.get("InstanceChargeTypePrepaidRenewFlag"),
            InstanceName=json_data.get("InstanceName"),
            InstanceStatus=json_data.get("InstanceStatus"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            KeyName=json_data.get("KeyName"),
            Password=json_data.get("Password"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            PrivateIp=json_data.get("PrivateIp"),
            ProjectId=json_data.get("ProjectId"),
            PublicIp=json_data.get("PublicIp"),
            RunningFlag=json_data.get("RunningFlag"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotInstanceType=json_data.get("SpotInstanceType"),
            SpotMaxPrice=json_data.get("SpotMaxPrice"),
            SubnetId=json_data.get("SubnetId"),
            SystemDiskId=json_data.get("SystemDiskId"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            SystemDiskType=json_data.get("SystemDiskType"),
            Tags=json_data.get("Tags"),
            UserData=json_data.get("UserData"),
            UserDataRaw=json_data.get("UserDataRaw"),
            VpcId=json_data.get("VpcId"),
            DataDisks=json_data.get("DataDisks"),
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
class DataDisks:
    DataDiskId: Optional[str]
    DataDiskSize: Optional[float]
    DataDiskType: Optional[str]
    DeleteWithInstance: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisks"]:
        if not json_data:
            return None
        return cls(
            DataDiskId=json_data.get("DataDiskId"),
            DataDiskSize=json_data.get("DataDiskSize"),
            DataDiskType=json_data.get("DataDiskType"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisks = DataDisks


