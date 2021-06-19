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
    IamRoleArn: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    PlanId: Optional[str]
    Resources: Optional[Sequence[str]]
    SelectionTag: Optional[Sequence["_SelectionTagDefinition"]]

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
            IamRoleArn=json_data.get("IamRoleArn"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PlanId=json_data.get("PlanId"),
            Resources=json_data.get("Resources"),
            SelectionTag=deserialize_list(json_data.get("SelectionTag"), SelectionTagDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SelectionTagDefinition(BaseModel):
    Key: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SelectionTagDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SelectionTagDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SelectionTagDefinition = SelectionTagDefinition


