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
    ClientCertificateEnabled: Optional[bool]
    DeveloperPortalUrl: Optional[str]
    GatewayDisabled: Optional[bool]
    GatewayRegionalUrl: Optional[str]
    GatewayUrl: Optional[str]
    Id: Optional[str]
    Location: Optional[str]
    ManagementApiUrl: Optional[str]
    MinApiVersion: Optional[str]
    Name: Optional[str]
    NotificationSenderEmail: Optional[str]
    Policy: Optional[Sequence["_PolicyDefinition"]]
    PortalUrl: Optional[str]
    PrivateIpAddresses: Optional[Sequence[str]]
    PublicIpAddresses: Optional[Sequence[str]]
    PublisherEmail: Optional[str]
    PublisherName: Optional[str]
    ResourceGroupName: Optional[str]
    ScmUrl: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    VirtualNetworkType: Optional[str]
    Zones: Optional[Sequence[str]]
    AdditionalLocation: Optional[Sequence["_AdditionalLocationDefinition"]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    HostnameConfiguration: Optional[Sequence["_HostnameConfigurationDefinition"]]
    Identity: Optional[Sequence["_IdentityDefinition"]]
    Protocols: Optional[Sequence["_ProtocolsDefinition"]]
    Security: Optional[Sequence["_SecurityDefinition"]]
    SignIn: Optional[Sequence["_SignInDefinition"]]
    SignUp: Optional[Sequence["_SignUpDefinition"]]
    TenantAccess: Optional[Sequence["_TenantAccessDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    VirtualNetworkConfiguration: Optional[Sequence["_VirtualNetworkConfigurationDefinition"]]

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
            ClientCertificateEnabled=json_data.get("ClientCertificateEnabled"),
            DeveloperPortalUrl=json_data.get("DeveloperPortalUrl"),
            GatewayDisabled=json_data.get("GatewayDisabled"),
            GatewayRegionalUrl=json_data.get("GatewayRegionalUrl"),
            GatewayUrl=json_data.get("GatewayUrl"),
            Id=json_data.get("Id"),
            Location=json_data.get("Location"),
            ManagementApiUrl=json_data.get("ManagementApiUrl"),
            MinApiVersion=json_data.get("MinApiVersion"),
            Name=json_data.get("Name"),
            NotificationSenderEmail=json_data.get("NotificationSenderEmail"),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
            PortalUrl=json_data.get("PortalUrl"),
            PrivateIpAddresses=json_data.get("PrivateIpAddresses"),
            PublicIpAddresses=json_data.get("PublicIpAddresses"),
            PublisherEmail=json_data.get("PublisherEmail"),
            PublisherName=json_data.get("PublisherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScmUrl=json_data.get("ScmUrl"),
            SkuName=json_data.get("SkuName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            VirtualNetworkType=json_data.get("VirtualNetworkType"),
            Zones=json_data.get("Zones"),
            AdditionalLocation=deserialize_list(json_data.get("AdditionalLocation"), AdditionalLocationDefinition),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            HostnameConfiguration=deserialize_list(json_data.get("HostnameConfiguration"), HostnameConfigurationDefinition),
            Identity=deserialize_list(json_data.get("Identity"), IdentityDefinition),
            Protocols=deserialize_list(json_data.get("Protocols"), ProtocolsDefinition),
            Security=deserialize_list(json_data.get("Security"), SecurityDefinition),
            SignIn=deserialize_list(json_data.get("SignIn"), SignInDefinition),
            SignUp=deserialize_list(json_data.get("SignUp"), SignUpDefinition),
            TenantAccess=deserialize_list(json_data.get("TenantAccess"), TenantAccessDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            VirtualNetworkConfiguration=deserialize_list(json_data.get("VirtualNetworkConfiguration"), VirtualNetworkConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyDefinition(BaseModel):
    XmlContent: Optional[str]
    XmlLink: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            XmlContent=json_data.get("XmlContent"),
            XmlLink=json_data.get("XmlLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


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
class AdditionalLocationDefinition(BaseModel):
    Location: Optional[str]
    VirtualNetworkConfiguration: Optional[Sequence["_VirtualNetworkConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalLocationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalLocationDefinition"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
            VirtualNetworkConfiguration=deserialize_list(json_data.get("VirtualNetworkConfiguration"), VirtualNetworkConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalLocationDefinition = AdditionalLocationDefinition


@dataclass
class VirtualNetworkConfigurationDefinition(BaseModel):
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualNetworkConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualNetworkConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualNetworkConfigurationDefinition = VirtualNetworkConfigurationDefinition


@dataclass
class CertificateDefinition(BaseModel):
    CertificatePassword: Optional[str]
    EncodedCertificate: Optional[str]
    StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificatePassword=json_data.get("CertificatePassword"),
            EncodedCertificate=json_data.get("EncodedCertificate"),
            StoreName=json_data.get("StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class HostnameConfigurationDefinition(BaseModel):
    DeveloperPortal: Optional[Sequence["_DeveloperPortalDefinition"]]
    Management: Optional[Sequence["_ManagementDefinition"]]
    Portal: Optional[Sequence["_PortalDefinition"]]
    Proxy: Optional[Sequence["_ProxyDefinition"]]
    Scm: Optional[Sequence["_ScmDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostnameConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostnameConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            DeveloperPortal=deserialize_list(json_data.get("DeveloperPortal"), DeveloperPortalDefinition),
            Management=deserialize_list(json_data.get("Management"), ManagementDefinition),
            Portal=deserialize_list(json_data.get("Portal"), PortalDefinition),
            Proxy=deserialize_list(json_data.get("Proxy"), ProxyDefinition),
            Scm=deserialize_list(json_data.get("Scm"), ScmDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostnameConfigurationDefinition = HostnameConfigurationDefinition


@dataclass
class DeveloperPortalDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeveloperPortalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeveloperPortalDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeveloperPortalDefinition = DeveloperPortalDefinition


@dataclass
class ManagementDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ManagementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagementDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagementDefinition = ManagementDefinition


@dataclass
class PortalDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PortalDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortalDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortalDefinition = PortalDefinition


@dataclass
class ProxyDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    DefaultSslBinding: Optional[bool]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ProxyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProxyDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            DefaultSslBinding=json_data.get("DefaultSslBinding"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProxyDefinition = ProxyDefinition


@dataclass
class ScmDefinition(BaseModel):
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ScmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScmDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            CertificatePassword=json_data.get("CertificatePassword"),
            HostName=json_data.get("HostName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            NegotiateClientCertificate=json_data.get("NegotiateClientCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScmDefinition = ScmDefinition


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
class ProtocolsDefinition(BaseModel):
    EnableHttp2: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ProtocolsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtocolsDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableHttp2=json_data.get("EnableHttp2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtocolsDefinition = ProtocolsDefinition


@dataclass
class SecurityDefinition(BaseModel):
    EnableBackendSsl30: Optional[bool]
    EnableBackendTls10: Optional[bool]
    EnableBackendTls11: Optional[bool]
    EnableFrontendSsl30: Optional[bool]
    EnableFrontendTls10: Optional[bool]
    EnableFrontendTls11: Optional[bool]
    EnableTripleDesCiphers: Optional[bool]
    TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled: Optional[bool]
    TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled: Optional[bool]
    TlsEcdheRsaWithAes128CbcShaCiphersEnabled: Optional[bool]
    TlsEcdheRsaWithAes256CbcShaCiphersEnabled: Optional[bool]
    TlsRsaWithAes128CbcSha256CiphersEnabled: Optional[bool]
    TlsRsaWithAes128CbcShaCiphersEnabled: Optional[bool]
    TlsRsaWithAes128GcmSha256CiphersEnabled: Optional[bool]
    TlsRsaWithAes256CbcSha256CiphersEnabled: Optional[bool]
    TlsRsaWithAes256CbcShaCiphersEnabled: Optional[bool]
    TripleDesCiphersEnabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SecurityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecurityDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableBackendSsl30=json_data.get("EnableBackendSsl30"),
            EnableBackendTls10=json_data.get("EnableBackendTls10"),
            EnableBackendTls11=json_data.get("EnableBackendTls11"),
            EnableFrontendSsl30=json_data.get("EnableFrontendSsl30"),
            EnableFrontendTls10=json_data.get("EnableFrontendTls10"),
            EnableFrontendTls11=json_data.get("EnableFrontendTls11"),
            EnableTripleDesCiphers=json_data.get("EnableTripleDesCiphers"),
            TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled=json_data.get("TlsEcdheEcdsaWithAes128CbcShaCiphersEnabled"),
            TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled=json_data.get("TlsEcdheEcdsaWithAes256CbcShaCiphersEnabled"),
            TlsEcdheRsaWithAes128CbcShaCiphersEnabled=json_data.get("TlsEcdheRsaWithAes128CbcShaCiphersEnabled"),
            TlsEcdheRsaWithAes256CbcShaCiphersEnabled=json_data.get("TlsEcdheRsaWithAes256CbcShaCiphersEnabled"),
            TlsRsaWithAes128CbcSha256CiphersEnabled=json_data.get("TlsRsaWithAes128CbcSha256CiphersEnabled"),
            TlsRsaWithAes128CbcShaCiphersEnabled=json_data.get("TlsRsaWithAes128CbcShaCiphersEnabled"),
            TlsRsaWithAes128GcmSha256CiphersEnabled=json_data.get("TlsRsaWithAes128GcmSha256CiphersEnabled"),
            TlsRsaWithAes256CbcSha256CiphersEnabled=json_data.get("TlsRsaWithAes256CbcSha256CiphersEnabled"),
            TlsRsaWithAes256CbcShaCiphersEnabled=json_data.get("TlsRsaWithAes256CbcShaCiphersEnabled"),
            TripleDesCiphersEnabled=json_data.get("TripleDesCiphersEnabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecurityDefinition = SecurityDefinition


@dataclass
class SignInDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SignInDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignInDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignInDefinition = SignInDefinition


@dataclass
class SignUpDefinition(BaseModel):
    Enabled: Optional[bool]
    TermsOfService: Optional[Sequence["_TermsOfServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SignUpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignUpDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            TermsOfService=deserialize_list(json_data.get("TermsOfService"), TermsOfServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignUpDefinition = SignUpDefinition


@dataclass
class TermsOfServiceDefinition(BaseModel):
    ConsentRequired: Optional[bool]
    Enabled: Optional[bool]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TermsOfServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TermsOfServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            ConsentRequired=json_data.get("ConsentRequired"),
            Enabled=json_data.get("Enabled"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TermsOfServiceDefinition = TermsOfServiceDefinition


@dataclass
class TenantAccessDefinition(BaseModel):
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TenantAccessDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TenantAccessDefinition"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TenantAccessDefinition = TenantAccessDefinition


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


