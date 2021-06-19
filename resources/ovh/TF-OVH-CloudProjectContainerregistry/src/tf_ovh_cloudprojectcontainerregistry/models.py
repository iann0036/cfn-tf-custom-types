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
    CreatedAt: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Plan: Optional[Sequence["_PlanDefinition3"]]
    PlanId: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    ServiceName: Optional[str]
    Size: Optional[float]
    Status: Optional[str]
    UpdatedAt: Optional[str]
    Url: Optional[str]
    Version: Optional[str]

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
            CreatedAt=json_data.get("CreatedAt"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Plan=deserialize_list(json_data.get("Plan"), PlanDefinition3),
            PlanId=json_data.get("PlanId"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            ServiceName=json_data.get("ServiceName"),
            Size=json_data.get("Size"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
            Url=json_data.get("Url"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PlanDefinition3(BaseModel):
    Code: Optional[str]
    CreatedAt: Optional[str]
    Features: Optional[Sequence["_PlanDefinition"]]
    Id: Optional[str]
    Name: Optional[str]
    RegistryLimits: Optional[Sequence["_PlanDefinition2"]]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PlanDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlanDefinition3"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            CreatedAt=json_data.get("CreatedAt"),
            Features=deserialize_list(json_data.get("Features"), PlanDefinition),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RegistryLimits=deserialize_list(json_data.get("RegistryLimits"), PlanDefinition2),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlanDefinition3 = PlanDefinition3


@dataclass
class PlanDefinition(BaseModel):
    Vulnerability: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_PlanDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlanDefinition"]:
        if not json_data:
            return None
        return cls(
            Vulnerability=json_data.get("Vulnerability"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlanDefinition = PlanDefinition


@dataclass
class PlanDefinition2(BaseModel):
    ImageStorage: Optional[float]
    ParallelRequest: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PlanDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlanDefinition2"]:
        if not json_data:
            return None
        return cls(
            ImageStorage=json_data.get("ImageStorage"),
            ParallelRequest=json_data.get("ParallelRequest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlanDefinition2 = PlanDefinition2


