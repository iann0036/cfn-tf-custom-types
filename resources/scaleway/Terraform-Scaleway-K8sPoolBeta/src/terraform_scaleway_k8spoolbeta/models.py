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
    Autohealing: Optional[bool]
    Autoscaling: Optional[bool]
    ClusterId: Optional[str]
    ContainerRuntime: Optional[str]
    CreatedAt: Optional[str]
    Id: Optional[str]
    MaxSize: Optional[float]
    MinSize: Optional[float]
    Name: Optional[str]
    NodeType: Optional[str]
    Nodes: Optional[Sequence["_Nodes"]]
    PlacementGroupId: Optional[str]
    Region: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    Version: Optional[str]
    WaitForPoolReady: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Autohealing=json_data.get("Autohealing"),
            Autoscaling=json_data.get("Autoscaling"),
            ClusterId=json_data.get("ClusterId"),
            ContainerRuntime=json_data.get("ContainerRuntime"),
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            MaxSize=json_data.get("MaxSize"),
            MinSize=json_data.get("MinSize"),
            Name=json_data.get("Name"),
            NodeType=json_data.get("NodeType"),
            Nodes=json_data.get("Nodes"),
            PlacementGroupId=json_data.get("PlacementGroupId"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Version=json_data.get("Version"),
            WaitForPoolReady=json_data.get("WaitForPoolReady"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Nodes:
    Name: Optional[str]
    PublicIp: Optional[str]
    PublicIpV6: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpV6=json_data.get("PublicIpV6"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


