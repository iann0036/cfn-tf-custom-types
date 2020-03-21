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
    AccessTier: Optional[str]
    AccountKind: Optional[str]
    AccountReplicationType: Optional[str]
    AccountTier: Optional[str]
    EnableHttpsTrafficOnly: Optional[bool]
    Id: Optional[str]
    IsHnsEnabled: Optional[bool]
    Location: Optional[str]
    Name: Optional[str]
    PrimaryAccessKey: Optional[str]
    PrimaryBlobConnectionString: Optional[str]
    PrimaryBlobEndpoint: Optional[str]
    PrimaryBlobHost: Optional[str]
    PrimaryConnectionString: Optional[str]
    PrimaryDfsEndpoint: Optional[str]
    PrimaryDfsHost: Optional[str]
    PrimaryFileEndpoint: Optional[str]
    PrimaryFileHost: Optional[str]
    PrimaryLocation: Optional[str]
    PrimaryQueueEndpoint: Optional[str]
    PrimaryQueueHost: Optional[str]
    PrimaryTableEndpoint: Optional[str]
    PrimaryTableHost: Optional[str]
    PrimaryWebEndpoint: Optional[str]
    PrimaryWebHost: Optional[str]
    ResourceGroupName: Optional[str]
    SecondaryAccessKey: Optional[str]
    SecondaryBlobConnectionString: Optional[str]
    SecondaryBlobEndpoint: Optional[str]
    SecondaryBlobHost: Optional[str]
    SecondaryConnectionString: Optional[str]
    SecondaryDfsEndpoint: Optional[str]
    SecondaryDfsHost: Optional[str]
    SecondaryFileEndpoint: Optional[str]
    SecondaryFileHost: Optional[str]
    SecondaryLocation: Optional[str]
    SecondaryQueueEndpoint: Optional[str]
    SecondaryQueueHost: Optional[str]
    SecondaryTableEndpoint: Optional[str]
    SecondaryTableHost: Optional[str]
    SecondaryWebEndpoint: Optional[str]
    SecondaryWebHost: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    BlobProperties: Optional[Sequence["_BlobProperties"]]
    CustomDomain: Optional[Sequence["_CustomDomain"]]
    Identity: Optional[Sequence["_Identity"]]
    NetworkRules: Optional[Sequence["_NetworkRules"]]
    QueueProperties: Optional[Sequence["_QueueProperties"]]
    StaticWebsite: Optional[Sequence["_StaticWebsite"]]
    Timeouts: Optional["_Timeouts"]
    CorsRule: Optional[Sequence["_CorsRule"]]
    DeleteRetentionPolicy: Optional[Sequence["_DeleteRetentionPolicy"]]
    HourMetrics: Optional[Sequence["_HourMetrics"]]
    Logging: Optional[Sequence["_Logging"]]
    MinuteMetrics: Optional[Sequence["_MinuteMetrics"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessTier=json_data.get("AccessTier"),
            AccountKind=json_data.get("AccountKind"),
            AccountReplicationType=json_data.get("AccountReplicationType"),
            AccountTier=json_data.get("AccountTier"),
            EnableHttpsTrafficOnly=json_data.get("EnableHttpsTrafficOnly"),
            Id=json_data.get("Id"),
            IsHnsEnabled=json_data.get("IsHnsEnabled"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            PrimaryAccessKey=json_data.get("PrimaryAccessKey"),
            PrimaryBlobConnectionString=json_data.get("PrimaryBlobConnectionString"),
            PrimaryBlobEndpoint=json_data.get("PrimaryBlobEndpoint"),
            PrimaryBlobHost=json_data.get("PrimaryBlobHost"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PrimaryDfsEndpoint=json_data.get("PrimaryDfsEndpoint"),
            PrimaryDfsHost=json_data.get("PrimaryDfsHost"),
            PrimaryFileEndpoint=json_data.get("PrimaryFileEndpoint"),
            PrimaryFileHost=json_data.get("PrimaryFileHost"),
            PrimaryLocation=json_data.get("PrimaryLocation"),
            PrimaryQueueEndpoint=json_data.get("PrimaryQueueEndpoint"),
            PrimaryQueueHost=json_data.get("PrimaryQueueHost"),
            PrimaryTableEndpoint=json_data.get("PrimaryTableEndpoint"),
            PrimaryTableHost=json_data.get("PrimaryTableHost"),
            PrimaryWebEndpoint=json_data.get("PrimaryWebEndpoint"),
            PrimaryWebHost=json_data.get("PrimaryWebHost"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryAccessKey=json_data.get("SecondaryAccessKey"),
            SecondaryBlobConnectionString=json_data.get("SecondaryBlobConnectionString"),
            SecondaryBlobEndpoint=json_data.get("SecondaryBlobEndpoint"),
            SecondaryBlobHost=json_data.get("SecondaryBlobHost"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            SecondaryDfsEndpoint=json_data.get("SecondaryDfsEndpoint"),
            SecondaryDfsHost=json_data.get("SecondaryDfsHost"),
            SecondaryFileEndpoint=json_data.get("SecondaryFileEndpoint"),
            SecondaryFileHost=json_data.get("SecondaryFileHost"),
            SecondaryLocation=json_data.get("SecondaryLocation"),
            SecondaryQueueEndpoint=json_data.get("SecondaryQueueEndpoint"),
            SecondaryQueueHost=json_data.get("SecondaryQueueHost"),
            SecondaryTableEndpoint=json_data.get("SecondaryTableEndpoint"),
            SecondaryTableHost=json_data.get("SecondaryTableHost"),
            SecondaryWebEndpoint=json_data.get("SecondaryWebEndpoint"),
            SecondaryWebHost=json_data.get("SecondaryWebHost"),
            Tags=json_data.get("Tags"),
            BlobProperties=json_data.get("BlobProperties"),
            CustomDomain=json_data.get("CustomDomain"),
            Identity=json_data.get("Identity"),
            NetworkRules=json_data.get("NetworkRules"),
            QueueProperties=json_data.get("QueueProperties"),
            StaticWebsite=json_data.get("StaticWebsite"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            CorsRule=json_data.get("CorsRule"),
            DeleteRetentionPolicy=json_data.get("DeleteRetentionPolicy"),
            HourMetrics=json_data.get("HourMetrics"),
            Logging=json_data.get("Logging"),
            MinuteMetrics=json_data.get("MinuteMetrics"),
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
class BlobProperties:
    CorsRule: Optional[Sequence["_CorsRule"]]
    DeleteRetentionPolicy: Optional[Sequence["_DeleteRetentionPolicy"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlobProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlobProperties"]:
        if not json_data:
            return None
        return cls(
            CorsRule=json_data.get("CorsRule"),
            DeleteRetentionPolicy=json_data.get("DeleteRetentionPolicy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlobProperties = BlobProperties


@dataclass
class CorsRule:
    AllowedHeaders: Optional[Sequence[str]]
    AllowedMethods: Optional[Sequence[str]]
    AllowedOrigins: Optional[Sequence[str]]
    ExposedHeaders: Optional[Sequence[str]]
    MaxAgeInSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CorsRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsRule"]:
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
_CorsRule = CorsRule


@dataclass
class DeleteRetentionPolicy:
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeleteRetentionPolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeleteRetentionPolicy"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeleteRetentionPolicy = DeleteRetentionPolicy


@dataclass
class CustomDomain:
    Name: Optional[str]
    UseSubdomain: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDomain"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDomain"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UseSubdomain=json_data.get("UseSubdomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDomain = CustomDomain


@dataclass
class Identity:
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class NetworkRules:
    Bypass: Optional[Sequence[str]]
    DefaultAction: Optional[str]
    IpRules: Optional[Sequence[str]]
    VirtualNetworkSubnetIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRules"]:
        if not json_data:
            return None
        return cls(
            Bypass=json_data.get("Bypass"),
            DefaultAction=json_data.get("DefaultAction"),
            IpRules=json_data.get("IpRules"),
            VirtualNetworkSubnetIds=json_data.get("VirtualNetworkSubnetIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRules = NetworkRules


@dataclass
class QueueProperties:
    CorsRule: Optional[Sequence["_CorsRule"]]
    HourMetrics: Optional[Sequence["_HourMetrics"]]
    Logging: Optional[Sequence["_Logging"]]
    MinuteMetrics: Optional[Sequence["_MinuteMetrics"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueueProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueueProperties"]:
        if not json_data:
            return None
        return cls(
            CorsRule=json_data.get("CorsRule"),
            HourMetrics=json_data.get("HourMetrics"),
            Logging=json_data.get("Logging"),
            MinuteMetrics=json_data.get("MinuteMetrics"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueueProperties = QueueProperties


@dataclass
class HourMetrics:
    Enabled: Optional[bool]
    IncludeApis: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HourMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourMetrics"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeApis=json_data.get("IncludeApis"),
            RetentionPolicyDays=json_data.get("RetentionPolicyDays"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourMetrics = HourMetrics


@dataclass
class Logging:
    Delete: Optional[bool]
    Read: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]
    Write: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Logging"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logging"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            RetentionPolicyDays=json_data.get("RetentionPolicyDays"),
            Version=json_data.get("Version"),
            Write=json_data.get("Write"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logging = Logging


@dataclass
class MinuteMetrics:
    Enabled: Optional[bool]
    IncludeApis: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinuteMetrics"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinuteMetrics"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeApis=json_data.get("IncludeApis"),
            RetentionPolicyDays=json_data.get("RetentionPolicyDays"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinuteMetrics = MinuteMetrics


@dataclass
class StaticWebsite:
    Error404Document: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticWebsite"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticWebsite"]:
        if not json_data:
            return None
        return cls(
            Error404Document=json_data.get("Error404Document"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticWebsite = StaticWebsite


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


