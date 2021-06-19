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
    DnsOverTls: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    InterfaceSelectMethod: Optional[str]
    Ip6Primary: Optional[str]
    Ip6Secondary: Optional[str]
    Primary: Optional[str]
    Secondary: Optional[str]
    SourceIp: Optional[str]
    SslCertificate: Optional[str]
    VdomDns: Optional[str]
    Vdomparam: Optional[str]
    ServerHostname: Optional[Sequence["_ServerHostnameDefinition"]]

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
            DnsOverTls=json_data.get("DnsOverTls"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            InterfaceSelectMethod=json_data.get("InterfaceSelectMethod"),
            Ip6Primary=json_data.get("Ip6Primary"),
            Ip6Secondary=json_data.get("Ip6Secondary"),
            Primary=json_data.get("Primary"),
            Secondary=json_data.get("Secondary"),
            SourceIp=json_data.get("SourceIp"),
            SslCertificate=json_data.get("SslCertificate"),
            VdomDns=json_data.get("VdomDns"),
            Vdomparam=json_data.get("Vdomparam"),
            ServerHostname=deserialize_list(json_data.get("ServerHostname"), ServerHostnameDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServerHostnameDefinition(BaseModel):
    Hostname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServerHostnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServerHostnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Hostname=json_data.get("Hostname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServerHostnameDefinition = ServerHostnameDefinition


