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
    ClassList: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    ServerVersion: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    CalcSha1: Optional[Sequence["_CalcSha1Definition"]]

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
            ClassList=json_data.get("ClassList"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            ServerVersion=json_data.get("ServerVersion"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            CalcSha1=deserialize_list(json_data.get("CalcSha1"), CalcSha1Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CalcSha1Definition(BaseModel):
    Sha1Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CalcSha1Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CalcSha1Definition"]:
        if not json_data:
            return None
        return cls(
            Sha1Value=json_data.get("Sha1Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CalcSha1Definition = CalcSha1Definition


