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
    CreatedAt: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ManagerNodeSpuNum: Optional[float]
    MaxSpuNum: Optional[float]
    Name: Optional[str]
    SubnetCidr: Optional[str]
    SubnetGateway: Optional[str]
    UsedSpuNum: Optional[float]
    VpcCidr: Optional[str]
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
            CreatedAt=json_data.get("CreatedAt"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ManagerNodeSpuNum=json_data.get("ManagerNodeSpuNum"),
            MaxSpuNum=json_data.get("MaxSpuNum"),
            Name=json_data.get("Name"),
            SubnetCidr=json_data.get("SubnetCidr"),
            SubnetGateway=json_data.get("SubnetGateway"),
            UsedSpuNum=json_data.get("UsedSpuNum"),
            VpcCidr=json_data.get("VpcCidr"),
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


