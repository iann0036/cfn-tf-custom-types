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
    AllPorts: Optional[bool]
    BackendService: Optional[str]
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IpProtocol: Optional[str]
    IpVersion: Optional[str]
    LoadBalancingScheme: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    NetworkTier: Optional[str]
    PortRange: Optional[str]
    Ports: Optional[Sequence[str]]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    ServiceLabel: Optional[str]
    ServiceName: Optional[str]
    Subnetwork: Optional[str]
    Target: Optional[str]
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
            AllPorts=json_data.get("AllPorts"),
            BackendService=json_data.get("BackendService"),
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IpProtocol=json_data.get("IpProtocol"),
            IpVersion=json_data.get("IpVersion"),
            LoadBalancingScheme=json_data.get("LoadBalancingScheme"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            NetworkTier=json_data.get("NetworkTier"),
            PortRange=json_data.get("PortRange"),
            Ports=json_data.get("Ports"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            ServiceLabel=json_data.get("ServiceLabel"),
            ServiceName=json_data.get("ServiceName"),
            Subnetwork=json_data.get("Subnetwork"),
            Target=json_data.get("Target"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


