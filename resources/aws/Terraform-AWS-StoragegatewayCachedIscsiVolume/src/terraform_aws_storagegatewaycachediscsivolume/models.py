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
    Arn: Optional[str]
    ChapEnabled: Optional[bool]
    GatewayArn: Optional[str]
    Id: Optional[str]
    LunNumber: Optional[float]
    NetworkInterfaceId: Optional[str]
    NetworkInterfacePort: Optional[float]
    SnapshotId: Optional[str]
    SourceVolumeArn: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TargetArn: Optional[str]
    TargetName: Optional[str]
    VolumeArn: Optional[str]
    VolumeId: Optional[str]
    VolumeSizeInBytes: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            ChapEnabled=json_data.get("ChapEnabled"),
            GatewayArn=json_data.get("GatewayArn"),
            Id=json_data.get("Id"),
            LunNumber=json_data.get("LunNumber"),
            NetworkInterfaceId=json_data.get("NetworkInterfaceId"),
            NetworkInterfacePort=json_data.get("NetworkInterfacePort"),
            SnapshotId=json_data.get("SnapshotId"),
            SourceVolumeArn=json_data.get("SourceVolumeArn"),
            Tags=json_data.get("Tags"),
            TargetArn=json_data.get("TargetArn"),
            TargetName=json_data.get("TargetName"),
            VolumeArn=json_data.get("VolumeArn"),
            VolumeId=json_data.get("VolumeId"),
            VolumeSizeInBytes=json_data.get("VolumeSizeInBytes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


