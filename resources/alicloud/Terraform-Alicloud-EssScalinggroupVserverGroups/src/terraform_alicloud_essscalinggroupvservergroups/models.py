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
    Force: Optional[bool]
    ScalingGroupId: Optional[str]
    VserverGroups: Optional[Sequence["_VserverGroups"]]
    VserverAttributes: Optional[Sequence["_VserverAttributes"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Force=json_data.get("Force"),
            ScalingGroupId=json_data.get("ScalingGroupId"),
            VserverGroups=json_data.get("VserverGroups"),
            VserverAttributes=json_data.get("VserverAttributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VserverGroups:
    LoadbalancerId: Optional[str]
    VserverAttributes: Optional[Sequence["_VserverAttributes"]]

    @classmethod
    def _deserialize(
        cls: Type["_VserverGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VserverGroups"]:
        if not json_data:
            return None
        return cls(
            LoadbalancerId=json_data.get("LoadbalancerId"),
            VserverAttributes=json_data.get("VserverAttributes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VserverGroups = VserverGroups


@dataclass
class VserverAttributes:
    Port: Optional[float]
    VserverGroupId: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_VserverAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VserverAttributes"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            VserverGroupId=json_data.get("VserverGroupId"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VserverAttributes = VserverAttributes


