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
    Attachments: Optional[Sequence["_AttachmentsDefinition"]]
    BillingCycle: Optional[str]
    Created: Optional[str]
    Description: Optional[str]
    Facility: Optional[str]
    Id: Optional[str]
    Locked: Optional[bool]
    Name: Optional[str]
    Plan: Optional[str]
    ProjectId: Optional[str]
    Size: Optional[float]
    State: Optional[str]
    Updated: Optional[str]
    SnapshotPolicies: Optional[Sequence["_SnapshotPoliciesDefinition"]]

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
            Attachments=deserialize_list(json_data.get("Attachments"), AttachmentsDefinition),
            BillingCycle=json_data.get("BillingCycle"),
            Created=json_data.get("Created"),
            Description=json_data.get("Description"),
            Facility=json_data.get("Facility"),
            Id=json_data.get("Id"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Plan=json_data.get("Plan"),
            ProjectId=json_data.get("ProjectId"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            Updated=json_data.get("Updated"),
            SnapshotPolicies=deserialize_list(json_data.get("SnapshotPolicies"), SnapshotPoliciesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AttachmentsDefinition(BaseModel):
    Href: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AttachmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AttachmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AttachmentsDefinition = AttachmentsDefinition


@dataclass
class SnapshotPoliciesDefinition(BaseModel):
    SnapshotCount: Optional[float]
    SnapshotFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            SnapshotCount=json_data.get("SnapshotCount"),
            SnapshotFrequency=json_data.get("SnapshotFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotPoliciesDefinition = SnapshotPoliciesDefinition


