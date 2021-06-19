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
    AcceptSummary: Optional[bool]
    AdvertiseMetric: Optional[float]
    AdvertiseType: Optional[str]
    DefaultRouteAdvertise: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    Type: Optional[str]
    VirtualRouter: Optional[str]
    ExtRange: Optional[Sequence["_ExtRangeDefinition"]]
    Range: Optional[Sequence["_RangeDefinition"]]

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
            AcceptSummary=json_data.get("AcceptSummary"),
            AdvertiseMetric=json_data.get("AdvertiseMetric"),
            AdvertiseType=json_data.get("AdvertiseType"),
            DefaultRouteAdvertise=json_data.get("DefaultRouteAdvertise"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            Type=json_data.get("Type"),
            VirtualRouter=json_data.get("VirtualRouter"),
            ExtRange=deserialize_list(json_data.get("ExtRange"), ExtRangeDefinition),
            Range=deserialize_list(json_data.get("Range"), RangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExtRangeDefinition(BaseModel):
    Action: Optional[str]
    Network: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExtRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExtRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExtRangeDefinition = ExtRangeDefinition


@dataclass
class RangeDefinition(BaseModel):
    Action: Optional[str]
    Network: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeDefinition = RangeDefinition


