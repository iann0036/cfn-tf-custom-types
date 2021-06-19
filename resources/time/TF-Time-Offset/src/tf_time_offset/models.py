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
    BaseRfc3339: Optional[str]
    Day: Optional[float]
    Hour: Optional[float]
    Id: Optional[str]
    Minute: Optional[float]
    Month: Optional[float]
    OffsetDays: Optional[float]
    OffsetHours: Optional[float]
    OffsetMinutes: Optional[float]
    OffsetMonths: Optional[float]
    OffsetSeconds: Optional[float]
    OffsetYears: Optional[float]
    Rfc3339: Optional[str]
    Second: Optional[float]
    Triggers: Optional[Sequence["_TriggersDefinition"]]
    Unix: Optional[float]
    Year: Optional[float]

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
            BaseRfc3339=json_data.get("BaseRfc3339"),
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
            Id=json_data.get("Id"),
            Minute=json_data.get("Minute"),
            Month=json_data.get("Month"),
            OffsetDays=json_data.get("OffsetDays"),
            OffsetHours=json_data.get("OffsetHours"),
            OffsetMinutes=json_data.get("OffsetMinutes"),
            OffsetMonths=json_data.get("OffsetMonths"),
            OffsetSeconds=json_data.get("OffsetSeconds"),
            OffsetYears=json_data.get("OffsetYears"),
            Rfc3339=json_data.get("Rfc3339"),
            Second=json_data.get("Second"),
            Triggers=deserialize_list(json_data.get("Triggers"), TriggersDefinition),
            Unix=json_data.get("Unix"),
            Year=json_data.get("Year"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TriggersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TriggersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TriggersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TriggersDefinition = TriggersDefinition


