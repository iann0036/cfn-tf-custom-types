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
    ArchiveSizeBytes: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DiskSizeGb: Optional[float]
    Family: Optional[str]
    LabelFingerprint: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    Licenses: Optional[Sequence[str]]
    Name: Optional[str]
    Project: Optional[str]
    SelfLink: Optional[str]
    SourceDisk: Optional[str]
    GuestOsFeatures: Optional[Sequence["_GuestOsFeatures"]]
    RawDisk: Optional[Sequence["_RawDisk"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ArchiveSizeBytes=json_data.get("ArchiveSizeBytes"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DiskSizeGb=json_data.get("DiskSizeGb"),
            Family=json_data.get("Family"),
            LabelFingerprint=json_data.get("LabelFingerprint"),
            Labels=json_data.get("Labels"),
            Licenses=json_data.get("Licenses"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            SourceDisk=json_data.get("SourceDisk"),
            GuestOsFeatures=json_data.get("GuestOsFeatures"),
            RawDisk=json_data.get("RawDisk"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class GuestOsFeatures:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GuestOsFeatures"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GuestOsFeatures"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GuestOsFeatures = GuestOsFeatures


@dataclass
class RawDisk:
    ContainerType: Optional[str]
    Sha1: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RawDisk"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RawDisk"]:
        if not json_data:
            return None
        return cls(
            ContainerType=json_data.get("ContainerType"),
            Sha1=json_data.get("Sha1"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RawDisk = RawDisk


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


