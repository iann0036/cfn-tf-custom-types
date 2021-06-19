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
    AcceptableConnections: Optional[str]
    Collaboration: Optional[str]
    DeviceId: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    PreferScenario: Optional[str]
    Vdomparam: Optional[str]
    DstPeer: Optional[Sequence["_DstPeerDefinition"]]
    SrcPeer: Optional[Sequence["_SrcPeerDefinition"]]

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
            AcceptableConnections=json_data.get("AcceptableConnections"),
            Collaboration=json_data.get("Collaboration"),
            DeviceId=json_data.get("DeviceId"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            PreferScenario=json_data.get("PreferScenario"),
            Vdomparam=json_data.get("Vdomparam"),
            DstPeer=deserialize_list(json_data.get("DstPeer"), DstPeerDefinition),
            SrcPeer=deserialize_list(json_data.get("SrcPeer"), SrcPeerDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstPeerDefinition(BaseModel):
    AuthType: Optional[float]
    DeviceId: Optional[str]
    EncodeType: Optional[float]
    Ip: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DstPeerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstPeerDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            DeviceId=json_data.get("DeviceId"),
            EncodeType=json_data.get("EncodeType"),
            Ip=json_data.get("Ip"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstPeerDefinition = DstPeerDefinition


@dataclass
class SrcPeerDefinition(BaseModel):
    AuthType: Optional[float]
    DeviceId: Optional[str]
    EncodeType: Optional[float]
    Ip: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SrcPeerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcPeerDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthType=json_data.get("AuthType"),
            DeviceId=json_data.get("DeviceId"),
            EncodeType=json_data.get("EncodeType"),
            Ip=json_data.get("Ip"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcPeerDefinition = SrcPeerDefinition


