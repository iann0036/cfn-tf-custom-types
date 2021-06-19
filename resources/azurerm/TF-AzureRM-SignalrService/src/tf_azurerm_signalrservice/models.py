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
    Hostname: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    PrimaryConnectionString: Optional[str]
    PublicPort: Optional[float]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    SecondaryConnectionString: Optional[str]
    ServerPort: Optional[float]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Cors: Optional[Sequence["_CorsDefinition"]]
    Features: Optional[Sequence["_FeaturesDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    UpstreamEndpoint: Optional[Sequence["_UpstreamEndpointDefinition"]]

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
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PublicPort=json_data.get("PublicPort"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            ServerPort=json_data.get("ServerPort"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Cors=deserialize_list(json_data.get("Cors"), CorsDefinition),
            Features=deserialize_list(json_data.get("Features"), FeaturesDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            UpstreamEndpoint=deserialize_list(json_data.get("UpstreamEndpoint"), UpstreamEndpointDefinition),
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
class CorsDefinition(BaseModel):
    AllowedOrigins: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_CorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedOrigins=json_data.get("AllowedOrigins"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsDefinition = CorsDefinition


@dataclass
class FeaturesDefinition(BaseModel):
    Flag: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FeaturesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FeaturesDefinition"]:
        if not json_data:
            return None
        return cls(
            Flag=json_data.get("Flag"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FeaturesDefinition = FeaturesDefinition


@dataclass
class SkuDefinition(BaseModel):
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SkuDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SkuDefinition"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SkuDefinition = SkuDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class UpstreamEndpointDefinition(BaseModel):
    CategoryPattern: Optional[Sequence[str]]
    EventPattern: Optional[Sequence[str]]
    HubPattern: Optional[Sequence[str]]
    UrlTemplate: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UpstreamEndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UpstreamEndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            CategoryPattern=json_data.get("CategoryPattern"),
            EventPattern=json_data.get("EventPattern"),
            HubPattern=json_data.get("HubPattern"),
            UrlTemplate=json_data.get("UrlTemplate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UpstreamEndpointDefinition = UpstreamEndpointDefinition


