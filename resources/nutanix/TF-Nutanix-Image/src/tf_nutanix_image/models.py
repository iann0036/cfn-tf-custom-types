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
    ApiVersion: Optional[str]
    Architecture: Optional[str]
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReferenceDefinition"]]
    Checksum: Optional[Sequence["_ChecksumDefinition"]]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ImageType: Optional[str]
    Metadata: Optional[Sequence["_MetadataDefinition"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReferenceDefinition"]]
    ProjectReference: Optional[Sequence["_ProjectReferenceDefinition"]]
    RetrievalUriList: Optional[Sequence[str]]
    SizeBytes: Optional[float]
    SourcePath: Optional[str]
    SourceUri: Optional[str]
    State: Optional[str]
    Version: Optional[Sequence["_VersionDefinition"]]
    Categories: Optional[Sequence["_CategoriesDefinition"]]

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
            ApiVersion=json_data.get("ApiVersion"),
            Architecture=json_data.get("Architecture"),
            AvailabilityZoneReference=deserialize_list(json_data.get("AvailabilityZoneReference"), AvailabilityZoneReferenceDefinition),
            Checksum=deserialize_list(json_data.get("Checksum"), ChecksumDefinition),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImageType=json_data.get("ImageType"),
            Metadata=deserialize_list(json_data.get("Metadata"), MetadataDefinition),
            Name=json_data.get("Name"),
            OwnerReference=deserialize_list(json_data.get("OwnerReference"), OwnerReferenceDefinition),
            ProjectReference=deserialize_list(json_data.get("ProjectReference"), ProjectReferenceDefinition),
            RetrievalUriList=json_data.get("RetrievalUriList"),
            SizeBytes=json_data.get("SizeBytes"),
            SourcePath=json_data.get("SourcePath"),
            SourceUri=json_data.get("SourceUri"),
            State=json_data.get("State"),
            Version=deserialize_list(json_data.get("Version"), VersionDefinition),
            Categories=deserialize_list(json_data.get("Categories"), CategoriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReferenceDefinition = AvailabilityZoneReferenceDefinition


@dataclass
class ChecksumDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChecksumDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChecksumDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChecksumDefinition = ChecksumDefinition


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
class OwnerReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReferenceDefinition = OwnerReferenceDefinition


@dataclass
class ProjectReferenceDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReferenceDefinition = ProjectReferenceDefinition


@dataclass
class VersionDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VersionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VersionDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VersionDefinition = VersionDefinition


@dataclass
class CategoriesDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CategoriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoriesDefinition = CategoriesDefinition


