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
    FastFailoverMax: Optional[float]
    FastFailoverWait: Optional[float]
    Id: Optional[str]
    InterControllerKey: Optional[str]
    InterControllerMode: Optional[str]
    InterControllerPri: Optional[str]
    Vdomparam: Optional[str]
    InterControllerPeer: Optional[Sequence["_InterControllerPeerDefinition"]]

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
            FastFailoverMax=json_data.get("FastFailoverMax"),
            FastFailoverWait=json_data.get("FastFailoverWait"),
            Id=json_data.get("Id"),
            InterControllerKey=json_data.get("InterControllerKey"),
            InterControllerMode=json_data.get("InterControllerMode"),
            InterControllerPri=json_data.get("InterControllerPri"),
            Vdomparam=json_data.get("Vdomparam"),
            InterControllerPeer=deserialize_list(json_data.get("InterControllerPeer"), InterControllerPeerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterControllerPeerDefinition(BaseModel):
    Id: Optional[float]
    PeerIp: Optional[str]
    PeerPort: Optional[float]
    PeerPriority: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InterControllerPeerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterControllerPeerDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            PeerIp=json_data.get("PeerIp"),
            PeerPort=json_data.get("PeerPort"),
            PeerPriority=json_data.get("PeerPriority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterControllerPeerDefinition = InterControllerPeerDefinition


