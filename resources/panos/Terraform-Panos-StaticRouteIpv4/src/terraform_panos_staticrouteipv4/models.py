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
    AdminDistance: Optional[float]
    BfdProfile: Optional[str]
    Destination: Optional[str]
    Interface: Optional[str]
    Metric: Optional[float]
    Name: Optional[str]
    NextHop: Optional[str]
    RouteTable: Optional[str]
    Type: Optional[str]
    VirtualRouter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdminDistance=json_data.get("AdminDistance"),
            BfdProfile=json_data.get("BfdProfile"),
            Destination=json_data.get("Destination"),
            Interface=json_data.get("Interface"),
            Metric=json_data.get("Metric"),
            Name=json_data.get("Name"),
            NextHop=json_data.get("NextHop"),
            RouteTable=json_data.get("RouteTable"),
            Type=json_data.get("Type"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


