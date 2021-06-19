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
    Arn: Optional[str]
    AssociatePublicIpAddress: Optional[bool]
    EbsOptimized: Optional[bool]
    EnableMonitoring: Optional[bool]
    IamInstanceProfile: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    InstanceType: Optional[str]
    KeyName: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    PlacementTenancy: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SpotPrice: Optional[str]
    UserData: Optional[str]
    UserDataBase64: Optional[str]
    VpcClassicLinkId: Optional[str]
    VpcClassicLinkSecurityGroups: Optional[Sequence[str]]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDeviceDefinition"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDeviceDefinition"]]
    MetadataOptions: Optional[Sequence["_MetadataOptionsDefinition"]]
    RootBlockDevice: Optional[Sequence["_RootBlockDeviceDefinition"]]

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
            Arn=json_data.get("Arn"),
            AssociatePublicIpAddress=json_data.get("AssociatePublicIpAddress"),
            EbsOptimized=json_data.get("EbsOptimized"),
            EnableMonitoring=json_data.get("EnableMonitoring"),
            IamInstanceProfile=json_data.get("IamInstanceProfile"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            InstanceType=json_data.get("InstanceType"),
            KeyName=json_data.get("KeyName"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            PlacementTenancy=json_data.get("PlacementTenancy"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SpotPrice=json_data.get("SpotPrice"),
            UserData=json_data.get("UserData"),
            UserDataBase64=json_data.get("UserDataBase64"),
            VpcClassicLinkId=json_data.get("VpcClassicLinkId"),
            VpcClassicLinkSecurityGroups=json_data.get("VpcClassicLinkSecurityGroups"),
            EbsBlockDevice=deserialize_list(json_data.get("EbsBlockDevice"), EbsBlockDeviceDefinition),
            EphemeralBlockDevice=deserialize_list(json_data.get("EphemeralBlockDevice"), EphemeralBlockDeviceDefinition),
            MetadataOptions=deserialize_list(json_data.get("MetadataOptions"), MetadataOptionsDefinition),
            RootBlockDevice=deserialize_list(json_data.get("RootBlockDevice"), RootBlockDeviceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EbsBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    NoDevice: Optional[bool]
    SnapshotId: Optional[str]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            DeviceName=json_data.get("DeviceName"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            NoDevice=json_data.get("NoDevice"),
            SnapshotId=json_data.get("SnapshotId"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsBlockDeviceDefinition = EbsBlockDeviceDefinition


@dataclass
class EphemeralBlockDeviceDefinition(BaseModel):
    DeviceName: Optional[str]
    VirtualName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EphemeralBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EphemeralBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            VirtualName=json_data.get("VirtualName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EphemeralBlockDeviceDefinition = EphemeralBlockDeviceDefinition


@dataclass
class MetadataOptionsDefinition(BaseModel):
    HttpEndpoint: Optional[str]
    HttpPutResponseHopLimit: Optional[float]
    HttpTokens: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpEndpoint=json_data.get("HttpEndpoint"),
            HttpPutResponseHopLimit=json_data.get("HttpPutResponseHopLimit"),
            HttpTokens=json_data.get("HttpTokens"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataOptionsDefinition = MetadataOptionsDefinition


@dataclass
class RootBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    Encrypted: Optional[bool]
    Iops: Optional[float]
    Throughput: Optional[float]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RootBlockDeviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RootBlockDeviceDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            Throughput=json_data.get("Throughput"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RootBlockDeviceDefinition = RootBlockDeviceDefinition


