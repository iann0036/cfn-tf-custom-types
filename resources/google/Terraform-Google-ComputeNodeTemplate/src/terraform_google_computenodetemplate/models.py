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
    Id: Optional[str]
    Name: Optional[str]
    NodeAffinityLabels: Optional[Sequence["_NodeAffinityLabels"]]
    NodeType: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    SelfLink: Optional[str]
    NodeTypeFlexibility: Optional[Sequence["_NodeTypeFlexibility"]]
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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NodeAffinityLabels=json_data.get("NodeAffinityLabels"),
            NodeType=json_data.get("NodeType"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            SelfLink=json_data.get("SelfLink"),
            NodeTypeFlexibility=json_data.get("NodeTypeFlexibility"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeAffinityLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeAffinityLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeAffinityLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeAffinityLabels = NodeAffinityLabels


@dataclass
class NodeTypeFlexibility:
    Cpus: Optional[str]
    Memory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeTypeFlexibility"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeTypeFlexibility"]:
        if not json_data:
            return None
        return cls(
            Cpus=json_data.get("Cpus"),
            Memory=json_data.get("Memory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeTypeFlexibility = NodeTypeFlexibility


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


