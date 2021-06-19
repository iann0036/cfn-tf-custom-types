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
    Id: Optional[str]
    Name: Optional[str]
    Vdomparam: Optional[str]
    NaiList: Optional[Sequence["_NaiListDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Vdomparam=json_data.get("Vdomparam"),
            NaiList=deserialize_list(json_data.get("NaiList"), NaiListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NaiListDefinition(BaseModel):
    Encoding: Optional[str]
    NaiRealm: Optional[str]
    Name: Optional[str]
    EapMethod: Optional[Sequence["_EapMethodDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NaiListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NaiListDefinition"]:
        if not json_data:
            return None
        return cls(
            Encoding=json_data.get("Encoding"),
            NaiRealm=json_data.get("NaiRealm"),
            Name=json_data.get("Name"),
            EapMethod=deserialize_list(json_data.get("EapMethod"), EapMethodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NaiListDefinition = NaiListDefinition


@dataclass
class EapMethodDefinition(BaseModel):
    Index: Optional[float]
    Method: Optional[str]
    AuthParam: Optional[Sequence["_AuthParamDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EapMethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EapMethodDefinition"]:
        if not json_data:
            return None
        return cls(
            Index=json_data.get("Index"),
            Method=json_data.get("Method"),
            AuthParam=deserialize_list(json_data.get("AuthParam"), AuthParamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EapMethodDefinition = EapMethodDefinition


@dataclass
class AuthParamDefinition(BaseModel):
    Id: Optional[str]
    Index: Optional[float]
    Val: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthParamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthParamDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            Val=json_data.get("Val"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthParamDefinition = AuthParamDefinition


