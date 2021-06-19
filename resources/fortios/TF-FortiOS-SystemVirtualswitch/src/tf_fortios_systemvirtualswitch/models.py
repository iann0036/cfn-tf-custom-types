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
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PhysicalSwitch: Optional[str]
    Span: Optional[str]
    SpanDestPort: Optional[str]
    SpanDirection: Optional[str]
    SpanSourcePort: Optional[str]
    Vdomparam: Optional[str]
    Port: Optional[Sequence["_PortDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PhysicalSwitch=json_data.get("PhysicalSwitch"),
            Span=json_data.get("Span"),
            SpanDestPort=json_data.get("SpanDestPort"),
            SpanDirection=json_data.get("SpanDirection"),
            SpanSourcePort=json_data.get("SpanSourcePort"),
            Vdomparam=json_data.get("Vdomparam"),
            Port=deserialize_list(json_data.get("Port"), PortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortDefinition(BaseModel):
    Alias: Optional[str]
    Name: Optional[str]
    Speed: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortDefinition"]:
        if not json_data:
            return None
        return cls(
            Alias=json_data.get("Alias"),
            Name=json_data.get("Name"),
            Speed=json_data.get("Speed"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortDefinition = PortDefinition


