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
    Branch: Optional[str]
    EnforceAdmins: Optional[bool]
    Etag: Optional[str]
    Id: Optional[str]
    Repository: Optional[str]
    RequireSignedCommits: Optional[bool]
    RequiredPullRequestReviews: Optional[Sequence["_RequiredPullRequestReviews"]]
    RequiredStatusChecks: Optional[Sequence["_RequiredStatusChecks"]]
    Restrictions: Optional[Sequence["_Restrictions"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Branch=json_data.get("Branch"),
            EnforceAdmins=json_data.get("EnforceAdmins"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            Repository=json_data.get("Repository"),
            RequireSignedCommits=json_data.get("RequireSignedCommits"),
            RequiredPullRequestReviews=json_data.get("RequiredPullRequestReviews"),
            RequiredStatusChecks=json_data.get("RequiredStatusChecks"),
            Restrictions=json_data.get("Restrictions"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RequiredPullRequestReviews:
    DismissStaleReviews: Optional[bool]
    DismissalTeams: Optional[Sequence[str]]
    DismissalUsers: Optional[Sequence[str]]
    IncludeAdmins: Optional[bool]
    RequireCodeOwnerReviews: Optional[bool]
    RequiredApprovingReviewCount: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredPullRequestReviews"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredPullRequestReviews"]:
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
_RequiredPullRequestReviews = RequiredPullRequestReviews


@dataclass
class RequiredStatusChecks:
    Contexts: Optional[Sequence[str]]
    IncludeAdmins: Optional[bool]
    Strict: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredStatusChecks"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredStatusChecks"]:
        if not json_data:
            return None
        return cls(
            Contexts=json_data.get("Contexts"),
            IncludeAdmins=json_data.get("IncludeAdmins"),
            Strict=json_data.get("Strict"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredStatusChecks = RequiredStatusChecks


@dataclass
class Restrictions:
    Teams: Optional[Sequence[str]]
    Users: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Restrictions"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Restrictions"]:
        if not json_data:
            return None
        return cls(
            Teams=json_data.get("Teams"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Restrictions = Restrictions


