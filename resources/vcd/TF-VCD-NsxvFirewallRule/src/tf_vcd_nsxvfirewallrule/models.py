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
    AboveRuleId: Optional[str]
    Action: Optional[str]
    EdgeGateway: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    LoggingEnabled: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    RuleTag: Optional[float]
    RuleType: Optional[str]
    Vdc: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    Service: Optional[Sequence["_ServiceDefinition"]]
    Source: Optional[Sequence["_SourceDefinition"]]

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
            AboveRuleId=json_data.get("AboveRuleId"),
            Action=json_data.get("Action"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LoggingEnabled=json_data.get("LoggingEnabled"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            RuleTag=json_data.get("RuleTag"),
            RuleType=json_data.get("RuleType"),
            Vdc=json_data.get("Vdc"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            Service=deserialize_list(json_data.get("Service"), ServiceDefinition),
            Source=deserialize_list(json_data.get("Source"), SourceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DestinationDefinition(BaseModel):
    Exclude: Optional[bool]
    GatewayInterfaces: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    OrgNetworks: Optional[Sequence[str]]
    VmIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            GatewayInterfaces=json_data.get("GatewayInterfaces"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            OrgNetworks=json_data.get("OrgNetworks"),
            VmIds=json_data.get("VmIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class ServiceDefinition(BaseModel):
    Port: Optional[str]
    Protocol: Optional[str]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceDefinition = ServiceDefinition


@dataclass
class SourceDefinition(BaseModel):
    Exclude: Optional[bool]
    GatewayInterfaces: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    OrgNetworks: Optional[Sequence[str]]
    VmIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            GatewayInterfaces=json_data.get("GatewayInterfaces"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            OrgNetworks=json_data.get("OrgNetworks"),
            VmIds=json_data.get("VmIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceDefinition = SourceDefinition


