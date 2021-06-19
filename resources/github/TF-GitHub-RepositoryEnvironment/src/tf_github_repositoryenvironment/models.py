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
    Environment: Optional[str]
    Id: Optional[str]
    Repository: Optional[str]
    WaitTimer: Optional[float]
    DeploymentBranchPolicy: Optional[Sequence["_DeploymentBranchPolicyDefinition"]]
    Reviewers: Optional[Sequence["_ReviewersDefinition"]]

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
            Environment=json_data.get("Environment"),
            Id=json_data.get("Id"),
            Repository=json_data.get("Repository"),
            WaitTimer=json_data.get("WaitTimer"),
            DeploymentBranchPolicy=deserialize_list(json_data.get("DeploymentBranchPolicy"), DeploymentBranchPolicyDefinition),
            Reviewers=deserialize_list(json_data.get("Reviewers"), ReviewersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeploymentBranchPolicyDefinition(BaseModel):
    CustomBranchPolicies: Optional[bool]
    ProtectedBranches: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_DeploymentBranchPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeploymentBranchPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomBranchPolicies=json_data.get("CustomBranchPolicies"),
            ProtectedBranches=json_data.get("ProtectedBranches"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeploymentBranchPolicyDefinition = DeploymentBranchPolicyDefinition


@dataclass
class ReviewersDefinition(BaseModel):
    Teams: Optional[Sequence[float]]
    Users: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_ReviewersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReviewersDefinition"]:
        if not json_data:
            return None
        return cls(
            Teams=json_data.get("Teams"),
            Users=json_data.get("Users"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReviewersDefinition = ReviewersDefinition


