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
    Checksum: Optional[str]
    ContainerFormat: Optional[str]
    CreatedAt: Optional[str]
    DiskFormat: Optional[str]
    File: Optional[str]
    Id: Optional[str]
    LicenseSwitch: Optional[str]
    LocalFilePath: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    MinDiskGb: Optional[float]
    MinRamMb: Optional[float]
    Name: Optional[str]
    Owner: Optional[str]
    Properties: Optional[Sequence["_PropertiesDefinition"]]
    Protected: Optional[bool]
    Region: Optional[str]
    Schema: Optional[str]
    SizeBytes: Optional[float]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdateAt: Optional[str]
    VerifyChecksum: Optional[bool]
    Visibility: Optional[str]
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
            Checksum=json_data.get("Checksum"),
            ContainerFormat=json_data.get("ContainerFormat"),
            CreatedAt=json_data.get("CreatedAt"),
            DiskFormat=json_data.get("DiskFormat"),
            File=json_data.get("File"),
            Id=json_data.get("Id"),
            LicenseSwitch=json_data.get("LicenseSwitch"),
            LocalFilePath=json_data.get("LocalFilePath"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            MinDiskGb=json_data.get("MinDiskGb"),
            MinRamMb=json_data.get("MinRamMb"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            Properties=deserialize_list(json_data.get("Properties"), PropertiesDefinition),
            Protected=json_data.get("Protected"),
            Region=json_data.get("Region"),
            Schema=json_data.get("Schema"),
            SizeBytes=json_data.get("SizeBytes"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdateAt=json_data.get("UpdateAt"),
            VerifyChecksum=json_data.get("VerifyChecksum"),
            Visibility=json_data.get("Visibility"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MetadataDefinition = MetadataDefinition


@dataclass
class PropertiesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PropertiesDefinition = PropertiesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


