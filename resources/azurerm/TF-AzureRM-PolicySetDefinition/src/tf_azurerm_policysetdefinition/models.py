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
    Description: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    ManagementGroupId: Optional[str]
    ManagementGroupName: Optional[str]
    Metadata: Optional[str]
    Name: Optional[str]
    Parameters: Optional[str]
    PolicyDefinitions: Optional[str]
    PolicyType: Optional[str]
    PolicyDefinitionGroup: Optional[Sequence["_PolicyDefinitionGroupDefinition"]]
    PolicyDefinitionReference: Optional[Sequence["_PolicyDefinitionReferenceDefinition"]]
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
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            ManagementGroupId=json_data.get("ManagementGroupId"),
            ManagementGroupName=json_data.get("ManagementGroupName"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            Parameters=json_data.get("Parameters"),
            PolicyDefinitions=json_data.get("PolicyDefinitions"),
            PolicyType=json_data.get("PolicyType"),
            PolicyDefinitionGroup=deserialize_list(json_data.get("PolicyDefinitionGroup"), PolicyDefinitionGroupDefinition),
            PolicyDefinitionReference=deserialize_list(json_data.get("PolicyDefinitionReference"), PolicyDefinitionReferenceDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyDefinitionGroupDefinition(BaseModel):
    AdditionalMetadataResourceId: Optional[str]
    Category: Optional[str]
    Description: Optional[str]
    DisplayName: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinitionGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinitionGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalMetadataResourceId=json_data.get("AdditionalMetadataResourceId"),
            Category=json_data.get("Category"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinitionGroupDefinition = PolicyDefinitionGroupDefinition


@dataclass
class PolicyDefinitionReferenceDefinition(BaseModel):
    ParameterValues: Optional[str]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    PolicyDefinitionId: Optional[str]
    PolicyGroupNames: Optional[Sequence[str]]
    ReferenceId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinitionReferenceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinitionReferenceDefinition"]:
        if not json_data:
            return None
        return cls(
            ParameterValues=json_data.get("ParameterValues"),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            PolicyDefinitionId=json_data.get("PolicyDefinitionId"),
            PolicyGroupNames=json_data.get("PolicyGroupNames"),
            ReferenceId=json_data.get("ReferenceId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinitionReferenceDefinition = PolicyDefinitionReferenceDefinition


@dataclass
class ParametersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


