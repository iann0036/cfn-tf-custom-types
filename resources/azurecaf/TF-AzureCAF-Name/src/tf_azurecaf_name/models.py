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
    CleanInput: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Passthrough: Optional[bool]
    Prefixes: Optional[Sequence[str]]
    RandomLength: Optional[float]
    RandomSeed: Optional[float]
    ResourceType: Optional[str]
    ResourceTypes: Optional[Sequence[str]]
    Result: Optional[str]
    Results: Optional[Sequence["_ResultsDefinition"]]
    Separator: Optional[str]
    Suffixes: Optional[Sequence[str]]
    UseSlug: Optional[bool]

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
            CleanInput=json_data.get("CleanInput"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Passthrough=json_data.get("Passthrough"),
            Prefixes=json_data.get("Prefixes"),
            RandomLength=json_data.get("RandomLength"),
            RandomSeed=json_data.get("RandomSeed"),
            ResourceType=json_data.get("ResourceType"),
            ResourceTypes=json_data.get("ResourceTypes"),
            Result=json_data.get("Result"),
            Results=deserialize_list(json_data.get("Results"), ResultsDefinition),
            Separator=json_data.get("Separator"),
            Suffixes=json_data.get("Suffixes"),
            UseSlug=json_data.get("UseSlug"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResultsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResultsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResultsDefinition = ResultsDefinition


