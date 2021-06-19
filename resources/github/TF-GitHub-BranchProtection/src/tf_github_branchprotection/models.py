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
    AllowsDeletions: Optional[bool]
    AllowsForcePushes: Optional[bool]
    EnforceAdmins: Optional[bool]
    Id: Optional[str]
    Pattern: Optional[str]
    PushRestrictions: Optional[Sequence[str]]
    RepositoryId: Optional[str]
    RequireSignedCommits: Optional[bool]
    RequiredPullRequestReviews: Optional[Sequence["_RequiredPullRequestReviewsDefinition"]]
    RequiredStatusChecks: Optional[Sequence["_RequiredStatusChecksDefinition"]]

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
            AllowsDeletions=json_data.get("AllowsDeletions"),
            AllowsForcePushes=json_data.get("AllowsForcePushes"),
            EnforceAdmins=json_data.get("EnforceAdmins"),
            Id=json_data.get("Id"),
            Pattern=json_data.get("Pattern"),
            PushRestrictions=json_data.get("PushRestrictions"),
            RepositoryId=json_data.get("RepositoryId"),
            RequireSignedCommits=json_data.get("RequireSignedCommits"),
            RequiredPullRequestReviews=deserialize_list(json_data.get("RequiredPullRequestReviews"), RequiredPullRequestReviewsDefinition),
            RequiredStatusChecks=deserialize_list(json_data.get("RequiredStatusChecks"), RequiredStatusChecksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequiredPullRequestReviewsDefinition(BaseModel):
    DismissStaleReviews: Optional[bool]
    DismissalRestrictions: Optional[Sequence[str]]
    RequireCodeOwnerReviews: Optional[bool]
    RequiredApprovingReviewCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredPullRequestReviewsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredPullRequestReviewsDefinition"]:
        if not json_data:
            return None
        return cls(
            DismissStaleReviews=json_data.get("DismissStaleReviews"),
            DismissalRestrictions=json_data.get("DismissalRestrictions"),
            RequireCodeOwnerReviews=json_data.get("RequireCodeOwnerReviews"),
            RequiredApprovingReviewCount=json_data.get("RequiredApprovingReviewCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredPullRequestReviewsDefinition = RequiredPullRequestReviewsDefinition


@dataclass
class RequiredStatusChecksDefinition(BaseModel):
    Contexts: Optional[Sequence[str]]
    Strict: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredStatusChecksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredStatusChecksDefinition"]:
        if not json_data:
            return None
        return cls(
            Contexts=json_data.get("Contexts"),
            Strict=json_data.get("Strict"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredStatusChecksDefinition = RequiredStatusChecksDefinition


