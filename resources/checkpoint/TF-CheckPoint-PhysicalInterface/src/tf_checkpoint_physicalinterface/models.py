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
    AutoNegotiation: Optional[str]
    Comments: Optional[str]
    Duplex: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Ipv4Address: Optional[str]
    Ipv4MaskLength: Optional[float]
    Ipv6Address: Optional[str]
    Ipv6Autoconfig: Optional[str]
    Ipv6MaskLength: Optional[float]
    MacAddr: Optional[str]
    MonitorMode: Optional[str]
    Mtu: Optional[float]
    Name: Optional[str]
    RxRingsize: Optional[str]
    Speed: Optional[str]
    TxRingsize: Optional[str]

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
            AutoNegotiation=json_data.get("AutoNegotiation"),
            Comments=json_data.get("Comments"),
            Duplex=json_data.get("Duplex"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Ipv4Address=json_data.get("Ipv4Address"),
            Ipv4MaskLength=json_data.get("Ipv4MaskLength"),
            Ipv6Address=json_data.get("Ipv6Address"),
            Ipv6Autoconfig=json_data.get("Ipv6Autoconfig"),
            Ipv6MaskLength=json_data.get("Ipv6MaskLength"),
            MacAddr=json_data.get("MacAddr"),
            MonitorMode=json_data.get("MonitorMode"),
            Mtu=json_data.get("Mtu"),
            Name=json_data.get("Name"),
            RxRingsize=json_data.get("RxRingsize"),
            Speed=json_data.get("Speed"),
            TxRingsize=json_data.get("TxRingsize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


