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
    EnableInboundForwarding: Optional[bool]
    EnableLogging: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    AlternativeNameServerConfig: Optional[Sequence["_AlternativeNameServerConfigDefinition"]]
    Networks: Optional[Sequence["_NetworksDefinition"]]
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
            EnableInboundForwarding=json_data.get("EnableInboundForwarding"),
            EnableLogging=json_data.get("EnableLogging"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            AlternativeNameServerConfig=deserialize_list(json_data.get("AlternativeNameServerConfig"), AlternativeNameServerConfigDefinition),
            Networks=deserialize_list(json_data.get("Networks"), NetworksDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AlternativeNameServerConfigDefinition(BaseModel):
    TargetNameServers: Optional[Sequence["_TargetNameServersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AlternativeNameServerConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlternativeNameServerConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetNameServers=deserialize_list(json_data.get("TargetNameServers"), TargetNameServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlternativeNameServerConfigDefinition = AlternativeNameServerConfigDefinition


@dataclass
class TargetNameServersDefinition(BaseModel):
    ForwardingPath: Optional[str]
    Ipv4Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetNameServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetNameServersDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardingPath=json_data.get("ForwardingPath"),
            Ipv4Address=json_data.get("Ipv4Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetNameServersDefinition = TargetNameServersDefinition


@dataclass
class NetworksDefinition(BaseModel):
    NetworkUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkUrl=json_data.get("NetworkUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksDefinition = NetworksDefinition


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


