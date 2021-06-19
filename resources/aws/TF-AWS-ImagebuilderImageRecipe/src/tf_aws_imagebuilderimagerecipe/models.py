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
    DateCreated: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    ParentImage: Optional[str]
    Platform: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Version: Optional[str]
    WorkingDirectory: Optional[str]
    BlockDeviceMapping: Optional[Sequence["_BlockDeviceMappingDefinition"]]
    Component: Optional[Sequence["_ComponentDefinition"]]

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
            DateCreated=json_data.get("DateCreated"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            ParentImage=json_data.get("ParentImage"),
            Platform=json_data.get("Platform"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Version=json_data.get("Version"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            BlockDeviceMapping=deserialize_list(json_data.get("BlockDeviceMapping"), BlockDeviceMappingDefinition),
            Component=deserialize_list(json_data.get("Component"), ComponentDefinition),
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
class BlockDeviceMappingDefinition(BaseModel):
    DeviceName: Optional[str]
    NoDevice: Optional[bool]
    VirtualName: Optional[str]
    Ebs: Optional[Sequence["_EbsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlockDeviceMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlockDeviceMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            DeviceName=json_data.get("DeviceName"),
            NoDevice=json_data.get("NoDevice"),
            VirtualName=json_data.get("VirtualName"),
            Ebs=deserialize_list(json_data.get("Ebs"), EbsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlockDeviceMappingDefinition = BlockDeviceMappingDefinition


@dataclass
class EbsDefinition(BaseModel):
    DeleteOnTermination: Optional[str]
    Encrypted: Optional[str]
    Iops: Optional[float]
    KmsKeyId: Optional[str]
    SnapshotId: Optional[str]
    VolumeSize: Optional[float]
    VolumeType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EbsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EbsDefinition"]:
        if not json_data:
            return None
        return cls(
            DeleteOnTermination=json_data.get("DeleteOnTermination"),
            Encrypted=json_data.get("Encrypted"),
            Iops=json_data.get("Iops"),
            KmsKeyId=json_data.get("KmsKeyId"),
            SnapshotId=json_data.get("SnapshotId"),
            VolumeSize=json_data.get("VolumeSize"),
            VolumeType=json_data.get("VolumeType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EbsDefinition = EbsDefinition


@dataclass
class ComponentDefinition(BaseModel):
    ComponentArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ComponentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ComponentDefinition"]:
        if not json_data:
            return None
        return cls(
            ComponentArn=json_data.get("ComponentArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ComponentDefinition = ComponentDefinition


