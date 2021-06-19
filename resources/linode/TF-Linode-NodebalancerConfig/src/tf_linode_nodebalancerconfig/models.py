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
    Algorithm: Optional[str]
    Check: Optional[str]
    CheckAttempts: Optional[float]
    CheckBody: Optional[str]
    CheckInterval: Optional[float]
    CheckPassive: Optional[bool]
    CheckPath: Optional[str]
    CheckTimeout: Optional[float]
    CipherSuite: Optional[str]
    Id: Optional[str]
    NodeStatus: Optional[Sequence["_NodeStatusDefinition"]]
    NodebalancerId: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
    ProxyProtocol: Optional[str]
    SslCert: Optional[str]
    SslCommonname: Optional[str]
    SslFingerprint: Optional[str]
    SslKey: Optional[str]
    Stickiness: Optional[str]

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
            Algorithm=json_data.get("Algorithm"),
            Check=json_data.get("Check"),
            CheckAttempts=json_data.get("CheckAttempts"),
            CheckBody=json_data.get("CheckBody"),
            CheckInterval=json_data.get("CheckInterval"),
            CheckPassive=json_data.get("CheckPassive"),
            CheckPath=json_data.get("CheckPath"),
            CheckTimeout=json_data.get("CheckTimeout"),
            CipherSuite=json_data.get("CipherSuite"),
            Id=json_data.get("Id"),
            NodeStatus=deserialize_list(json_data.get("NodeStatus"), NodeStatusDefinition),
            NodebalancerId=json_data.get("NodebalancerId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            SslCert=json_data.get("SslCert"),
            SslCommonname=json_data.get("SslCommonname"),
            SslFingerprint=json_data.get("SslFingerprint"),
            SslKey=json_data.get("SslKey"),
            Stickiness=json_data.get("Stickiness"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeStatusDefinition(BaseModel):
    Down: Optional[float]
    Up: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodeStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Down=json_data.get("Down"),
            Up=json_data.get("Up"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeStatusDefinition = NodeStatusDefinition


