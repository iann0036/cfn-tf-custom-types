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
    CommonCriteriaMode: Optional[bool]
    DefaultLicenseTier: Optional[str]
    DnsVirtualserviceRefs: Optional[Sequence[str]]
    DockerMode: Optional[bool]
    EnableCors: Optional[bool]
    FipsMode: Optional[bool]
    Id: Optional[str]
    SshCiphers: Optional[Sequence[str]]
    SshHmacs: Optional[Sequence[str]]
    Uuid: Optional[str]
    WelcomeWorkflowComplete: Optional[bool]
    AdminAuthConfiguration: Optional[Sequence["_AdminAuthConfigurationDefinition"]]
    DnsConfiguration: Optional[Sequence["_DnsConfigurationDefinition"]]
    EmailConfiguration: Optional[Sequence["_EmailConfigurationDefinition"]]
    GlobalTenantConfig: Optional[Sequence["_GlobalTenantConfigDefinition"]]
    LinuxConfiguration: Optional[Sequence["_LinuxConfigurationDefinition"]]
    MgmtIpAccessControl: Optional[Sequence["_MgmtIpAccessControlDefinition"]]
    NtpConfiguration: Optional[Sequence["_NtpConfigurationDefinition"]]
    PortalConfiguration: Optional[Sequence["_PortalConfigurationDefinition"]]
    ProxyConfiguration: Optional[Sequence["_ProxyConfigurationDefinition"]]
    SecureChannelConfiguration: Optional[Sequence["_SecureChannelConfigurationDefinition"]]
    SnmpConfiguration: Optional[Sequence["_SnmpConfigurationDefinition"]]

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
            CommonCriteriaMode=json_data.get("CommonCriteriaMode"),
            DefaultLicenseTier=json_data.get("DefaultLicenseTier"),
            DnsVirtualserviceRefs=json_data.get("DnsVirtualserviceRefs"),
            DockerMode=json_data.get("DockerMode"),
            EnableCors=json_data.get("EnableCors"),
            FipsMode=json_data.get("FipsMode"),
            Id=json_data.get("Id"),
            SshCiphers=json_data.get("SshCiphers"),
            SshHmacs=json_data.get("SshHmacs"),
            Uuid=json_data.get("Uuid"),
            WelcomeWorkflowComplete=json_data.get("WelcomeWorkflowComplete"),
            AdminAuthConfiguration=deserialize_list(json_data.get("AdminAuthConfiguration"), AdminAuthConfigurationDefinition),
            DnsConfiguration=deserialize_list(json_data.get("DnsConfiguration"), DnsConfigurationDefinition),
            EmailConfiguration=deserialize_list(json_data.get("EmailConfiguration"), EmailConfigurationDefinition),
            GlobalTenantConfig=deserialize_list(json_data.get("GlobalTenantConfig"), GlobalTenantConfigDefinition),
            LinuxConfiguration=deserialize_list(json_data.get("LinuxConfiguration"), LinuxConfigurationDefinition),
            MgmtIpAccessControl=deserialize_list(json_data.get("MgmtIpAccessControl"), MgmtIpAccessControlDefinition),
            NtpConfiguration=deserialize_list(json_data.get("NtpConfiguration"), NtpConfigurationDefinition),
            PortalConfiguration=deserialize_list(json_data.get("PortalConfiguration"), PortalConfigurationDefinition),
            ProxyConfiguration=deserialize_list(json_data.get("ProxyConfiguration"), ProxyConfigurationDefinition),
            SecureChannelConfiguration=deserialize_list(json_data.get("SecureChannelConfiguration"), SecureChannelConfigurationDefinition),
            SnmpConfiguration=deserialize_list(json_data.get("SnmpConfiguration"), SnmpConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdminAuthConfigurationDefinition(BaseModel):
    AllowLocalUserLogin: Optional[bool]
    AuthProfileRef: Optional[str]
    AlternateAuthConfigurations: Optional[Sequence["_AlternateAuthConfigurationsDefinition"]]
    MappingRules: Optional[Sequence["_MappingRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdminAuthConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdminAuthConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowLocalUserLogin=json_data.get("AllowLocalUserLogin"),
            AuthProfileRef=json_data.get("AuthProfileRef"),
            AlternateAuthConfigurations=deserialize_list(json_data.get("AlternateAuthConfigurations"), AlternateAuthConfigurationsDefinition),
            MappingRules=deserialize_list(json_data.get("MappingRules"), MappingRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdminAuthConfigurationDefinition = AdminAuthConfigurationDefinition


@dataclass
class AlternateAuthConfigurationsDefinition(BaseModel):
    AuthProfileRef: Optional[str]
    Index: Optional[float]
    MappingRules: Optional[Sequence["_MappingRulesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlternateAuthConfigurationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternateAuthConfigurationsDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthProfileRef=json_data.get("AuthProfileRef"),
            Index=json_data.get("Index"),
            MappingRules=deserialize_list(json_data.get("MappingRules"), MappingRulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternateAuthConfigurationsDefinition = AlternateAuthConfigurationsDefinition


@dataclass
class MappingRulesDefinition(BaseModel):
    AssignPolicy: Optional[str]
    AssignRole: Optional[str]
    AssignTenant: Optional[str]
    AssignUserprofile: Optional[str]
    Index: Optional[float]
    IsSuperuser: Optional[bool]
    PolicyAttributeName: Optional[str]
    RoleAttributeName: Optional[str]
    RoleRefs: Optional[Sequence[str]]
    TenantAttributeName: Optional[str]
    TenantRefs: Optional[Sequence[str]]
    UserprofileAttributeName: Optional[str]
    UserprofileRef: Optional[str]
    AttributeMatch: Optional[Sequence["_AttributeMatchDefinition"]]
    GroupMatch: Optional[Sequence["_GroupMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MappingRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MappingRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            AssignPolicy=json_data.get("AssignPolicy"),
            AssignRole=json_data.get("AssignRole"),
            AssignTenant=json_data.get("AssignTenant"),
            AssignUserprofile=json_data.get("AssignUserprofile"),
            Index=json_data.get("Index"),
            IsSuperuser=json_data.get("IsSuperuser"),
            PolicyAttributeName=json_data.get("PolicyAttributeName"),
            RoleAttributeName=json_data.get("RoleAttributeName"),
            RoleRefs=json_data.get("RoleRefs"),
            TenantAttributeName=json_data.get("TenantAttributeName"),
            TenantRefs=json_data.get("TenantRefs"),
            UserprofileAttributeName=json_data.get("UserprofileAttributeName"),
            UserprofileRef=json_data.get("UserprofileRef"),
            AttributeMatch=deserialize_list(json_data.get("AttributeMatch"), AttributeMatchDefinition),
            GroupMatch=deserialize_list(json_data.get("GroupMatch"), GroupMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MappingRulesDefinition = MappingRulesDefinition


@dataclass
class AttributeMatchDefinition(BaseModel):
    Criteria: Optional[str]
    Name: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AttributeMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttributeMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            Name=json_data.get("Name"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttributeMatchDefinition = AttributeMatchDefinition


@dataclass
class GroupMatchDefinition(BaseModel):
    Criteria: Optional[str]
    Groups: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_GroupMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GroupMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Criteria=json_data.get("Criteria"),
            Groups=json_data.get("Groups"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GroupMatchDefinition = GroupMatchDefinition


@dataclass
class DnsConfigurationDefinition(BaseModel):
    SearchDomain: Optional[str]
    ServerList: Optional[Sequence["_ServerListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnsConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SearchDomain=json_data.get("SearchDomain"),
            ServerList=deserialize_list(json_data.get("ServerList"), ServerListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsConfigurationDefinition = DnsConfigurationDefinition


@dataclass
class ServerListDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerListDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerListDefinition = ServerListDefinition


@dataclass
class EmailConfigurationDefinition(BaseModel):
    AuthPassword: Optional[str]
    AuthUsername: Optional[str]
    DisableTls: Optional[bool]
    FromEmail: Optional[str]
    MailServerName: Optional[str]
    MailServerPort: Optional[float]
    SmtpType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EmailConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EmailConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthPassword=json_data.get("AuthPassword"),
            AuthUsername=json_data.get("AuthUsername"),
            DisableTls=json_data.get("DisableTls"),
            FromEmail=json_data.get("FromEmail"),
            MailServerName=json_data.get("MailServerName"),
            MailServerPort=json_data.get("MailServerPort"),
            SmtpType=json_data.get("SmtpType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EmailConfigurationDefinition = EmailConfigurationDefinition


@dataclass
class GlobalTenantConfigDefinition(BaseModel):
    SeInProviderContext: Optional[bool]
    TenantAccessToProviderSe: Optional[bool]
    TenantVrf: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_GlobalTenantConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GlobalTenantConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            SeInProviderContext=json_data.get("SeInProviderContext"),
            TenantAccessToProviderSe=json_data.get("TenantAccessToProviderSe"),
            TenantVrf=json_data.get("TenantVrf"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GlobalTenantConfigDefinition = GlobalTenantConfigDefinition


@dataclass
class LinuxConfigurationDefinition(BaseModel):
    Banner: Optional[str]
    CisMode: Optional[bool]
    Motd: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LinuxConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LinuxConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Banner=json_data.get("Banner"),
            CisMode=json_data.get("CisMode"),
            Motd=json_data.get("Motd"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LinuxConfigurationDefinition = LinuxConfigurationDefinition


@dataclass
class MgmtIpAccessControlDefinition(BaseModel):
    ApiAccess: Optional[Sequence["_ApiAccessDefinition"]]
    ShellServerAccess: Optional[Sequence["_ShellServerAccessDefinition"]]
    SnmpAccess: Optional[Sequence["_SnmpAccessDefinition"]]
    SshAccess: Optional[Sequence["_SshAccessDefinition"]]
    SysintAccess: Optional[Sequence["_SysintAccessDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MgmtIpAccessControlDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MgmtIpAccessControlDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiAccess=deserialize_list(json_data.get("ApiAccess"), ApiAccessDefinition),
            ShellServerAccess=deserialize_list(json_data.get("ShellServerAccess"), ShellServerAccessDefinition),
            SnmpAccess=deserialize_list(json_data.get("SnmpAccess"), SnmpAccessDefinition),
            SshAccess=deserialize_list(json_data.get("SshAccess"), SshAccessDefinition),
            SysintAccess=deserialize_list(json_data.get("SysintAccess"), SysintAccessDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MgmtIpAccessControlDefinition = MgmtIpAccessControlDefinition


@dataclass
class ApiAccessDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ApiAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApiAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApiAccessDefinition = ApiAccessDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class RangesDefinition(BaseModel):
    Begin: Optional[Sequence["_BeginDefinition"]]
    End: Optional[Sequence["_EndDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            Begin=deserialize_list(json_data.get("Begin"), BeginDefinition),
            End=deserialize_list(json_data.get("End"), EndDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class BeginDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BeginDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BeginDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BeginDefinition = BeginDefinition


@dataclass
class EndDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EndDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndDefinition = EndDefinition


@dataclass
class ShellServerAccessDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ShellServerAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShellServerAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShellServerAccessDefinition = ShellServerAccessDefinition


@dataclass
class SnmpAccessDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpAccessDefinition = SnmpAccessDefinition


@dataclass
class SshAccessDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SshAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SshAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SshAccessDefinition = SshAccessDefinition


@dataclass
class SysintAccessDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SysintAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SysintAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SysintAccessDefinition = SysintAccessDefinition


@dataclass
class NtpConfigurationDefinition(BaseModel):
    NtpAuthenticationKeys: Optional[Sequence["_NtpAuthenticationKeysDefinition"]]
    NtpServerList: Optional[Sequence["_NtpServerListDefinition"]]
    NtpServers: Optional[Sequence["_NtpServersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NtpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            NtpAuthenticationKeys=deserialize_list(json_data.get("NtpAuthenticationKeys"), NtpAuthenticationKeysDefinition),
            NtpServerList=deserialize_list(json_data.get("NtpServerList"), NtpServerListDefinition),
            NtpServers=deserialize_list(json_data.get("NtpServers"), NtpServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpConfigurationDefinition = NtpConfigurationDefinition


@dataclass
class NtpAuthenticationKeysDefinition(BaseModel):
    Algorithm: Optional[str]
    Key: Optional[str]
    KeyNumber: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NtpAuthenticationKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpAuthenticationKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            Key=json_data.get("Key"),
            KeyNumber=json_data.get("KeyNumber"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpAuthenticationKeysDefinition = NtpAuthenticationKeysDefinition


@dataclass
class NtpServerListDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NtpServerListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpServerListDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpServerListDefinition = NtpServerListDefinition


@dataclass
class NtpServersDefinition(BaseModel):
    KeyNumber: Optional[float]
    Server: Optional[Sequence["_ServerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NtpServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NtpServersDefinition"]:
        if not json_data:
            return None
        return cls(
            KeyNumber=json_data.get("KeyNumber"),
            Server=deserialize_list(json_data.get("Server"), ServerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NtpServersDefinition = NtpServersDefinition


@dataclass
class ServerDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerDefinition = ServerDefinition


@dataclass
class PortalConfigurationDefinition(BaseModel):
    AllowBasicAuthentication: Optional[bool]
    ApiForceTimeout: Optional[float]
    DisableRemoteCliShell: Optional[bool]
    DisableSwagger: Optional[bool]
    EnableClickjackingProtection: Optional[bool]
    EnableHttp: Optional[bool]
    EnableHttps: Optional[bool]
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    MinimumPasswordLength: Optional[float]
    PasswordStrengthCheck: Optional[bool]
    RedirectToHttps: Optional[bool]
    SslkeyandcertificateRefs: Optional[Sequence[str]]
    SslprofileRef: Optional[str]
    UseUuidFromInput: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PortalConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowBasicAuthentication=json_data.get("AllowBasicAuthentication"),
            ApiForceTimeout=json_data.get("ApiForceTimeout"),
            DisableRemoteCliShell=json_data.get("DisableRemoteCliShell"),
            DisableSwagger=json_data.get("DisableSwagger"),
            EnableClickjackingProtection=json_data.get("EnableClickjackingProtection"),
            EnableHttp=json_data.get("EnableHttp"),
            EnableHttps=json_data.get("EnableHttps"),
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            MinimumPasswordLength=json_data.get("MinimumPasswordLength"),
            PasswordStrengthCheck=json_data.get("PasswordStrengthCheck"),
            RedirectToHttps=json_data.get("RedirectToHttps"),
            SslkeyandcertificateRefs=json_data.get("SslkeyandcertificateRefs"),
            SslprofileRef=json_data.get("SslprofileRef"),
            UseUuidFromInput=json_data.get("UseUuidFromInput"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalConfigurationDefinition = PortalConfigurationDefinition


@dataclass
class ProxyConfigurationDefinition(BaseModel):
    Host: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyConfigurationDefinition = ProxyConfigurationDefinition


@dataclass
class SecureChannelConfigurationDefinition(BaseModel):
    SslkeyandcertificateRefs: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SecureChannelConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecureChannelConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SslkeyandcertificateRefs=json_data.get("SslkeyandcertificateRefs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecureChannelConfigurationDefinition = SecureChannelConfigurationDefinition


@dataclass
class SnmpConfigurationDefinition(BaseModel):
    Community: Optional[str]
    LargeTrapPayload: Optional[bool]
    SysContact: Optional[str]
    SysLocation: Optional[str]
    Version: Optional[str]
    SnmpV3Config: Optional[Sequence["_SnmpV3ConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Community=json_data.get("Community"),
            LargeTrapPayload=json_data.get("LargeTrapPayload"),
            SysContact=json_data.get("SysContact"),
            SysLocation=json_data.get("SysLocation"),
            Version=json_data.get("Version"),
            SnmpV3Config=deserialize_list(json_data.get("SnmpV3Config"), SnmpV3ConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpConfigurationDefinition = SnmpConfigurationDefinition


@dataclass
class SnmpV3ConfigDefinition(BaseModel):
    EngineId: Optional[str]
    User: Optional[Sequence["_UserDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SnmpV3ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnmpV3ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            EngineId=json_data.get("EngineId"),
            User=deserialize_list(json_data.get("User"), UserDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnmpV3ConfigDefinition = SnmpV3ConfigDefinition


@dataclass
class UserDefinition(BaseModel):
    AuthPassphrase: Optional[str]
    AuthType: Optional[str]
    PrivPassphrase: Optional[str]
    PrivType: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UserDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UserDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthPassphrase=json_data.get("AuthPassphrase"),
            AuthType=json_data.get("AuthType"),
            PrivPassphrase=json_data.get("PrivPassphrase"),
            PrivType=json_data.get("PrivType"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UserDefinition = UserDefinition


