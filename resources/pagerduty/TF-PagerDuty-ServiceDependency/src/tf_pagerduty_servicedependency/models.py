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
    Dependency: Optional[Sequence["_DependencyDefinition"]]

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
            Dependency=deserialize_list(json_data.get("Dependency"), DependencyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DependencyDefinition(BaseModel):
    Type: Optional[str]
    DependentService: Optional[Sequence["_DependentServiceDefinition"]]
    SupportingService: Optional[Sequence["_SupportingServiceDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DependencyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DependencyDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            DependentService=deserialize_list(json_data.get("DependentService"), DependentServiceDefinition),
            SupportingService=deserialize_list(json_data.get("SupportingService"), SupportingServiceDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DependencyDefinition = DependencyDefinition


@dataclass
class DependentServiceDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DependentServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DependentServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DependentServiceDefinition = DependentServiceDefinition


@dataclass
class SupportingServiceDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SupportingServiceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SupportingServiceDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SupportingServiceDefinition = SupportingServiceDefinition


