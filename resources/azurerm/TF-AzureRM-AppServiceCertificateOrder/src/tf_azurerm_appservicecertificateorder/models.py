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
    AppServiceCertificateNotRenewableReasons: Optional[Sequence[str]]
    AutoRenew: Optional[bool]
    Certificates: Optional[Sequence["_CertificatesDefinition"]]
    Csr: Optional[str]
    DistinguishedName: Optional[str]
    DomainVerificationToken: Optional[str]
    ExpirationTime: Optional[str]
    Id: Optional[str]
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
    Tags: Optional[Sequence["_TagsDefinition"]]
    ValidityInYears: Optional[float]
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
            AppServiceCertificateNotRenewableReasons=json_data.get("AppServiceCertificateNotRenewableReasons"),
            AutoRenew=json_data.get("AutoRenew"),
            Certificates=deserialize_list(json_data.get("Certificates"), CertificatesDefinition),
            Csr=json_data.get("Csr"),
            DistinguishedName=json_data.get("DistinguishedName"),
            DomainVerificationToken=json_data.get("DomainVerificationToken"),
            ExpirationTime=json_data.get("ExpirationTime"),
            Id=json_data.get("Id"),
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
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            ValidityInYears=json_data.get("ValidityInYears"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificatesDefinition(BaseModel):
    CertificateName: Optional[str]
    KeyVaultId: Optional[str]
    KeyVaultSecretName: Optional[str]
    ProvisioningState: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            KeyVaultId=json_data.get("KeyVaultId"),
            KeyVaultSecretName=json_data.get("KeyVaultSecretName"),
            ProvisioningState=json_data.get("ProvisioningState"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificatesDefinition = CertificatesDefinition


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


