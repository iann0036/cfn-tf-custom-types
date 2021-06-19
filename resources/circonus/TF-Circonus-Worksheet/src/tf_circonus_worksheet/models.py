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
    Favourite: Optional[bool]
    Graphs: Optional[Sequence[str]]
    Id: Optional[str]
    Notes: Optional[str]
    Tags: Optional[Sequence[str]]
    Title: Optional[str]
    SmartQueries: Optional[Sequence["_SmartQueriesDefinition"]]

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
            Favourite=json_data.get("Favourite"),
            Graphs=json_data.get("Graphs"),
            Id=json_data.get("Id"),
            Notes=json_data.get("Notes"),
            Tags=json_data.get("Tags"),
            Title=json_data.get("Title"),
            SmartQueries=deserialize_list(json_data.get("SmartQueries"), SmartQueriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SmartQueriesDefinition(BaseModel):
    Name: Optional[str]
    Order: Optional[Sequence[str]]
    Query: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SmartQueriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SmartQueriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Order=json_data.get("Order"),
            Query=json_data.get("Query"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SmartQueriesDefinition = SmartQueriesDefinition


