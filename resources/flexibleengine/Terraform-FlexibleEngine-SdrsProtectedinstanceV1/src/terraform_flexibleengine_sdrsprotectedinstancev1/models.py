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
    DeleteTargetEip: Optional[bool]
    DeleteTargetServer: Optional[bool]
    Description: Optional[str]
    GroupId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PrimaryIpAddress: Optional[str]
    PrimarySubnetId: Optional[str]
    ServerId: Optional[str]
    TargetServer: Optional[str]
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
            ClusterId=json_data.get("ClusterId"),
            DeleteTargetEip=json_data.get("DeleteTargetEip"),
            DeleteTargetServer=json_data.get("DeleteTargetServer"),
            Description=json_data.get("Description"),
            GroupId=json_data.get("GroupId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PrimaryIpAddress=json_data.get("PrimaryIpAddress"),
            PrimarySubnetId=json_data.get("PrimarySubnetId"),
            ServerId=json_data.get("ServerId"),
            TargetServer=json_data.get("TargetServer"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


