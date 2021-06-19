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
    Arn: Optional[str]
    AssumeRolePolicy: Optional[str]
    CreateDate: Optional[str]
    Description: Optional[str]
    ForceDetachPolicies: Optional[bool]
    Id: Optional[str]
    ManagedPolicyArns: Optional[Sequence[str]]
    MaxSessionDuration: Optional[float]
    Name: Optional[str]
    NamePrefix: Optional[str]
    Path: Optional[str]
    PermissionsBoundary: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    UniqueId: Optional[str]
    InlinePolicy: Optional[Sequence["_InlinePolicyDefinition"]]

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
            Arn=json_data.get("Arn"),
            AssumeRolePolicy=json_data.get("AssumeRolePolicy"),
            CreateDate=json_data.get("CreateDate"),
            Description=json_data.get("Description"),
            ForceDetachPolicies=json_data.get("ForceDetachPolicies"),
            Id=json_data.get("Id"),
            ManagedPolicyArns=json_data.get("ManagedPolicyArns"),
            MaxSessionDuration=json_data.get("MaxSessionDuration"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            Path=json_data.get("Path"),
            PermissionsBoundary=json_data.get("PermissionsBoundary"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            UniqueId=json_data.get("UniqueId"),
            InlinePolicy=deserialize_list(json_data.get("InlinePolicy"), InlinePolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class InlinePolicyDefinition(BaseModel):
    Name: Optional[str]
    Policy: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InlinePolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InlinePolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InlinePolicyDefinition = InlinePolicyDefinition


