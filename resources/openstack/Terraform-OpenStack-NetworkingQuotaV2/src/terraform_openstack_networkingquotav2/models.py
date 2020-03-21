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
    Floatingip: Optional[float]
    Network: Optional[float]
    Port: Optional[float]
    ProjectId: Optional[str]
    RbacPolicy: Optional[float]
    Region: Optional[str]
    Router: Optional[float]
    SecurityGroup: Optional[float]
    SecurityGroupRule: Optional[float]
    Subnet: Optional[float]
    Subnetpool: Optional[float]
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
            Floatingip=json_data.get("Floatingip"),
            Network=json_data.get("Network"),
            Port=json_data.get("Port"),
            ProjectId=json_data.get("ProjectId"),
            RbacPolicy=json_data.get("RbacPolicy"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            SecurityGroup=json_data.get("SecurityGroup"),
            SecurityGroupRule=json_data.get("SecurityGroupRule"),
            Subnet=json_data.get("Subnet"),
            Subnetpool=json_data.get("Subnetpool"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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


