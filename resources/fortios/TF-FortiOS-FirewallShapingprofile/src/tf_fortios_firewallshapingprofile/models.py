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
    Comment: Optional[str]
    DefaultClassId: Optional[float]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    ProfileName: Optional[str]
    Type: Optional[str]
    Vdomparam: Optional[str]
    ShapingEntries: Optional[Sequence["_ShapingEntriesDefinition"]]

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
            Comment=json_data.get("Comment"),
            DefaultClassId=json_data.get("DefaultClassId"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            ProfileName=json_data.get("ProfileName"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            ShapingEntries=deserialize_list(json_data.get("ShapingEntries"), ShapingEntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ShapingEntriesDefinition(BaseModel):
    BurstInMsec: Optional[float]
    CburstInMsec: Optional[float]
    ClassId: Optional[float]
    GuaranteedBandwidthPercentage: Optional[float]
    Id: Optional[float]
    Limit: Optional[float]
    Max: Optional[float]
    MaximumBandwidthPercentage: Optional[float]
    Min: Optional[float]
    Priority: Optional[str]
    RedProbability: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ShapingEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ShapingEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            BurstInMsec=json_data.get("BurstInMsec"),
            CburstInMsec=json_data.get("CburstInMsec"),
            ClassId=json_data.get("ClassId"),
            GuaranteedBandwidthPercentage=json_data.get("GuaranteedBandwidthPercentage"),
            Id=json_data.get("Id"),
            Limit=json_data.get("Limit"),
            Max=json_data.get("Max"),
            MaximumBandwidthPercentage=json_data.get("MaximumBandwidthPercentage"),
            Min=json_data.get("Min"),
            Priority=json_data.get("Priority"),
            RedProbability=json_data.get("RedProbability"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ShapingEntriesDefinition = ShapingEntriesDefinition


