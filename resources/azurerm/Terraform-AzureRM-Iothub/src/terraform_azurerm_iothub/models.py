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
    EventHubEventsEndpoint: Optional[str]
    EventHubEventsPath: Optional[str]
    EventHubOperationsEndpoint: Optional[str]
    EventHubOperationsPath: Optional[str]
    EventHubPartitionCount: Optional[float]
    EventHubRetentionInDays: Optional[float]
    Hostname: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SharedAccessPolicy: Optional[Sequence["_SharedAccessPolicy"]]
    Tags: Optional[Sequence["_Tags"]]
    Type: Optional[str]
    Endpoint: Optional[Sequence["_Endpoint"]]
    FallbackRoute: Optional[Sequence["_FallbackRoute"]]
    FileUpload: Optional[Sequence["_FileUpload"]]
    IpFilterRule: Optional[Sequence["_IpFilterRule"]]
    Route: Optional[Sequence["_Route"]]
    Sku: Optional[Sequence["_Sku"]]
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
            EventHubEventsEndpoint=json_data.get("EventHubEventsEndpoint"),
            EventHubEventsPath=json_data.get("EventHubEventsPath"),
            EventHubOperationsEndpoint=json_data.get("EventHubOperationsEndpoint"),
            EventHubOperationsPath=json_data.get("EventHubOperationsPath"),
            EventHubPartitionCount=json_data.get("EventHubPartitionCount"),
            EventHubRetentionInDays=json_data.get("EventHubRetentionInDays"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SharedAccessPolicy=json_data.get("SharedAccessPolicy"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            Endpoint=json_data.get("Endpoint"),
            FallbackRoute=json_data.get("FallbackRoute"),
            FileUpload=json_data.get("FileUpload"),
            IpFilterRule=json_data.get("IpFilterRule"),
            Route=json_data.get("Route"),
            Sku=json_data.get("Sku"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SharedAccessPolicy:
    KeyName: Optional[str]
    Permissions: Optional[str]
    PrimaryKey: Optional[str]
    SecondaryKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SharedAccessPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharedAccessPolicy"]:
        if not json_data:
            return None
        return cls(
            KeyName=json_data.get("KeyName"),
            Permissions=json_data.get("Permissions"),
            PrimaryKey=json_data.get("PrimaryKey"),
            SecondaryKey=json_data.get("SecondaryKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharedAccessPolicy = SharedAccessPolicy


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Endpoint:
    BatchFrequencyInSeconds: Optional[float]
    ConnectionString: Optional[str]
    ContainerName: Optional[str]
    Encoding: Optional[str]
    FileNameFormat: Optional[str]
    MaxChunkSizeInBytes: Optional[float]
    Name: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoint"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoint"]:
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
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoint = Endpoint


@dataclass
class FallbackRoute:
    Condition: Optional[str]
    Enabled: Optional[bool]
    EndpointNames: Optional[Sequence[str]]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FallbackRoute"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FallbackRoute"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Enabled=json_data.get("Enabled"),
            EndpointNames=json_data.get("EndpointNames"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FallbackRoute = FallbackRoute


@dataclass
class FileUpload:
    ConnectionString: Optional[str]
    ContainerName: Optional[str]
    DefaultTtl: Optional[str]
    LockDuration: Optional[str]
    MaxDeliveryCount: Optional[float]
    Notifications: Optional[bool]
    SasTtl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileUpload"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileUpload"]:
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
_FileUpload = FileUpload


@dataclass
class IpFilterRule:
    Action: Optional[str]
    IpMask: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpFilterRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpFilterRule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IpMask=json_data.get("IpMask"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpFilterRule = IpFilterRule


@dataclass
class Route:
    Condition: Optional[str]
    Enabled: Optional[bool]
    EndpointNames: Optional[Sequence[str]]
    Name: Optional[str]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Route"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Route"]:
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
_Route = Route


@dataclass
class Sku:
    Capacity: Optional[float]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Sku"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Sku"]:
        if not json_data:
            return None
        return cls(
            Capacity=json_data.get("Capacity"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Sku = Sku


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


