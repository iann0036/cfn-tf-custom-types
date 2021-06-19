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
    Architecture: Optional[str]
    Arn: Optional[str]
    Description: Optional[str]
    EnaSupport: Optional[bool]
    Hypervisor: Optional[str]
    Id: Optional[str]
    ImageLocation: Optional[str]
    ImageOwnerAlias: Optional[str]
    ImageType: Optional[str]
    KernelId: Optional[str]
    ManageEbsSnapshots: Optional[bool]
    Name: Optional[str]
    OwnerId: Optional[str]
    Platform: Optional[str]
    PlatformDetails: Optional[str]
    Public: Optional[bool]
    RamdiskId: Optional[str]
    RootDeviceName: Optional[str]
    RootSnapshotId: Optional[str]
    SriovNetSupport: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UsageOperation: Optional[str]
    VirtualizationType: Optional[str]
    EbsBlockDevice: Optional[Sequence["_EbsBlockDeviceDefinition"]]
    EphemeralBlockDevice: Optional[Sequence["_EphemeralBlockDeviceDefinition"]]
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
            Architecture=json_data.get("Architecture"),
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            EnaSupport=json_data.get("EnaSupport"),
            Hypervisor=json_data.get("Hypervisor"),
            Id=json_data.get("Id"),
            ImageLocation=json_data.get("ImageLocation"),
            ImageOwnerAlias=json_data.get("ImageOwnerAlias"),
            ImageType=json_data.get("ImageType"),
            KernelId=json_data.get("KernelId"),
            ManageEbsSnapshots=json_data.get("ManageEbsSnapshots"),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            Platform=json_data.get("Platform"),
            PlatformDetails=json_data.get("PlatformDetails"),
            Public=json_data.get("Public"),
            RamdiskId=json_data.get("RamdiskId"),
            RootDeviceName=json_data.get("RootDeviceName"),
            RootSnapshotId=json_data.get("RootSnapshotId"),
            SriovNetSupport=json_data.get("SriovNetSupport"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UsageOperation=json_data.get("UsageOperation"),
            VirtualizationType=json_data.get("VirtualizationType"),
            EbsBlockDevice=deserialize_list(json_data.get("EbsBlockDevice"), EbsBlockDeviceDefinition),
            EphemeralBlockDevice=deserialize_list(json_data.get("EphemeralBlockDevice"), EphemeralBlockDeviceDefinition),
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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class EbsBlockDeviceDefinition(BaseModel):
    DeleteOnTermination: Optional[bool]
    DeviceName: Optional[str]
    Encrypted: Optional[bool]
    Iops: Optional[float]
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
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


