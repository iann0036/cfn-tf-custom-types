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
    CommonName: Optional[str]
    Fingerprint: Optional[str]
    LbId: Optional[str]
    Name: Optional[str]
    NotValidAfter: Optional[str]
    NotValidBefore: Optional[str]
    Status: Optional[str]
    SubjectAlternativeName: Optional[str]
    CustomCertificate: Optional[Sequence["_CustomCertificate"]]
    Letsencrypt: Optional[Sequence["_Letsencrypt"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CommonName=json_data.get("CommonName"),
            Fingerprint=json_data.get("Fingerprint"),
            LbId=json_data.get("LbId"),
            Name=json_data.get("Name"),
            NotValidAfter=json_data.get("NotValidAfter"),
            NotValidBefore=json_data.get("NotValidBefore"),
            Status=json_data.get("Status"),
            SubjectAlternativeName=json_data.get("SubjectAlternativeName"),
            CustomCertificate=json_data.get("CustomCertificate"),
            Letsencrypt=json_data.get("Letsencrypt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomCertificate:
    CertificateChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCertificate"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCertificate"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCertificate = CustomCertificate


@dataclass
class Letsencrypt:
    CommonName: Optional[str]
    SubjectAlternativeName: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Letsencrypt"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Letsencrypt"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            SubjectAlternativeName=json_data.get("SubjectAlternativeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Letsencrypt = Letsencrypt


