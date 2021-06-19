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
    Description: Optional[str]
    EnvKey: Optional[str]
    Excluded: Optional[Sequence[str]]
    Id: Optional[str]
    Included: Optional[Sequence[str]]
    Key: Optional[str]
    Name: Optional[str]
    ProjectKey: Optional[str]
    Tags: Optional[Sequence[str]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            Description=json_data.get("Description"),
            EnvKey=json_data.get("EnvKey"),
            Excluded=json_data.get("Excluded"),
            Id=json_data.get("Id"),
            Included=json_data.get("Included"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            ProjectKey=json_data.get("ProjectKey"),
            Tags=json_data.get("Tags"),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RulesDefinition(BaseModel):
    BucketBy: Optional[str]
    Weight: Optional[float]
    Clauses: Optional[Sequence["_ClausesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            BucketBy=json_data.get("BucketBy"),
            Weight=json_data.get("Weight"),
            Clauses=deserialize_list(json_data.get("Clauses"), ClausesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class ClausesDefinition(BaseModel):
    Attribute: Optional[str]
    Negate: Optional[bool]
    Op: Optional[str]
    ValueType: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ClausesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClausesDefinition"]:
        if not json_data:
            return None
        return cls(
            Attribute=json_data.get("Attribute"),
            Negate=json_data.get("Negate"),
            Op=json_data.get("Op"),
            ValueType=json_data.get("ValueType"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClausesDefinition = ClausesDefinition


