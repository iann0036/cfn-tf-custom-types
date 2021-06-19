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
    Description: Optional[str]
    DestRange: Optional[str]
    Id: Optional[str]
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
            Description=json_data.get("Description"),
            DestRange=json_data.get("DestRange"),
            Id=json_data.get("Id"),
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


