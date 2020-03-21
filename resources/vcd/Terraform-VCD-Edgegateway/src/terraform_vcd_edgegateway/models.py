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
    Advanced: Optional[bool]
    Configuration: Optional[str]
    DefaultExternalNetworkIp: Optional[str]
    DefaultGatewayNetwork: Optional[str]
    Description: Optional[str]
    DistributedRouting: Optional[bool]
    ExternalNetworkIps: Optional[Sequence[str]]
    ExternalNetworks: Optional[Sequence[str]]
    FipsModeEnabled: Optional[bool]
    FwDefaultRuleAction: Optional[str]
    FwDefaultRuleLoggingEnabled: Optional[bool]
    FwEnabled: Optional[bool]
    HaEnabled: Optional[bool]
    LbAccelerationEnabled: Optional[bool]
    LbEnabled: Optional[bool]
    LbLoggingEnabled: Optional[bool]
    LbLoglevel: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    UseDefaultRouteForDnsRelay: Optional[bool]
    Vdc: Optional[str]
    ExternalNetwork: Optional[Sequence["_ExternalNetwork"]]
    Subnet: Optional[Sequence["_Subnet"]]
    SuballocatePool: Optional[Sequence["_SuballocatePool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Advanced=json_data.get("Advanced"),
            Configuration=json_data.get("Configuration"),
            DefaultExternalNetworkIp=json_data.get("DefaultExternalNetworkIp"),
            DefaultGatewayNetwork=json_data.get("DefaultGatewayNetwork"),
            Description=json_data.get("Description"),
            DistributedRouting=json_data.get("DistributedRouting"),
            ExternalNetworkIps=json_data.get("ExternalNetworkIps"),
            ExternalNetworks=json_data.get("ExternalNetworks"),
            FipsModeEnabled=json_data.get("FipsModeEnabled"),
            FwDefaultRuleAction=json_data.get("FwDefaultRuleAction"),
            FwDefaultRuleLoggingEnabled=json_data.get("FwDefaultRuleLoggingEnabled"),
            FwEnabled=json_data.get("FwEnabled"),
            HaEnabled=json_data.get("HaEnabled"),
            LbAccelerationEnabled=json_data.get("LbAccelerationEnabled"),
            LbEnabled=json_data.get("LbEnabled"),
            LbLoggingEnabled=json_data.get("LbLoggingEnabled"),
            LbLoglevel=json_data.get("LbLoglevel"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            UseDefaultRouteForDnsRelay=json_data.get("UseDefaultRouteForDnsRelay"),
            Vdc=json_data.get("Vdc"),
            ExternalNetwork=json_data.get("ExternalNetwork"),
            Subnet=json_data.get("Subnet"),
            SuballocatePool=json_data.get("SuballocatePool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExternalNetwork:
    EnableRateLimit: Optional[bool]
    IncomingRateLimit: Optional[float]
    Name: Optional[str]
    OutgoingRateLimit: Optional[float]
    Subnet: Optional[Sequence["_Subnet"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalNetwork"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalNetwork"]:
        if not json_data:
            return None
        return cls(
            EnableRateLimit=json_data.get("EnableRateLimit"),
            IncomingRateLimit=json_data.get("IncomingRateLimit"),
            Name=json_data.get("Name"),
            OutgoingRateLimit=json_data.get("OutgoingRateLimit"),
            Subnet=json_data.get("Subnet"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalNetwork = ExternalNetwork


@dataclass
class Subnet:
    Gateway: Optional[str]
    IpAddress: Optional[str]
    Netmask: Optional[str]
    UseForDefaultRoute: Optional[bool]
    SuballocatePool: Optional[Sequence["_SuballocatePool"]]

    @classmethod
    def _deserialize(
        cls: Type["_Subnet"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Subnet"]:
        if not json_data:
            return None
        return cls(
            Gateway=json_data.get("Gateway"),
            IpAddress=json_data.get("IpAddress"),
            Netmask=json_data.get("Netmask"),
            UseForDefaultRoute=json_data.get("UseForDefaultRoute"),
            SuballocatePool=json_data.get("SuballocatePool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Subnet = Subnet


@dataclass
class SuballocatePool:
    EndAddress: Optional[str]
    StartAddress: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SuballocatePool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SuballocatePool"]:
        if not json_data:
            return None
        return cls(
            EndAddress=json_data.get("EndAddress"),
            StartAddress=json_data.get("StartAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SuballocatePool = SuballocatePool


