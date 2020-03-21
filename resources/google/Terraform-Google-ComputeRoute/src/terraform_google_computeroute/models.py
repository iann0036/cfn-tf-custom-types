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
    Description: Optional[str]
    DestRange: Optional[str]
    Name: Optional[str]
    Network: Optional[str]
    NextHopGateway: Optional[str]
    NextHopIlb: Optional[str]
    NextHopInstance: Optional[str]
    NextHopInstanceZone: Optional[str]
    NextHopIp: Optional[str]
    NextHopNetwork: Optional[str]
    NextHopVpnTunnel: Optional[str]
    Priority: Optional[float]
    Project: Optional[str]
    SelfLink: Optional[str]
    Tags: Optional[Sequence[str]]
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
            Description=json_data.get("Description"),
            DestRange=json_data.get("DestRange"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            NextHopGateway=json_data.get("NextHopGateway"),
            NextHopIlb=json_data.get("NextHopIlb"),
            NextHopInstance=json_data.get("NextHopInstance"),
            NextHopInstanceZone=json_data.get("NextHopInstanceZone"),
            NextHopIp=json_data.get("NextHopIp"),
            NextHopNetwork=json_data.get("NextHopNetwork"),
            NextHopVpnTunnel=json_data.get("NextHopVpnTunnel"),
            Priority=json_data.get("Priority"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Tags=json_data.get("Tags"),
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


