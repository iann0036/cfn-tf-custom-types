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
    AutoUpgrade: Optional[bool]
    ClusterSubnet: Optional[str]
    CreatedAt: Optional[str]
    Endpoint: Optional[str]
    Id: Optional[str]
    Ipv4Address: Optional[str]
    KubeConfig: Optional[Sequence["_KubeConfigDefinition"]]
    Name: Optional[str]
    Region: Optional[str]
    ServiceSubnet: Optional[str]
    Status: Optional[str]
    SurgeUpgrade: Optional[bool]
    Tags: Optional[Sequence[str]]
    UpdatedAt: Optional[str]
    Urn: Optional[str]
    Version: Optional[str]
    VpcUuid: Optional[str]
    NodePool: Optional[Sequence["_NodePoolDefinition"]]

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
            AutoUpgrade=json_data.get("AutoUpgrade"),
            ClusterSubnet=json_data.get("ClusterSubnet"),
            CreatedAt=json_data.get("CreatedAt"),
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Ipv4Address=json_data.get("Ipv4Address"),
            KubeConfig=deserialize_list(json_data.get("KubeConfig"), KubeConfigDefinition),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            ServiceSubnet=json_data.get("ServiceSubnet"),
            Status=json_data.get("Status"),
            SurgeUpgrade=json_data.get("SurgeUpgrade"),
            Tags=json_data.get("Tags"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Urn=json_data.get("Urn"),
            Version=json_data.get("Version"),
            VpcUuid=json_data.get("VpcUuid"),
            NodePool=deserialize_list(json_data.get("NodePool"), NodePoolDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class KubeConfigDefinition(BaseModel):
    ClientCertificate: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCertificate: Optional[str]
    ExpiresAt: Optional[str]
    Host: Optional[str]
    RawConfig: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KubeConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KubeConfigDefinition"]:
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
_KubeConfigDefinition = KubeConfigDefinition


@dataclass
class NodePoolDefinition(BaseModel):
    AutoScale: Optional[bool]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    MaxNodes: Optional[float]
    MinNodes: Optional[float]
    Name: Optional[str]
    NodeCount: Optional[float]
    Size: Optional[str]
    Tags: Optional[Sequence[str]]
    Taint: Optional[Sequence["_TaintDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NodePoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodePoolDefinition"]:
        if not json_data:
            return None
        return cls(
            AutoScale=json_data.get("AutoScale"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            MaxNodes=json_data.get("MaxNodes"),
            MinNodes=json_data.get("MinNodes"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
            Taint=deserialize_list(json_data.get("Taint"), TaintDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodePoolDefinition = NodePoolDefinition


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
class TaintDefinition(BaseModel):
    Effect: Optional[str]
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TaintDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TaintDefinition"]:
        if not json_data:
            return None
        return cls(
            Effect=json_data.get("Effect"),
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TaintDefinition = TaintDefinition


