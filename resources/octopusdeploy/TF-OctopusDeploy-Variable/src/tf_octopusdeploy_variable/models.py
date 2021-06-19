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
    EncryptedValue: Optional[str]
    Id: Optional[str]
    IsEditable: Optional[bool]
    IsSensitive: Optional[bool]
    KeyFingerprint: Optional[str]
    Name: Optional[str]
    OwnerId: Optional[str]
    PgpKey: Optional[str]
    ProjectId: Optional[str]
    SensitiveValue: Optional[str]
    Type: Optional[str]
    Value: Optional[str]
    Prompt: Optional[Sequence["_PromptDefinition"]]
    Scope: Optional[Sequence["_ScopeDefinition"]]

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
            EncryptedValue=json_data.get("EncryptedValue"),
            Id=json_data.get("Id"),
            IsEditable=json_data.get("IsEditable"),
            IsSensitive=json_data.get("IsSensitive"),
            KeyFingerprint=json_data.get("KeyFingerprint"),
            Name=json_data.get("Name"),
            OwnerId=json_data.get("OwnerId"),
            PgpKey=json_data.get("PgpKey"),
            ProjectId=json_data.get("ProjectId"),
            SensitiveValue=json_data.get("SensitiveValue"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
            Prompt=deserialize_list(json_data.get("Prompt"), PromptDefinition),
            Scope=deserialize_list(json_data.get("Scope"), ScopeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PromptDefinition(BaseModel):
    Description: Optional[str]
    IsRequired: Optional[bool]
    Label: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PromptDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PromptDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            IsRequired=json_data.get("IsRequired"),
            Label=json_data.get("Label"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PromptDefinition = PromptDefinition


@dataclass
class ScopeDefinition(BaseModel):
    Actions: Optional[Sequence[str]]
    Channels: Optional[Sequence[str]]
    Environments: Optional[Sequence[str]]
    Machines: Optional[Sequence[str]]
    Roles: Optional[Sequence[str]]
    TenantTags: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ScopeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScopeDefinition"]:
        if not json_data:
            return None
        return cls(
            Actions=json_data.get("Actions"),
            Channels=json_data.get("Channels"),
            Environments=json_data.get("Environments"),
            Machines=json_data.get("Machines"),
            Roles=json_data.get("Roles"),
            TenantTags=json_data.get("TenantTags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScopeDefinition = ScopeDefinition


