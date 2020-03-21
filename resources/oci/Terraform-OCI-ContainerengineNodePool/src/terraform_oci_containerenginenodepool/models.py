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
    ClusterId: Optional[str]
    CompartmentId: Optional[str]
    KubernetesVersion: Optional[str]
    Name: Optional[str]
    NodeImageId: Optional[str]
    NodeImageName: Optional[str]
    NodeMetadata: Optional[Sequence["_NodeMetadata"]]
    NodeShape: Optional[str]
    NodeSource: Optional[Sequence["_NodeSource"]]
    Nodes: Optional[Sequence["_Nodes"]]
    QuantityPerSubnet: Optional[float]
    SshPublicKey: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    InitialNodeLabels: Optional[Sequence["_InitialNodeLabels"]]
    NodeConfigDetails: Optional[Sequence["_NodeConfigDetails"]]
    NodeSourceDetails: Optional[Sequence["_NodeSourceDetails"]]
    Timeouts: Optional["_Timeouts"]
    PlacementConfigs: Optional[Sequence["_PlacementConfigs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterId=json_data.get("ClusterId"),
            CompartmentId=json_data.get("CompartmentId"),
            KubernetesVersion=json_data.get("KubernetesVersion"),
            Name=json_data.get("Name"),
            NodeImageId=json_data.get("NodeImageId"),
            NodeImageName=json_data.get("NodeImageName"),
            NodeMetadata=json_data.get("NodeMetadata"),
            NodeShape=json_data.get("NodeShape"),
            NodeSource=json_data.get("NodeSource"),
            Nodes=json_data.get("Nodes"),
            QuantityPerSubnet=json_data.get("QuantityPerSubnet"),
            SshPublicKey=json_data.get("SshPublicKey"),
            SubnetIds=json_data.get("SubnetIds"),
            InitialNodeLabels=json_data.get("InitialNodeLabels"),
            NodeConfigDetails=json_data.get("NodeConfigDetails"),
            NodeSourceDetails=json_data.get("NodeSourceDetails"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            PlacementConfigs=json_data.get("PlacementConfigs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NodeMetadata:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeMetadata"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeMetadata"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeMetadata = NodeMetadata


@dataclass
class NodeSource:
    ImageId: Optional[str]
    SourceName: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSource"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSource"]:
        if not json_data:
            return None
        return cls(
            ImageId=json_data.get("ImageId"),
            SourceName=json_data.get("SourceName"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSource = NodeSource


@dataclass
class Nodes:
    AvailabilityDomain: Optional[str]
    Error: Optional[Sequence["_Error"]]
    FaultDomain: Optional[str]
    Id: Optional[str]
    LifecycleDetails: Optional[str]
    Name: Optional[str]
    NodePoolId: Optional[str]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    State: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Nodes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Nodes"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            Error=json_data.get("Error"),
            FaultDomain=json_data.get("FaultDomain"),
            Id=json_data.get("Id"),
            LifecycleDetails=json_data.get("LifecycleDetails"),
            Name=json_data.get("Name"),
            NodePoolId=json_data.get("NodePoolId"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            State=json_data.get("State"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Nodes = Nodes


@dataclass
class Error:
    Code: Optional[str]
    Message: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Error"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Error"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Message=json_data.get("Message"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Error = Error


@dataclass
class InitialNodeLabels:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InitialNodeLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InitialNodeLabels"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InitialNodeLabels = InitialNodeLabels


@dataclass
class NodeConfigDetails:
    Size: Optional[float]
    PlacementConfigs: Optional[Sequence["_PlacementConfigs"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodeConfigDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeConfigDetails"]:
        if not json_data:
            return None
        return cls(
            Size=json_data.get("Size"),
            PlacementConfigs=json_data.get("PlacementConfigs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeConfigDetails = NodeConfigDetails


@dataclass
class PlacementConfigs:
    AvailabilityDomain: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlacementConfigs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlacementConfigs"]:
        if not json_data:
            return None
        return cls(
            AvailabilityDomain=json_data.get("AvailabilityDomain"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlacementConfigs = PlacementConfigs


@dataclass
class NodeSourceDetails:
    ImageId: Optional[str]
    SourceType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeSourceDetails"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeSourceDetails"]:
        if not json_data:
            return None
        return cls(
            ImageId=json_data.get("ImageId"),
            SourceType=json_data.get("SourceType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeSourceDetails = NodeSourceDetails


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


