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
    Arn: Optional[str]
    CertificateAuthorityArn: Optional[str]
    CertificateBody: Optional[str]
    CertificateChain: Optional[str]
    DomainName: Optional[str]
    DomainValidationOptions: Optional[Sequence["_DomainValidationOptions"]]
    Id: Optional[str]
    PrivateKey: Optional[str]
    SubjectAlternativeNames: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    ValidationEmails: Optional[Sequence[str]]
    ValidationMethod: Optional[str]
    Options: Optional[Sequence["_Options"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            CertificateBody=json_data.get("CertificateBody"),
            CertificateChain=json_data.get("CertificateChain"),
            DomainName=json_data.get("DomainName"),
            DomainValidationOptions=json_data.get("DomainValidationOptions"),
            Id=json_data.get("Id"),
            PrivateKey=json_data.get("PrivateKey"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            Tags=json_data.get("Tags"),
            ValidationEmails=json_data.get("ValidationEmails"),
            ValidationMethod=json_data.get("ValidationMethod"),
            Options=json_data.get("Options"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DomainValidationOptions:
    DomainName: Optional[str]
    ResourceRecordName: Optional[str]
    ResourceRecordType: Optional[str]
    ResourceRecordValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainValidationOptions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainValidationOptions"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            ResourceRecordName=json_data.get("ResourceRecordName"),
            ResourceRecordType=json_data.get("ResourceRecordType"),
            ResourceRecordValue=json_data.get("ResourceRecordValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainValidationOptions = DomainValidationOptions


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Options:
    CertificateTransparencyLoggingPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            CertificateTransparencyLoggingPreference=json_data.get("CertificateTransparencyLoggingPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


