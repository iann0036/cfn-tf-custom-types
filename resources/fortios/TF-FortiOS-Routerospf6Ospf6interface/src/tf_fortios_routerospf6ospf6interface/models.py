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
    AreaId: Optional[str]
    Authentication: Optional[str]
    Bfd: Optional[str]
    Cost: Optional[float]
    DeadInterval: Optional[float]
    DynamicSortSubtable: Optional[str]
    HelloInterval: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    IpsecAuthAlg: Optional[str]
    IpsecEncAlg: Optional[str]
    KeyRolloverInterval: Optional[float]
    Mtu: Optional[float]
    MtuIgnore: Optional[str]
    Name: Optional[str]
    NetworkType: Optional[str]
    Priority: Optional[float]
    RetransmitInterval: Optional[float]
    Status: Optional[str]
    TransmitDelay: Optional[float]
    Vdomparam: Optional[str]
    IpsecKeys: Optional[Sequence["_IpsecKeysDefinition"]]
    Neighbor: Optional[Sequence["_NeighborDefinition"]]

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
            AreaId=json_data.get("AreaId"),
            Authentication=json_data.get("Authentication"),
            Bfd=json_data.get("Bfd"),
            Cost=json_data.get("Cost"),
            DeadInterval=json_data.get("DeadInterval"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            HelloInterval=json_data.get("HelloInterval"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpsecAuthAlg=json_data.get("IpsecAuthAlg"),
            IpsecEncAlg=json_data.get("IpsecEncAlg"),
            KeyRolloverInterval=json_data.get("KeyRolloverInterval"),
            Mtu=json_data.get("Mtu"),
            MtuIgnore=json_data.get("MtuIgnore"),
            Name=json_data.get("Name"),
            NetworkType=json_data.get("NetworkType"),
            Priority=json_data.get("Priority"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            Status=json_data.get("Status"),
            TransmitDelay=json_data.get("TransmitDelay"),
            Vdomparam=json_data.get("Vdomparam"),
            IpsecKeys=deserialize_list(json_data.get("IpsecKeys"), IpsecKeysDefinition),
            Neighbor=deserialize_list(json_data.get("Neighbor"), NeighborDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpsecKeysDefinition(BaseModel):
    AuthKey: Optional[str]
    EncKey: Optional[str]
    Spi: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_IpsecKeysDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsecKeysDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthKey=json_data.get("AuthKey"),
            EncKey=json_data.get("EncKey"),
            Spi=json_data.get("Spi"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsecKeysDefinition = IpsecKeysDefinition


@dataclass
class NeighborDefinition(BaseModel):
    Cost: Optional[float]
    Ip6: Optional[str]
    PollInterval: Optional[float]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NeighborDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NeighborDefinition"]:
        if not json_data:
            return None
        return cls(
            Cost=json_data.get("Cost"),
            Ip6=json_data.get("Ip6"),
            PollInterval=json_data.get("PollInterval"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NeighborDefinition = NeighborDefinition


