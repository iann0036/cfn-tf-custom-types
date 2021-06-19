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
    Certificate: Optional[str]
    CertificateAuthorityArn: Optional[str]
    CertificateChain: Optional[str]
    CertificateSigningRequest: Optional[str]
    Id: Optional[str]
    SigningAlgorithm: Optional[str]
    TemplateArn: Optional[str]
    Validity: Optional[Sequence["_ValidityDefinition"]]

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
            Certificate=json_data.get("Certificate"),
            CertificateAuthorityArn=json_data.get("CertificateAuthorityArn"),
            CertificateChain=json_data.get("CertificateChain"),
            CertificateSigningRequest=json_data.get("CertificateSigningRequest"),
            Id=json_data.get("Id"),
            SigningAlgorithm=json_data.get("SigningAlgorithm"),
            TemplateArn=json_data.get("TemplateArn"),
            Validity=deserialize_list(json_data.get("Validity"), ValidityDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ValidityDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ValidityDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidityDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidityDefinition = ValidityDefinition


