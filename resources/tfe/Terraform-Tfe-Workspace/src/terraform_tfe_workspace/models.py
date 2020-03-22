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
    AutoApply: Optional[bool]
    ExternalId: Optional[str]
    FileTriggersEnabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Operations: Optional[bool]
    Organization: Optional[str]
    QueueAllRuns: Optional[bool]
    SshKeyId: Optional[str]
    TerraformVersion: Optional[str]
    TriggerPrefixes: Optional[Sequence[str]]
    WorkingDirectory: Optional[str]
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
            AutoApply=json_data.get("AutoApply"),
            ExternalId=json_data.get("ExternalId"),
            FileTriggersEnabled=json_data.get("FileTriggersEnabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Operations=json_data.get("Operations"),
            Organization=json_data.get("Organization"),
            QueueAllRuns=json_data.get("QueueAllRuns"),
            SshKeyId=json_data.get("SshKeyId"),
            TerraformVersion=json_data.get("TerraformVersion"),
            TriggerPrefixes=json_data.get("TriggerPrefixes"),
            WorkingDirectory=json_data.get("WorkingDirectory"),
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


