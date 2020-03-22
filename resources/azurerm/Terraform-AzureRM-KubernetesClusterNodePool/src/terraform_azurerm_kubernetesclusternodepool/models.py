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
    AvailabilityZones: Optional[Sequence[str]]
    EnableAutoScaling: Optional[bool]
    EnableNodePublicIp: Optional[bool]
    Id: Optional[str]
    KubernetesClusterId: Optional[str]
    MaxCount: Optional[float]
    MaxPods: Optional[float]
    MinCount: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    NodeLabels: Optional[Sequence["_NodeLabels"]]
    NodeTaints: Optional[Sequence[str]]
    OsDiskSizeGb: Optional[float]
    OsType: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    VmSize: Optional[str]
    VnetSubnetId: Optional[str]
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
            AvailabilityZones=json_data.get("AvailabilityZones"),
            EnableAutoScaling=json_data.get("EnableAutoScaling"),
            EnableNodePublicIp=json_data.get("EnableNodePublicIp"),
            Id=json_data.get("Id"),
            KubernetesClusterId=json_data.get("KubernetesClusterId"),
            MaxCount=json_data.get("MaxCount"),
            MaxPods=json_data.get("MaxPods"),
            MinCount=json_data.get("MinCount"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            NodeLabels=json_data.get("NodeLabels"),
            NodeTaints=json_data.get("NodeTaints"),
            OsDiskSizeGb=json_data.get("OsDiskSizeGb"),
            OsType=json_data.get("OsType"),
            Tags=json_data.get("Tags"),
            VmSize=json_data.get("VmSize"),
            VnetSubnetId=json_data.get("VnetSubnetId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeLabels = NodeLabels


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


