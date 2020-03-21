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
    AboveRuleId: Optional[str]
    Action: Optional[str]
    EdgeGateway: Optional[str]
    Enabled: Optional[bool]
    LoggingEnabled: Optional[bool]
    Name: Optional[str]
    Org: Optional[str]
    RuleTag: Optional[float]
    RuleType: Optional[str]
    Vdc: Optional[str]
    Destination: Optional[Sequence["_Destination"]]
    Service: Optional[Sequence["_Service"]]
    Source: Optional[Sequence["_Source"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AboveRuleId=json_data.get("AboveRuleId"),
            Action=json_data.get("Action"),
            EdgeGateway=json_data.get("EdgeGateway"),
            Enabled=json_data.get("Enabled"),
            LoggingEnabled=json_data.get("LoggingEnabled"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            RuleTag=json_data.get("RuleTag"),
            RuleType=json_data.get("RuleType"),
            Vdc=json_data.get("Vdc"),
            Destination=json_data.get("Destination"),
            Service=json_data.get("Service"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Destination:
    Exclude: Optional[bool]
    GatewayInterfaces: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    OrgNetworks: Optional[Sequence[str]]
    VirtualMachineIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            GatewayInterfaces=json_data.get("GatewayInterfaces"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            OrgNetworks=json_data.get("OrgNetworks"),
            VirtualMachineIds=json_data.get("VirtualMachineIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class Service:
    Port: Optional[str]
    Protocol: Optional[str]
    SourcePort: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Service"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Service"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SourcePort=json_data.get("SourcePort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Service = Service


@dataclass
class Source:
    Exclude: Optional[bool]
    GatewayInterfaces: Optional[Sequence[str]]
    IpAddresses: Optional[Sequence[str]]
    IpSets: Optional[Sequence[str]]
    OrgNetworks: Optional[Sequence[str]]
    VirtualMachineIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Source"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Source"]:
        if not json_data:
            return None
        return cls(
            Exclude=json_data.get("Exclude"),
            GatewayInterfaces=json_data.get("GatewayInterfaces"),
            IpAddresses=json_data.get("IpAddresses"),
            IpSets=json_data.get("IpSets"),
            OrgNetworks=json_data.get("OrgNetworks"),
            VirtualMachineIds=json_data.get("VirtualMachineIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Source = Source


