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
    AllMetadata: Optional[Sequence["_AllMetadata"]]
    AvailabilityZone: Optional[str]
    Description: Optional[str]
    ExportLocations: Optional[Sequence["_ExportLocations"]]
    HasReplicas: Optional[bool]
    Host: Optional[str]
    IsPublic: Optional[bool]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    ReplicationType: Optional[str]
    ShareNetworkId: Optional[str]
    ShareProto: Optional[str]
    ShareServerId: Optional[str]
    ShareType: Optional[str]
    Size: Optional[float]
    SnapshotId: Optional[str]
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
            AllMetadata=json_data.get("AllMetadata"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Description=json_data.get("Description"),
            ExportLocations=json_data.get("ExportLocations"),
            HasReplicas=json_data.get("HasReplicas"),
            Host=json_data.get("Host"),
            IsPublic=json_data.get("IsPublic"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            ReplicationType=json_data.get("ReplicationType"),
            ShareNetworkId=json_data.get("ShareNetworkId"),
            ShareProto=json_data.get("ShareProto"),
            ShareServerId=json_data.get("ShareServerId"),
            ShareType=json_data.get("ShareType"),
            Size=json_data.get("Size"),
            SnapshotId=json_data.get("SnapshotId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllMetadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllMetadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllMetadata = AllMetadata


@dataclass
class ExportLocations:
    Path: Optional[str]
    Preferred: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExportLocations"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExportLocations"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Preferred=json_data.get("Preferred"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExportLocations = ExportLocations


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


