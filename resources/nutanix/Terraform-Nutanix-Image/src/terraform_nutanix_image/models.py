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
    ApiVersion: Optional[str]
    Architecture: Optional[str]
    AvailabilityZoneReference: Optional[Sequence["_AvailabilityZoneReference"]]
    Checksum: Optional[Sequence["_Checksum"]]
    ClusterName: Optional[str]
    ClusterUuid: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ImageType: Optional[str]
    Metadata: Optional[Sequence["_Metadata"]]
    Name: Optional[str]
    OwnerReference: Optional[Sequence["_OwnerReference"]]
    ProjectReference: Optional[Sequence["_ProjectReference"]]
    RetrievalUriList: Optional[Sequence[str]]
    SizeBytes: Optional[float]
    SourcePath: Optional[str]
    SourceUri: Optional[str]
    State: Optional[str]
    Version: Optional[Sequence["_Version"]]
    Categories: Optional[Sequence["_Categories"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ApiVersion=json_data.get("ApiVersion"),
            Architecture=json_data.get("Architecture"),
            AvailabilityZoneReference=json_data.get("AvailabilityZoneReference"),
            Checksum=json_data.get("Checksum"),
            ClusterName=json_data.get("ClusterName"),
            ClusterUuid=json_data.get("ClusterUuid"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImageType=json_data.get("ImageType"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            OwnerReference=json_data.get("OwnerReference"),
            ProjectReference=json_data.get("ProjectReference"),
            RetrievalUriList=json_data.get("RetrievalUriList"),
            SizeBytes=json_data.get("SizeBytes"),
            SourcePath=json_data.get("SourcePath"),
            SourceUri=json_data.get("SourceUri"),
            State=json_data.get("State"),
            Version=json_data.get("Version"),
            Categories=json_data.get("Categories"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AvailabilityZoneReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AvailabilityZoneReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AvailabilityZoneReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AvailabilityZoneReference = AvailabilityZoneReference


@dataclass
class Checksum:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Checksum"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Checksum"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Checksum = Checksum


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
class OwnerReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OwnerReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OwnerReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OwnerReference = OwnerReference


@dataclass
class ProjectReference:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectReference"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectReference"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectReference = ProjectReference


@dataclass
class Version:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Version"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Version"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Version = Version


@dataclass
class Categories:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Categories"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Categories"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Categories = Categories


