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
    CertificateArn: Optional[str]
    CertificateBody: Optional[str]
    CertificateChain: Optional[str]
    CertificateName: Optional[str]
    CertificatePrivateKey: Optional[str]
    CertificateUploadDate: Optional[str]
    CloudfrontDomainName: Optional[str]
    CloudfrontZoneId: Optional[str]
    DomainName: Optional[str]
    RegionalCertificateArn: Optional[str]
    RegionalCertificateName: Optional[str]
    RegionalDomainName: Optional[str]
    RegionalZoneId: Optional[str]
    SecurityPolicy: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    EndpointConfiguration: Optional[Sequence["_EndpointConfiguration"]]

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
            CertificateArn=json_data.get("CertificateArn"),
            CertificateBody=json_data.get("CertificateBody"),
            CertificateChain=json_data.get("CertificateChain"),
            CertificateName=json_data.get("CertificateName"),
            CertificatePrivateKey=json_data.get("CertificatePrivateKey"),
            CertificateUploadDate=json_data.get("CertificateUploadDate"),
            CloudfrontDomainName=json_data.get("CloudfrontDomainName"),
            CloudfrontZoneId=json_data.get("CloudfrontZoneId"),
            DomainName=json_data.get("DomainName"),
            RegionalCertificateArn=json_data.get("RegionalCertificateArn"),
            RegionalCertificateName=json_data.get("RegionalCertificateName"),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            RegionalZoneId=json_data.get("RegionalZoneId"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            Tags=json_data.get("Tags"),
            EndpointConfiguration=json_data.get("EndpointConfiguration"),
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
class EndpointConfiguration:
    Types: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfiguration"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfiguration = EndpointConfiguration


