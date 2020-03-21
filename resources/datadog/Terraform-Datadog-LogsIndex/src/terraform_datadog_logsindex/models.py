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
    Name: Optional[str]
    ExclusionFilter: Optional[Sequence["_ExclusionFilter"]]
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
            Name=json_data.get("Name"),
            ExclusionFilter=json_data.get("ExclusionFilter"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExclusionFilter:
    IsEnabled: Optional[bool]
    Name: Optional[str]
    Filter: Optional[Sequence["_Filter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionFilter"]:
        if not json_data:
            return None
        return cls(
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            Filter=json_data.get("Filter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionFilter = ExclusionFilter


@dataclass
class Filter:
    Query: Optional[str]
    SampleRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Query=json_data.get("Query"),
            SampleRate=json_data.get("SampleRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


