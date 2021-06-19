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
    AgentPoolId: Optional[str]
    AllowDestroyPlan: Optional[bool]
    AutoApply: Optional[bool]
    Description: Optional[str]
    ExecutionMode: Optional[str]
    FileTriggersEnabled: Optional[bool]
    GlobalRemoteState: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Operations: Optional[bool]
    Organization: Optional[str]
    QueueAllRuns: Optional[bool]
    RemoteStateConsumerIds: Optional[Sequence[str]]
    SpeculativeEnabled: Optional[bool]
    SshKeyId: Optional[str]
    TerraformVersion: Optional[str]
    TriggerPrefixes: Optional[Sequence[str]]
    WorkingDirectory: Optional[str]
    VcsRepo: Optional[Sequence["_VcsRepoDefinition"]]

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
            AgentPoolId=json_data.get("AgentPoolId"),
            AllowDestroyPlan=json_data.get("AllowDestroyPlan"),
            AutoApply=json_data.get("AutoApply"),
            Description=json_data.get("Description"),
            ExecutionMode=json_data.get("ExecutionMode"),
            FileTriggersEnabled=json_data.get("FileTriggersEnabled"),
            GlobalRemoteState=json_data.get("GlobalRemoteState"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Operations=json_data.get("Operations"),
            Organization=json_data.get("Organization"),
            QueueAllRuns=json_data.get("QueueAllRuns"),
            RemoteStateConsumerIds=json_data.get("RemoteStateConsumerIds"),
            SpeculativeEnabled=json_data.get("SpeculativeEnabled"),
            SshKeyId=json_data.get("SshKeyId"),
            TerraformVersion=json_data.get("TerraformVersion"),
            TriggerPrefixes=json_data.get("TriggerPrefixes"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
            VcsRepo=deserialize_list(json_data.get("VcsRepo"), VcsRepoDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VcsRepoDefinition(BaseModel):
    Branch: Optional[str]
    Identifier: Optional[str]
    IngressSubmodules: Optional[bool]
    OauthTokenId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcsRepoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcsRepoDefinition"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            Identifier=json_data.get("Identifier"),
            IngressSubmodules=json_data.get("IngressSubmodules"),
            OauthTokenId=json_data.get("OauthTokenId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcsRepoDefinition = VcsRepoDefinition


