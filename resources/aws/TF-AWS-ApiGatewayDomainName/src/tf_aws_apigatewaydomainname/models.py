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
    Id: Optional[str]
    RegionalCertificateArn: Optional[str]
    RegionalCertificateName: Optional[str]
    RegionalDomainName: Optional[str]
    RegionalZoneId: Optional[str]
    SecurityPolicy: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    EndpointConfiguration: Optional[Sequence["_EndpointConfigurationDefinition"]]
    MutualTlsAuthentication: Optional[Sequence["_MutualTlsAuthenticationDefinition"]]

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
            Id=json_data.get("Id"),
            RegionalCertificateArn=json_data.get("RegionalCertificateArn"),
            RegionalCertificateName=json_data.get("RegionalCertificateName"),
            RegionalDomainName=json_data.get("RegionalDomainName"),
            RegionalZoneId=json_data.get("RegionalZoneId"),
            SecurityPolicy=json_data.get("SecurityPolicy"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            EndpointConfiguration=deserialize_list(json_data.get("EndpointConfiguration"), EndpointConfigurationDefinition),
            MutualTlsAuthentication=deserialize_list(json_data.get("MutualTlsAuthentication"), MutualTlsAuthenticationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class EndpointConfigurationDefinition(BaseModel):
    Types: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_EndpointConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EndpointConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Types=json_data.get("Types"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EndpointConfigurationDefinition = EndpointConfigurationDefinition


@dataclass
class MutualTlsAuthenticationDefinition(BaseModel):
    TruststoreUri: Optional[str]
    TruststoreVersion: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MutualTlsAuthenticationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MutualTlsAuthenticationDefinition"]:
        if not json_data:
            return None
        return cls(
            TruststoreUri=json_data.get("TruststoreUri"),
            TruststoreVersion=json_data.get("TruststoreVersion"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MutualTlsAuthenticationDefinition = MutualTlsAuthenticationDefinition


