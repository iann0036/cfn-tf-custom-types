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
    Id: Optional[str]
    Region: Optional[str]
    ScalingConfigurationName: Optional[str]
    InstanceConfig: Optional[Sequence["_InstanceConfig"]]
    Disk: Optional[Sequence["_Disk"]]
    Personality: Optional[Sequence["_Personality"]]
    PublicIp: Optional[Sequence["_PublicIp"]]
    Eip: Optional[Sequence["_Eip"]]
    Bandwidth: Optional[Sequence["_Bandwidth"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            Region=json_data.get("Region"),
            ScalingConfigurationName=json_data.get("ScalingConfigurationName"),
            InstanceConfig=json_data.get("InstanceConfig"),
            Disk=json_data.get("Disk"),
            Personality=json_data.get("Personality"),
            PublicIp=json_data.get("PublicIp"),
            Eip=json_data.get("Eip"),
            Bandwidth=json_data.get("Bandwidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InstanceConfig:
    Flavor: Optional[str]
    Image: Optional[str]
    InstanceId: Optional[str]
    KeyName: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    UserData: Optional[str]
    Disk: Optional[Sequence["_Disk"]]
    Personality: Optional[Sequence["_Personality"]]
    PublicIp: Optional[Sequence["_PublicIp"]]

    @classmethod
    def _deserialize(
        cls: Type["_InstanceConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InstanceConfig"]:
        if not json_data:
            return None
        return cls(
            Flavor=json_data.get("Flavor"),
            Image=json_data.get("Image"),
            InstanceId=json_data.get("InstanceId"),
            KeyName=json_data.get("KeyName"),
            Metadata=json_data.get("Metadata"),
            UserData=json_data.get("UserData"),
            Disk=json_data.get("Disk"),
            Personality=json_data.get("Personality"),
            PublicIp=json_data.get("PublicIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InstanceConfig = InstanceConfig


@dataclass
class Metadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Metadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Metadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Metadata = Metadata


@dataclass
class Disk:
    DiskType: Optional[str]
    KmsId: Optional[str]
    Size: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Disk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Disk"]:
        if not json_data:
            return None
        return cls(
            DiskType=json_data.get("DiskType"),
            KmsId=json_data.get("KmsId"),
            Size=json_data.get("Size"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Disk = Disk


@dataclass
class Personality:
    Content: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Personality"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Personality"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Personality = Personality


@dataclass
class PublicIp:
    Eip: Optional[Sequence["_Eip"]]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIp"]:
        if not json_data:
            return None
        return cls(
            Eip=json_data.get("Eip"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIp = PublicIp


@dataclass
class Eip:
    IpType: Optional[str]
    Bandwidth: Optional[Sequence["_Bandwidth"]]

    @classmethod
    def _deserialize(
        cls: Type["_Eip"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Eip"]:
        if not json_data:
            return None
        return cls(
            IpType=json_data.get("IpType"),
            Bandwidth=json_data.get("Bandwidth"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Eip = Eip


@dataclass
class Bandwidth:
    ChargingMode: Optional[str]
    ShareType: Optional[str]
    Size: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Bandwidth"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bandwidth"]:
        if not json_data:
            return None
        return cls(
            ChargingMode=json_data.get("ChargingMode"),
            ShareType=json_data.get("ShareType"),
            Size=json_data.get("Size"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bandwidth = Bandwidth


