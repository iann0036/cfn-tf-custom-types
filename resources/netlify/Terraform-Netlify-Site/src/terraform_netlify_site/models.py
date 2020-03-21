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
    AccountName: Optional[str]
    AccountSlug: Optional[str]
    CustomDomain: Optional[str]
    DeployUrl: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Repo: Optional[Sequence["_Repo"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountName=json_data.get("AccountName"),
            AccountSlug=json_data.get("AccountSlug"),
            CustomDomain=json_data.get("CustomDomain"),
            DeployUrl=json_data.get("DeployUrl"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Repo=json_data.get("Repo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Repo:
    Command: Optional[str]
    DeployKeyId: Optional[str]
    Dir: Optional[str]
    Provider: Optional[str]
    RepoBranch: Optional[str]
    RepoPath: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Repo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Repo"]:
        if not json_data:
            return None
        return cls(
            Command=json_data.get("Command"),
            DeployKeyId=json_data.get("DeployKeyId"),
            Dir=json_data.get("Dir"),
            Provider=json_data.get("Provider"),
            RepoBranch=json_data.get("RepoBranch"),
            RepoPath=json_data.get("RepoPath"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Repo = Repo


