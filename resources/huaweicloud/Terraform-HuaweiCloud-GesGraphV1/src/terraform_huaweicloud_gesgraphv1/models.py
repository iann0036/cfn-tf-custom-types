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
    AutoAssign: Optional[bool]
    AvailabilityZone: Optional[str]
    Created: Optional[str]
    EdgesetPath: Optional[Sequence["_EdgesetPath"]]
    EipId: Optional[str]
    GraphSizeType: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrivateIp: Optional[str]
    PublicIp: Optional[str]
    Region: Optional[str]
    SchemaPath: Optional[Sequence["_SchemaPath"]]
    SecurityGroupId: Optional[str]
    SubnetId: Optional[str]
    Version: Optional[str]
    VertexsetPath: Optional[Sequence["_VertexsetPath"]]
    VpcId: Optional[str]
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
            AutoAssign=json_data.get("AutoAssign"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Created=json_data.get("Created"),
            EdgesetPath=json_data.get("EdgesetPath"),
            EipId=json_data.get("EipId"),
            GraphSizeType=json_data.get("GraphSizeType"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrivateIp=json_data.get("PrivateIp"),
            PublicIp=json_data.get("PublicIp"),
            Region=json_data.get("Region"),
            SchemaPath=json_data.get("SchemaPath"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SubnetId=json_data.get("SubnetId"),
            Version=json_data.get("Version"),
            VertexsetPath=json_data.get("VertexsetPath"),
            VpcId=json_data.get("VpcId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EdgesetPath:
    Path: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EdgesetPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EdgesetPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EdgesetPath = EdgesetPath


@dataclass
class SchemaPath:
    Path: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SchemaPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SchemaPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SchemaPath = SchemaPath


@dataclass
class VertexsetPath:
    Path: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VertexsetPath"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VertexsetPath"]:
        if not json_data:
            return None
        return cls(
            Path=json_data.get("Path"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VertexsetPath = VertexsetPath


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


