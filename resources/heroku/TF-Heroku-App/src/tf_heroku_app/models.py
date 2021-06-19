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
    Acm: Optional[bool]
    AllConfigVars: Optional[Sequence["_AllConfigVarsDefinition"]]
    Buildpacks: Optional[Sequence[str]]
    ConfigVars: Optional[Sequence["_ConfigVarsDefinition"]]
    GitUrl: Optional[str]
    HerokuHostname: Optional[str]
    Id: Optional[str]
    InternalRouting: Optional[bool]
    Name: Optional[str]
    Region: Optional[str]
    SensitiveConfigVars: Optional[Sequence["_SensitiveConfigVarsDefinition"]]
    Space: Optional[str]
    Stack: Optional[str]
    Uuid: Optional[str]
    WebUrl: Optional[str]
    Organization: Optional[Sequence["_OrganizationDefinition"]]

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
            Acm=json_data.get("Acm"),
            AllConfigVars=deserialize_list(json_data.get("AllConfigVars"), AllConfigVarsDefinition),
            Buildpacks=json_data.get("Buildpacks"),
            ConfigVars=deserialize_list(json_data.get("ConfigVars"), ConfigVarsDefinition),
            GitUrl=json_data.get("GitUrl"),
            HerokuHostname=json_data.get("HerokuHostname"),
            Id=json_data.get("Id"),
            InternalRouting=json_data.get("InternalRouting"),
            Name=json_data.get("Name"),
            Region=json_data.get("Region"),
            SensitiveConfigVars=deserialize_list(json_data.get("SensitiveConfigVars"), SensitiveConfigVarsDefinition),
            Space=json_data.get("Space"),
            Stack=json_data.get("Stack"),
            Uuid=json_data.get("Uuid"),
            WebUrl=json_data.get("WebUrl"),
            Organization=deserialize_list(json_data.get("Organization"), OrganizationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AllConfigVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AllConfigVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AllConfigVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AllConfigVarsDefinition = AllConfigVarsDefinition


@dataclass
class ConfigVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigVarsDefinition = ConfigVarsDefinition


@dataclass
class SensitiveConfigVarsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SensitiveConfigVarsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SensitiveConfigVarsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SensitiveConfigVarsDefinition = SensitiveConfigVarsDefinition


@dataclass
class OrganizationDefinition(BaseModel):
    Locked: Optional[bool]
    Name: Optional[str]
    Personal: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_OrganizationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganizationDefinition"]:
        if not json_data:
            return None
        return cls(
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Personal=json_data.get("Personal"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganizationDefinition = OrganizationDefinition


