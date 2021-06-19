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
    Description: Optional[str]
    Global: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Organization: Optional[str]
    PoliciesPath: Optional[str]
    PolicyIds: Optional[Sequence[str]]
    WorkspaceIds: Optional[Sequence[str]]
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
            Description=json_data.get("Description"),
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Organization=json_data.get("Organization"),
            PoliciesPath=json_data.get("PoliciesPath"),
            PolicyIds=json_data.get("PolicyIds"),
            WorkspaceIds=json_data.get("WorkspaceIds"),
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


