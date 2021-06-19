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
    AccessTier: Optional[str]
    AccountKind: Optional[str]
    AccountReplicationType: Optional[str]
    AccountTier: Optional[str]
    AllowBlobPublicAccess: Optional[bool]
    EnableHttpsTrafficOnly: Optional[bool]
    Id: Optional[str]
    IsHnsEnabled: Optional[bool]
    LargeFileShareEnabled: Optional[bool]
    Location: Optional[str]
    MinTlsVersion: Optional[str]
    Name: Optional[str]
    Nfsv3Enabled: Optional[bool]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    AzureFilesAuthentication: Optional[Sequence["_AzureFilesAuthenticationDefinition"]]
    BlobProperties: Optional[Sequence["_BlobPropertiesDefinition"]]
    CustomDomain: Optional[Sequence["_CustomDomainDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    NetworkRules: Optional[Sequence["_NetworkRulesDefinition"]]
    QueueProperties: Optional[Sequence["_QueuePropertiesDefinition"]]
    Routing: Optional[Sequence["_RoutingDefinition"]]
    ShareProperties: Optional[Sequence["_SharePropertiesDefinition"]]
    StaticWebsite: Optional[Sequence["_StaticWebsiteDefinition"]]
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
            AccessTier=json_data.get("AccessTier"),
            AccountKind=json_data.get("AccountKind"),
            AccountReplicationType=json_data.get("AccountReplicationType"),
            AccountTier=json_data.get("AccountTier"),
            AllowBlobPublicAccess=json_data.get("AllowBlobPublicAccess"),
            EnableHttpsTrafficOnly=json_data.get("EnableHttpsTrafficOnly"),
            Id=json_data.get("Id"),
            IsHnsEnabled=json_data.get("IsHnsEnabled"),
            LargeFileShareEnabled=json_data.get("LargeFileShareEnabled"),
            Location=json_data.get("Location"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            Name=json_data.get("Name"),
            Nfsv3Enabled=json_data.get("Nfsv3Enabled"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AzureFilesAuthentication=deserialize_list(json_data.get("AzureFilesAuthentication"), AzureFilesAuthenticationDefinition),
            BlobProperties=deserialize_list(json_data.get("BlobProperties"), BlobPropertiesDefinition),
            CustomDomain=deserialize_list(json_data.get("CustomDomain"), CustomDomainDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            NetworkRules=deserialize_list(json_data.get("NetworkRules"), NetworkRulesDefinition),
            QueueProperties=deserialize_list(json_data.get("QueueProperties"), QueuePropertiesDefinition),
            Routing=deserialize_list(json_data.get("Routing"), RoutingDefinition),
            ShareProperties=deserialize_list(json_data.get("ShareProperties"), SharePropertiesDefinition),
            StaticWebsite=deserialize_list(json_data.get("StaticWebsite"), StaticWebsiteDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class AzureFilesAuthenticationDefinition(BaseModel):
    DirectoryType: Optional[str]
    ActiveDirectory: Optional[Sequence["_ActiveDirectoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AzureFilesAuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureFilesAuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            DirectoryType=json_data.get("DirectoryType"),
            ActiveDirectory=deserialize_list(json_data.get("ActiveDirectory"), ActiveDirectoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureFilesAuthenticationDefinition = AzureFilesAuthenticationDefinition


@dataclass
class ActiveDirectoryDefinition(BaseModel):
    DomainGuid: Optional[str]
    DomainName: Optional[str]
    DomainSid: Optional[str]
    ForestName: Optional[str]
    NetbiosDomainName: Optional[str]
    StorageSid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainGuid=json_data.get("DomainGuid"),
            DomainName=json_data.get("DomainName"),
            DomainSid=json_data.get("DomainSid"),
            ForestName=json_data.get("ForestName"),
            NetbiosDomainName=json_data.get("NetbiosDomainName"),
            StorageSid=json_data.get("StorageSid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectoryDefinition = ActiveDirectoryDefinition


@dataclass
class BlobPropertiesDefinition(BaseModel):
    ChangeFeedEnabled: Optional[bool]
    DefaultServiceVersion: Optional[str]
    LastAccessTimeEnabled: Optional[bool]
    VersioningEnabled: Optional[bool]
    ContainerDeleteRetentionPolicy: Optional[Sequence["_ContainerDeleteRetentionPolicyDefinition"]]
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    DeleteRetentionPolicy: Optional[Sequence["_DeleteRetentionPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BlobPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BlobPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ChangeFeedEnabled=json_data.get("ChangeFeedEnabled"),
            DefaultServiceVersion=json_data.get("DefaultServiceVersion"),
            LastAccessTimeEnabled=json_data.get("LastAccessTimeEnabled"),
            VersioningEnabled=json_data.get("VersioningEnabled"),
            ContainerDeleteRetentionPolicy=deserialize_list(json_data.get("ContainerDeleteRetentionPolicy"), ContainerDeleteRetentionPolicyDefinition),
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            DeleteRetentionPolicy=deserialize_list(json_data.get("DeleteRetentionPolicy"), DeleteRetentionPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BlobPropertiesDefinition = BlobPropertiesDefinition


@dataclass
class ContainerDeleteRetentionPolicyDefinition(BaseModel):
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerDeleteRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerDeleteRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerDeleteRetentionPolicyDefinition = ContainerDeleteRetentionPolicyDefinition


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
class DeleteRetentionPolicyDefinition(BaseModel):
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DeleteRetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeleteRetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeleteRetentionPolicyDefinition = DeleteRetentionPolicyDefinition


@dataclass
class CustomDomainDefinition(BaseModel):
    Name: Optional[str]
    UseSubdomain: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CustomDomainDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomDomainDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            UseSubdomain=json_data.get("UseSubdomain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomDomainDefinition = CustomDomainDefinition


@dataclass
class IdentityDefinition(BaseModel):
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IdentityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IdentityDefinition"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IdentityDefinition = IdentityDefinition


@dataclass
class NetworkRulesDefinition(BaseModel):
    Bypass: Optional[Sequence[str]]
    DefaultAction: Optional[str]
    IpRules: Optional[Sequence[str]]
    VirtualNetworkSubnetIds: Optional[Sequence[str]]
    PrivateLinkAccess: Optional[Sequence["_PrivateLinkAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Bypass=json_data.get("Bypass"),
            DefaultAction=json_data.get("DefaultAction"),
            IpRules=json_data.get("IpRules"),
            VirtualNetworkSubnetIds=json_data.get("VirtualNetworkSubnetIds"),
            PrivateLinkAccess=deserialize_list(json_data.get("PrivateLinkAccess"), PrivateLinkAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkRulesDefinition = NetworkRulesDefinition


@dataclass
class PrivateLinkAccessDefinition(BaseModel):
    EndpointResourceId: Optional[str]
    EndpointTenantId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateLinkAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateLinkAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            EndpointResourceId=json_data.get("EndpointResourceId"),
            EndpointTenantId=json_data.get("EndpointTenantId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateLinkAccessDefinition = PrivateLinkAccessDefinition


@dataclass
class QueuePropertiesDefinition(BaseModel):
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    HourMetrics: Optional[Sequence["_HourMetricsDefinition"]]
    Logging: Optional[Sequence["_LoggingDefinition"]]
    MinuteMetrics: Optional[Sequence["_MinuteMetricsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_QueuePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QueuePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            HourMetrics=deserialize_list(json_data.get("HourMetrics"), HourMetricsDefinition),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
            MinuteMetrics=deserialize_list(json_data.get("MinuteMetrics"), MinuteMetricsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_QueuePropertiesDefinition = QueuePropertiesDefinition


@dataclass
class HourMetricsDefinition(BaseModel):
    Enabled: Optional[bool]
    IncludeApis: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HourMetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HourMetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeApis=json_data.get("IncludeApis"),
            RetentionPolicyDays=json_data.get("RetentionPolicyDays"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HourMetricsDefinition = HourMetricsDefinition


@dataclass
class LoggingDefinition(BaseModel):
    Delete: Optional[bool]
    Read: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]
    Write: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
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
_LoggingDefinition = LoggingDefinition


@dataclass
class MinuteMetricsDefinition(BaseModel):
    Enabled: Optional[bool]
    IncludeApis: Optional[bool]
    RetentionPolicyDays: Optional[float]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MinuteMetricsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MinuteMetricsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            IncludeApis=json_data.get("IncludeApis"),
            RetentionPolicyDays=json_data.get("RetentionPolicyDays"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MinuteMetricsDefinition = MinuteMetricsDefinition


@dataclass
class RoutingDefinition(BaseModel):
    Choice: Optional[str]
    PublishInternetEndpoints: Optional[bool]
    PublishMicrosoftEndpoints: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingDefinition"]:
        if not json_data:
            return None
        return cls(
            Choice=json_data.get("Choice"),
            PublishInternetEndpoints=json_data.get("PublishInternetEndpoints"),
            PublishMicrosoftEndpoints=json_data.get("PublishMicrosoftEndpoints"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingDefinition = RoutingDefinition


@dataclass
class SharePropertiesDefinition(BaseModel):
    CorsRule: Optional[Sequence["_CorsRuleDefinition"]]
    RetentionPolicy: Optional[Sequence["_RetentionPolicyDefinition"]]
    Smb: Optional[Sequence["_SmbDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SharePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SharePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            CorsRule=deserialize_list(json_data.get("CorsRule"), CorsRuleDefinition),
            RetentionPolicy=deserialize_list(json_data.get("RetentionPolicy"), RetentionPolicyDefinition),
            Smb=deserialize_list(json_data.get("Smb"), SmbDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SharePropertiesDefinition = SharePropertiesDefinition


@dataclass
class RetentionPolicyDefinition(BaseModel):
    Days: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RetentionPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RetentionPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Days=json_data.get("Days"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RetentionPolicyDefinition = RetentionPolicyDefinition


@dataclass
class SmbDefinition(BaseModel):
    AuthenticationTypes: Optional[Sequence[str]]
    ChannelEncryptionType: Optional[Sequence[str]]
    KerberosTicketEncryptionType: Optional[Sequence[str]]
    Versions: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SmbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmbDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationTypes=json_data.get("AuthenticationTypes"),
            ChannelEncryptionType=json_data.get("ChannelEncryptionType"),
            KerberosTicketEncryptionType=json_data.get("KerberosTicketEncryptionType"),
            Versions=json_data.get("Versions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmbDefinition = SmbDefinition


@dataclass
class StaticWebsiteDefinition(BaseModel):
    Error404Document: Optional[str]
    IndexDocument: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StaticWebsiteDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StaticWebsiteDefinition"]:
        if not json_data:
            return None
        return cls(
            Error404Document=json_data.get("Error404Document"),
            IndexDocument=json_data.get("IndexDocument"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StaticWebsiteDefinition = StaticWebsiteDefinition


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


