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
    DisplayName: Optional[str]
    Id: Optional[str]
    InstanceType: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Cluster: Optional[Sequence["_Cluster"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            InstanceType=json_data.get("InstanceType"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Cluster=json_data.get("Cluster"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Cluster:
    ClusterId: Optional[str]
    NumNodes: Optional[float]
    StorageType: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Cluster"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Cluster"]:
        if not json_data:
            return None
        return cls(
            ClusterId=json_data.get("ClusterId"),
            NumNodes=json_data.get("NumNodes"),
            StorageType=json_data.get("StorageType"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Cluster = Cluster


