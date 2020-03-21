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
    Global: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Organization: Optional[str]
    PoliciesPath: Optional[str]
    PolicyIds: Optional[Sequence[str]]
    WorkspaceExternalIds: Optional[Sequence[str]]
    VcsRepo: Optional[Sequence["_VcsRepo"]]

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
            Global=json_data.get("Global"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Organization=json_data.get("Organization"),
            PoliciesPath=json_data.get("PoliciesPath"),
            PolicyIds=json_data.get("PolicyIds"),
            WorkspaceExternalIds=json_data.get("WorkspaceExternalIds"),
            VcsRepo=json_data.get("VcsRepo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class VcsRepo:
    Branch: Optional[str]
    Identifier: Optional[str]
    IngressSubmodules: Optional[bool]
    OauthTokenId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VcsRepo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VcsRepo"]:
        if not json_data:
            return None
        return cls(
            Branch=json_data.get("Branch"),
            Identifier=json_data.get("Identifier"),
            IngressSubmodules=json_data.get("IngressSubmodules"),
            OauthTokenId=json_data.get("OauthTokenId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VcsRepo = VcsRepo


