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
    Action: Optional[str]
    FailureAction: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServiceGroup: Optional[str]
    SharedPartitionPersistSourceIpTemplate: Optional[float]
    SharedPartitionTcpProxyTemplate: Optional[float]
    SourceIp: Optional[str]
    TcpProxy: Optional[str]
    TemplatePersistSourceIpShared: Optional[str]
    TemplateTcpProxyShared: Optional[str]
    Timeout: Optional[float]
    Type: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    BypassIpCfg: Optional[Sequence["_BypassIpCfgDefinition"]]
    RequestHeaderForwardList: Optional[Sequence["_RequestHeaderForwardListDefinition"]]

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
            Action=json_data.get("Action"),
            FailureAction=json_data.get("FailureAction"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServiceGroup=json_data.get("ServiceGroup"),
            SharedPartitionPersistSourceIpTemplate=json_data.get("SharedPartitionPersistSourceIpTemplate"),
            SharedPartitionTcpProxyTemplate=json_data.get("SharedPartitionTcpProxyTemplate"),
            SourceIp=json_data.get("SourceIp"),
            TcpProxy=json_data.get("TcpProxy"),
            TemplatePersistSourceIpShared=json_data.get("TemplatePersistSourceIpShared"),
            TemplateTcpProxyShared=json_data.get("TemplateTcpProxyShared"),
            Timeout=json_data.get("Timeout"),
            Type=json_data.get("Type"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            BypassIpCfg=deserialize_list(json_data.get("BypassIpCfg"), BypassIpCfgDefinition),
            RequestHeaderForwardList=deserialize_list(json_data.get("RequestHeaderForwardList"), RequestHeaderForwardListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BypassIpCfgDefinition(BaseModel):
    BypassIp: Optional[str]
    Mask: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BypassIpCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BypassIpCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            BypassIp=json_data.get("BypassIp"),
            Mask=json_data.get("Mask"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BypassIpCfgDefinition = BypassIpCfgDefinition


@dataclass
class RequestHeaderForwardListDefinition(BaseModel):
    RequestHeaderForward: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequestHeaderForwardListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequestHeaderForwardListDefinition"]:
        if not json_data:
            return None
        return cls(
            RequestHeaderForward=json_data.get("RequestHeaderForward"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequestHeaderForwardListDefinition = RequestHeaderForwardListDefinition


