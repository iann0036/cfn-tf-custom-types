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
    BranchFilter: Optional[str]
    Id: Optional[str]
    PayloadUrl: Optional[str]
    ProjectName: Optional[str]
    Secret: Optional[str]
    Url: Optional[str]
    FilterGroup: Optional[Sequence["_FilterGroupDefinition"]]

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
            BranchFilter=json_data.get("BranchFilter"),
            Id=json_data.get("Id"),
            PayloadUrl=json_data.get("PayloadUrl"),
            ProjectName=json_data.get("ProjectName"),
            Secret=json_data.get("Secret"),
            Url=json_data.get("Url"),
            FilterGroup=deserialize_list(json_data.get("FilterGroup"), FilterGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterGroupDefinition(BaseModel):
    Filter: Optional[Sequence["_FilterDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Filter=deserialize_list(json_data.get("Filter"), FilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterGroupDefinition = FilterGroupDefinition


@dataclass
class FilterDefinition(BaseModel):
    ExcludeMatchedPattern: Optional[bool]
    Pattern: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterDefinition"]:
        if not json_data:
            return None
        return cls(
            ExcludeMatchedPattern=json_data.get("ExcludeMatchedPattern"),
            Pattern=json_data.get("Pattern"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterDefinition = FilterDefinition


