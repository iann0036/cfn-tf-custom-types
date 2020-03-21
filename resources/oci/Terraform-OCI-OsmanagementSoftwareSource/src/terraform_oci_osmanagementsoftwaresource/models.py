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
    ArchType: Optional[str]
    AssociatedManagedInstances: Optional[Sequence["_AssociatedManagedInstances"]]
    ChecksumType: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    GpgKeyFingerprint: Optional[str]
    GpgKeyId: Optional[str]
    GpgKeyUrl: Optional[str]
    Id: Optional[str]
    MaintainerEmail: Optional[str]
    MaintainerName: Optional[str]
    MaintainerPhone: Optional[str]
    Packages: Optional[float]
    ParentId: Optional[str]
    ParentName: Optional[str]
    RepoType: Optional[str]
    State: Optional[str]
    Status: Optional[str]
    Url: Optional[str]
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
            ArchType=json_data.get("ArchType"),
            AssociatedManagedInstances=json_data.get("AssociatedManagedInstances"),
            ChecksumType=json_data.get("ChecksumType"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            FreeformTags=json_data.get("FreeformTags"),
            GpgKeyFingerprint=json_data.get("GpgKeyFingerprint"),
            GpgKeyId=json_data.get("GpgKeyId"),
            GpgKeyUrl=json_data.get("GpgKeyUrl"),
            Id=json_data.get("Id"),
            MaintainerEmail=json_data.get("MaintainerEmail"),
            MaintainerName=json_data.get("MaintainerName"),
            MaintainerPhone=json_data.get("MaintainerPhone"),
            Packages=json_data.get("Packages"),
            ParentId=json_data.get("ParentId"),
            ParentName=json_data.get("ParentName"),
            RepoType=json_data.get("RepoType"),
            State=json_data.get("State"),
            Status=json_data.get("Status"),
            Url=json_data.get("Url"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AssociatedManagedInstances:
    DisplayName: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AssociatedManagedInstances"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AssociatedManagedInstances"]:
        if not json_data:
            return None
        return cls(
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AssociatedManagedInstances = AssociatedManagedInstances


@dataclass
class DefinedTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


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


