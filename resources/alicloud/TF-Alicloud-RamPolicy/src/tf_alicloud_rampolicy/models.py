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
    AttachmentCount: Optional[float]
    DefaultVersion: Optional[str]
    Description: Optional[str]
    Document: Optional[str]
    Force: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    PolicyDocument: Optional[str]
    PolicyName: Optional[str]
    RotateStrategy: Optional[str]
    Type: Optional[str]
    Version: Optional[str]
    VersionId: Optional[str]
    Statement: Optional[Sequence["_StatementDefinition"]]
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
            AttachmentCount=json_data.get("AttachmentCount"),
            DefaultVersion=json_data.get("DefaultVersion"),
            Description=json_data.get("Description"),
            Document=json_data.get("Document"),
            Force=json_data.get("Force"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PolicyDocument=json_data.get("PolicyDocument"),
            PolicyName=json_data.get("PolicyName"),
            RotateStrategy=json_data.get("RotateStrategy"),
            Type=json_data.get("Type"),
            Version=json_data.get("Version"),
            VersionId=json_data.get("VersionId"),
            Statement=deserialize_list(json_data.get("Statement"), StatementDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StatementDefinition(BaseModel):
    Action: Optional[Sequence[str]]
    Effect: Optional[str]
    Resource: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_StatementDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatementDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Effect=json_data.get("Effect"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatementDefinition = StatementDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


