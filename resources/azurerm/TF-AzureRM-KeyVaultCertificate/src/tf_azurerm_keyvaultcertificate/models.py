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
    CertificateAttribute: Optional[Sequence["_CertificateAttributeDefinition"]]
    CertificateData: Optional[str]
    CertificateDataBase64: Optional[str]
    Id: Optional[str]
    KeyVaultId: Optional[str]
    Name: Optional[str]
    SecretId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Thumbprint: Optional[str]
    Version: Optional[str]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    CertificatePolicy: Optional[Sequence["_CertificatePolicyDefinition"]]
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
            CertificateAttribute=deserialize_list(json_data.get("CertificateAttribute"), CertificateAttributeDefinition),
            CertificateData=json_data.get("CertificateData"),
            CertificateDataBase64=json_data.get("CertificateDataBase64"),
            Id=json_data.get("Id"),
            KeyVaultId=json_data.get("KeyVaultId"),
            Name=json_data.get("Name"),
            SecretId=json_data.get("SecretId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Thumbprint=json_data.get("Thumbprint"),
            Version=json_data.get("Version"),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            CertificatePolicy=deserialize_list(json_data.get("CertificatePolicy"), CertificatePolicyDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificateAttributeDefinition(BaseModel):
    Created: Optional[str]
    Enabled: Optional[bool]
    Expires: Optional[str]
    NotBefore: Optional[str]
    RecoveryLevel: Optional[str]
    Updated: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateAttributeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateAttributeDefinition"]:
        if not json_data:
            return None
        return cls(
            Created=json_data.get("Created"),
            Enabled=json_data.get("Enabled"),
            Expires=json_data.get("Expires"),
            NotBefore=json_data.get("NotBefore"),
            RecoveryLevel=json_data.get("RecoveryLevel"),
            Updated=json_data.get("Updated"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateAttributeDefinition = CertificateAttributeDefinition


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
class CertificateDefinition(BaseModel):
    Contents: Optional[str]
    Password: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            Contents=json_data.get("Contents"),
            Password=json_data.get("Password"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class CertificatePolicyDefinition(BaseModel):
    IssuerParameters: Optional[Sequence["_IssuerParametersDefinition"]]
    KeyProperties: Optional[Sequence["_KeyPropertiesDefinition"]]
    LifetimeAction: Optional[Sequence["_LifetimeActionDefinition"]]
    SecretProperties: Optional[Sequence["_SecretPropertiesDefinition"]]
    X509CertificateProperties: Optional[Sequence["_X509CertificatePropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificatePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificatePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            IssuerParameters=deserialize_list(json_data.get("IssuerParameters"), IssuerParametersDefinition),
            KeyProperties=deserialize_list(json_data.get("KeyProperties"), KeyPropertiesDefinition),
            LifetimeAction=deserialize_list(json_data.get("LifetimeAction"), LifetimeActionDefinition),
            SecretProperties=deserialize_list(json_data.get("SecretProperties"), SecretPropertiesDefinition),
            X509CertificateProperties=deserialize_list(json_data.get("X509CertificateProperties"), X509CertificatePropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificatePolicyDefinition = CertificatePolicyDefinition


@dataclass
class IssuerParametersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IssuerParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IssuerParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IssuerParametersDefinition = IssuerParametersDefinition


@dataclass
class KeyPropertiesDefinition(BaseModel):
    Curve: Optional[str]
    Exportable: Optional[bool]
    KeySize: Optional[float]
    KeyType: Optional[str]
    ReuseKey: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_KeyPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeyPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Curve=json_data.get("Curve"),
            Exportable=json_data.get("Exportable"),
            KeySize=json_data.get("KeySize"),
            KeyType=json_data.get("KeyType"),
            ReuseKey=json_data.get("ReuseKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeyPropertiesDefinition = KeyPropertiesDefinition


@dataclass
class LifetimeActionDefinition(BaseModel):
    Action: Optional[Sequence["_ActionDefinition"]]
    Trigger: Optional[Sequence["_TriggerDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LifetimeActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LifetimeActionDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=deserialize_list(json_data.get("Action"), ActionDefinition),
            Trigger=deserialize_list(json_data.get("Trigger"), TriggerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LifetimeActionDefinition = LifetimeActionDefinition


@dataclass
class ActionDefinition(BaseModel):
    ActionType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionType=json_data.get("ActionType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionDefinition = ActionDefinition


@dataclass
class TriggerDefinition(BaseModel):
    DaysBeforeExpiry: Optional[float]
    LifetimePercentage: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_TriggerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggerDefinition"]:
        if not json_data:
            return None
        return cls(
            DaysBeforeExpiry=json_data.get("DaysBeforeExpiry"),
            LifetimePercentage=json_data.get("LifetimePercentage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggerDefinition = TriggerDefinition


@dataclass
class SecretPropertiesDefinition(BaseModel):
    ContentType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecretPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecretPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ContentType=json_data.get("ContentType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecretPropertiesDefinition = SecretPropertiesDefinition


@dataclass
class X509CertificatePropertiesDefinition(BaseModel):
    ExtendedKeyUsage: Optional[Sequence[str]]
    KeyUsage: Optional[Sequence[str]]
    Subject: Optional[str]
    ValidityInMonths: Optional[float]
    SubjectAlternativeNames: Optional[Sequence["_SubjectAlternativeNamesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_X509CertificatePropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_X509CertificatePropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            ExtendedKeyUsage=json_data.get("ExtendedKeyUsage"),
            KeyUsage=json_data.get("KeyUsage"),
            Subject=json_data.get("Subject"),
            ValidityInMonths=json_data.get("ValidityInMonths"),
            SubjectAlternativeNames=deserialize_list(json_data.get("SubjectAlternativeNames"), SubjectAlternativeNamesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_X509CertificatePropertiesDefinition = X509CertificatePropertiesDefinition


@dataclass
class SubjectAlternativeNamesDefinition(BaseModel):
    DnsNames: Optional[Sequence[str]]
    Emails: Optional[Sequence[str]]
    Upns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAlternativeNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAlternativeNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            DnsNames=json_data.get("DnsNames"),
            Emails=json_data.get("Emails"),
            Upns=json_data.get("Upns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAlternativeNamesDefinition = SubjectAlternativeNamesDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


