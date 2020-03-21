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
    AppServiceName: Optional[str]
    AppServicePlanId: Optional[str]
    AppSettings: Optional[Sequence["_AppSettings"]]
    ClientAffinityEnabled: Optional[bool]
    DefaultSiteHostname: Optional[str]
    Enabled: Optional[bool]
    HttpsOnly: Optional[bool]
    Id: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    SiteCredential: Optional[Sequence["_SiteCredential"]]
    Tags: Optional[Sequence["_Tags"]]
    AuthSettings: Optional[Sequence["_AuthSettings"]]
    ConnectionString: Optional[Sequence["_ConnectionString"]]
    Identity: Optional[Sequence["_Identity"]]
    Logs: Optional[Sequence["_Logs"]]
    SiteConfig: Optional[Sequence["_SiteConfig"]]
    Timeouts: Optional["_Timeouts"]
    ActiveDirectory: Optional[Sequence["_ActiveDirectory"]]
    Facebook: Optional[Sequence["_Facebook"]]
    Google: Optional[Sequence["_Google"]]
    Microsoft: Optional[Sequence["_Microsoft"]]
    Twitter: Optional[Sequence["_Twitter"]]
    ApplicationLogs: Optional[Sequence["_ApplicationLogs"]]
    HttpLogs: Optional[Sequence["_HttpLogs"]]
    Cors: Optional[Sequence["_Cors"]]
    AzureBlobStorage: Optional[Sequence["_AzureBlobStorage"]]
    FileSystem: Optional[Sequence["_FileSystem"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppServiceName=json_data.get("AppServiceName"),
            AppServicePlanId=json_data.get("AppServicePlanId"),
            AppSettings=json_data.get("AppSettings"),
            ClientAffinityEnabled=json_data.get("ClientAffinityEnabled"),
            DefaultSiteHostname=json_data.get("DefaultSiteHostname"),
            Enabled=json_data.get("Enabled"),
            HttpsOnly=json_data.get("HttpsOnly"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SiteCredential=json_data.get("SiteCredential"),
            Tags=json_data.get("Tags"),
            AuthSettings=json_data.get("AuthSettings"),
            ConnectionString=json_data.get("ConnectionString"),
            Identity=json_data.get("Identity"),
            Logs=json_data.get("Logs"),
            SiteConfig=json_data.get("SiteConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ActiveDirectory=json_data.get("ActiveDirectory"),
            Facebook=json_data.get("Facebook"),
            Google=json_data.get("Google"),
            Microsoft=json_data.get("Microsoft"),
            Twitter=json_data.get("Twitter"),
            ApplicationLogs=json_data.get("ApplicationLogs"),
            HttpLogs=json_data.get("HttpLogs"),
            Cors=json_data.get("Cors"),
            AzureBlobStorage=json_data.get("AzureBlobStorage"),
            FileSystem=json_data.get("FileSystem"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppSettings:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AppSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppSettings"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppSettings = AppSettings


@dataclass
class SiteCredential:
    Password: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SiteCredential"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteCredential"]:
        if not json_data:
            return None
        return cls(
            Password=json_data.get("Password"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteCredential = SiteCredential


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
class AuthSettings:
    AdditionalLoginParams: Optional[Sequence["_AdditionalLoginParams"]]
    AllowedExternalRedirectUrls: Optional[Sequence[str]]
    DefaultProvider: Optional[str]
    Enabled: Optional[bool]
    Issuer: Optional[str]
    RuntimeVersion: Optional[str]
    TokenRefreshExtensionHours: Optional[float]
    TokenStoreEnabled: Optional[bool]
    UnauthenticatedClientAction: Optional[str]
    ActiveDirectory: Optional[Sequence["_ActiveDirectory"]]
    Facebook: Optional[Sequence["_Facebook"]]
    Google: Optional[Sequence["_Google"]]
    Microsoft: Optional[Sequence["_Microsoft"]]
    Twitter: Optional[Sequence["_Twitter"]]

    @classmethod
    def _deserialize(
        cls: Type["_AuthSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthSettings"]:
        if not json_data:
            return None
        return cls(
            AdditionalLoginParams=json_data.get("AdditionalLoginParams"),
            AllowedExternalRedirectUrls=json_data.get("AllowedExternalRedirectUrls"),
            DefaultProvider=json_data.get("DefaultProvider"),
            Enabled=json_data.get("Enabled"),
            Issuer=json_data.get("Issuer"),
            RuntimeVersion=json_data.get("RuntimeVersion"),
            TokenRefreshExtensionHours=json_data.get("TokenRefreshExtensionHours"),
            TokenStoreEnabled=json_data.get("TokenStoreEnabled"),
            UnauthenticatedClientAction=json_data.get("UnauthenticatedClientAction"),
            ActiveDirectory=json_data.get("ActiveDirectory"),
            Facebook=json_data.get("Facebook"),
            Google=json_data.get("Google"),
            Microsoft=json_data.get("Microsoft"),
            Twitter=json_data.get("Twitter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthSettings = AuthSettings


@dataclass
class AdditionalLoginParams:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalLoginParams"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalLoginParams"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalLoginParams = AdditionalLoginParams


@dataclass
class ActiveDirectory:
    AllowedAudiences: Optional[Sequence[str]]
    ClientId: Optional[str]
    ClientSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActiveDirectory"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActiveDirectory"]:
        if not json_data:
            return None
        return cls(
            AllowedAudiences=json_data.get("AllowedAudiences"),
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActiveDirectory = ActiveDirectory


@dataclass
class Facebook:
    AppId: Optional[str]
    AppSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Facebook"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Facebook"]:
        if not json_data:
            return None
        return cls(
            AppId=json_data.get("AppId"),
            AppSecret=json_data.get("AppSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Facebook = Facebook


@dataclass
class Google:
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Google"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Google"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Google = Google


@dataclass
class Microsoft:
    ClientId: Optional[str]
    ClientSecret: Optional[str]
    OauthScopes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Microsoft"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Microsoft"]:
        if not json_data:
            return None
        return cls(
            ClientId=json_data.get("ClientId"),
            ClientSecret=json_data.get("ClientSecret"),
            OauthScopes=json_data.get("OauthScopes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Microsoft = Microsoft


@dataclass
class Twitter:
    ConsumerKey: Optional[str]
    ConsumerSecret: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Twitter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Twitter"]:
        if not json_data:
            return None
        return cls(
            ConsumerKey=json_data.get("ConsumerKey"),
            ConsumerSecret=json_data.get("ConsumerSecret"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Twitter = Twitter


@dataclass
class ConnectionString:
    Name: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionString"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionString"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionString = ConnectionString


@dataclass
class Identity:
    IdentityIds: Optional[Sequence[str]]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Identity"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Identity"]:
        if not json_data:
            return None
        return cls(
            IdentityIds=json_data.get("IdentityIds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Identity = Identity


@dataclass
class Logs:
    ApplicationLogs: Optional[Sequence["_ApplicationLogs"]]
    HttpLogs: Optional[Sequence["_HttpLogs"]]

    @classmethod
    def _deserialize(
        cls: Type["_Logs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Logs"]:
        if not json_data:
            return None
        return cls(
            ApplicationLogs=json_data.get("ApplicationLogs"),
            HttpLogs=json_data.get("HttpLogs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Logs = Logs


@dataclass
class ApplicationLogs:
    AzureBlobStorage: Optional[Sequence["_AzureBlobStorage"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationLogs"]:
        if not json_data:
            return None
        return cls(
            AzureBlobStorage=json_data.get("AzureBlobStorage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationLogs = ApplicationLogs


@dataclass
class AzureBlobStorage:
    RetentionInDays: Optional[float]
    SasUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AzureBlobStorage"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AzureBlobStorage"]:
        if not json_data:
            return None
        return cls(
            RetentionInDays=json_data.get("RetentionInDays"),
            SasUrl=json_data.get("SasUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AzureBlobStorage = AzureBlobStorage


@dataclass
class HttpLogs:
    AzureBlobStorage: Optional[Sequence["_AzureBlobStorage"]]
    FileSystem: Optional[Sequence["_FileSystem"]]

    @classmethod
    def _deserialize(
        cls: Type["_HttpLogs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpLogs"]:
        if not json_data:
            return None
        return cls(
            AzureBlobStorage=json_data.get("AzureBlobStorage"),
            FileSystem=json_data.get("FileSystem"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpLogs = HttpLogs


@dataclass
class FileSystem:
    RetentionInDays: Optional[float]
    RetentionInMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FileSystem"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileSystem"]:
        if not json_data:
            return None
        return cls(
            RetentionInDays=json_data.get("RetentionInDays"),
            RetentionInMb=json_data.get("RetentionInMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileSystem = FileSystem


@dataclass
class SiteConfig:
    AlwaysOn: Optional[bool]
    AppCommandLine: Optional[str]
    AutoSwapSlotName: Optional[str]
    DefaultDocuments: Optional[Sequence[str]]
    DotnetFrameworkVersion: Optional[str]
    FtpsState: Optional[str]
    Http2Enabled: Optional[bool]
    IpRestriction: Optional[Sequence["_IpRestriction"]]
    JavaContainer: Optional[str]
    JavaContainerVersion: Optional[str]
    JavaVersion: Optional[str]
    LinuxFxVersion: Optional[str]
    LocalMysqlEnabled: Optional[bool]
    ManagedPipelineMode: Optional[str]
    MinTlsVersion: Optional[str]
    PhpVersion: Optional[str]
    PythonVersion: Optional[str]
    RemoteDebuggingEnabled: Optional[bool]
    RemoteDebuggingVersion: Optional[str]
    ScmType: Optional[str]
    Use32BitWorkerProcess: Optional[bool]
    WebsocketsEnabled: Optional[bool]
    WindowsFxVersion: Optional[str]
    Cors: Optional[Sequence["_Cors"]]

    @classmethod
    def _deserialize(
        cls: Type["_SiteConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SiteConfig"]:
        if not json_data:
            return None
        return cls(
            AlwaysOn=json_data.get("AlwaysOn"),
            AppCommandLine=json_data.get("AppCommandLine"),
            AutoSwapSlotName=json_data.get("AutoSwapSlotName"),
            DefaultDocuments=json_data.get("DefaultDocuments"),
            DotnetFrameworkVersion=json_data.get("DotnetFrameworkVersion"),
            FtpsState=json_data.get("FtpsState"),
            Http2Enabled=json_data.get("Http2Enabled"),
            IpRestriction=json_data.get("IpRestriction"),
            JavaContainer=json_data.get("JavaContainer"),
            JavaContainerVersion=json_data.get("JavaContainerVersion"),
            JavaVersion=json_data.get("JavaVersion"),
            LinuxFxVersion=json_data.get("LinuxFxVersion"),
            LocalMysqlEnabled=json_data.get("LocalMysqlEnabled"),
            ManagedPipelineMode=json_data.get("ManagedPipelineMode"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            PhpVersion=json_data.get("PhpVersion"),
            PythonVersion=json_data.get("PythonVersion"),
            RemoteDebuggingEnabled=json_data.get("RemoteDebuggingEnabled"),
            RemoteDebuggingVersion=json_data.get("RemoteDebuggingVersion"),
            ScmType=json_data.get("ScmType"),
            Use32BitWorkerProcess=json_data.get("Use32BitWorkerProcess"),
            WebsocketsEnabled=json_data.get("WebsocketsEnabled"),
            WindowsFxVersion=json_data.get("WindowsFxVersion"),
            Cors=json_data.get("Cors"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SiteConfig = SiteConfig


@dataclass
class IpRestriction:
    IpAddress: Optional[str]
    VirtualNetworkSubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRestriction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRestriction"]:
        if not json_data:
            return None
        return cls(
            IpAddress=json_data.get("IpAddress"),
            VirtualNetworkSubnetId=json_data.get("VirtualNetworkSubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRestriction = IpRestriction


@dataclass
class Cors:
    AllowedOrigins: Optional[Sequence[str]]
    SupportCredentials: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Cors"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cors"]:
        if not json_data:
            return None
        return cls(
            AllowedOrigins=json_data.get("AllowedOrigins"),
            SupportCredentials=json_data.get("SupportCredentials"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cors = Cors


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


