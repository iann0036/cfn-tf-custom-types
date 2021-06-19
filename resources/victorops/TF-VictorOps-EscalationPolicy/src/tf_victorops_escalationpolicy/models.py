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
    Id: Optional[str]
    IgnoreCustomPagingPolicies: Optional[bool]
    Name: Optional[str]
    TeamId: Optional[str]
    Step: Optional[Sequence["_StepDefinition"]]

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
            Id=json_data.get("Id"),
            IgnoreCustomPagingPolicies=json_data.get("IgnoreCustomPagingPolicies"),
            Name=json_data.get("Name"),
            TeamId=json_data.get("TeamId"),
            Step=deserialize_list(json_data.get("Step"), StepDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StepDefinition(BaseModel):
    Entries: Optional[Sequence[Sequence["_EntriesDefinition"]]]
    Timeout: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StepDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepDefinition"]:
        if not json_data:
            return None
        return cls(
            Entries=deserialize_list(json_data.get("Entries"), <ResolvedType(ContainerType.MODEL, EntriesDefinition)>),
            Timeout=json_data.get("Timeout"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepDefinition = StepDefinition


@dataclass
class EntriesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition


