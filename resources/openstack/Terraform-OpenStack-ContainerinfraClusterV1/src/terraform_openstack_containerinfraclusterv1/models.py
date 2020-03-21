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
    ApiAddress: Optional[str]
    ClusterTemplateId: Optional[str]
    CoeVersion: Optional[str]
    ContainerVersion: Optional[str]
    CreateTimeout: Optional[float]
    CreatedAt: Optional[str]
    DiscoveryUrl: Optional[str]
    DockerVolumeSize: Optional[float]
    FixedNetwork: Optional[str]
    FixedSubnet: Optional[str]
    Flavor: Optional[str]
    Id: Optional[str]
    Keypair: Optional[str]
    Labels: Optional[Sequence["_Labels"]]
    MasterAddresses: Optional[str]
    MasterCount: Optional[float]
    MasterFlavor: Optional[str]
    Name: Optional[str]
    NodeAddresses: Optional[str]
    NodeCount: Optional[float]
    ProjectId: Optional[str]
    Region: Optional[str]
    StackId: Optional[str]
    UpdatedAt: Optional[str]
    UserId: Optional[str]
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
            ApiAddress=json_data.get("ApiAddress"),
            ClusterTemplateId=json_data.get("ClusterTemplateId"),
            CoeVersion=json_data.get("CoeVersion"),
            ContainerVersion=json_data.get("ContainerVersion"),
            CreateTimeout=json_data.get("CreateTimeout"),
            CreatedAt=json_data.get("CreatedAt"),
            DiscoveryUrl=json_data.get("DiscoveryUrl"),
            DockerVolumeSize=json_data.get("DockerVolumeSize"),
            FixedNetwork=json_data.get("FixedNetwork"),
            FixedSubnet=json_data.get("FixedSubnet"),
            Flavor=json_data.get("Flavor"),
            Id=json_data.get("Id"),
            Keypair=json_data.get("Keypair"),
            Labels=json_data.get("Labels"),
            MasterAddresses=json_data.get("MasterAddresses"),
            MasterCount=json_data.get("MasterCount"),
            MasterFlavor=json_data.get("MasterFlavor"),
            Name=json_data.get("Name"),
            NodeAddresses=json_data.get("NodeAddresses"),
            NodeCount=json_data.get("NodeCount"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            StackId=json_data.get("StackId"),
            UpdatedAt=json_data.get("UpdatedAt"),
            UserId=json_data.get("UserId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
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


