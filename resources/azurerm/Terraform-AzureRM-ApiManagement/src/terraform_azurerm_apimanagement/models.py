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
    GatewayRegionalUrl: Optional[str]
    GatewayUrl: Optional[str]
    Location: Optional[str]
    ManagementApiUrl: Optional[str]
    Name: Optional[str]
    NotificationSenderEmail: Optional[str]
    Policy: Optional[Sequence["_Policy"]]
    PortalUrl: Optional[str]
    PublicIpAddresses: Optional[Sequence[str]]
    PublisherEmail: Optional[str]
    PublisherName: Optional[str]
    ResourceGroupName: Optional[str]
    ScmUrl: Optional[str]
    SkuName: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    AdditionalLocation: Optional[Sequence["_AdditionalLocation"]]
    Certificate: Optional[Sequence["_Certificate"]]
    HostnameConfiguration: Optional[Sequence["_HostnameConfiguration"]]
    Identity: Optional[Sequence["_Identity"]]
    Protocols: Optional[Sequence["_Protocols"]]
    Security: Optional[Sequence["_Security"]]
    SignIn: Optional[Sequence["_SignIn"]]
    SignUp: Optional[Sequence["_SignUp"]]
    Timeouts: Optional["_Timeouts"]
    Management: Optional[Sequence["_Management"]]
    Portal: Optional[Sequence["_Portal"]]
    Proxy: Optional[Sequence["_Proxy"]]
    Scm: Optional[Sequence["_Scm"]]
    TermsOfService: Optional[Sequence["_TermsOfService"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            GatewayRegionalUrl=json_data.get("GatewayRegionalUrl"),
            GatewayUrl=json_data.get("GatewayUrl"),
            Location=json_data.get("Location"),
            ManagementApiUrl=json_data.get("ManagementApiUrl"),
            Name=json_data.get("Name"),
            NotificationSenderEmail=json_data.get("NotificationSenderEmail"),
            Policy=json_data.get("Policy"),
            PortalUrl=json_data.get("PortalUrl"),
            PublicIpAddresses=json_data.get("PublicIpAddresses"),
            PublisherEmail=json_data.get("PublisherEmail"),
            PublisherName=json_data.get("PublisherName"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ScmUrl=json_data.get("ScmUrl"),
            SkuName=json_data.get("SkuName"),
            Tags=json_data.get("Tags"),
            AdditionalLocation=json_data.get("AdditionalLocation"),
            Certificate=json_data.get("Certificate"),
            HostnameConfiguration=json_data.get("HostnameConfiguration"),
            Identity=json_data.get("Identity"),
            Protocols=json_data.get("Protocols"),
            Security=json_data.get("Security"),
            SignIn=json_data.get("SignIn"),
            SignUp=json_data.get("SignUp"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            Management=json_data.get("Management"),
            Portal=json_data.get("Portal"),
            Proxy=json_data.get("Proxy"),
            Scm=json_data.get("Scm"),
            TermsOfService=json_data.get("TermsOfService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Policy:
    XmlContent: Optional[str]
    XmlLink: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Policy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Policy"]:
        if not json_data:
            return None
        return cls(
            XmlContent=json_data.get("XmlContent"),
            XmlLink=json_data.get("XmlLink"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Policy = Policy


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
class AdditionalLocation:
    Location: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalLocation"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalLocation"]:
        if not json_data:
            return None
        return cls(
            Location=json_data.get("Location"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalLocation = AdditionalLocation


@dataclass
class Certificate:
    CertificatePassword: Optional[str]
    EncodedCertificate: Optional[str]
    StoreName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            CertificatePassword=json_data.get("CertificatePassword"),
            EncodedCertificate=json_data.get("EncodedCertificate"),
            StoreName=json_data.get("StoreName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


@dataclass
class HostnameConfiguration:
    Management: Optional[Sequence["_Management"]]
    Portal: Optional[Sequence["_Portal"]]
    Proxy: Optional[Sequence["_Proxy"]]
    Scm: Optional[Sequence["_Scm"]]

    @classmethod
    def _deserialize(
        cls: Type["_HostnameConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostnameConfiguration"]:
        if not json_data:
            return None
        return cls(
            Management=json_data.get("Management"),
            Portal=json_data.get("Portal"),
            Proxy=json_data.get("Proxy"),
            Scm=json_data.get("Scm"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostnameConfiguration = HostnameConfiguration


@dataclass
class Management:
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Management"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Management"]:
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
_Management = Management


@dataclass
class Portal:
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Portal"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Portal"]:
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
_Portal = Portal


@dataclass
class Proxy:
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    DefaultSslBinding: Optional[bool]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Proxy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Proxy"]:
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
_Proxy = Proxy


@dataclass
class Scm:
    Certificate: Optional[str]
    CertificatePassword: Optional[str]
    HostName: Optional[str]
    KeyVaultId: Optional[str]
    NegotiateClientCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Scm"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Scm"]:
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
_Scm = Scm


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
class Protocols:
    EnableHttp2: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Protocols"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Protocols"]:
        if not json_data:
            return None
        return cls(
            EnableHttp2=json_data.get("EnableHttp2"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Protocols = Protocols


@dataclass
class Security:
    EnableBackendSsl30: Optional[bool]
    EnableBackendTls10: Optional[bool]
    EnableBackendTls11: Optional[bool]
    EnableFrontendSsl30: Optional[bool]
    EnableFrontendTls10: Optional[bool]
    EnableFrontendTls11: Optional[bool]
    EnableTripleDesCiphers: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_Security"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Security"]:
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
        )


# work around possible type aliasing issues when variable has same name as a model
_Security = Security


@dataclass
class SignIn:
    Enabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SignIn"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignIn"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignIn = SignIn


@dataclass
class SignUp:
    Enabled: Optional[bool]
    TermsOfService: Optional[Sequence["_TermsOfService"]]

    @classmethod
    def _deserialize(
        cls: Type["_SignUp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SignUp"]:
        if not json_data:
            return None
        return cls(
            Enabled=json_data.get("Enabled"),
            TermsOfService=json_data.get("TermsOfService"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SignUp = SignUp


@dataclass
class TermsOfService:
    ConsentRequired: Optional[bool]
    Enabled: Optional[bool]
    Text: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TermsOfService"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TermsOfService"]:
        if not json_data:
            return None
        return cls(
            ConsentRequired=json_data.get("ConsentRequired"),
            Enabled=json_data.get("Enabled"),
            Text=json_data.get("Text"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TermsOfService = TermsOfService


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


