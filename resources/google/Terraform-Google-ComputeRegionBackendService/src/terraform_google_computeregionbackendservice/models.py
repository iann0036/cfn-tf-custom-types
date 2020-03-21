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
    ConnectionDrainingTimeoutSec: Optional[float]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Fingerprint: Optional[str]
    HealthChecks: Optional[Sequence[str]]
    LoadBalancingScheme: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Protocol: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    SessionAffinity: Optional[str]
    TimeoutSec: Optional[float]
    Backend: Optional[Sequence["_Backend"]]
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
            ConnectionDrainingTimeoutSec=json_data.get("ConnectionDrainingTimeoutSec"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Fingerprint=json_data.get("Fingerprint"),
            HealthChecks=json_data.get("HealthChecks"),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Protocol=json_data.get("Protocol"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            SessionAffinity=json_data.get("SessionAffinity"),
            TimeoutSec=json_data.get("TimeoutSec"),
            Backend=json_data.get("Backend"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Backend:
    BalancingMode: Optional[str]
    CapacityScaler: Optional[float]
    Description: Optional[str]
    Group: Optional[str]
    MaxConnections: Optional[float]
    MaxConnectionsPerEndpoint: Optional[float]
    MaxConnectionsPerInstance: Optional[float]
    MaxRate: Optional[float]
    MaxRatePerEndpoint: Optional[float]
    MaxRatePerInstance: Optional[float]
    MaxUtilization: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Backend"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Backend"]:
        if not json_data:
            return None
        return cls(
            BalancingMode=json_data.get("BalancingMode"),
            CapacityScaler=json_data.get("CapacityScaler"),
            Description=json_data.get("Description"),
            Group=json_data.get("Group"),
            MaxConnections=json_data.get("MaxConnections"),
            MaxConnectionsPerEndpoint=json_data.get("MaxConnectionsPerEndpoint"),
            MaxConnectionsPerInstance=json_data.get("MaxConnectionsPerInstance"),
            MaxRate=json_data.get("MaxRate"),
            MaxRatePerEndpoint=json_data.get("MaxRatePerEndpoint"),
            MaxRatePerInstance=json_data.get("MaxRatePerInstance"),
            MaxUtilization=json_data.get("MaxUtilization"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Backend = Backend


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


