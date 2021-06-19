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
    Id: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    AppLearningInfo: Optional[Sequence["_AppLearningInfoDefinition"]]

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
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            AppLearningInfo=deserialize_list(json_data.get("AppLearningInfo"), AppLearningInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AppLearningInfoDefinition(BaseModel):
    AppId: Optional[str]
    VsUuid: Optional[str]
    UriInfo: Optional[Sequence["_UriInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AppLearningInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AppLearningInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            AppId=json_data.get("AppId"),
            VsUuid=json_data.get("VsUuid"),
            UriInfo=deserialize_list(json_data.get("UriInfo"), UriInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AppLearningInfoDefinition = AppLearningInfoDefinition


@dataclass
class UriInfoDefinition(BaseModel):
    UriHits: Optional[float]
    UriKey: Optional[str]
    ParamInfo: Optional[Sequence["_ParamInfoDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_UriInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UriInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            UriHits=json_data.get("UriHits"),
            UriKey=json_data.get("UriKey"),
            ParamInfo=deserialize_list(json_data.get("ParamInfo"), ParamInfoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_UriInfoDefinition = UriInfoDefinition


@dataclass
class ParamInfoDefinition(BaseModel):
    ParamHits: Optional[float]
    ParamKey: Optional[str]
    ParamSizeClasses: Optional[Sequence["_ParamSizeClassesDefinition"]]
    ParamTypeClasses: Optional[Sequence["_ParamTypeClassesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParamInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            ParamHits=json_data.get("ParamHits"),
            ParamKey=json_data.get("ParamKey"),
            ParamSizeClasses=deserialize_list(json_data.get("ParamSizeClasses"), ParamSizeClassesDefinition),
            ParamTypeClasses=deserialize_list(json_data.get("ParamTypeClasses"), ParamTypeClassesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamInfoDefinition = ParamInfoDefinition


@dataclass
class ParamSizeClassesDefinition(BaseModel):
    Hits: Optional[float]
    Len: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamSizeClassesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamSizeClassesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hits=json_data.get("Hits"),
            Len=json_data.get("Len"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamSizeClassesDefinition = ParamSizeClassesDefinition


@dataclass
class ParamTypeClassesDefinition(BaseModel):
    Hits: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParamTypeClassesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParamTypeClassesDefinition"]:
        if not json_data:
            return None
        return cls(
            Hits=json_data.get("Hits"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParamTypeClassesDefinition = ParamTypeClassesDefinition


