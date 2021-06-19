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
    ClusterId: Optional[str]
    DefaultProjectId: Optional[str]
    Id: Optional[str]
    KubeConfig: Optional[str]
    NodePoolIds: Optional[Sequence[str]]
    Nodes: Optional[Sequence["_NodesDefinition5"]]
    StateConfirm: Optional[float]
    Synced: Optional[bool]
    SystemProjectId: Optional[str]
    WaitAlerting: Optional[bool]
    WaitCatalogs: Optional[bool]
    WaitMonitoring: Optional[bool]
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
            ClusterId=json_data.get("ClusterId"),
            DefaultProjectId=json_data.get("DefaultProjectId"),
            Id=json_data.get("Id"),
            KubeConfig=json_data.get("KubeConfig"),
            NodePoolIds=json_data.get("NodePoolIds"),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition5),
            StateConfirm=json_data.get("StateConfirm"),
            Synced=json_data.get("Synced"),
            SystemProjectId=json_data.get("SystemProjectId"),
            WaitAlerting=json_data.get("WaitAlerting"),
            WaitCatalogs=json_data.get("WaitCatalogs"),
            WaitMonitoring=json_data.get("WaitMonitoring"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodesDefinition5(BaseModel):
    Annotations: Optional[Sequence["_NodesDefinition"]]
    Capacity: Optional[Sequence["_NodesDefinition2"]]
    ClusterId: Optional[str]
    ExternalIpAddress: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    Labels: Optional[Sequence["_NodesDefinition3"]]
    Name: Optional[str]
    NodePoolId: Optional[str]
    NodeTemplateId: Optional[str]
    ProviderId: Optional[str]
    RequestedHostname: Optional[str]
    Roles: Optional[Sequence[str]]
    SshUser: Optional[str]
    SystemInfo: Optional[Sequence["_NodesDefinition4"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition5"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition5"]:
        if not json_data:
            return None
        return cls(
            Annotations=deserialize_list(json_data.get("Annotations"), NodesDefinition),
            Capacity=deserialize_list(json_data.get("Capacity"), NodesDefinition2),
            ClusterId=json_data.get("ClusterId"),
            ExternalIpAddress=json_data.get("ExternalIpAddress"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Labels=deserialize_list(json_data.get("Labels"), NodesDefinition3),
            Name=json_data.get("Name"),
            NodePoolId=json_data.get("NodePoolId"),
            NodeTemplateId=json_data.get("NodeTemplateId"),
            ProviderId=json_data.get("ProviderId"),
            RequestedHostname=json_data.get("RequestedHostname"),
            Roles=json_data.get("Roles"),
            SshUser=json_data.get("SshUser"),
            SystemInfo=deserialize_list(json_data.get("SystemInfo"), NodesDefinition4),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition5 = NodesDefinition5


@dataclass
class NodesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class NodesDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition2 = NodesDefinition2


@dataclass
class NodesDefinition3(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition3"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition3 = NodesDefinition3


@dataclass
class NodesDefinition4(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition4"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition4"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition4 = NodesDefinition4


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


