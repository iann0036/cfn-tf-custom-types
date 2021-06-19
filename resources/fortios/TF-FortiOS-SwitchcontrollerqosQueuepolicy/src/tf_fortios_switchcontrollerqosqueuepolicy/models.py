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
    RateBy: Optional[str]
    Schedule: Optional[str]
    Vdomparam: Optional[str]
    CosQueue: Optional[Sequence["_CosQueueDefinition"]]

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
            RateBy=json_data.get("RateBy"),
            Schedule=json_data.get("Schedule"),
            Vdomparam=json_data.get("Vdomparam"),
            CosQueue=deserialize_list(json_data.get("CosQueue"), CosQueueDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CosQueueDefinition(BaseModel):
    Description: Optional[str]
    DropPolicy: Optional[str]
    Ecn: Optional[str]
    MaxRate: Optional[float]
    MaxRatePercent: Optional[float]
    MinRate: Optional[float]
    MinRatePercent: Optional[float]
    Name: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CosQueueDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CosQueueDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            DropPolicy=json_data.get("DropPolicy"),
            Ecn=json_data.get("Ecn"),
            MaxRate=json_data.get("MaxRate"),
            MaxRatePercent=json_data.get("MaxRatePercent"),
            MinRate=json_data.get("MinRate"),
            MinRatePercent=json_data.get("MinRatePercent"),
            Name=json_data.get("Name"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CosQueueDefinition = CosQueueDefinition


