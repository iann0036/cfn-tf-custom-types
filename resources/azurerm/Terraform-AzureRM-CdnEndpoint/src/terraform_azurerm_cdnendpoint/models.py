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
    ContentTypesToCompress: Optional[Sequence[str]]
    HostName: Optional[str]
    Id: Optional[str]
    IsCompressionEnabled: Optional[bool]
    IsHttpAllowed: Optional[bool]
    IsHttpsAllowed: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    OptimizationType: Optional[str]
    OriginHostHeader: Optional[str]
    OriginPath: Optional[str]
    ProbePath: Optional[str]
    ProfileName: Optional[str]
    QuerystringCachingBehaviour: Optional[str]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    GeoFilter: Optional[Sequence["_GeoFilter"]]
    Origin: Optional[Sequence["_Origin"]]
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
            ContentTypesToCompress=json_data.get("ContentTypesToCompress"),
            HostName=json_data.get("HostName"),
            Id=json_data.get("Id"),
            IsCompressionEnabled=json_data.get("IsCompressionEnabled"),
            IsHttpAllowed=json_data.get("IsHttpAllowed"),
            IsHttpsAllowed=json_data.get("IsHttpsAllowed"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OptimizationType=json_data.get("OptimizationType"),
            OriginHostHeader=json_data.get("OriginHostHeader"),
            OriginPath=json_data.get("OriginPath"),
            ProbePath=json_data.get("ProbePath"),
            ProfileName=json_data.get("ProfileName"),
            QuerystringCachingBehaviour=json_data.get("QuerystringCachingBehaviour"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=json_data.get("Tags"),
            GeoFilter=json_data.get("GeoFilter"),
            Origin=json_data.get("Origin"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class GeoFilter:
    Action: Optional[str]
    CountryCodes: Optional[Sequence[str]]
    RelativePath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoFilter"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CountryCodes=json_data.get("CountryCodes"),
            RelativePath=json_data.get("RelativePath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoFilter = GeoFilter


@dataclass
class Origin:
    HostName: Optional[str]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Origin"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origin"]:
        if not json_data:
            return None
        return cls(
            HostName=json_data.get("HostName"),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origin = Origin


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


