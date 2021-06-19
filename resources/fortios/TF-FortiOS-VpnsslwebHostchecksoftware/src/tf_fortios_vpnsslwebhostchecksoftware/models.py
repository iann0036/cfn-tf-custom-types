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
    DynamicSortSubtable: Optional[str]
    Guid: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OsType: Optional[str]
    Type: Optional[str]
    Vdomparam: Optional[str]
    Version: Optional[str]
    CheckItemList: Optional[Sequence["_CheckItemListDefinition"]]

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
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Guid=json_data.get("Guid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            Version=json_data.get("Version"),
            CheckItemList=deserialize_list(json_data.get("CheckItemList"), CheckItemListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CheckItemListDefinition(BaseModel):
    Action: Optional[str]
    Id: Optional[float]
    Target: Optional[str]
    Type: Optional[str]
    Version: Optional[str]
    Md5s: Optional[Sequence["_Md5sDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CheckItemListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CheckItemListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
            Target=json_data.get("Target"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            Md5s=deserialize_list(json_data.get("Md5s"), Md5sDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CheckItemListDefinition = CheckItemListDefinition


@dataclass
class Md5sDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Md5sDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Md5sDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Md5sDefinition = Md5sDefinition


