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
    BalancerId: Optional[str]
    Id: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TlsConfig: Optional[Sequence["_TlsConfigDefinition"]]

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
            BalancerId=json_data.get("BalancerId"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TlsConfig=deserialize_list(json_data.get("TlsConfig"), TlsConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TlsConfigDefinition(BaseModel):
    CertificateIds: Optional[Sequence[str]]
    CipherSuites: Optional[Sequence[str]]
    MaxVersion: Optional[str]
    MinVersion: Optional[str]
    PreferServerCipherSuites: Optional[bool]
    SessionTicketsDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateIds=json_data.get("CertificateIds"),
            CipherSuites=json_data.get("CipherSuites"),
            MaxVersion=json_data.get("MaxVersion"),
            MinVersion=json_data.get("MinVersion"),
            PreferServerCipherSuites=json_data.get("PreferServerCipherSuites"),
            SessionTicketsDisabled=json_data.get("SessionTicketsDisabled"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsConfigDefinition = TlsConfigDefinition


