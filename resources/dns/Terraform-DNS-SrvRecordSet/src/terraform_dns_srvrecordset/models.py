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
    Name: Optional[str]
    Ttl: Optional[float]
    Zone: Optional[str]
    Srv: Optional[Sequence["_Srv"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            Ttl=json_data.get("Ttl"),
            Zone=json_data.get("Zone"),
            Srv=json_data.get("Srv"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Srv:
    Port: Optional[float]
    Priority: Optional[float]
    Target: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Srv"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Srv"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Target=json_data.get("Target"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Srv = Srv


