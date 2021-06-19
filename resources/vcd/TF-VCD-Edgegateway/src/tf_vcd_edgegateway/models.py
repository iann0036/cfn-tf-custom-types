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
    Configuration: Optional[str]
    DefaultExternalNetworkIp: Optional[str]
    Description: Optional[str]
    DistributedRouting: Optional[bool]
    ExternalNetworkIps: Optional[Sequence[str]]
    FipsModeEnabled: Optional[bool]
    FwDefaultRuleAction: Optional[str]
    FwDefaultRuleLoggingEnabled: Optional[bool]
    FwEnabled: Optional[bool]
    HaEnabled: Optional[bool]
    Id: Optional[str]
    LbAccelerationEnabled: Optional[bool]
    LbEnabled: Optional[bool]
    LbLoggingEnabled: Optional[bool]
    LbLoglevel: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    UseDefaultRouteForDnsRelay: Optional[bool]
    Vdc: Optional[str]
    ExternalNetwork: Optional[Sequence["_ExternalNetworkDefinition"]]

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
            Configuration=json_data.get("Configuration"),
            DefaultExternalNetworkIp=json_data.get("DefaultExternalNetworkIp"),
            Description=json_data.get("Description"),
            DistributedRouting=json_data.get("DistributedRouting"),
            ExternalNetworkIps=json_data.get("ExternalNetworkIps"),
            FipsModeEnabled=json_data.get("FipsModeEnabled"),
            FwDefaultRuleAction=json_data.get("FwDefaultRuleAction"),
            FwDefaultRuleLoggingEnabled=json_data.get("FwDefaultRuleLoggingEnabled"),
            FwEnabled=json_data.get("FwEnabled"),
            HaEnabled=json_data.get("HaEnabled"),
            Id=json_data.get("Id"),
            LbAccelerationEnabled=json_data.get("LbAccelerationEnabled"),
            LbEnabled=json_data.get("LbEnabled"),
            LbLoggingEnabled=json_data.get("LbLoggingEnabled"),
            LbLoglevel=json_data.get("LbLoglevel"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            UseDefaultRouteForDnsRelay=json_data.get("UseDefaultRouteForDnsRelay"),
            Vdc=json_data.get("Vdc"),
            ExternalNetwork=deserialize_list(json_data.get("ExternalNetwork"), ExternalNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExternalNetworkDefinition(BaseModel):
    EnableRateLimit: Optional[bool]
    IncomingRateLimit: Optional[float]
    Name: Optional[str]
    OutgoingRateLimit: Optional[float]
    Subnet: Optional[Sequence["_SubnetDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            EnableRateLimit=json_data.get("EnableRateLimit"),
            IncomingRateLimit=json_data.get("IncomingRateLimit"),
            Name=json_data.get("Name"),
            OutgoingRateLimit=json_data.get("OutgoingRateLimit"),
            Subnet=deserialize_list(json_data.get("Subnet"), SubnetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalNetworkDefinition = ExternalNetworkDefinition


@dataclass
class SubnetDefinition(BaseModel):
    Gateway: Optional[str]
    IpAddress: Optional[str]
    Netmask: Optional[str]
    UseForDefaultRoute: Optional[bool]
    SuballocatePool: Optional[Sequence["_SuballocatePoolDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubnetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubnetDefinition"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            IpAddress=json_data.get("IpAddress"),
            Netmask=json_data.get("Netmask"),
            UseForDefaultRoute=json_data.get("UseForDefaultRoute"),
            SuballocatePool=deserialize_list(json_data.get("SuballocatePool"), SuballocatePoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubnetDefinition = SubnetDefinition


@dataclass
class SuballocatePoolDefinition(BaseModel):
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuballocatePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuballocatePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuballocatePoolDefinition = SuballocatePoolDefinition


