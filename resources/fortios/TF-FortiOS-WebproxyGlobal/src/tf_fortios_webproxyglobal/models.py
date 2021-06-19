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
    DynamicSortSubtable: Optional[str]
    FastPolicyMatch: Optional[str]
    ForwardProxyAuth: Optional[str]
    ForwardServerAffinityTimeout: Optional[float]
    Id: Optional[str]
    LearnClientIp: Optional[str]
    LearnClientIpFromHeader: Optional[str]
    MaxMessageLength: Optional[float]
    MaxRequestLength: Optional[float]
    MaxWafBodyCacheLength: Optional[float]
    ProxyFqdn: Optional[str]
    SslCaCert: Optional[str]
    SslCert: Optional[str]
    StrictWebCheck: Optional[str]
    TunnelNonHttp: Optional[str]
    UnknownHttpVersion: Optional[str]
    Vdomparam: Optional[str]
    WebproxyProfile: Optional[str]
    LearnClientIpSrcaddr: Optional[Sequence["_LearnClientIpSrcaddrDefinition"]]
    LearnClientIpSrcaddr6: Optional[Sequence["_LearnClientIpSrcaddr6Definition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            FastPolicyMatch=json_data.get("FastPolicyMatch"),
            ForwardProxyAuth=json_data.get("ForwardProxyAuth"),
            ForwardServerAffinityTimeout=json_data.get("ForwardServerAffinityTimeout"),
            Id=json_data.get("Id"),
            LearnClientIp=json_data.get("LearnClientIp"),
            LearnClientIpFromHeader=json_data.get("LearnClientIpFromHeader"),
            MaxMessageLength=json_data.get("MaxMessageLength"),
            MaxRequestLength=json_data.get("MaxRequestLength"),
            MaxWafBodyCacheLength=json_data.get("MaxWafBodyCacheLength"),
            ProxyFqdn=json_data.get("ProxyFqdn"),
            SslCaCert=json_data.get("SslCaCert"),
            SslCert=json_data.get("SslCert"),
            StrictWebCheck=json_data.get("StrictWebCheck"),
            TunnelNonHttp=json_data.get("TunnelNonHttp"),
            UnknownHttpVersion=json_data.get("UnknownHttpVersion"),
            Vdomparam=json_data.get("Vdomparam"),
            WebproxyProfile=json_data.get("WebproxyProfile"),
            LearnClientIpSrcaddr=deserialize_list(json_data.get("LearnClientIpSrcaddr"), LearnClientIpSrcaddrDefinition),
            LearnClientIpSrcaddr6=deserialize_list(json_data.get("LearnClientIpSrcaddr6"), LearnClientIpSrcaddr6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LearnClientIpSrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LearnClientIpSrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LearnClientIpSrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LearnClientIpSrcaddrDefinition = LearnClientIpSrcaddrDefinition


@dataclass
class LearnClientIpSrcaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LearnClientIpSrcaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LearnClientIpSrcaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LearnClientIpSrcaddr6Definition = LearnClientIpSrcaddr6Definition


