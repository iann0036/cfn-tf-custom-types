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
    FtpIncomingPort: Optional[str]
    FtpOverHttp: Optional[str]
    HttpIncomingPort: Optional[str]
    HttpsIncomingPort: Optional[str]
    HttpsReplacementMessage: Optional[str]
    Id: Optional[str]
    IncomingIp: Optional[str]
    IncomingIp6: Optional[str]
    Ipv6Status: Optional[str]
    MessageUponServerError: Optional[str]
    OutgoingIp: Optional[str]
    OutgoingIp6: Optional[str]
    PacFileData: Optional[str]
    PacFileName: Optional[str]
    PacFileServerPort: Optional[str]
    PacFileServerStatus: Optional[str]
    PacFileUrl: Optional[str]
    PrefDnsResult: Optional[str]
    Realm: Optional[str]
    SecDefaultAction: Optional[str]
    Socks: Optional[str]
    SocksIncomingPort: Optional[str]
    SslAlgorithm: Optional[str]
    Status: Optional[str]
    StrictGuest: Optional[str]
    TraceAuthNoRsp: Optional[str]
    UnknownHttpVersion: Optional[str]
    Vdomparam: Optional[str]
    PacPolicy: Optional[Sequence["_PacPolicyDefinition"]]

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
            FtpIncomingPort=json_data.get("FtpIncomingPort"),
            FtpOverHttp=json_data.get("FtpOverHttp"),
            HttpIncomingPort=json_data.get("HttpIncomingPort"),
            HttpsIncomingPort=json_data.get("HttpsIncomingPort"),
            HttpsReplacementMessage=json_data.get("HttpsReplacementMessage"),
            Id=json_data.get("Id"),
            IncomingIp=json_data.get("IncomingIp"),
            IncomingIp6=json_data.get("IncomingIp6"),
            Ipv6Status=json_data.get("Ipv6Status"),
            MessageUponServerError=json_data.get("MessageUponServerError"),
            OutgoingIp=json_data.get("OutgoingIp"),
            OutgoingIp6=json_data.get("OutgoingIp6"),
            PacFileData=json_data.get("PacFileData"),
            PacFileName=json_data.get("PacFileName"),
            PacFileServerPort=json_data.get("PacFileServerPort"),
            PacFileServerStatus=json_data.get("PacFileServerStatus"),
            PacFileUrl=json_data.get("PacFileUrl"),
            PrefDnsResult=json_data.get("PrefDnsResult"),
            Realm=json_data.get("Realm"),
            SecDefaultAction=json_data.get("SecDefaultAction"),
            Socks=json_data.get("Socks"),
            SocksIncomingPort=json_data.get("SocksIncomingPort"),
            SslAlgorithm=json_data.get("SslAlgorithm"),
            Status=json_data.get("Status"),
            StrictGuest=json_data.get("StrictGuest"),
            TraceAuthNoRsp=json_data.get("TraceAuthNoRsp"),
            UnknownHttpVersion=json_data.get("UnknownHttpVersion"),
            Vdomparam=json_data.get("Vdomparam"),
            PacPolicy=deserialize_list(json_data.get("PacPolicy"), PacPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PacPolicyDefinition(BaseModel):
    Comments: Optional[str]
    PacFileData: Optional[str]
    PacFileName: Optional[str]
    Policyid: Optional[float]
    Status: Optional[str]
    Dstaddr: Optional[Sequence["_DstaddrDefinition"]]
    Srcaddr: Optional[Sequence["_SrcaddrDefinition"]]
    Srcaddr6: Optional[Sequence["_Srcaddr6Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PacPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PacPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Comments=json_data.get("Comments"),
            PacFileData=json_data.get("PacFileData"),
            PacFileName=json_data.get("PacFileName"),
            Policyid=json_data.get("Policyid"),
            Status=json_data.get("Status"),
            Dstaddr=deserialize_list(json_data.get("Dstaddr"), DstaddrDefinition),
            Srcaddr=deserialize_list(json_data.get("Srcaddr"), SrcaddrDefinition),
            Srcaddr6=deserialize_list(json_data.get("Srcaddr6"), Srcaddr6Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PacPolicyDefinition = PacPolicyDefinition


@dataclass
class DstaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstaddrDefinition = DstaddrDefinition


@dataclass
class SrcaddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcaddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcaddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcaddrDefinition = SrcaddrDefinition


@dataclass
class Srcaddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Srcaddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srcaddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srcaddr6Definition = Srcaddr6Definition


