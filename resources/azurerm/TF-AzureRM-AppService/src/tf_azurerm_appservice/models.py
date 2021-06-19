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
    AppServicePlanId: Optional[str]
    AppSettings: Optional[Sequence["_AppSettingsDefinition"]]
    ClientAffinityEnabled: Optional[bool]
    ClientCertEnabled: Optional[bool]
    CustomDomainVerificationId: Optional[str]
    DefaultSiteHostname: Optional[str]
    Enabled: Optional[bool]
    HttpsOnly: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    OutboundIpAddressList: Optional[Sequence[str]]
    OutboundIpAddresses: Optional[str]
    PossibleOutboundIpAddressList: Optional[Sequence[str]]
    PossibleOutboundIpAddresses: Optional[str]
    ResourceGroupName: Optional[str]
    SiteCredential: Optional[Sequence["_SiteCredentialDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    AuthSettings: Optional[Sequence["_AuthSettingsDefinition"]]
    Backup: Optional[Sequence["_BackupDefinition"]]
    ConnectionString: Optional[Sequence["_ConnectionStringDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Logs: Optional[Sequence["_LogsDefinition"]]
    SiteConfig: Optional[Sequence["_SiteConfigDefinition"]]
    SourceControl: Optional[Sequence["_SourceControlDefinition"]]
    StorageAccount: Optional[Sequence["_StorageAccountDefinition"]]
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
            AppServicePlanId=json_data.get("AppServicePlanId"),
            AppSettings=deserialize_list(json_data.get("AppSettings"), AppSettingsDefinition),
            ClientAffinityEnabled=json_data.get("ClientAffinityEnabled"),
            ClientCertEnabled=json_data.get("ClientCertEnabled"),
            CustomDomainVerificationId=json_data.get("CustomDomainVerificationId"),
            DefaultSiteHostname=json_data.get("DefaultSiteHostname"),
            Enabled=json_data.get("Enabled"),
            HttpsOnly=json_data.get("HttpsOnly"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OutboundIpAddressList=json_data.get("OutboundIpAddressList"),
            OutboundIpAddresses=json_data.get("OutboundIpAddresses"),
            PossibleOutboundIpAddressList=json_data.get("PossibleOutboundIpAddressList"),
            PossibleOutboundIpAddresses=json_data.get("PossibleOutboundIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SiteCredential=deserialize_list(json_data.get("SiteCredential"), SiteCredentialDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            AuthSettings=deserialize_list(json_data.get("AuthSettings"), AuthSettingsDefinition),
            Backup=deserialize_list(json_data.get("Backup"), BackupDefinition),
            ConnectionString=deserialize_list(json_data.get("ConnectionString"), ConnectionStringDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Logs=deserialize_list(json_data.get("Logs"), LogsDefinition),
            SiteConfig=deserialize_list(json_data.get("SiteConfig"), SiteConfigDefinition),
            SourceControl=deserialize_list(json_data.get("SourceControl"), SourceControlDefinition),
            StorageAccount=deserialize_list(json_data.get("StorageAccount"), StorageAccountDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppSettingsDefinition = AppSettingsDefinition


@dataclass
class SiteCredentialDefinition(BaseModel):
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteCredentialDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteCredentialDefinition"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteCredentialDefinition = SiteCredentialDefinition


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
class AuthSettingsDefinition(BaseModel):
    AdditionalLoginParams: Optional[Sequence["_AdditionalLoginParamsDefinition"]]
    AllowedExternalRedirectUrls: Optional[Sequence[str]]
    DefaultProvider: Optional[str]
    Enabled: Optional[bool]
    Issuer: Optional[str]
    RuntimeVersion: Optional[str]
    TokenRefreshExtensionHours: Optional[float]
    TokenStoreEnabled: Optional[bool]
    UnauthenticatedClientAction: Optional[str]
    ActiveDirectory: Optional[Sequence["_ActiveDirectoryDefinition"]]
    Facebook: Optional[Sequence["_FacebookDefinition"]]
    Google: Optional[Sequence["_GoogleDefinition"]]
    Microsoft: Optional[Sequence["_MicrosoftDefinition"]]
    Twitter: Optional[Sequence["_TwitterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalLoginParams=deserialize_list(json_data.get("AdditionalLoginParams"), AdditionalLoginParamsDefinition),
            AllowedExternalRedirectUrls=json_data.get("AllowedExternalRedirectUrls"),
            DefaultProvider=json_data.get("DefaultProvider"),
            Enabled=json_data.get("Enabled"),
            Issuer=json_data.get("Issuer"),
            RuntimeVersion=json_data.get("RuntimeVersion"),
            TokenRefreshExtensionHours=json_data.get("TokenRefreshExtensionHours"),
            TokenStoreEnabled=json_data.get("TokenStoreEnabled"),
            UnauthenticatedClientAction=json_data.get("UnauthenticatedClientAction"),
            ActiveDirectory=deserialize_list(json_data.get("ActiveDirectory"), ActiveDirectoryDefinition),
            Facebook=deserialize_list(json_data.get("Facebook"), FacebookDefinition),
            Google=deserialize_list(json_data.get("Google"), GoogleDefinition),
            Microsoft=deserialize_list(json_data.get("Microsoft"), MicrosoftDefinition),
            Twitter=deserialize_list(json_data.get("Twitter"), TwitterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthSettingsDefinition = AuthSettingsDefinition


@dataclass
class AdditionalLoginParamsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalLoginParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalLoginParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalLoginParamsDefinition = AdditionalLoginParamsDefinition


@dataclass
class ActiveDirectoryDefinition(BaseModel):
    AllowedAudiences: Optional[Sequence[str]]
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectoryDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedAudiences=json_data.get("AllowedAudiences"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectoryDefinition = ActiveDirectoryDefinition


@dataclass
class FacebookDefinition(BaseModel):
    AppId: Optional[str]
    AppSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_FacebookDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FacebookDefinition"]:
        if not json_data:
            return None
        return cls(
            AppId=json_data.get("AppId"),
            AppSecret=json_data.get("AppSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FacebookDefinition = FacebookDefinition


@dataclass
class GoogleDefinition(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GoogleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GoogleDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GoogleDefinition = GoogleDefinition


@dataclass
class MicrosoftDefinition(BaseModel):
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MicrosoftDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicrosoftDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicrosoftDefinition = MicrosoftDefinition


@dataclass
class TwitterDefinition(BaseModel):
    ConsumerKey: Optional[str]
    ConsumerSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TwitterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TwitterDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsumerKey=json_data.get("ConsumerKey"),
            ConsumerSecret=json_data.get("ConsumerSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TwitterDefinition = TwitterDefinition


@dataclass
class BackupDefinition(BaseModel):
    Enabled: Optional[bool]
    Name: Optional[str]
    StorageAccountUrl: Optional[str]
    Schedule: Optional[Sequence["_ScheduleDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            StorageAccountUrl=json_data.get("StorageAccountUrl"),
            Schedule=deserialize_list(json_data.get("Schedule"), ScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupDefinition = BackupDefinition


@dataclass
class ScheduleDefinition(BaseModel):
    FrequencyInterval: Optional[float]
    FrequencyUnit: Optional[str]
    KeepAtLeastOneBackup: Optional[bool]
    RetentionPeriodInDays: Optional[float]
    StartTime: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            FrequencyInterval=json_data.get("FrequencyInterval"),
            FrequencyUnit=json_data.get("FrequencyUnit"),
            KeepAtLeastOneBackup=json_data.get("KeepAtLeastOneBackup"),
            RetentionPeriodInDays=json_data.get("RetentionPeriodInDays"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScheduleDefinition = ScheduleDefinition


@dataclass
class ConnectionStringDefinition(BaseModel):
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionStringDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionStringDefinition = ConnectionStringDefinition


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
class LogsDefinition(BaseModel):
    DetailedErrorMessagesEnabled: Optional[bool]
    FailedRequestTracingEnabled: Optional[bool]
    ApplicationLogs: Optional[Sequence["_ApplicationLogsDefinition"]]
    HttpLogs: Optional[Sequence["_HttpLogsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogsDefinition"]:
        if not json_data:
            return None
        return cls(
            DetailedErrorMessagesEnabled=json_data.get("DetailedErrorMessagesEnabled"),
            FailedRequestTracingEnabled=json_data.get("FailedRequestTracingEnabled"),
            ApplicationLogs=deserialize_list(json_data.get("ApplicationLogs"), ApplicationLogsDefinition),
            HttpLogs=deserialize_list(json_data.get("HttpLogs"), HttpLogsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogsDefinition = LogsDefinition


@dataclass
class ApplicationLogsDefinition(BaseModel):
    FileSystemLevel: Optional[str]
    AzureBlobStorage: Optional[Sequence["_AzureBlobStorageDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            FileSystemLevel=json_data.get("FileSystemLevel"),
            AzureBlobStorage=deserialize_list(json_data.get("AzureBlobStorage"), AzureBlobStorageDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationLogsDefinition = ApplicationLogsDefinition


@dataclass
class AzureBlobStorageDefinition(BaseModel):
    RetentionInDays: Optional[float]
    SasUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureBlobStorageDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureBlobStorageDefinition"]:
        if not json_data:
            return None
        return cls(
            RetentionInDays=json_data.get("RetentionInDays"),
            SasUrl=json_data.get("SasUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureBlobStorageDefinition = AzureBlobStorageDefinition


@dataclass
class HttpLogsDefinition(BaseModel):
    AzureBlobStorage: Optional[Sequence["_AzureBlobStorageDefinition"]]
    FileSystem: Optional[Sequence["_FileSystemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpLogsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpLogsDefinition"]:
        if not json_data:
            return None
        return cls(
            AzureBlobStorage=deserialize_list(json_data.get("AzureBlobStorage"), AzureBlobStorageDefinition),
            FileSystem=deserialize_list(json_data.get("FileSystem"), FileSystemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpLogsDefinition = HttpLogsDefinition


@dataclass
class FileSystemDefinition(BaseModel):
    RetentionInDays: Optional[float]
    RetentionInMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystemDefinition"]:
        if not json_data:
            return None
        return cls(
            RetentionInDays=json_data.get("RetentionInDays"),
            RetentionInMb=json_data.get("RetentionInMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystemDefinition = FileSystemDefinition


@dataclass
class SiteConfigDefinition(BaseModel):
    AlwaysOn: Optional[bool]
    AppCommandLine: Optional[str]
    AutoSwapSlotName: Optional[str]
    DefaultDocuments: Optional[Sequence[str]]
    DotnetFrameworkVersion: Optional[str]
    FtpsState: Optional[str]
    HealthCheckPath: Optional[str]
    Http2Enabled: Optional[bool]
    IpRestriction: Optional[Sequence["_IpRestrictionDefinition2"]]
    JavaContainer: Optional[str]
    JavaContainerVersion: Optional[str]
    JavaVersion: Optional[str]
    LinuxFxVersion: Optional[str]
    LocalMysqlEnabled: Optional[bool]
    ManagedPipelineMode: Optional[str]
    MinTlsVersion: Optional[str]
    NumberOfWorkers: Optional[float]
    PhpVersion: Optional[str]
    PythonVersion: Optional[str]
    RemoteDebuggingEnabled: Optional[bool]
    RemoteDebuggingVersion: Optional[str]
    ScmIpRestriction: Optional[Sequence["_ScmIpRestrictionDefinition2"]]
    ScmType: Optional[str]
    ScmUseMainIpRestriction: Optional[bool]
    Use32BitWorkerProcess: Optional[bool]
    WebsocketsEnabled: Optional[bool]
    WindowsFxVersion: Optional[str]
    Cors: Optional[Sequence["_CorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AlwaysOn=json_data.get("AlwaysOn"),
            AppCommandLine=json_data.get("AppCommandLine"),
            AutoSwapSlotName=json_data.get("AutoSwapSlotName"),
            DefaultDocuments=json_data.get("DefaultDocuments"),
            DotnetFrameworkVersion=json_data.get("DotnetFrameworkVersion"),
            FtpsState=json_data.get("FtpsState"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            Http2Enabled=json_data.get("Http2Enabled"),
            IpRestriction=deserialize_list(json_data.get("IpRestriction"), IpRestrictionDefinition2),
            JavaContainer=json_data.get("JavaContainer"),
            JavaContainerVersion=json_data.get("JavaContainerVersion"),
            JavaVersion=json_data.get("JavaVersion"),
            LinuxFxVersion=json_data.get("LinuxFxVersion"),
            LocalMysqlEnabled=json_data.get("LocalMysqlEnabled"),
            ManagedPipelineMode=json_data.get("ManagedPipelineMode"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            NumberOfWorkers=json_data.get("NumberOfWorkers"),
            PhpVersion=json_data.get("PhpVersion"),
            PythonVersion=json_data.get("PythonVersion"),
            RemoteDebuggingEnabled=json_data.get("RemoteDebuggingEnabled"),
            RemoteDebuggingVersion=json_data.get("RemoteDebuggingVersion"),
            ScmIpRestriction=deserialize_list(json_data.get("ScmIpRestriction"), ScmIpRestrictionDefinition2),
            ScmType=json_data.get("ScmType"),
            ScmUseMainIpRestriction=json_data.get("ScmUseMainIpRestriction"),
            Use32BitWorkerProcess=json_data.get("Use32BitWorkerProcess"),
            WebsocketsEnabled=json_data.get("WebsocketsEnabled"),
            WindowsFxVersion=json_data.get("WindowsFxVersion"),
            Cors=deserialize_list(json_data.get("Cors"), CorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteConfigDefinition = SiteConfigDefinition


@dataclass
class IpRestrictionDefinition2(BaseModel):
    Action: Optional[str]
    Headers: Optional[Sequence["_IpRestrictionDefinition"]]
    IpAddress: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ServiceTag: Optional[str]
    VirtualNetworkSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRestrictionDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRestrictionDefinition2"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Headers=deserialize_list(json_data.get("Headers"), IpRestrictionDefinition),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ServiceTag=json_data.get("ServiceTag"),
            VirtualNetworkSubnetId=json_data.get("VirtualNetworkSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRestrictionDefinition2 = IpRestrictionDefinition2


@dataclass
class IpRestrictionDefinition(BaseModel):
    XAzureFdid: Optional[Sequence[str]]
    XFdHealthProbe: Optional[Sequence[str]]
    XForwardedFor: Optional[Sequence[str]]
    XForwardedHost: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            XAzureFdid=json_data.get("XAzureFdid"),
            XFdHealthProbe=json_data.get("XFdHealthProbe"),
            XForwardedFor=json_data.get("XForwardedFor"),
            XForwardedHost=json_data.get("XForwardedHost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRestrictionDefinition = IpRestrictionDefinition


@dataclass
class ScmIpRestrictionDefinition2(BaseModel):
    Action: Optional[str]
    Headers: Optional[Sequence["_ScmIpRestrictionDefinition"]]
    IpAddress: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    ServiceTag: Optional[str]
    VirtualNetworkSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScmIpRestrictionDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScmIpRestrictionDefinition2"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Headers=deserialize_list(json_data.get("Headers"), ScmIpRestrictionDefinition),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            ServiceTag=json_data.get("ServiceTag"),
            VirtualNetworkSubnetId=json_data.get("VirtualNetworkSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScmIpRestrictionDefinition2 = ScmIpRestrictionDefinition2


@dataclass
class ScmIpRestrictionDefinition(BaseModel):
    XAzureFdid: Optional[Sequence[str]]
    XFdHealthProbe: Optional[Sequence[str]]
    XForwardedFor: Optional[Sequence[str]]
    XForwardedHost: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ScmIpRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScmIpRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            XAzureFdid=json_data.get("XAzureFdid"),
            XFdHealthProbe=json_data.get("XFdHealthProbe"),
            XForwardedFor=json_data.get("XForwardedFor"),
            XForwardedHost=json_data.get("XForwardedHost"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScmIpRestrictionDefinition = ScmIpRestrictionDefinition


@dataclass
class CorsDefinition(BaseModel):
    AllowedOrigins: Optional[Sequence[str]]
    SupportCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CorsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedOrigins=json_data.get("AllowedOrigins"),
            SupportCredentials=json_data.get("SupportCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CorsDefinition = CorsDefinition


@dataclass
class SourceControlDefinition(BaseModel):
    Branch: Optional[str]
    ManualIntegration: Optional[bool]
    RepoUrl: Optional[str]
    RollbackEnabled: Optional[bool]
    UseMercurial: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SourceControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceControlDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            ManualIntegration=json_data.get("ManualIntegration"),
            RepoUrl=json_data.get("RepoUrl"),
            RollbackEnabled=json_data.get("RollbackEnabled"),
            UseMercurial=json_data.get("UseMercurial"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceControlDefinition = SourceControlDefinition


@dataclass
class StorageAccountDefinition(BaseModel):
    AccessKey: Optional[str]
    AccountName: Optional[str]
    MountPath: Optional[str]
    Name: Optional[str]
    ShareName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StorageAccountDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StorageAccountDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            AccountName=json_data.get("AccountName"),
            MountPath=json_data.get("MountPath"),
            Name=json_data.get("Name"),
            ShareName=json_data.get("ShareName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StorageAccountDefinition = StorageAccountDefinition


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


