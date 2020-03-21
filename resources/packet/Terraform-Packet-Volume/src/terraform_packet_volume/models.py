# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    Attachments: Optional[Sequence["_Attachments"]]
    BillingCycle: Optional[str]
    Created: Optional[str]
    Description: Optional[str]
    Facility: Optional[str]
    Locked: Optional[bool]
    Name: Optional[str]
    Plan: Optional[str]
    ProjectId: Optional[str]
    Size: Optional[float]
    State: Optional[str]
    Updated: Optional[str]
    SnapshotPolicies: Optional[Sequence["_SnapshotPolicies"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Attachments=json_data.get("Attachments"),
            BillingCycle=json_data.get("BillingCycle"),
            Created=json_data.get("Created"),
            Description=json_data.get("Description"),
            Facility=json_data.get("Facility"),
            Locked=json_data.get("Locked"),
            Name=json_data.get("Name"),
            Plan=json_data.get("Plan"),
            ProjectId=json_data.get("ProjectId"),
            Size=json_data.get("Size"),
            State=json_data.get("State"),
            Updated=json_data.get("Updated"),
            SnapshotPolicies=json_data.get("SnapshotPolicies"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Attachments:
    Href: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Attachments"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Attachments"]:
        if not json_data:
            return None
        return cls(
            Href=json_data.get("Href"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Attachments = Attachments


@dataclass
class SnapshotPolicies:
    SnapshotCount: Optional[float]
    SnapshotFrequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnapshotPolicies"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnapshotPolicies"]:
        if not json_data:
            return None
        return cls(
            SnapshotCount=json_data.get("SnapshotCount"),
            SnapshotFrequency=json_data.get("SnapshotFrequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnapshotPolicies = SnapshotPolicies


