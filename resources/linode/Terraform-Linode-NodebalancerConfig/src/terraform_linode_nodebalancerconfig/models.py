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
    NodeStatus: Optional[Sequence["_NodeStatus"]]
    NodebalancerId: Optional[float]
    Port: Optional[float]
    Protocol: Optional[str]
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
            NodeStatus=json_data.get("NodeStatus"),
            NodebalancerId=json_data.get("NodebalancerId"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SslCert=json_data.get("SslCert"),
            SslCommonname=json_data.get("SslCommonname"),
            SslFingerprint=json_data.get("SslFingerprint"),
            SslKey=json_data.get("SslKey"),
            Stickiness=json_data.get("Stickiness"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeStatus:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeStatus"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeStatus"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeStatus = NodeStatus


