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
    AutoReleaseTime: Optional[str]
    Description: Optional[str]
    HostName: Optional[str]
    ImageId: Optional[str]
    ImageOwnerAlias: Optional[str]
    InstanceChargeType: Optional[str]
    InstanceName: Optional[str]
    InstanceType: Optional[str]
    InternetChargeType: Optional[str]
    InternetMaxBandwidthIn: Optional[float]
    InternetMaxBandwidthOut: Optional[float]
    IoOptimized: Optional[str]
    KeyPairName: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    RamRoleName: Optional[str]
    ResourceGroupId: Optional[str]
    SecurityEnhancementStrategy: Optional[str]
    SecurityGroupId: Optional[str]
    SpotPriceLimit: Optional[float]
    SpotStrategy: Optional[str]
    SystemDiskCategory: Optional[str]
    SystemDiskDescription: Optional[str]
    SystemDiskName: Optional[str]
    SystemDiskSize: Optional[float]
    Tags: Optional[Sequence["_Tags"]]
    Userdata: Optional[str]
    VpcId: Optional[str]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    DataDisks: Optional[Sequence["_DataDisks"]]
    NetworkInterfaces: Optional[Sequence["_NetworkInterfaces"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoReleaseTime=json_data.get("AutoReleaseTime"),
            Description=json_data.get("Description"),
            HostName=json_data.get("HostName"),
            ImageId=json_data.get("ImageId"),
            ImageOwnerAlias=json_data.get("ImageOwnerAlias"),
            InstanceChargeType=json_data.get("InstanceChargeType"),
            InstanceName=json_data.get("InstanceName"),
            InstanceType=json_data.get("InstanceType"),
            InternetChargeType=json_data.get("InternetChargeType"),
            InternetMaxBandwidthIn=json_data.get("InternetMaxBandwidthIn"),
            InternetMaxBandwidthOut=json_data.get("InternetMaxBandwidthOut"),
            IoOptimized=json_data.get("IoOptimized"),
            KeyPairName=json_data.get("KeyPairName"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            RamRoleName=json_data.get("RamRoleName"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityEnhancementStrategy=json_data.get("SecurityEnhancementStrategy"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SpotPriceLimit=json_data.get("SpotPriceLimit"),
            SpotStrategy=json_data.get("SpotStrategy"),
            SystemDiskCategory=json_data.get("SystemDiskCategory"),
            SystemDiskDescription=json_data.get("SystemDiskDescription"),
            SystemDiskName=json_data.get("SystemDiskName"),
            SystemDiskSize=json_data.get("SystemDiskSize"),
            Tags=json_data.get("Tags"),
            Userdata=json_data.get("Userdata"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            DataDisks=json_data.get("DataDisks"),
            NetworkInterfaces=json_data.get("NetworkInterfaces"),
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
    Category: Optional[str]
    DeleteWithInstance: Optional[bool]
    Description: Optional[str]
    Encrypted: Optional[bool]
    Name: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DataDisks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DataDisks"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            DeleteWithInstance=json_data.get("DeleteWithInstance"),
            Description=json_data.get("Description"),
            Encrypted=json_data.get("Encrypted"),
            Name=json_data.get("Name"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DataDisks = DataDisks


@dataclass
class NetworkInterfaces:
    Description: Optional[str]
    Name: Optional[str]
    PrimaryIp: Optional[str]
    SecurityGroupId: Optional[str]
    VswitchId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInterfaces"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInterfaces"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            PrimaryIp=json_data.get("PrimaryIp"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            VswitchId=json_data.get("VswitchId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInterfaces = NetworkInterfaces


