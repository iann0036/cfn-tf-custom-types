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
    AuthorizedNetwork: Optional[str]
    CreateTime: Optional[str]
    DiscoveryEndpoint: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MemcacheFullVersion: Optional[str]
    MemcacheNodes: Optional[Sequence["_MemcacheNodesDefinition"]]
    MemcacheVersion: Optional[str]
    Name: Optional[str]
    NodeCount: Optional[float]
    Project: Optional[str]
    Region: Optional[str]
    Zones: Optional[Sequence[str]]
    MemcacheParameters: Optional[Sequence["_MemcacheParametersDefinition"]]
    NodeConfig: Optional[Sequence["_NodeConfigDefinition"]]
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
            AuthorizedNetwork=json_data.get("AuthorizedNetwork"),
            CreateTime=json_data.get("CreateTime"),
            DiscoveryEndpoint=json_data.get("DiscoveryEndpoint"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MemcacheFullVersion=json_data.get("MemcacheFullVersion"),
            MemcacheNodes=deserialize_list(json_data.get("MemcacheNodes"), MemcacheNodesDefinition),
            MemcacheVersion=json_data.get("MemcacheVersion"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Zones=json_data.get("Zones"),
            MemcacheParameters=deserialize_list(json_data.get("MemcacheParameters"), MemcacheParametersDefinition),
            NodeConfig=deserialize_list(json_data.get("NodeConfig"), NodeConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class MemcacheNodesDefinition(BaseModel):
    Host: Optional[str]
    NodeId: Optional[str]
    Port: Optional[float]
    State: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MemcacheNodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemcacheNodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            NodeId=json_data.get("NodeId"),
            Port=json_data.get("Port"),
            State=json_data.get("State"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemcacheNodesDefinition = MemcacheNodesDefinition


@dataclass
class MemcacheParametersDefinition(BaseModel):
    Params: Optional[Sequence["_ParamsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MemcacheParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MemcacheParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Params=deserialize_list(json_data.get("Params"), ParamsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MemcacheParametersDefinition = MemcacheParametersDefinition


@dataclass
class ParamsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamsDefinition = ParamsDefinition


@dataclass
class NodeConfigDefinition(BaseModel):
    CpuCount: Optional[float]
    MemorySizeMb: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CpuCount=json_data.get("CpuCount"),
            MemorySizeMb=json_data.get("MemorySizeMb"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDefinition = NodeConfigDefinition


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


