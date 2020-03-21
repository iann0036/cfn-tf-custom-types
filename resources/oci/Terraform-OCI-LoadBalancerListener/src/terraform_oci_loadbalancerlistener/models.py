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
    DefaultBackendSetName: Optional[str]
    HostnameNames: Optional[Sequence[str]]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    PathRouteSetName: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    RuleSetNames: Optional[Sequence[str]]
    State: Optional[str]
    ConnectionConfiguration: Optional[Sequence["_ConnectionConfiguration"]]
    SslConfiguration: Optional[Sequence["_SslConfiguration"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultBackendSetName=json_data.get("DefaultBackendSetName"),
            HostnameNames=json_data.get("HostnameNames"),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            PathRouteSetName=json_data.get("PathRouteSetName"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            RuleSetNames=json_data.get("RuleSetNames"),
            State=json_data.get("State"),
            ConnectionConfiguration=json_data.get("ConnectionConfiguration"),
            SslConfiguration=json_data.get("SslConfiguration"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionConfiguration:
    BackendTcpProxyProtocolVersion: Optional[float]
    IdleTimeoutInSeconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionConfiguration"]:
        if not json_data:
            return None
        return cls(
            BackendTcpProxyProtocolVersion=json_data.get("BackendTcpProxyProtocolVersion"),
            IdleTimeoutInSeconds=json_data.get("IdleTimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionConfiguration = ConnectionConfiguration


@dataclass
class SslConfiguration:
    CertificateName: Optional[str]
    VerifyDepth: Optional[float]
    VerifyPeerCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfiguration"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfiguration"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            VerifyDepth=json_data.get("VerifyDepth"),
            VerifyPeerCertificate=json_data.get("VerifyPeerCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfiguration = SslConfiguration


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


