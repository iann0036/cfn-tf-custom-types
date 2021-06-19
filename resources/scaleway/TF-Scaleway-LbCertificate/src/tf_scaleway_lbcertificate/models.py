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
    CommonName: Optional[str]
    Fingerprint: Optional[str]
    Id: Optional[str]
    LbId: Optional[str]
    Name: Optional[str]
    NotValidAfter: Optional[str]
    NotValidBefore: Optional[str]
    Status: Optional[str]
    SubjectAlternativeName: Optional[Sequence[str]]
    CustomCertificate: Optional[Sequence["_CustomCertificateDefinition"]]
    Letsencrypt: Optional[Sequence["_LetsencryptDefinition"]]
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
            CommonName=json_data.get("CommonName"),
            Fingerprint=json_data.get("Fingerprint"),
            Id=json_data.get("Id"),
            LbId=json_data.get("LbId"),
            Name=json_data.get("Name"),
            NotValidAfter=json_data.get("NotValidAfter"),
            NotValidBefore=json_data.get("NotValidBefore"),
            Status=json_data.get("Status"),
            SubjectAlternativeName=json_data.get("SubjectAlternativeName"),
            CustomCertificate=deserialize_list(json_data.get("CustomCertificate"), CustomCertificateDefinition),
            Letsencrypt=deserialize_list(json_data.get("Letsencrypt"), LetsencryptDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomCertificateDefinition(BaseModel):
    CertificateChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomCertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomCertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomCertificateDefinition = CustomCertificateDefinition


@dataclass
class LetsencryptDefinition(BaseModel):
    CommonName: Optional[str]
    SubjectAlternativeName: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_LetsencryptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LetsencryptDefinition"]:
        if not json_data:
            return None
        return cls(
            CommonName=json_data.get("CommonName"),
            SubjectAlternativeName=json_data.get("SubjectAlternativeName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LetsencryptDefinition = LetsencryptDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Default: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Default=json_data.get("Default"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


