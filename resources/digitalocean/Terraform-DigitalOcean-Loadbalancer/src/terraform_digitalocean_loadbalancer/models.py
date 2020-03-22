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
    Algorithm: Optional[str]
    DropletIds: Optional[Sequence[float]]
    DropletTag: Optional[str]
    EnableProxyProtocol: Optional[bool]
    Id: Optional[str]
    Ip: Optional[str]
    Name: Optional[str]
    RedirectHttpToHttps: Optional[bool]
    Region: Optional[str]
    Status: Optional[str]
    Urn: Optional[str]
    ForwardingRule: Optional[Sequence["_ForwardingRule"]]
    Healthcheck: Optional[Sequence["_Healthcheck"]]
    StickySessions: Optional[Sequence["_StickySessions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Algorithm=json_data.get("Algorithm"),
            DropletIds=json_data.get("DropletIds"),
            DropletTag=json_data.get("DropletTag"),
            EnableProxyProtocol=json_data.get("EnableProxyProtocol"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            RedirectHttpToHttps=json_data.get("RedirectHttpToHttps"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            Urn=json_data.get("Urn"),
            ForwardingRule=json_data.get("ForwardingRule"),
            Healthcheck=json_data.get("Healthcheck"),
            StickySessions=json_data.get("StickySessions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ForwardingRule:
    CertificateId: Optional[str]
    EntryPort: Optional[float]
    EntryProtocol: Optional[str]
    TargetPort: Optional[float]
    TargetProtocol: Optional[str]
    TlsPassthrough: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingRule"]:
        if not json_data:
            return None
        return cls(
            CertificateId=json_data.get("CertificateId"),
            EntryPort=json_data.get("EntryPort"),
            EntryProtocol=json_data.get("EntryProtocol"),
            TargetPort=json_data.get("TargetPort"),
            TargetProtocol=json_data.get("TargetProtocol"),
            TlsPassthrough=json_data.get("TlsPassthrough"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingRule = ForwardingRule


@dataclass
class Healthcheck:
    CheckIntervalSeconds: Optional[float]
    HealthyThreshold: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ResponseTimeoutSeconds: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Healthcheck"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Healthcheck"]:
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
_Healthcheck = Healthcheck


@dataclass
class StickySessions:
    CookieName: Optional[str]
    CookieTtlSeconds: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StickySessions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StickySessions"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            CookieTtlSeconds=json_data.get("CookieTtlSeconds"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StickySessions = StickySessions


