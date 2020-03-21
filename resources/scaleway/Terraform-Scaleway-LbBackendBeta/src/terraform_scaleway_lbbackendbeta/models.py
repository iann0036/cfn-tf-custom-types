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
    ForwardPort: Optional[float]
    ForwardPortAlgorithm: Optional[str]
    ForwardProtocol: Optional[str]
    HealthCheckDelay: Optional[str]
    HealthCheckMaxRetries: Optional[float]
    HealthCheckPort: Optional[float]
    HealthCheckTimeout: Optional[str]
    Id: Optional[str]
    LbId: Optional[str]
    Name: Optional[str]
    OnMarkedDownAction: Optional[str]
    SendProxyV2: Optional[bool]
    ServerIps: Optional[Sequence[str]]
    StickySessions: Optional[str]
    StickySessionsCookieName: Optional[str]
    TimeoutConnect: Optional[str]
    TimeoutServer: Optional[str]
    TimeoutTunnel: Optional[str]
    HealthCheckHttp: Optional[Sequence["_HealthCheckHttp"]]
    HealthCheckHttps: Optional[Sequence["_HealthCheckHttps"]]
    HealthCheckTcp: Optional[Sequence["_HealthCheckTcp"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ForwardPort=json_data.get("ForwardPort"),
            ForwardPortAlgorithm=json_data.get("ForwardPortAlgorithm"),
            ForwardProtocol=json_data.get("ForwardProtocol"),
            HealthCheckDelay=json_data.get("HealthCheckDelay"),
            HealthCheckMaxRetries=json_data.get("HealthCheckMaxRetries"),
            HealthCheckPort=json_data.get("HealthCheckPort"),
            HealthCheckTimeout=json_data.get("HealthCheckTimeout"),
            Id=json_data.get("Id"),
            LbId=json_data.get("LbId"),
            Name=json_data.get("Name"),
            OnMarkedDownAction=json_data.get("OnMarkedDownAction"),
            SendProxyV2=json_data.get("SendProxyV2"),
            ServerIps=json_data.get("ServerIps"),
            StickySessions=json_data.get("StickySessions"),
            StickySessionsCookieName=json_data.get("StickySessionsCookieName"),
            TimeoutConnect=json_data.get("TimeoutConnect"),
            TimeoutServer=json_data.get("TimeoutServer"),
            TimeoutTunnel=json_data.get("TimeoutTunnel"),
            HealthCheckHttp=json_data.get("HealthCheckHttp"),
            HealthCheckHttps=json_data.get("HealthCheckHttps"),
            HealthCheckTcp=json_data.get("HealthCheckTcp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HealthCheckHttp:
    Code: Optional[float]
    Method: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckHttp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckHttp"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Method=json_data.get("Method"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckHttp = HealthCheckHttp


@dataclass
class HealthCheckHttps:
    Code: Optional[float]
    Method: Optional[str]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckHttps"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckHttps"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Method=json_data.get("Method"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckHttps = HealthCheckHttps


@dataclass
class HealthCheckTcp:
    IsPropertyDefined: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckTcp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckTcp"]:
        if not json_data:
            return None
        return cls(
            IsPropertyDefined=json_data.get("IsPropertyDefined"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckTcp = HealthCheckTcp


