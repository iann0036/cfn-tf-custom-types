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
    AuthLevel: Optional[str]
    AuthType: Optional[str]
    AutoDiscoverKdc: Optional[str]
    ConnectProtocol: Optional[str]
    DomainName: Optional[str]
    DynamicSortSubtable: Optional[str]
    HttpAuthType: Optional[str]
    Id: Optional[str]
    Ip: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    ServerName: Optional[str]
    SslMinProtoVersion: Optional[str]
    Username: Optional[str]
    Vdomparam: Optional[str]
    KdcIp: Optional[Sequence["_KdcIpDefinition"]]

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
            AuthLevel=json_data.get("AuthLevel"),
            AuthType=json_data.get("AuthType"),
            AutoDiscoverKdc=json_data.get("AutoDiscoverKdc"),
            ConnectProtocol=json_data.get("ConnectProtocol"),
            DomainName=json_data.get("DomainName"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            HttpAuthType=json_data.get("HttpAuthType"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            ServerName=json_data.get("ServerName"),
            SslMinProtoVersion=json_data.get("SslMinProtoVersion"),
            Username=json_data.get("Username"),
            Vdomparam=json_data.get("Vdomparam"),
            KdcIp=deserialize_list(json_data.get("KdcIp"), KdcIpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KdcIpDefinition(BaseModel):
    Ipv4: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KdcIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KdcIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Ipv4=json_data.get("Ipv4"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KdcIpDefinition = KdcIpDefinition


