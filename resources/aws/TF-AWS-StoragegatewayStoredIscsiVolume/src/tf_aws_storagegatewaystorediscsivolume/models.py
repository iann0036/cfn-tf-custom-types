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
    ChapEnabled: Optional[bool]
    DiskId: Optional[str]
    GatewayArn: Optional[str]
    Id: Optional[str]
    KmsEncrypted: Optional[bool]
    KmsKey: Optional[str]
    LunNumber: Optional[float]
    NetworkInterfaceId: Optional[str]
    NetworkInterfacePort: Optional[float]
    PreserveExistingData: Optional[bool]
    SnapshotId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    TargetArn: Optional[str]
    TargetName: Optional[str]
    VolumeAttachmentStatus: Optional[str]
    VolumeId: Optional[str]
    VolumeSizeInBytes: Optional[float]
    VolumeStatus: Optional[str]
    VolumeType: Optional[str]

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
            ChapEnabled=json_data.get("ChapEnabled"),
            DiskId=json_data.get("DiskId"),
            GatewayArn=json_data.get("GatewayArn"),
            Id=json_data.get("Id"),
            KmsEncrypted=json_data.get("KmsEncrypted"),
            KmsKey=json_data.get("KmsKey"),
            LunNumber=json_data.get("LunNumber"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            NetworkInterfacePort=json_data.get("NetworkInterfacePort"),
            PreserveExistingData=json_data.get("PreserveExistingData"),
            SnapshotId=json_data.get("SnapshotId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            TargetArn=json_data.get("TargetArn"),
            TargetName=json_data.get("TargetName"),
            VolumeAttachmentStatus=json_data.get("VolumeAttachmentStatus"),
            VolumeId=json_data.get("VolumeId"),
            VolumeSizeInBytes=json_data.get("VolumeSizeInBytes"),
            VolumeStatus=json_data.get("VolumeStatus"),
            VolumeType=json_data.get("VolumeType"),
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


