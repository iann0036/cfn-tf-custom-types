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
    Bucket: Optional[str]
    Namespace: Optional[str]
    TimeCreated: Optional[str]
    Rules: Optional[Sequence["_Rules"]]
    Timeouts: Optional["_Timeouts"]
    ObjectNameFilter: Optional[Sequence["_ObjectNameFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bucket=json_data.get("Bucket"),
            Namespace=json_data.get("Namespace"),
            TimeCreated=json_data.get("TimeCreated"),
            Rules=json_data.get("Rules"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            ObjectNameFilter=json_data.get("ObjectNameFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rules:
    Action: Optional[str]
    IsEnabled: Optional[bool]
    Name: Optional[str]
    TimeAmount: Optional[str]
    TimeUnit: Optional[str]
    ObjectNameFilter: Optional[Sequence["_ObjectNameFilter"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rules"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            IsEnabled=json_data.get("IsEnabled"),
            Name=json_data.get("Name"),
            TimeAmount=json_data.get("TimeAmount"),
            TimeUnit=json_data.get("TimeUnit"),
            ObjectNameFilter=json_data.get("ObjectNameFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rules = Rules


@dataclass
class ObjectNameFilter:
    ExclusionPatterns: Optional[Sequence[str]]
    InclusionPatterns: Optional[Sequence[str]]
    InclusionPrefixes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ObjectNameFilter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ObjectNameFilter"]:
        if not json_data:
            return None
        return cls(
            ExclusionPatterns=json_data.get("ExclusionPatterns"),
            InclusionPatterns=json_data.get("InclusionPatterns"),
            InclusionPrefixes=json_data.get("InclusionPrefixes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ObjectNameFilter = ObjectNameFilter


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


