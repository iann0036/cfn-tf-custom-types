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
    Branch: Optional[str]
    EnforceAdmins: Optional[bool]
    Etag: Optional[str]
    Id: Optional[str]
    Repository: Optional[str]
    RequireSignedCommits: Optional[bool]
    RequiredPullRequestReviews: Optional[Sequence["_RequiredPullRequestReviewsDefinition"]]
    RequiredStatusChecks: Optional[Sequence["_RequiredStatusChecksDefinition"]]
    Restrictions: Optional[Sequence["_RestrictionsDefinition"]]

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
            Branch=json_data.get("Branch"),
            EnforceAdmins=json_data.get("EnforceAdmins"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Repository=json_data.get("Repository"),
            RequireSignedCommits=json_data.get("RequireSignedCommits"),
            RequiredPullRequestReviews=deserialize_list(json_data.get("RequiredPullRequestReviews"), RequiredPullRequestReviewsDefinition),
            RequiredStatusChecks=deserialize_list(json_data.get("RequiredStatusChecks"), RequiredStatusChecksDefinition),
            Restrictions=deserialize_list(json_data.get("Restrictions"), RestrictionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequiredPullRequestReviewsDefinition(BaseModel):
    DismissStaleReviews: Optional[bool]
    DismissalTeams: Optional[Sequence[str]]
    DismissalUsers: Optional[Sequence[str]]
    IncludeAdmins: Optional[bool]
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
            DismissalTeams=json_data.get("DismissalTeams"),
            DismissalUsers=json_data.get("DismissalUsers"),
            IncludeAdmins=json_data.get("IncludeAdmins"),
            RequireCodeOwnerReviews=json_data.get("RequireCodeOwnerReviews"),
            RequiredApprovingReviewCount=json_data.get("RequiredApprovingReviewCount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredPullRequestReviewsDefinition = RequiredPullRequestReviewsDefinition


@dataclass
class RequiredStatusChecksDefinition(BaseModel):
    Contexts: Optional[Sequence[str]]
    IncludeAdmins: Optional[bool]
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
            IncludeAdmins=json_data.get("IncludeAdmins"),
            Strict=json_data.get("Strict"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredStatusChecksDefinition = RequiredStatusChecksDefinition


@dataclass
class RestrictionsDefinition(BaseModel):
    Apps: Optional[Sequence[str]]
    Teams: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_RestrictionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RestrictionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Apps=json_data.get("Apps"),
            Teams=json_data.get("Teams"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RestrictionsDefinition = RestrictionsDefinition


