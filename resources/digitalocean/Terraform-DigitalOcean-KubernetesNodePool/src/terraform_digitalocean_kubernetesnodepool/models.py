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
    ActualNodeCount: Optional[float]
    AutoScale: Optional[bool]
    ClusterId: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    Nodes: Optional[Sequence["_Nodes"]]
    Size: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ActualNodeCount=json_data.get("ActualNodeCount"),
            AutoScale=json_data.get("AutoScale"),
            ClusterId=json_data.get("ClusterId"),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Nodes=json_data.get("Nodes"),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Labels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


@dataclass
class Nodes:
    CreatedAt: Optional[str]
    DropletId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            DropletId=json_data.get("DropletId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


