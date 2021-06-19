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
    ClusterId: Optional[str]
    FileContent: Optional[str]
    FileExtType: Optional[str]
    FileName: Optional[str]
    FileType: Optional[str]
    Id: Optional[str]
    TableInfos: Optional[Sequence["_TableInfosDefinition"]]
    TablegroupId: Optional[str]

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
            ClusterId=json_data.get("ClusterId"),
            FileContent=json_data.get("FileContent"),
            FileExtType=json_data.get("FileExtType"),
            FileName=json_data.get("FileName"),
            FileType=json_data.get("FileType"),
            Id=json_data.get("Id"),
            TableInfos=deserialize_list(json_data.get("TableInfos"), TableInfosDefinition),
            TablegroupId=json_data.get("TablegroupId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TableInfosDefinition(BaseModel):
    Error: Optional[str]
    IndexKeySet: Optional[str]
    KeyFields: Optional[str]
    SumKeyFieldSize: Optional[float]
    SumValueFieldSize: Optional[float]
    TableName: Optional[str]
    ValueFields: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TableInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TableInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            Error=json_data.get("Error"),
            IndexKeySet=json_data.get("IndexKeySet"),
            KeyFields=json_data.get("KeyFields"),
            SumKeyFieldSize=json_data.get("SumKeyFieldSize"),
            SumValueFieldSize=json_data.get("SumValueFieldSize"),
            TableName=json_data.get("TableName"),
            ValueFields=json_data.get("ValueFields"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TableInfosDefinition = TableInfosDefinition


