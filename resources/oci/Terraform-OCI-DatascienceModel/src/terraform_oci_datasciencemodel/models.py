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
    ArtifactContentDisposition: Optional[str]
    ArtifactContentLength: Optional[str]
    ArtifactContentMd5: Optional[str]
    ArtifactLastModified: Optional[str]
    CompartmentId: Optional[str]
    CreatedBy: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    Description: Optional[str]
    DisplayName: Optional[str]
    EmptyModel: Optional[bool]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    ModelArtifact: Optional[str]
    ProjectId: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
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
            ArtifactContentDisposition=json_data.get("ArtifactContentDisposition"),
            ArtifactContentLength=json_data.get("ArtifactContentLength"),
            ArtifactContentMd5=json_data.get("ArtifactContentMd5"),
            ArtifactLastModified=json_data.get("ArtifactLastModified"),
            CompartmentId=json_data.get("CompartmentId"),
            CreatedBy=json_data.get("CreatedBy"),
            DefinedTags=json_data.get("DefinedTags"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            EmptyModel=json_data.get("EmptyModel"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            ModelArtifact=json_data.get("ModelArtifact"),
            ProjectId=json_data.get("ProjectId"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
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


