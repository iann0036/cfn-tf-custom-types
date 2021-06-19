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
    ChunkNetmask: Optional[str]
    EndAddress: Optional[str]
    Ethernet: Optional[float]
    Gateway: Optional[str]
    Id: Optional[str]
    IpRr: Optional[float]
    Netmask: Optional[str]
    PoolName: Optional[str]
    PortOverload: Optional[float]
    ScaleoutDeviceId: Optional[float]
    StartAddress: Optional[str]
    UseIfIp: Optional[float]
    Uuid: Optional[str]
    Vrid: Optional[float]

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
            ChunkNetmask=json_data.get("ChunkNetmask"),
            EndAddress=json_data.get("EndAddress"),
            Ethernet=json_data.get("Ethernet"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            IpRr=json_data.get("IpRr"),
            Netmask=json_data.get("Netmask"),
            PoolName=json_data.get("PoolName"),
            PortOverload=json_data.get("PortOverload"),
            ScaleoutDeviceId=json_data.get("ScaleoutDeviceId"),
            StartAddress=json_data.get("StartAddress"),
            UseIfIp=json_data.get("UseIfIp"),
            Uuid=json_data.get("Uuid"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


