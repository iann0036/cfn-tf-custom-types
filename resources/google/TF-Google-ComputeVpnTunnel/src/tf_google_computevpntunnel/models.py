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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DetailedStatus: Optional[str]
    Id: Optional[str]
    IkeVersion: Optional[float]
    LocalTrafficSelector: Optional[Sequence[str]]
    Name: Optional[str]
    PeerExternalGateway: Optional[str]
    PeerExternalGatewayInterface: Optional[float]
    PeerGcpGateway: Optional[str]
    PeerIp: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    RemoteTrafficSelector: Optional[Sequence[str]]
    Router: Optional[str]
    SelfLink: Optional[str]
    SharedSecret: Optional[str]
    SharedSecretHash: Optional[str]
    TargetVpnGateway: Optional[str]
    TunnelId: Optional[str]
    VpnGateway: Optional[str]
    VpnGatewayInterface: Optional[float]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DetailedStatus=json_data.get("DetailedStatus"),
            Id=json_data.get("Id"),
            IkeVersion=json_data.get("IkeVersion"),
            LocalTrafficSelector=json_data.get("LocalTrafficSelector"),
            Name=json_data.get("Name"),
            PeerExternalGateway=json_data.get("PeerExternalGateway"),
            PeerExternalGatewayInterface=json_data.get("PeerExternalGatewayInterface"),
            PeerGcpGateway=json_data.get("PeerGcpGateway"),
            PeerIp=json_data.get("PeerIp"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            RemoteTrafficSelector=json_data.get("RemoteTrafficSelector"),
            Router=json_data.get("Router"),
            SelfLink=json_data.get("SelfLink"),
            SharedSecret=json_data.get("SharedSecret"),
            SharedSecretHash=json_data.get("SharedSecretHash"),
            TargetVpnGateway=json_data.get("TargetVpnGateway"),
            TunnelId=json_data.get("TunnelId"),
            VpnGateway=json_data.get("VpnGateway"),
            VpnGatewayInterface=json_data.get("VpnGatewayInterface"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


