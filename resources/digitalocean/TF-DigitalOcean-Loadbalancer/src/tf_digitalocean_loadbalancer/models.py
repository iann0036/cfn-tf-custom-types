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
    Algorithm: Optional[str]
    DropletIds: Optional[Sequence[float]]
    DropletTag: Optional[str]
    EnableBackendKeepalive: Optional[bool]
    EnableProxyProtocol: Optional[bool]
    Id: Optional[str]
    Ip: Optional[str]
    Name: Optional[str]
    RedirectHttpToHttps: Optional[bool]
    Region: Optional[str]
    Size: Optional[str]
    Status: Optional[str]
    Urn: Optional[str]
    VpcUuid: Optional[str]
    ForwardingRule: Optional[Sequence["_ForwardingRuleDefinition"]]
    Healthcheck: Optional[Sequence["_HealthcheckDefinition"]]
    StickySessions: Optional[Sequence["_StickySessionsDefinition"]]

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
            Algorithm=json_data.get("Algorithm"),
            DropletIds=json_data.get("DropletIds"),
            DropletTag=json_data.get("DropletTag"),
            EnableBackendKeepalive=json_data.get("EnableBackendKeepalive"),
            EnableProxyProtocol=json_data.get("EnableProxyProtocol"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            RedirectHttpToHttps=json_data.get("RedirectHttpToHttps"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Urn=json_data.get("Urn"),
            VpcUuid=json_data.get("VpcUuid"),
            ForwardingRule=deserialize_list(json_data.get("ForwardingRule"), ForwardingRuleDefinition),
            Healthcheck=deserialize_list(json_data.get("Healthcheck"), HealthcheckDefinition),
            StickySessions=deserialize_list(json_data.get("StickySessions"), StickySessionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ForwardingRuleDefinition(BaseModel):
    CertificateId: Optional[str]
    CertificateName: Optional[str]
    EntryPort: Optional[float]
    EntryProtocol: Optional[str]
    TargetPort: Optional[float]
    TargetProtocol: Optional[str]
    TlsPassthrough: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateId=json_data.get("CertificateId"),
            CertificateName=json_data.get("CertificateName"),
            EntryPort=json_data.get("EntryPort"),
            EntryProtocol=json_data.get("EntryProtocol"),
            TargetPort=json_data.get("TargetPort"),
            TargetProtocol=json_data.get("TargetProtocol"),
            TlsPassthrough=json_data.get("TlsPassthrough"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingRuleDefinition = ForwardingRuleDefinition


@dataclass
class HealthcheckDefinition(BaseModel):
    CheckIntervalSeconds: Optional[float]
    HealthyThreshold: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ResponseTimeoutSeconds: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthcheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthcheckDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckIntervalSeconds=json_data.get("CheckIntervalSeconds"),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ResponseTimeoutSeconds=json_data.get("ResponseTimeoutSeconds"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthcheckDefinition = HealthcheckDefinition


@dataclass
class StickySessionsDefinition(BaseModel):
    CookieName: Optional[str]
    CookieTtlSeconds: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StickySessionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StickySessionsDefinition"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            CookieTtlSeconds=json_data.get("CookieTtlSeconds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StickySessionsDefinition = StickySessionsDefinition


