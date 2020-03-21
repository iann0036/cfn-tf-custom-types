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
    AllowNat: Optional[str]
    AllowSnat: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    LoadBalancingMode: Optional[str]
    Monitors: Optional[Sequence[str]]
    Name: Optional[str]
    ReselectTries: Optional[float]
    ServiceDownAction: Optional[str]
    SlowRampTime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowNat=json_data.get("AllowNat"),
            AllowSnat=json_data.get("AllowSnat"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LoadBalancingMode=json_data.get("LoadBalancingMode"),
            Monitors=json_data.get("Monitors"),
            Name=json_data.get("Name"),
            ReselectTries=json_data.get("ReselectTries"),
            ServiceDownAction=json_data.get("ServiceDownAction"),
            SlowRampTime=json_data.get("SlowRampTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


