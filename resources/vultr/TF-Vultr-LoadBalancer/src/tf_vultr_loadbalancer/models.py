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
    AttachedInstances: Optional[Sequence[str]]
    BalancingAlgorithm: Optional[str]
    CookieName: Optional[str]
    HasSsl: Optional[bool]
    Id: Optional[str]
    Ipv4: Optional[str]
    Ipv6: Optional[str]
    Label: Optional[str]
    PrivateNetwork: Optional[str]
    ProxyProtocol: Optional[bool]
    Region: Optional[str]
    SslRedirect: Optional[bool]
    Status: Optional[str]
    FirewallRules: Optional[Sequence["_FirewallRulesDefinition"]]
    ForwardingRules: Optional[Sequence["_ForwardingRulesDefinition"]]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    Ssl: Optional[Sequence["_SslDefinition"]]

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
            AttachedInstances=json_data.get("AttachedInstances"),
            BalancingAlgorithm=json_data.get("BalancingAlgorithm"),
            CookieName=json_data.get("CookieName"),
            HasSsl=json_data.get("HasSsl"),
            Id=json_data.get("Id"),
            Ipv4=json_data.get("Ipv4"),
            Ipv6=json_data.get("Ipv6"),
            Label=json_data.get("Label"),
            PrivateNetwork=json_data.get("PrivateNetwork"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            Region=json_data.get("Region"),
            SslRedirect=json_data.get("SslRedirect"),
            Status=json_data.get("Status"),
            FirewallRules=deserialize_list(json_data.get("FirewallRules"), FirewallRulesDefinition),
            ForwardingRules=deserialize_list(json_data.get("ForwardingRules"), ForwardingRulesDefinition),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            Ssl=deserialize_list(json_data.get("Ssl"), SslDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FirewallRulesDefinition(BaseModel):
    IpType: Optional[str]
    Port: Optional[float]
    Source: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirewallRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirewallRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            IpType=json_data.get("IpType"),
            Port=json_data.get("Port"),
            Source=json_data.get("Source"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirewallRulesDefinition = FirewallRulesDefinition


@dataclass
class ForwardingRulesDefinition(BaseModel):
    BackendPort: Optional[float]
    BackendProtocol: Optional[str]
    FrontendPort: Optional[float]
    FrontendProtocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendPort=json_data.get("BackendPort"),
            BackendProtocol=json_data.get("BackendProtocol"),
            FrontendPort=json_data.get("FrontendPort"),
            FrontendProtocol=json_data.get("FrontendProtocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingRulesDefinition = ForwardingRulesDefinition


@dataclass
class HealthCheckDefinition(BaseModel):
    CheckInterval: Optional[float]
    HealthyThreshold: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ResponseTimeout: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckInterval=json_data.get("CheckInterval"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ResponseTimeout=json_data.get("ResponseTimeout"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class SslDefinition(BaseModel):
    Certificate: Optional[str]
    Chain: Optional[str]
    PrivateKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslDefinition"]:
        if not json_data:
            return None
        return cls(
            Certificate=json_data.get("Certificate"),
            Chain=json_data.get("Chain"),
            PrivateKey=json_data.get("PrivateKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslDefinition = SslDefinition


