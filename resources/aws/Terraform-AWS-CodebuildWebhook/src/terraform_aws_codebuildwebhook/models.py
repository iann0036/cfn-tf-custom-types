# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    BranchFilter: Optional[str]
    PayloadUrl: Optional[str]
    ProjectName: Optional[str]
    Secret: Optional[str]
    Url: Optional[str]
    FilterGroup: Optional[Sequence["_FilterGroup"]]
    Filter: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BranchFilter=json_data.get("BranchFilter"),
            PayloadUrl=json_data.get("PayloadUrl"),
            ProjectName=json_data.get("ProjectName"),
            Secret=json_data.get("Secret"),
            Url=json_data.get("Url"),
            FilterGroup=json_data.get("FilterGroup"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FilterGroup:
    Filter: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_FilterGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterGroup"]:
        if not json_data:
            return None
        return cls(
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterGroup = FilterGroup


@dataclass
class Filter:
    ExcludeMatchedPattern: Optional[bool]
    Pattern: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            ExcludeMatchedPattern=json_data.get("ExcludeMatchedPattern"),
            Pattern=json_data.get("Pattern"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


