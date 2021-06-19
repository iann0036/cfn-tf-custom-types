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
    Alias: Optional[str]
    Allowaccess: Optional[str]
    Defaultgw: Optional[str]
    Description: Optional[str]
    DeviceIdentification: Optional[str]
    Distance: Optional[str]
    DnsServerOverride: Optional[str]
    Id: Optional[str]
    Interface: Optional[str]
    Ip: Optional[str]
    Mode: Optional[str]
    Mtu: Optional[str]
    MtuOverride: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Speed: Optional[str]
    Status: Optional[str]
    TcpMss: Optional[str]
    Type: Optional[str]
    Vdom: Optional[str]
    Vlanid: Optional[str]

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
            Alias=json_data.get("Alias"),
            Allowaccess=json_data.get("Allowaccess"),
            Defaultgw=json_data.get("Defaultgw"),
            Description=json_data.get("Description"),
            DeviceIdentification=json_data.get("DeviceIdentification"),
            Distance=json_data.get("Distance"),
            DnsServerOverride=json_data.get("DnsServerOverride"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            Ip=json_data.get("Ip"),
            Mode=json_data.get("Mode"),
            Mtu=json_data.get("Mtu"),
            MtuOverride=json_data.get("MtuOverride"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Speed=json_data.get("Speed"),
            Status=json_data.get("Status"),
            TcpMss=json_data.get("TcpMss"),
            Type=json_data.get("Type"),
            Vdom=json_data.get("Vdom"),
            Vlanid=json_data.get("Vlanid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


