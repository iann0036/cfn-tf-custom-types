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
    ArchiveSizeBytes: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DiskSizeGb: Optional[float]
    Family: Optional[str]
    Id: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Licenses: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SourceDisk: Optional[str]
    SourceImage: Optional[str]
    SourceSnapshot: Optional[str]
    GuestOsFeatures: Optional[Sequence["_GuestOsFeaturesDefinition"]]
    RawDisk: Optional[Sequence["_RawDiskDefinition"]]
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
            ArchiveSizeBytes=json_data.get("ArchiveSizeBytes"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Family=json_data.get("Family"),
            Id=json_data.get("Id"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Licenses=json_data.get("Licenses"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SourceDisk=json_data.get("SourceDisk"),
            SourceImage=json_data.get("SourceImage"),
            SourceSnapshot=json_data.get("SourceSnapshot"),
            GuestOsFeatures=deserialize_list(json_data.get("GuestOsFeatures"), GuestOsFeaturesDefinition),
            RawDisk=deserialize_list(json_data.get("RawDisk"), RawDiskDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class GuestOsFeaturesDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestOsFeaturesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestOsFeaturesDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestOsFeaturesDefinition = GuestOsFeaturesDefinition


@dataclass
class RawDiskDefinition(BaseModel):
    ContainerType: Optional[str]
    Sha1: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RawDiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RawDiskDefinition"]:
        if not json_data:
            return None
        return cls(
            ContainerType=json_data.get("ContainerType"),
            Sha1=json_data.get("Sha1"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RawDiskDefinition = RawDiskDefinition


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


