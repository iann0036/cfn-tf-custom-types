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
    AppServiceCertificateNotRenewableReasons: Optional[Sequence[str]]
    AutoRenew: Optional[bool]
    Certificates: Optional[Sequence["_Certificates"]]
    Csr: Optional[str]
    DistinguishedName: Optional[str]
    DomainVerificationToken: Optional[str]
    ExpirationTime: Optional[str]
    IntermediateThumbprint: Optional[str]
    IsPrivateKeyExternal: Optional[bool]
    KeySize: Optional[float]
    Location: Optional[str]
    Name: Optional[str]
    ProductType: Optional[str]
    ResourceGroupName: Optional[str]
    RootThumbprint: Optional[str]
    SignedCertificateThumbprint: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    ValidityInYears: Optional[float]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppServiceCertificateNotRenewableReasons=json_data.get("AppServiceCertificateNotRenewableReasons"),
            AutoRenew=json_data.get("AutoRenew"),
            Certificates=json_data.get("Certificates"),
            Csr=json_data.get("Csr"),
            DistinguishedName=json_data.get("DistinguishedName"),
            DomainVerificationToken=json_data.get("DomainVerificationToken"),
            ExpirationTime=json_data.get("ExpirationTime"),
            IntermediateThumbprint=json_data.get("IntermediateThumbprint"),
            IsPrivateKeyExternal=json_data.get("IsPrivateKeyExternal"),
            KeySize=json_data.get("KeySize"),
            Location=json_data.get("Location"),
            Name=json_data.get("Name"),
            ProductType=json_data.get("ProductType"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            RootThumbprint=json_data.get("RootThumbprint"),
            SignedCertificateThumbprint=json_data.get("SignedCertificateThumbprint"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            ValidityInYears=json_data.get("ValidityInYears"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Certificates:
    CertificateName: Optional[str]
    KeyVaultId: Optional[str]
    KeyVaultSecretName: Optional[str]
    ProvisioningState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Certificates"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Certificates"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            KeyVaultSecretName=json_data.get("KeyVaultSecretName"),
            ProvisioningState=json_data.get("ProvisioningState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Certificates = Certificates


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


