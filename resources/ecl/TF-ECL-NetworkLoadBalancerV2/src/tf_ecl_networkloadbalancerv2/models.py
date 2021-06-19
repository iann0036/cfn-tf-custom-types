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
    AdminPassword: Optional[str]
    AdminUsername: Optional[str]
    AvailabilityZone: Optional[str]
    DefaultGateway: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LoadBalancerPlanId: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    TenantId: Optional[str]
    UserPassword: Optional[str]
    UserUsername: Optional[str]
    Interfaces: Optional[Sequence["_InterfacesDefinition"]]
    SyslogServers: Optional[Sequence["_SyslogServersDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            AdminPassword=json_data.get("AdminPassword"),
            AdminUsername=json_data.get("AdminUsername"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            DefaultGateway=json_data.get("DefaultGateway"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LoadBalancerPlanId=json_data.get("LoadBalancerPlanId"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            TenantId=json_data.get("TenantId"),
            UserPassword=json_data.get("UserPassword"),
            UserUsername=json_data.get("UserUsername"),
            Interfaces=deserialize_list(json_data.get("Interfaces"), InterfacesDefinition),
            SyslogServers=deserialize_list(json_data.get("SyslogServers"), SyslogServersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InterfacesDefinition(BaseModel):
    Description: Optional[str]
    IpAddress: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    SlotNumber: Optional[float]
    VirtualIpAddress: Optional[str]
    VirtualIpProperties: Optional[Sequence["_VirtualIpPropertiesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_InterfacesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InterfacesDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            SlotNumber=json_data.get("SlotNumber"),
            VirtualIpAddress=json_data.get("VirtualIpAddress"),
            VirtualIpProperties=deserialize_list(json_data.get("VirtualIpProperties"), VirtualIpPropertiesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_InterfacesDefinition = InterfacesDefinition


@dataclass
class VirtualIpPropertiesDefinition(BaseModel):
    Protocol: Optional[str]
    Vrid: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualIpPropertiesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualIpPropertiesDefinition"]:
        if not json_data:
            return None
        return cls(
            Protocol=json_data.get("Protocol"),
            Vrid=json_data.get("Vrid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualIpPropertiesDefinition = VirtualIpPropertiesDefinition


@dataclass
class SyslogServersDefinition(BaseModel):
    AclLogging: Optional[str]
    AppflowLogging: Optional[str]
    DateFormat: Optional[str]
    Description: Optional[str]
    IpAddress: Optional[str]
    LogFacility: Optional[str]
    LogLevel: Optional[str]
    Name: Optional[str]
    PortNumber: Optional[float]
    Priority: Optional[float]
    TcpLogging: Optional[str]
    TenantId: Optional[str]
    TimeZone: Optional[str]
    TransportType: Optional[str]
    UserConfigurableLogMessages: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SyslogServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SyslogServersDefinition"]:
        if not json_data:
            return None
        return cls(
            AclLogging=json_data.get("AclLogging"),
            AppflowLogging=json_data.get("AppflowLogging"),
            DateFormat=json_data.get("DateFormat"),
            Description=json_data.get("Description"),
            IpAddress=json_data.get("IpAddress"),
            LogFacility=json_data.get("LogFacility"),
            LogLevel=json_data.get("LogLevel"),
            Name=json_data.get("Name"),
            PortNumber=json_data.get("PortNumber"),
            Priority=json_data.get("Priority"),
            TcpLogging=json_data.get("TcpLogging"),
            TenantId=json_data.get("TenantId"),
            TimeZone=json_data.get("TimeZone"),
            TransportType=json_data.get("TransportType"),
            UserConfigurableLogMessages=json_data.get("UserConfigurableLogMessages"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SyslogServersDefinition = SyslogServersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


