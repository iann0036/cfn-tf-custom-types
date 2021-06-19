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
    Description: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    LastKnownPort: Optional[str]
    LastKnownSwitch: Optional[str]
    LastSeen: Optional[float]
    Mac: Optional[str]
    MacPolicy: Optional[str]
    MatchedNacPolicy: Optional[str]
    PortPolicy: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]

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
            Description=json_data.get("Description"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            LastKnownPort=json_data.get("LastKnownPort"),
            LastKnownSwitch=json_data.get("LastKnownSwitch"),
            LastSeen=json_data.get("LastSeen"),
            Mac=json_data.get("Mac"),
            MacPolicy=json_data.get("MacPolicy"),
            MatchedNacPolicy=json_data.get("MatchedNacPolicy"),
            PortPolicy=json_data.get("PortPolicy"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


