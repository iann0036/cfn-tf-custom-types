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
    ChangeSetName: Optional[str]
    ChangeSetType: Optional[str]
    Description: Optional[str]
    DisableRollback: Optional[bool]
    Id: Optional[str]
    NotificationUrls: Optional[Sequence[str]]
    RamRoleName: Optional[str]
    ReplacementOption: Optional[str]
    StackId: Optional[str]
    StackName: Optional[str]
    StackPolicyBody: Optional[str]
    StackPolicyDuringUpdateBody: Optional[str]
    StackPolicyDuringUpdateUrl: Optional[str]
    StackPolicyUrl: Optional[str]
    Status: Optional[str]
    TemplateBody: Optional[str]
    TemplateUrl: Optional[str]
    TimeoutInMinutes: Optional[float]
    UsePreviousParameters: Optional[bool]
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
            ChangeSetName=json_data.get("ChangeSetName"),
            ChangeSetType=json_data.get("ChangeSetType"),
            Description=json_data.get("Description"),
            DisableRollback=json_data.get("DisableRollback"),
            Id=json_data.get("Id"),
            NotificationUrls=json_data.get("NotificationUrls"),
            RamRoleName=json_data.get("RamRoleName"),
            ReplacementOption=json_data.get("ReplacementOption"),
            StackId=json_data.get("StackId"),
            StackName=json_data.get("StackName"),
            StackPolicyBody=json_data.get("StackPolicyBody"),
            StackPolicyDuringUpdateBody=json_data.get("StackPolicyDuringUpdateBody"),
            StackPolicyDuringUpdateUrl=json_data.get("StackPolicyDuringUpdateUrl"),
            StackPolicyUrl=json_data.get("StackPolicyUrl"),
            Status=json_data.get("Status"),
            TemplateBody=json_data.get("TemplateBody"),
            TemplateUrl=json_data.get("TemplateUrl"),
            TimeoutInMinutes=json_data.get("TimeoutInMinutes"),
            UsePreviousParameters=json_data.get("UsePreviousParameters"),
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

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition

