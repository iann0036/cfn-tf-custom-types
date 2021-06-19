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
    Force: Optional[bool]
    Id: Optional[str]
    ScalingGroupId: Optional[str]
    VserverGroups: Optional[Sequence["_VserverGroupsDefinition"]]

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
            Force=json_data.get("Force"),
            Id=json_data.get("Id"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            VserverGroups=deserialize_list(json_data.get("VserverGroups"), VserverGroupsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VserverGroupsDefinition(BaseModel):
    LoadbalancerId: Optional[str]
    VserverAttributes: Optional[Sequence["_VserverAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_VserverGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VserverGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            LoadbalancerId=json_data.get("LoadbalancerId"),
            VserverAttributes=deserialize_list(json_data.get("VserverAttributes"), VserverAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_VserverGroupsDefinition = VserverGroupsDefinition


@dataclass
class VserverAttributesDefinition(BaseModel):
    Port: Optional[float]
    VserverGroupId: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VserverAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VserverAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            VserverGroupId=json_data.get("VserverGroupId"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VserverAttributesDefinition = VserverAttributesDefinition


