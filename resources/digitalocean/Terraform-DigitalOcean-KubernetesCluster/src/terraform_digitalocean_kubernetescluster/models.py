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
    ClusterSubnet: Optional[str]
    CreatedAt: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    Ipv4Address: Optional[str]
    KubeConfig: Optional[Sequence["_KubeConfig"]]
    Name: Optional[str]
    Region: Optional[str]
    ServiceSubnet: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    Version: Optional[str]
    NodePool: Optional[Sequence["_NodePool"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterSubnet=json_data.get("ClusterSubnet"),
            CreatedAt=json_data.get("CreatedAt"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Ipv4Address=json_data.get("Ipv4Address"),
            KubeConfig=json_data.get("KubeConfig"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ServiceSubnet=json_data.get("ServiceSubnet"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Version=json_data.get("Version"),
            NodePool=json_data.get("NodePool"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeConfig:
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    ExpiresAt: Optional[str]
    Host: Optional[str]
    RawConfig: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeConfig"]:
        if not json_data:
            return None
        return cls(
            ClientCertificate=json_data.get("ClientCertificate"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCertificate=json_data.get("ClusterCaCertificate"),
            ExpiresAt=json_data.get("ExpiresAt"),
            Host=json_data.get("Host"),
            RawConfig=json_data.get("RawConfig"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KubeConfig = KubeConfig


@dataclass
class NodePool:
    AutoScale: Optional[bool]
    Labels: Optional[Sequence["_Labels"]]
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    Size: Optional[str]
    Tags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_NodePool"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePool"]:
        if not json_data:
            return None
        return cls(
            AutoScale=json_data.get("AutoScale"),
            Labels=json_data.get("Labels"),
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePool = NodePool


@dataclass
class Labels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Labels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Labels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Labels = Labels


