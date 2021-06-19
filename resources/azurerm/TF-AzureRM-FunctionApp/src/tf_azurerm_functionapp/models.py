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
    ClientCertMode: Optional[str]
    CustomDomainVerificationId: Optional[str]
    DailyMemoryTimeQuota: Optional[float]
    DefaultHostname: Optional[str]
    EnableBuiltinLogging: Optional[bool]
    Enabled: Optional[bool]
    HttpsOnly: Optional[bool]
    Id: Optional[str]
    Kind: Optional[str]
    Location: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    OutboundIpAddresses: Optional[str]
    PossibleOutboundIpAddresses: Optional[str]
    ResourceGroupName: Optional[str]
    SiteCredential: Optional[Sequence["_SiteCredentialDefinition"]]
    StorageAccountAccessKey: Optional[str]
    StorageAccountName: Optional[str]
    StorageConnectionString: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    AuthSettings: Optional[Sequence["_AuthSettingsDefinition"]]
    ConnectionString: Optional[Sequence["_ConnectionStringDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    SiteConfig: Optional[Sequence["_SiteConfigDefinition"]]
    SourceControl: Optional[Sequence["_SourceControlDefinition"]]
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
            ClientCertMode=json_data.get("ClientCertMode"),
            CustomDomainVerificationId=json_data.get("CustomDomainVerificationId"),
            DailyMemoryTimeQuota=json_data.get("DailyMemoryTimeQuota"),
            DefaultHostname=json_data.get("DefaultHostname"),
            EnableBuiltinLogging=json_data.get("EnableBuiltinLogging"),
            Enabled=json_data.get("Enabled"),
            HttpsOnly=json_data.get("HttpsOnly"),
            Id=json_data.get("Id"),
            Kind=json_data.get("Kind"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            OutboundIpAddresses=json_data.get("OutboundIpAddresses"),
            PossibleOutboundIpAddresses=json_data.get("PossibleOutboundIpAddresses"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SiteCredential=deserialize_list(json_data.get("SiteCredential"), SiteCredentialDefinition),
            StorageAccountAccessKey=json_data.get("StorageAccountAccessKey"),
            StorageAccountName=json_data.get("StorageAccountName"),
            StorageConnectionString=json_data.get("StorageConnectionString"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            AuthSettings=deserialize_list(json_data.get("AuthSettings"), AuthSettingsDefinition),
            ConnectionString=deserialize_list(json_data.get("ConnectionString"), ConnectionStringDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            SiteConfig=deserialize_list(json_data.get("SiteConfig"), SiteConfigDefinition),
            SourceControl=deserialize_list(json_data.get("SourceControl"), SourceControlDefinition),
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
class SiteConfigDefinition(BaseModel):
    AlwaysOn: Optional[bool]
    AutoSwapSlotName: Optional[str]
    FtpsState: Optional[str]
    HealthCheckPath: Optional[str]
    Http2Enabled: Optional[bool]
    IpRestriction: Optional[Sequence["_IpRestrictionDefinition2"]]
    JavaVersion: Optional[str]
    LinuxFxVersion: Optional[str]
    MinTlsVersion: Optional[str]
    PreWarmedInstanceCount: Optional[float]
    ScmIpRestriction: Optional[Sequence["_ScmIpRestrictionDefinition2"]]
    ScmType: Optional[str]
    ScmUseMainIpRestriction: Optional[bool]
    Use32BitWorkerProcess: Optional[bool]
    WebsocketsEnabled: Optional[bool]
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
            AutoSwapSlotName=json_data.get("AutoSwapSlotName"),
            FtpsState=json_data.get("FtpsState"),
            HealthCheckPath=json_data.get("HealthCheckPath"),
            Http2Enabled=json_data.get("Http2Enabled"),
            IpRestriction=deserialize_list(json_data.get("IpRestriction"), IpRestrictionDefinition2),
            JavaVersion=json_data.get("JavaVersion"),
            LinuxFxVersion=json_data.get("LinuxFxVersion"),
            MinTlsVersion=json_data.get("MinTlsVersion"),
            PreWarmedInstanceCount=json_data.get("PreWarmedInstanceCount"),
            ScmIpRestriction=deserialize_list(json_data.get("ScmIpRestriction"), ScmIpRestrictionDefinition2),
            ScmType=json_data.get("ScmType"),
            ScmUseMainIpRestriction=json_data.get("ScmUseMainIpRestriction"),
            Use32BitWorkerProcess=json_data.get("Use32BitWorkerProcess"),
            WebsocketsEnabled=json_data.get("WebsocketsEnabled"),
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


