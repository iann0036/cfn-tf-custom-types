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
    DefaultBackendSetName: Optional[str]
    HostnameNames: Optional[Sequence[str]]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    Name: Optional[str]
    PathRouteSetName: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    RoutingPolicyName: Optional[str]
    RuleSetNames: Optional[Sequence[str]]
    State: Optional[str]
    ConnectionConfiguration: Optional[Sequence["_ConnectionConfigurationDefinition"]]
    SslConfiguration: Optional[Sequence["_SslConfigurationDefinition"]]
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
            DefaultBackendSetName=json_data.get("DefaultBackendSetName"),
            HostnameNames=json_data.get("HostnameNames"),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            Name=json_data.get("Name"),
            PathRouteSetName=json_data.get("PathRouteSetName"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            RoutingPolicyName=json_data.get("RoutingPolicyName"),
            RuleSetNames=json_data.get("RuleSetNames"),
            State=json_data.get("State"),
            ConnectionConfiguration=deserialize_list(json_data.get("ConnectionConfiguration"), ConnectionConfigurationDefinition),
            SslConfiguration=deserialize_list(json_data.get("SslConfiguration"), SslConfigurationDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ConnectionConfigurationDefinition(BaseModel):
    BackendTcpProxyProtocolVersion: Optional[float]
    IdleTimeoutInSeconds: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendTcpProxyProtocolVersion=json_data.get("BackendTcpProxyProtocolVersion"),
            IdleTimeoutInSeconds=json_data.get("IdleTimeoutInSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionConfigurationDefinition = ConnectionConfigurationDefinition


@dataclass
class SslConfigurationDefinition(BaseModel):
    CertificateName: Optional[str]
    CipherSuiteName: Optional[str]
    Protocols: Optional[Sequence[str]]
    ServerOrderPreference: Optional[str]
    VerifyDepth: Optional[float]
    VerifyPeerCertificate: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SslConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateName=json_data.get("CertificateName"),
            CipherSuiteName=json_data.get("CipherSuiteName"),
            Protocols=json_data.get("Protocols"),
            ServerOrderPreference=json_data.get("ServerOrderPreference"),
            VerifyDepth=json_data.get("VerifyDepth"),
            VerifyPeerCertificate=json_data.get("VerifyPeerCertificate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslConfigurationDefinition = SslConfigurationDefinition


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


