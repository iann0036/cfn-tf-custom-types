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
    CompartmentId: Optional[str]
    Id: Optional[str]
    KubernetesVersion: Optional[str]
    Name: Optional[str]
    NodeImageId: Optional[str]
    NodeImageName: Optional[str]
    NodeMetadata: Optional[Sequence["_NodeMetadataDefinition"]]
    NodeShape: Optional[str]
    NodeSource: Optional[Sequence["_NodeSourceDefinition"]]
    Nodes: Optional[Sequence["_NodesDefinition2"]]
    QuantityPerSubnet: Optional[float]
    SshPublicKey: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    InitialNodeLabels: Optional[Sequence["_InitialNodeLabelsDefinition"]]
    NodeConfigDetails: Optional[Sequence["_NodeConfigDetailsDefinition"]]
    NodeShapeConfig: Optional[Sequence["_NodeShapeConfigDefinition"]]
    NodeSourceDetails: Optional[Sequence["_NodeSourceDetailsDefinition"]]
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
            CompartmentId=json_data.get("CompartmentId"),
            Id=json_data.get("Id"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            Name=json_data.get("Name"),
            NodeImageId=json_data.get("NodeImageId"),
            NodeImageName=json_data.get("NodeImageName"),
            NodeMetadata=deserialize_list(json_data.get("NodeMetadata"), NodeMetadataDefinition),
            NodeShape=json_data.get("NodeShape"),
            NodeSource=deserialize_list(json_data.get("NodeSource"), NodeSourceDefinition),
            Nodes=deserialize_list(json_data.get("Nodes"), NodesDefinition2),
            QuantityPerSubnet=json_data.get("QuantityPerSubnet"),
            SshPublicKey=json_data.get("SshPublicKey"),
            SubnetIds=json_data.get("SubnetIds"),
            InitialNodeLabels=deserialize_list(json_data.get("InitialNodeLabels"), InitialNodeLabelsDefinition),
            NodeConfigDetails=deserialize_list(json_data.get("NodeConfigDetails"), NodeConfigDetailsDefinition),
            NodeShapeConfig=deserialize_list(json_data.get("NodeShapeConfig"), NodeShapeConfigDefinition),
            NodeSourceDetails=deserialize_list(json_data.get("NodeSourceDetails"), NodeSourceDetailsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeMetadataDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeMetadataDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeMetadataDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeMetadataDefinition = NodeMetadataDefinition


@dataclass
class NodeSourceDefinition(BaseModel):
    ImageId: Optional[str]
    SourceName: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSourceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSourceDefinition"]:
        if not json_data:
            return None
        return cls(
            ImageId=json_data.get("ImageId"),
            SourceName=json_data.get("SourceName"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSourceDefinition = NodeSourceDefinition


@dataclass
class NodesDefinition2(BaseModel):
    AvailabilityDomain: Optional[str]
    Error: Optional[Sequence["_NodesDefinition"]]
    FaultDomain: Optional[str]
    Id: Optional[str]
    KubernetesVersion: Optional[str]
    LifecycleDetails: Optional[str]
    Name: Optional[str]
    NodePoolId: Optional[str]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition2"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            Error=deserialize_list(json_data.get("Error"), NodesDefinition),
            FaultDomain=json_data.get("FaultDomain"),
            Id=json_data.get("Id"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Name=json_data.get("Name"),
            NodePoolId=json_data.get("NodePoolId"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition2 = NodesDefinition2


@dataclass
class NodesDefinition(BaseModel):
    Code: Optional[str]
    Message: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodesDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Message=json_data.get("Message"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodesDefinition = NodesDefinition


@dataclass
class InitialNodeLabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialNodeLabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialNodeLabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialNodeLabelsDefinition = InitialNodeLabelsDefinition


@dataclass
class NodeConfigDetailsDefinition(BaseModel):
    Size: Optional[float]
    PlacementConfigs: Optional[Sequence["_PlacementConfigsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            PlacementConfigs=deserialize_list(json_data.get("PlacementConfigs"), PlacementConfigsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDetailsDefinition = NodeConfigDetailsDefinition


@dataclass
class PlacementConfigsDefinition(BaseModel):
    AvailabilityDomain: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConfigsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConfigsDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConfigsDefinition = PlacementConfigsDefinition


@dataclass
class NodeShapeConfigDefinition(BaseModel):
    MemoryInGbs: Optional[float]
    Ocpus: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NodeShapeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeShapeConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            MemoryInGbs=json_data.get("MemoryInGbs"),
            Ocpus=json_data.get("Ocpus"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeShapeConfigDefinition = NodeShapeConfigDefinition


@dataclass
class NodeSourceDetailsDefinition(BaseModel):
    BootVolumeSizeInGbs: Optional[str]
    ImageId: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSourceDetailsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSourceDetailsDefinition"]:
        if not json_data:
            return None
        return cls(
            BootVolumeSizeInGbs=json_data.get("BootVolumeSizeInGbs"),
            ImageId=json_data.get("ImageId"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSourceDetailsDefinition = NodeSourceDetailsDefinition


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


