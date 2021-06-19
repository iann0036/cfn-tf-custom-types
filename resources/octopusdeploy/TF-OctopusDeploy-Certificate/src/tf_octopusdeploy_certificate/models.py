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
    Archived: Optional[str]
    CertificateData: Optional[str]
    CertificateDataFormat: Optional[str]
    Environments: Optional[Sequence[str]]
    HasPrivateKey: Optional[bool]
    Id: Optional[str]
    IsExpired: Optional[bool]
    IssuerCommonName: Optional[str]
    IssuerDistinguishedName: Optional[str]
    IssuerOrganization: Optional[str]
    Name: Optional[str]
    NotAfter: Optional[str]
    NotBefore: Optional[str]
    Notes: Optional[str]
    Password: Optional[str]
    ReplacedBy: Optional[str]
    SelfSigned: Optional[bool]
    SerialNumber: Optional[str]
    SignatureAlgorithmName: Optional[str]
    SubjectAlternativeNames: Optional[Sequence[str]]
    SubjectCommonName: Optional[str]
    SubjectDistinguishedName: Optional[str]
    SubjectOrganization: Optional[str]
    TenantTags: Optional[Sequence[str]]
    TenantedDeploymentParticipation: Optional[str]
    Tenants: Optional[Sequence[str]]
    Thumbprint: Optional[str]
    Version: Optional[float]

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
            Archived=json_data.get("Archived"),
            CertificateData=json_data.get("CertificateData"),
            CertificateDataFormat=json_data.get("CertificateDataFormat"),
            Environments=json_data.get("Environments"),
            HasPrivateKey=json_data.get("HasPrivateKey"),
            Id=json_data.get("Id"),
            IsExpired=json_data.get("IsExpired"),
            IssuerCommonName=json_data.get("IssuerCommonName"),
            IssuerDistinguishedName=json_data.get("IssuerDistinguishedName"),
            IssuerOrganization=json_data.get("IssuerOrganization"),
            Name=json_data.get("Name"),
            NotAfter=json_data.get("NotAfter"),
            NotBefore=json_data.get("NotBefore"),
            Notes=json_data.get("Notes"),
            Password=json_data.get("Password"),
            ReplacedBy=json_data.get("ReplacedBy"),
            SelfSigned=json_data.get("SelfSigned"),
            SerialNumber=json_data.get("SerialNumber"),
            SignatureAlgorithmName=json_data.get("SignatureAlgorithmName"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            SubjectCommonName=json_data.get("SubjectCommonName"),
            SubjectDistinguishedName=json_data.get("SubjectDistinguishedName"),
            SubjectOrganization=json_data.get("SubjectOrganization"),
            TenantTags=json_data.get("TenantTags"),
            TenantedDeploymentParticipation=json_data.get("TenantedDeploymentParticipation"),
            Tenants=json_data.get("Tenants"),
            Thumbprint=json_data.get("Thumbprint"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


