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
    ChangeTime: Optional[str]
    CreateTime: Optional[str]
    Id: Optional[str]
    Kubeconfig: Optional[str]
    Labels: Optional[Sequence[str]]
    ListenPort: Optional[Sequence["_ListenPortDefinition"]]
    Name: Optional[str]
    NetworkUuid: Optional[str]
    Release: Optional[str]
    SecurityZoneUuid: Optional[str]
    ServiceTemplateUuid: Optional[str]
    Status: Optional[str]
    UsageInMinutes: Optional[float]
    NodePool: Optional[Sequence["_NodePoolDefinition"]]
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
            ChangeTime=json_data.get("ChangeTime"),
            CreateTime=json_data.get("CreateTime"),
            Id=json_data.get("Id"),
            Kubeconfig=json_data.get("Kubeconfig"),
            Labels=json_data.get("Labels"),
            ListenPort=deserialize_list(json_data.get("ListenPort"), ListenPortDefinition),
            Name=json_data.get("Name"),
            NetworkUuid=json_data.get("NetworkUuid"),
            Release=json_data.get("Release"),
            SecurityZoneUuid=json_data.get("SecurityZoneUuid"),
            ServiceTemplateUuid=json_data.get("ServiceTemplateUuid"),
            Status=json_data.get("Status"),
            UsageInMinutes=json_data.get("UsageInMinutes"),
            NodePool=deserialize_list(json_data.get("NodePool"), NodePoolDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ListenPortDefinition(BaseModel):
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ListenPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenPortDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenPortDefinition = ListenPortDefinition


@dataclass
class NodePoolDefinition(BaseModel):
    Cores: Optional[float]
    Memory: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    Storage: Optional[float]
    StorageType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Cores=json_data.get("Cores"),
            Memory=json_data.get("Memory"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Storage=json_data.get("Storage"),
            StorageType=json_data.get("StorageType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePoolDefinition = NodePoolDefinition


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


