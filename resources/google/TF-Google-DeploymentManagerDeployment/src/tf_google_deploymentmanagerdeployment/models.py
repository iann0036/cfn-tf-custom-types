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
    CreatePolicy: Optional[str]
    DeletePolicy: Optional[str]
    DeploymentId: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Manifest: Optional[str]
    Name: Optional[str]
    Preview: Optional[bool]
    Project: Optional[str]
    SelfLink: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Target: Optional[Sequence["_TargetDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            CreatePolicy=json_data.get("CreatePolicy"),
            DeletePolicy=json_data.get("DeletePolicy"),
            DeploymentId=json_data.get("DeploymentId"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Manifest=json_data.get("Manifest"),
            Name=json_data.get("Name"),
            Preview=json_data.get("Preview"),
            Project=json_data.get("Project"),
            SelfLink=json_data.get("SelfLink"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Target=deserialize_list(json_data.get("Target"), TargetDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class LabelsDefinition(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class TargetDefinition(BaseModel):
    Config: Optional[Sequence["_ConfigDefinition"]]
    Imports: Optional[Sequence["_ImportsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=deserialize_list(json_data.get("Config"), ConfigDefinition),
            Imports=deserialize_list(json_data.get("Imports"), ImportsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetDefinition = TargetDefinition


@dataclass
class ConfigDefinition(BaseModel):
    Content: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConfigDefinition = ConfigDefinition


@dataclass
class ImportsDefinition(BaseModel):
    Content: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ImportsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ImportsDefinition"]:
        if not json_data:
            return None
        return cls(
            Content=json_data.get("Content"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ImportsDefinition = ImportsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


