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
    ClusterType: Optional[str]
    Cname: Optional[str]
    ConnectionTime: Optional[float]
    Domain: Optional[str]
    DomainName: Optional[str]
    Http2Port: Optional[Sequence[str]]
    HttpPort: Optional[Sequence[str]]
    HttpToUserIp: Optional[str]
    HttpsPort: Optional[Sequence[str]]
    HttpsRedirect: Optional[str]
    Id: Optional[str]
    InstanceId: Optional[str]
    IsAccessProduct: Optional[str]
    LoadBalancing: Optional[str]
    ReadTime: Optional[float]
    ResourceGroupId: Optional[str]
    SourceIps: Optional[Sequence[str]]
    WriteTime: Optional[float]
    LogHeaders: Optional[Sequence["_LogHeadersDefinition"]]

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
            ClusterType=json_data.get("ClusterType"),
            Cname=json_data.get("Cname"),
            ConnectionTime=json_data.get("ConnectionTime"),
            Domain=json_data.get("Domain"),
            DomainName=json_data.get("DomainName"),
            Http2Port=json_data.get("Http2Port"),
            HttpPort=json_data.get("HttpPort"),
            HttpToUserIp=json_data.get("HttpToUserIp"),
            HttpsPort=json_data.get("HttpsPort"),
            HttpsRedirect=json_data.get("HttpsRedirect"),
            Id=json_data.get("Id"),
            InstanceId=json_data.get("InstanceId"),
            IsAccessProduct=json_data.get("IsAccessProduct"),
            LoadBalancing=json_data.get("LoadBalancing"),
            ReadTime=json_data.get("ReadTime"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SourceIps=json_data.get("SourceIps"),
            WriteTime=json_data.get("WriteTime"),
            LogHeaders=deserialize_list(json_data.get("LogHeaders"), LogHeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LogHeadersDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LogHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LogHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LogHeadersDefinition = LogHeadersDefinition


