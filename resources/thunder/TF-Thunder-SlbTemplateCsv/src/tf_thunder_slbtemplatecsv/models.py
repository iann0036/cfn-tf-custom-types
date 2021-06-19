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
    CsvName: Optional[str]
    DelimChar: Optional[str]
    DelimNum: Optional[float]
    Id: Optional[str]
    Ipv6Enable: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    MultipleFields: Optional[Sequence["_MultipleFieldsDefinition"]]

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
            CsvName=json_data.get("CsvName"),
            DelimChar=json_data.get("DelimChar"),
            DelimNum=json_data.get("DelimNum"),
            Id=json_data.get("Id"),
            Ipv6Enable=json_data.get("Ipv6Enable"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            MultipleFields=deserialize_list(json_data.get("MultipleFields"), MultipleFieldsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MultipleFieldsDefinition(BaseModel):
    CsvType: Optional[str]
    Field: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MultipleFieldsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultipleFieldsDefinition"]:
        if not json_data:
            return None
        return cls(
            CsvType=json_data.get("CsvType"),
            Field=json_data.get("Field"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultipleFieldsDefinition = MultipleFieldsDefinition


