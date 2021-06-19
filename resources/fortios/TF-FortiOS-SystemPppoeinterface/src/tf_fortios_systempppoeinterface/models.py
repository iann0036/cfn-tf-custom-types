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
    AcName: Optional[str]
    AuthType: Optional[str]
    Device: Optional[str]
    DialOnDemand: Optional[str]
    DiscRetryTimeout: Optional[float]
    Id: Optional[str]
    IdleTimeout: Optional[float]
    Ipunnumbered: Optional[str]
    Ipv6: Optional[str]
    LcpEchoInterval: Optional[float]
    LcpMaxEchoFails: Optional[float]
    Name: Optional[str]
    PadtRetryTimeout: Optional[float]
    Password: Optional[str]
    PppoeUnnumberedNegotiate: Optional[str]
    ServiceName: Optional[str]
    Username: Optional[str]
    Vdomparam: Optional[str]

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
            AcName=json_data.get("AcName"),
            AuthType=json_data.get("AuthType"),
            Device=json_data.get("Device"),
            DialOnDemand=json_data.get("DialOnDemand"),
            DiscRetryTimeout=json_data.get("DiscRetryTimeout"),
            Id=json_data.get("Id"),
            IdleTimeout=json_data.get("IdleTimeout"),
            Ipunnumbered=json_data.get("Ipunnumbered"),
            Ipv6=json_data.get("Ipv6"),
            LcpEchoInterval=json_data.get("LcpEchoInterval"),
            LcpMaxEchoFails=json_data.get("LcpMaxEchoFails"),
            Name=json_data.get("Name"),
            PadtRetryTimeout=json_data.get("PadtRetryTimeout"),
            Password=json_data.get("Password"),
            PppoeUnnumberedNegotiate=json_data.get("PppoeUnnumberedNegotiate"),
            ServiceName=json_data.get("ServiceName"),
            Username=json_data.get("Username"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


