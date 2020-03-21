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
    CertificateData: Optional[str]
    KeyVaultId: Optional[str]
    Name: Optional[str]
    SecretId: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Thumbprint: Optional[str]
    Version: Optional[str]
    Certificate: Optional[Sequence["_Certificate"]]
    CertificatePolicy: Optional[Sequence["_CertificatePolicy"]]
    Timeouts: Optional["_Timeouts"]
    IssuerParameters: Optional[Sequence["_IssuerParameters"]]
    KeyProperties: Optional[Sequence["_KeyProperties"]]
    LifetimeAction: Optional[Sequence["_LifetimeAction"]]
    SecretProperties: Optional[Sequence["_SecretProperties"]]
    X509CertificateProperties: Optional[Sequence["_X509CertificateProperties"]]
    Action: Optional[Sequence["_Action"]]
    Trigger: Optional[Sequence["_Trigger"]]
    SubjectAlternativeNames: Optional[Sequence["_SubjectAlternativeNames"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateData=json_data.get("CertificateData"),
            KeyVaultId=json_data.get("KeyVaultId"),
            Name=json_data.get("Name"),
            SecretId=json_data.get("SecretId"),
            Tags=json_data.get("Tags"),
            Thumbprint=json_data.get("Thumbprint"),
            Version=json_data.get("Version"),
            Certificate=json_data.get("Certificate"),
            CertificatePolicy=json_data.get("CertificatePolicy"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            IssuerParameters=json_data.get("IssuerParameters"),
            KeyProperties=json_data.get("KeyProperties"),
            LifetimeAction=json_data.get("LifetimeAction"),
            SecretProperties=json_data.get("SecretProperties"),
            X509CertificateProperties=json_data.get("X509CertificateProperties"),
            Action=json_data.get("Action"),
            Trigger=json_data.get("Trigger"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
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
class Certificate:
    Contents: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificate"]:
        if not json_data:
            return None
        return cls(
            Contents=json_data.get("Contents"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificate = Certificate


@dataclass
class CertificatePolicy:
    IssuerParameters: Optional[Sequence["_IssuerParameters"]]
    KeyProperties: Optional[Sequence["_KeyProperties"]]
    LifetimeAction: Optional[Sequence["_LifetimeAction"]]
    SecretProperties: Optional[Sequence["_SecretProperties"]]
    X509CertificateProperties: Optional[Sequence["_X509CertificateProperties"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificatePolicy"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificatePolicy"]:
        if not json_data:
            return None
        return cls(
            IssuerParameters=json_data.get("IssuerParameters"),
            KeyProperties=json_data.get("KeyProperties"),
            LifetimeAction=json_data.get("LifetimeAction"),
            SecretProperties=json_data.get("SecretProperties"),
            X509CertificateProperties=json_data.get("X509CertificateProperties"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificatePolicy = CertificatePolicy


@dataclass
class IssuerParameters:
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerParameters"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerParameters"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuerParameters = IssuerParameters


@dataclass
class KeyProperties:
    Exportable: Optional[bool]
    KeySize: Optional[float]
    KeyType: Optional[str]
    ReuseKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyProperties"]:
        if not json_data:
            return None
        return cls(
            Exportable=json_data.get("Exportable"),
            KeySize=json_data.get("KeySize"),
            KeyType=json_data.get("KeyType"),
            ReuseKey=json_data.get("ReuseKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyProperties = KeyProperties


@dataclass
class LifetimeAction:
    Action: Optional[Sequence["_Action"]]
    Trigger: Optional[Sequence["_Trigger"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifetimeAction"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifetimeAction"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Trigger=json_data.get("Trigger"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifetimeAction = LifetimeAction


@dataclass
class Action:
    ActionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Action"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Action"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Action = Action


@dataclass
class Trigger:
    DaysBeforeExpiry: Optional[float]
    LifetimePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Trigger"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Trigger"]:
        if not json_data:
            return None
        return cls(
            DaysBeforeExpiry=json_data.get("DaysBeforeExpiry"),
            LifetimePercentage=json_data.get("LifetimePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Trigger = Trigger


@dataclass
class SecretProperties:
    ContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretProperties"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretProperties = SecretProperties


@dataclass
class X509CertificateProperties:
    ExtendedKeyUsage: Optional[Sequence[str]]
    KeyUsage: Optional[Sequence[str]]
    Subject: Optional[str]
    ValidityInMonths: Optional[float]
    SubjectAlternativeNames: Optional[Sequence["_SubjectAlternativeNames"]]

    @classmethod
    def _deserialize(
        cls: Type["_X509CertificateProperties"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_X509CertificateProperties"]:
        if not json_data:
            return None
        return cls(
            ExtendedKeyUsage=json_data.get("ExtendedKeyUsage"),
            KeyUsage=json_data.get("KeyUsage"),
            Subject=json_data.get("Subject"),
            ValidityInMonths=json_data.get("ValidityInMonths"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
        )


# work around possible type aliasing issues when variable has same name as a model
_X509CertificateProperties = X509CertificateProperties


@dataclass
class SubjectAlternativeNames:
    DnsNames: Optional[Sequence[str]]
    Emails: Optional[Sequence[str]]
    Upns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAlternativeNames"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAlternativeNames"]:
        if not json_data:
            return None
        return cls(
            DnsNames=json_data.get("DnsNames"),
            Emails=json_data.get("Emails"),
            Upns=json_data.get("Upns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAlternativeNames = SubjectAlternativeNames


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


