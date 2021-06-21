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
    AnpName: Optional[str]
    EpgName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    SchemaId: Optional[str]
    TemplateName: Optional[str]
    Expressions: Optional[Sequence["_ExpressionsDefinition"]]

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
            AnpName=json_data.get("AnpName"),
            EpgName=json_data.get("EpgName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            SchemaId=json_data.get("SchemaId"),
            TemplateName=json_data.get("TemplateName"),
            Expressions=deserialize_list(json_data.get("Expressions"), ExpressionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExpressionsDefinition(BaseModel):
    Key: Optional[str]
    Operator: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExpressionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpressionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Operator=json_data.get("Operator"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpressionsDefinition = ExpressionsDefinition

