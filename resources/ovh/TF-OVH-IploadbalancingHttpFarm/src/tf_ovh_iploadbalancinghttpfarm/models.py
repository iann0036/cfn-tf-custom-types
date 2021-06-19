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
    Balance: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Port: Optional[float]
    ServiceName: Optional[str]
    Stickiness: Optional[str]
    VrackNetworkId: Optional[float]
    Zone: Optional[str]
    Probe: Optional[Sequence["_ProbeDefinition"]]

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
            Balance=json_data.get("Balance"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            ServiceName=json_data.get("ServiceName"),
            Stickiness=json_data.get("Stickiness"),
            VrackNetworkId=json_data.get("VrackNetworkId"),
            Zone=json_data.get("Zone"),
            Probe=deserialize_list(json_data.get("Probe"), ProbeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ProbeDefinition(BaseModel):
    ForceSsl: Optional[bool]
    Interval: Optional[float]
    Match: Optional[str]
    Method: Optional[str]
    Negate: Optional[bool]
    Pattern: Optional[str]
    Port: Optional[float]
    Type: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProbeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProbeDefinition"]:
        if not json_data:
            return None
        return cls(
            ForceSsl=json_data.get("ForceSsl"),
            Interval=json_data.get("Interval"),
            Match=json_data.get("Match"),
            Method=json_data.get("Method"),
            Negate=json_data.get("Negate"),
            Pattern=json_data.get("Pattern"),
            Port=json_data.get("Port"),
            Type=json_data.get("Type"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProbeDefinition = ProbeDefinition


