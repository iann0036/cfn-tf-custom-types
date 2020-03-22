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
    ConnectionStrings: Optional[Sequence[str]]
    EnableAutomaticFailover: Optional[bool]
    EnableMultipleWriteLocations: Optional[bool]
    Endpoint: Optional[str]
    Id: Optional[str]
    IpRangeFilter: Optional[str]
    IsVirtualNetworkFilterEnabled: Optional[bool]
    Kind: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    OfferType: Optional[str]
    PrimaryMasterKey: Optional[str]
    PrimaryReadonlyMasterKey: Optional[str]
    ReadEndpoints: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    SecondaryMasterKey: Optional[str]
    SecondaryReadonlyMasterKey: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    WriteEndpoints: Optional[Sequence[str]]
    Capabilities: Optional[Sequence["_Capabilities"]]
    ConsistencyPolicy: Optional[Sequence["_ConsistencyPolicy"]]
    GeoLocation: Optional[Sequence["_GeoLocation"]]
    Timeouts: Optional["_Timeouts"]
    VirtualNetworkRule: Optional[Sequence["_VirtualNetworkRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectionStrings=json_data.get("ConnectionStrings"),
            EnableAutomaticFailover=json_data.get("EnableAutomaticFailover"),
            EnableMultipleWriteLocations=json_data.get("EnableMultipleWriteLocations"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            IpRangeFilter=json_data.get("IpRangeFilter"),
            IsVirtualNetworkFilterEnabled=json_data.get("IsVirtualNetworkFilterEnabled"),
            Kind=json_data.get("Kind"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OfferType=json_data.get("OfferType"),
            PrimaryMasterKey=json_data.get("PrimaryMasterKey"),
            PrimaryReadonlyMasterKey=json_data.get("PrimaryReadonlyMasterKey"),
            ReadEndpoints=json_data.get("ReadEndpoints"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryMasterKey=json_data.get("SecondaryMasterKey"),
            SecondaryReadonlyMasterKey=json_data.get("SecondaryReadonlyMasterKey"),
            Tags=json_data.get("Tags"),
            WriteEndpoints=json_data.get("WriteEndpoints"),
            Capabilities=json_data.get("Capabilities"),
            ConsistencyPolicy=json_data.get("ConsistencyPolicy"),
            GeoLocation=json_data.get("GeoLocation"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            VirtualNetworkRule=json_data.get("VirtualNetworkRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class Capabilities:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Capabilities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Capabilities"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Capabilities = Capabilities


@dataclass
class ConsistencyPolicy:
    ConsistencyLevel: Optional[str]
    MaxIntervalInSeconds: Optional[float]
    MaxStalenessPrefix: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConsistencyPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsistencyPolicy"]:
        if not json_data:
            return None
        return cls(
            ConsistencyLevel=json_data.get("ConsistencyLevel"),
            MaxIntervalInSeconds=json_data.get("MaxIntervalInSeconds"),
            MaxStalenessPrefix=json_data.get("MaxStalenessPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsistencyPolicy = ConsistencyPolicy


@dataclass
class GeoLocation:
    FailoverPriority: Optional[float]
    Location: Optional[str]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocation"]:
        if not json_data:
            return None
        return cls(
            FailoverPriority=json_data.get("FailoverPriority"),
            Location=json_data.get("Location"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocation = GeoLocation


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


@dataclass
class VirtualNetworkRule:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkRule"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkRule = VirtualNetworkRule


