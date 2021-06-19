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
    CertificateAuthorityArn: Optional[str]
    CertificateBody: Optional[str]
    CertificateChain: Optional[str]
    DomainName: Optional[str]
    DomainValidationOptions: Optional[Sequence["_DomainValidationOptionsDefinition"]]
    Id: Optional[str]
    PrivateKey: Optional[str]
    Status: Optional[str]
    SubjectAlternativeNames: Optional[Sequence[str]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    ValidationEmails: Optional[Sequence[str]]
    ValidationMethod: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]

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
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            CertificateBody=json_data.get("CertificateBody"),
            CertificateChain=json_data.get("CertificateChain"),
            DomainName=json_data.get("DomainName"),
            DomainValidationOptions=deserialize_list(json_data.get("DomainValidationOptions"), DomainValidationOptionsDefinition),
            Id=json_data.get("Id"),
            PrivateKey=json_data.get("PrivateKey"),
            Status=json_data.get("Status"),
            SubjectAlternativeNames=json_data.get("SubjectAlternativeNames"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            ValidationEmails=json_data.get("ValidationEmails"),
            ValidationMethod=json_data.get("ValidationMethod"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DomainValidationOptionsDefinition(BaseModel):
    DomainName: Optional[str]
    ResourceRecordName: Optional[str]
    ResourceRecordType: Optional[str]
    ResourceRecordValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DomainValidationOptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainValidationOptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainName=json_data.get("DomainName"),
            ResourceRecordName=json_data.get("ResourceRecordName"),
            ResourceRecordType=json_data.get("ResourceRecordType"),
            ResourceRecordValue=json_data.get("ResourceRecordValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainValidationOptionsDefinition = DomainValidationOptionsDefinition


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
class OptionsDefinition(BaseModel):
    CertificateTransparencyLoggingPreference: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateTransparencyLoggingPreference=json_data.get("CertificateTransparencyLoggingPreference"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


