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
    AccessKeyMetadataWritesEnabled: Optional[bool]
    AnalyticalStorageEnabled: Optional[bool]
    ConnectionStrings: Optional[Sequence[str]]
    EnableAutomaticFailover: Optional[bool]
    EnableFreeTier: Optional[bool]
    EnableMultipleWriteLocations: Optional[bool]
    Endpoint: Optional[str]
    Id: Optional[str]
    IpRangeFilter: Optional[str]
    IsVirtualNetworkFilterEnabled: Optional[bool]
    KeyVaultKeyId: Optional[str]
    Kind: Optional[str]
    Location: Optional[str]
    MongoServerVersion: Optional[str]
    Name: Optional[str]
    NetworkAclBypassForAzureServices: Optional[bool]
    NetworkAclBypassIds: Optional[Sequence[str]]
    OfferType: Optional[str]
    PrimaryKey: Optional[str]
    PrimaryMasterKey: Optional[str]
    PrimaryReadonlyKey: Optional[str]
    PrimaryReadonlyMasterKey: Optional[str]
    PublicNetworkAccessEnabled: Optional[bool]
    ReadEndpoints: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    SecondaryKey: Optional[str]
    SecondaryMasterKey: Optional[str]
    SecondaryReadonlyKey: Optional[str]
    SecondaryReadonlyMasterKey: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    WriteEndpoints: Optional[Sequence[str]]
    Backup: Optional[Sequence["_BackupDefinition"]]
    Capabilities: Optional[Sequence["_CapabilitiesDefinition"]]
    ConsistencyPolicy: Optional[Sequence["_ConsistencyPolicyDefinition"]]
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    GeoLocation: Optional[Sequence["_GeoLocationDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VirtualNetworkRule: Optional[Sequence["_VirtualNetworkRuleDefinition"]]

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
            AccessKeyMetadataWritesEnabled=json_data.get("AccessKeyMetadataWritesEnabled"),
            AnalyticalStorageEnabled=json_data.get("AnalyticalStorageEnabled"),
            ConnectionStrings=json_data.get("ConnectionStrings"),
            EnableAutomaticFailover=json_data.get("EnableAutomaticFailover"),
            EnableFreeTier=json_data.get("EnableFreeTier"),
            EnableMultipleWriteLocations=json_data.get("EnableMultipleWriteLocations"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            IpRangeFilter=json_data.get("IpRangeFilter"),
            IsVirtualNetworkFilterEnabled=json_data.get("IsVirtualNetworkFilterEnabled"),
            KeyVaultKeyId=json_data.get("KeyVaultKeyId"),
            Kind=json_data.get("Kind"),
            Location=json_data.get("Location"),
            MongoServerVersion=json_data.get("MongoServerVersion"),
            Name=json_data.get("Name"),
            NetworkAclBypassForAzureServices=json_data.get("NetworkAclBypassForAzureServices"),
            NetworkAclBypassIds=json_data.get("NetworkAclBypassIds"),
            OfferType=json_data.get("OfferType"),
            PrimaryKey=json_data.get("PrimaryKey"),
            PrimaryMasterKey=json_data.get("PrimaryMasterKey"),
            PrimaryReadonlyKey=json_data.get("PrimaryReadonlyKey"),
            PrimaryReadonlyMasterKey=json_data.get("PrimaryReadonlyMasterKey"),
            PublicNetworkAccessEnabled=json_data.get("PublicNetworkAccessEnabled"),
            ReadEndpoints=json_data.get("ReadEndpoints"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryKey=json_data.get("SecondaryKey"),
            SecondaryMasterKey=json_data.get("SecondaryMasterKey"),
            SecondaryReadonlyKey=json_data.get("SecondaryReadonlyKey"),
            SecondaryReadonlyMasterKey=json_data.get("SecondaryReadonlyMasterKey"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            WriteEndpoints=json_data.get("WriteEndpoints"),
            Backup=deserialize_list(json_data.get("Backup"), BackupDefinition),
            Capabilities=deserialize_list(json_data.get("Capabilities"), CapabilitiesDefinition),
            ConsistencyPolicy=deserialize_list(json_data.get("ConsistencyPolicy"), ConsistencyPolicyDefinition),
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            GeoLocation=deserialize_list(json_data.get("GeoLocation"), GeoLocationDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VirtualNetworkRule=deserialize_list(json_data.get("VirtualNetworkRule"), VirtualNetworkRuleDefinition),
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
class BackupDefinition(BaseModel):
    IntervalInMinutes: Optional[float]
    RetentionInHours: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDefinition"]:
        if not json_data:
            return None
        return cls(
            IntervalInMinutes=json_data.get("IntervalInMinutes"),
            RetentionInHours=json_data.get("RetentionInHours"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDefinition = BackupDefinition


@dataclass
class CapabilitiesDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CapabilitiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CapabilitiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CapabilitiesDefinition = CapabilitiesDefinition


@dataclass
class ConsistencyPolicyDefinition(BaseModel):
    ConsistencyLevel: Optional[str]
    MaxIntervalInSeconds: Optional[float]
    MaxStalenessPrefix: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ConsistencyPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConsistencyPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsistencyLevel=json_data.get("ConsistencyLevel"),
            MaxIntervalInSeconds=json_data.get("MaxIntervalInSeconds"),
            MaxStalenessPrefix=json_data.get("MaxStalenessPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConsistencyPolicyDefinition = ConsistencyPolicyDefinition


@dataclass
class CorsRuleDefinition(BaseModel):
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    MaxAgeInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHeaders=json_data.get("AllowedHeaders"),
            AllowedMethods=json_data.get("AllowedMethods"),
            AllowedOrigins=json_data.get("AllowedOrigins"),
            ExposedHeaders=json_data.get("ExposedHeaders"),
            MaxAgeInSeconds=json_data.get("MaxAgeInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsRuleDefinition = CorsRuleDefinition


@dataclass
class GeoLocationDefinition(BaseModel):
    FailoverPriority: Optional[float]
    Location: Optional[str]
    Prefix: Optional[str]
    ZoneRedundant: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GeoLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GeoLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            FailoverPriority=json_data.get("FailoverPriority"),
            Location=json_data.get("Location"),
            Prefix=json_data.get("Prefix"),
            ZoneRedundant=json_data.get("ZoneRedundant"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GeoLocationDefinition = GeoLocationDefinition


@dataclass
class IdentityDefinition(BaseModel):
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


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
class VirtualNetworkRuleDefinition(BaseModel):
    Id: Optional[str]
    IgnoreMissingVnetServiceEndpoint: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            IgnoreMissingVnetServiceEndpoint=json_data.get("IgnoreMissingVnetServiceEndpoint"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkRuleDefinition = VirtualNetworkRuleDefinition


