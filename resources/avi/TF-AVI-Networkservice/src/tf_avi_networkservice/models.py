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
    CloudRef: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SeGroupRef: Optional[str]
    ServiceType: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    VrfRef: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    RoutingService: Optional[Sequence["_RoutingServiceDefinition"]]

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
            CloudRef=json_data.get("CloudRef"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SeGroupRef=json_data.get("SeGroupRef"),
            ServiceType=json_data.get("ServiceType"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            VrfRef=json_data.get("VrfRef"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            RoutingService=deserialize_list(json_data.get("RoutingService"), RoutingServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class RoutingServiceDefinition(BaseModel):
    AdvertiseBackendNetworks: Optional[bool]
    EnableAutoGateway: Optional[bool]
    EnableRouting: Optional[bool]
    EnableVipOnAllInterfaces: Optional[bool]
    EnableVmac: Optional[bool]
    GracefulRestart: Optional[bool]
    NatPolicyRef: Optional[str]
    RoutingByLinuxIpstack: Optional[bool]
    FloatingIntfIp: Optional[Sequence["_FloatingIntfIpDefinition"]]
    FloatingIntfIpSe2: Optional[Sequence["_FloatingIntfIpSe2Definition"]]
    FlowtableProfile: Optional[Sequence["_FlowtableProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RoutingServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoutingServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            AdvertiseBackendNetworks=json_data.get("AdvertiseBackendNetworks"),
            EnableAutoGateway=json_data.get("EnableAutoGateway"),
            EnableRouting=json_data.get("EnableRouting"),
            EnableVipOnAllInterfaces=json_data.get("EnableVipOnAllInterfaces"),
            EnableVmac=json_data.get("EnableVmac"),
            GracefulRestart=json_data.get("GracefulRestart"),
            NatPolicyRef=json_data.get("NatPolicyRef"),
            RoutingByLinuxIpstack=json_data.get("RoutingByLinuxIpstack"),
            FloatingIntfIp=deserialize_list(json_data.get("FloatingIntfIp"), FloatingIntfIpDefinition),
            FloatingIntfIpSe2=deserialize_list(json_data.get("FloatingIntfIpSe2"), FloatingIntfIpSe2Definition),
            FlowtableProfile=deserialize_list(json_data.get("FlowtableProfile"), FlowtableProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoutingServiceDefinition = RoutingServiceDefinition


@dataclass
class FloatingIntfIpDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIntfIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIntfIpDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIntfIpDefinition = FloatingIntfIpDefinition


@dataclass
class FloatingIntfIpSe2Definition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FloatingIntfIpSe2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FloatingIntfIpSe2Definition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FloatingIntfIpSe2Definition = FloatingIntfIpSe2Definition


@dataclass
class FlowtableProfileDefinition(BaseModel):
    IcmpIdleTimeout: Optional[float]
    TcpClosedTimeout: Optional[float]
    TcpConnectionSetupTimeout: Optional[float]
    TcpHalfClosedTimeout: Optional[float]
    TcpIdleTimeout: Optional[float]
    TcpResetTimeout: Optional[float]
    UdpIdleTimeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_FlowtableProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FlowtableProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            IcmpIdleTimeout=json_data.get("IcmpIdleTimeout"),
            TcpClosedTimeout=json_data.get("TcpClosedTimeout"),
            TcpConnectionSetupTimeout=json_data.get("TcpConnectionSetupTimeout"),
            TcpHalfClosedTimeout=json_data.get("TcpHalfClosedTimeout"),
            TcpIdleTimeout=json_data.get("TcpIdleTimeout"),
            TcpResetTimeout=json_data.get("TcpResetTimeout"),
            UdpIdleTimeout=json_data.get("UdpIdleTimeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FlowtableProfileDefinition = FlowtableProfileDefinition


