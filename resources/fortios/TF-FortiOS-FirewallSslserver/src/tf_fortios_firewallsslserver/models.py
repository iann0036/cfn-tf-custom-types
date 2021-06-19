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
    AddHeaderXForwardedProto: Optional[str]
    Id: Optional[str]
    Ip: Optional[str]
    MappedPort: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    SslAlgorithm: Optional[str]
    SslCert: Optional[str]
    SslClientRenegotiation: Optional[str]
    SslDhBits: Optional[str]
    SslMaxVersion: Optional[str]
    SslMinVersion: Optional[str]
    SslMode: Optional[str]
    SslSendEmptyFrags: Optional[str]
    UrlRewrite: Optional[str]
    Vdomparam: Optional[str]

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
            AddHeaderXForwardedProto=json_data.get("AddHeaderXForwardedProto"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            MappedPort=json_data.get("MappedPort"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            SslAlgorithm=json_data.get("SslAlgorithm"),
            SslCert=json_data.get("SslCert"),
            SslClientRenegotiation=json_data.get("SslClientRenegotiation"),
            SslDhBits=json_data.get("SslDhBits"),
            SslMaxVersion=json_data.get("SslMaxVersion"),
            SslMinVersion=json_data.get("SslMinVersion"),
            SslMode=json_data.get("SslMode"),
            SslSendEmptyFrags=json_data.get("SslSendEmptyFrags"),
            UrlRewrite=json_data.get("UrlRewrite"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


