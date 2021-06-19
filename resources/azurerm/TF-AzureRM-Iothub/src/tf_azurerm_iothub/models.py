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
    Endpoint: Optional[Sequence["_EndpointDefinition"]]
    Enrichment: Optional[Sequence["_EnrichmentDefinition"]]
    EventHubEventsEndpoint: Optional[str]
    EventHubEventsPath: Optional[str]
    EventHubOperationsEndpoint: Optional[str]
    EventHubOperationsPath: Optional[str]
    EventHubPartitionCount: Optional[float]
    EventHubRetentionInDays: Optional[float]
    Hostname: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    MinTlsVersion: Optional[str]
    Name: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ResourceGroupName: Optional[str]
    Route: Optional[Sequence["_RouteDefinition"]]
    SharedAccessPolicy: Optional[Sequence["_SharedAccessPolicyDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Type: Optional[str]
    FallbackRoute: Optional[Sequence["_FallbackRouteDefinition"]]
    FileUpload: Optional[Sequence["_FileUploadDefinition"]]
    IpFilterRule: Optional[Sequence["_IpFilterRuleDefinition"]]
    Sku: Optional[Sequence["_SkuDefinition"]]
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
            Endpoint=deserialize_list(json_data.get("Endpoint"), EndpointDefinition),
            Enrichment=deserialize_list(json_data.get("Enrichment"), EnrichmentDefinition),
            EventHubEventsEndpoint=json_data.get("EventHubEventsEndpoint"),
            EventHubEventsPath=json_data.get("EventHubEventsPath"),
            EventHubOperationsEndpoint=json_data.get("EventHubOperationsEndpoint"),
            EventHubOperationsPath=json_data.get("EventHubOperationsPath"),
            EventHubPartitionCount=json_data.get("EventHubPartitionCount"),
            EventHubRetentionInDays=json_data.get("EventHubRetentionInDays"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Name=json_data.get("Name"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Route=deserialize_list(json_data.get("Route"), RouteDefinition),
            SharedAccessPolicy=deserialize_list(json_data.get("SharedAccessPolicy"), SharedAccessPolicyDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Type=json_data.get("Type"),
            FallbackRoute=deserialize_list(json_data.get("FallbackRoute"), FallbackRouteDefinition),
            FileUpload=deserialize_list(json_data.get("FileUpload"), FileUploadDefinition),
            IpFilterRule=deserialize_list(json_data.get("IpFilterRule"), IpFilterRuleDefinition),
            Sku=deserialize_list(json_data.get("Sku"), SkuDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EndpointDefinition(BaseModel):
    BatchFrequencyInSeconds: Optional[float]
    ConnectionString: Optional[str]
    ContainerName: Optional[str]
    Encoding: Optional[str]
    FileNameFormat: Optional[str]
    MaxChunkSizeInBytes: Optional[float]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointDefinition"]:
        if not json_data:
            return None
        return cls(
            BatchFrequencyInSeconds=json_data.get("BatchFrequencyInSeconds"),
            ConnectionString=json_data.get("ConnectionString"),
            ContainerName=json_data.get("ContainerName"),
            Encoding=json_data.get("Encoding"),
            FileNameFormat=json_data.get("FileNameFormat"),
            MaxChunkSizeInBytes=json_data.get("MaxChunkSizeInBytes"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointDefinition = EndpointDefinition


@dataclass
class EnrichmentDefinition(BaseModel):
    EndpointNames: Optional[Sequence[str]]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EnrichmentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EnrichmentDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointNames=json_data.get("EndpointNames"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EnrichmentDefinition = EnrichmentDefinition


@dataclass
class RouteDefinition(BaseModel):
    Condition: Optional[str]
    Enabled: Optional[bool]
    EndpointNames: Optional[Sequence[str]]
    Name: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Enabled=json_data.get("Enabled"),
            EndpointNames=json_data.get("EndpointNames"),
            Name=json_data.get("Name"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RouteDefinition = RouteDefinition


@dataclass
class SharedAccessPolicyDefinition(BaseModel):
    KeyName: Optional[str]
    Permissions: Optional[str]
    PrimaryKey: Optional[str]
    SecondaryKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharedAccessPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedAccessPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyName=json_data.get("KeyName"),
            Permissions=json_data.get("Permissions"),
            PrimaryKey=json_data.get("PrimaryKey"),
            SecondaryKey=json_data.get("SecondaryKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedAccessPolicyDefinition = SharedAccessPolicyDefinition


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
class FallbackRouteDefinition(BaseModel):
    Condition: Optional[str]
    Enabled: Optional[bool]
    EndpointNames: Optional[Sequence[str]]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FallbackRouteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FallbackRouteDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Enabled=json_data.get("Enabled"),
            EndpointNames=json_data.get("EndpointNames"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FallbackRouteDefinition = FallbackRouteDefinition


@dataclass
class FileUploadDefinition(BaseModel):
    ConnectionString: Optional[str]
    ContainerName: Optional[str]
    DefaultTtl: Optional[str]
    LockDuration: Optional[str]
    MaxDeliveryCount: Optional[float]
    Notifications: Optional[bool]
    SasTtl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileUploadDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileUploadDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            ContainerName=json_data.get("ContainerName"),
            DefaultTtl=json_data.get("DefaultTtl"),
            LockDuration=json_data.get("LockDuration"),
            MaxDeliveryCount=json_data.get("MaxDeliveryCount"),
            Notifications=json_data.get("Notifications"),
            SasTtl=json_data.get("SasTtl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileUploadDefinition = FileUploadDefinition


@dataclass
class IpFilterRuleDefinition(BaseModel):
    Action: Optional[str]
    IpMask: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpFilterRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpFilterRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpMask=json_data.get("IpMask"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpFilterRuleDefinition = IpFilterRuleDefinition


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


