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
    AutomaticReviewApps: Optional[bool]
    BaseName: Optional[str]
    DestroyStaleApps: Optional[bool]
    Id: Optional[str]
    OrgRepo: Optional[str]
    PipelineId: Optional[str]
    RepoId: Optional[float]
    StaleDays: Optional[float]
    WaitForCi: Optional[bool]
    DeployTarget: Optional[Sequence["_DeployTargetDefinition"]]

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
            AutomaticReviewApps=json_data.get("AutomaticReviewApps"),
            BaseName=json_data.get("BaseName"),
            DestroyStaleApps=json_data.get("DestroyStaleApps"),
            Id=json_data.get("Id"),
            OrgRepo=json_data.get("OrgRepo"),
            PipelineId=json_data.get("PipelineId"),
            RepoId=json_data.get("RepoId"),
            StaleDays=json_data.get("StaleDays"),
            WaitForCi=json_data.get("WaitForCi"),
            DeployTarget=deserialize_list(json_data.get("DeployTarget"), DeployTargetDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeployTargetDefinition(BaseModel):
    Id: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeployTargetDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeployTargetDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeployTargetDefinition = DeployTargetDefinition


