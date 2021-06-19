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
    Adom: Optional[str]
    Category: Optional[str]
    Comment: Optional[str]
    Fqdn: Optional[str]
    IcmpCode: Optional[float]
    IcmpType: Optional[float]
    Id: Optional[str]
    Iprange: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ProtocolNumber: Optional[float]
    Proxy: Optional[str]
    SctpPortrange: Optional[Sequence[str]]
    TcpPortrange: Optional[Sequence[str]]
    UdpPortrange: Optional[Sequence[str]]

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
            Adom=json_data.get("Adom"),
            Category=json_data.get("Category"),
            Comment=json_data.get("Comment"),
            Fqdn=json_data.get("Fqdn"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Id=json_data.get("Id"),
            Iprange=json_data.get("Iprange"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ProtocolNumber=json_data.get("ProtocolNumber"),
            Proxy=json_data.get("Proxy"),
            SctpPortrange=json_data.get("SctpPortrange"),
            TcpPortrange=json_data.get("TcpPortrange"),
            UdpPortrange=json_data.get("UdpPortrange"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


