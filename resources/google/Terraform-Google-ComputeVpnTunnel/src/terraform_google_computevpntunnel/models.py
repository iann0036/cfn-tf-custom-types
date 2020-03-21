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
    CreationTimestamp: Optional[str]
    Description: Optional[str]
    DetailedStatus: Optional[str]
    IkeVersion: Optional[float]
    LocalTrafficSelector: Optional[Sequence[str]]
    Name: Optional[str]
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
            CreationTimestamp=json_data.get("CreationTimestamp"),
            Description=json_data.get("Description"),
            DetailedStatus=json_data.get("DetailedStatus"),
            IkeVersion=json_data.get("IkeVersion"),
            LocalTrafficSelector=json_data.get("LocalTrafficSelector"),
            Name=json_data.get("Name"),
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
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


