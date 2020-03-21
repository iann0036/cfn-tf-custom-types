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
    BalancerId: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    TlsConfig: Optional[Sequence["_TlsConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BalancerId=json_data.get("BalancerId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            Tags=json_data.get("Tags"),
            TlsConfig=json_data.get("TlsConfig"),
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
class TlsConfig:
    CertificateIds: Optional[Sequence[str]]
    CipherSuites: Optional[Sequence[str]]
    MaxVersion: Optional[str]
    MinVersion: Optional[str]
    PreferServerCipherSuites: Optional[bool]
    SessionTicketsDisabled: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_TlsConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsConfig"]:
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
_TlsConfig = TlsConfig


