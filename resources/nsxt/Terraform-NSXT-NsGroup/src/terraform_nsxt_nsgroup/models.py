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
    Description: Optional[str]
    DisplayName: Optional[str]
    Revision: Optional[float]
    Member: Optional[Sequence["_Member"]]
    MembershipCriteria: Optional[Sequence["_MembershipCriteria"]]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Revision=json_data.get("Revision"),
            Member=json_data.get("Member"),
            MembershipCriteria=json_data.get("MembershipCriteria"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Member:
    TargetType: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Member"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Member"]:
        if not json_data:
            return None
        return cls(
            TargetType=json_data.get("TargetType"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Member = Member


@dataclass
class MembershipCriteria:
    Scope: Optional[str]
    ScopeOp: Optional[str]
    Tag: Optional[str]
    TagOp: Optional[str]
    TargetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembershipCriteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembershipCriteria"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            ScopeOp=json_data.get("ScopeOp"),
            Tag=json_data.get("Tag"),
            TagOp=json_data.get("TagOp"),
            TargetType=json_data.get("TargetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembershipCriteria = MembershipCriteria


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


