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
    AccountIds: Optional[str]
    AdministrationRoleName: Optional[str]
    Description: Optional[str]
    ExecutionRoleName: Optional[str]
    Id: Optional[str]
    OperationDescription: Optional[str]
    OperationPreferences: Optional[str]
    RegionIds: Optional[str]
    StackGroupId: Optional[str]
    StackGroupName: Optional[str]
    Status: Optional[str]
    TemplateBody: Optional[str]
    TemplateUrl: Optional[str]
    TemplateVersion: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
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
            AccountIds=json_data.get("AccountIds"),
            AdministrationRoleName=json_data.get("AdministrationRoleName"),
            Description=json_data.get("Description"),
            ExecutionRoleName=json_data.get("ExecutionRoleName"),
            Id=json_data.get("Id"),
            OperationDescription=json_data.get("OperationDescription"),
            OperationPreferences=json_data.get("OperationPreferences"),
            RegionIds=json_data.get("RegionIds"),
            StackGroupId=json_data.get("StackGroupId"),
            StackGroupName=json_data.get("StackGroupName"),
            Status=json_data.get("Status"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateUrl=json_data.get("TemplateUrl"),
            TemplateVersion=json_data.get("TemplateVersion"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ParametersDefinition(BaseModel):
    ParameterKey: Optional[str]
    ParameterValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            ParameterKey=json_data.get("ParameterKey"),
            ParameterValue=json_data.get("ParameterValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


