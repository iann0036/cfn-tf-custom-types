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
    DefaultProjectId: Optional[str]
    Description: Optional[str]
    DomainId: Optional[str]
    Enabled: Optional[bool]
    Extra: Optional[Sequence["_Extra"]]
    Id: Optional[str]
    IgnoreChangePasswordUponFirstUse: Optional[bool]
    IgnoreLockoutFailureAttempts: Optional[bool]
    IgnorePasswordExpiry: Optional[bool]
    MultiFactorAuthEnabled: Optional[bool]
    Name: Optional[str]
    Password: Optional[str]
    Region: Optional[str]
    MultiFactorAuthRule: Optional[Sequence["_MultiFactorAuthRule"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DefaultProjectId=json_data.get("DefaultProjectId"),
            Description=json_data.get("Description"),
            DomainId=json_data.get("DomainId"),
            Enabled=json_data.get("Enabled"),
            Extra=json_data.get("Extra"),
            Id=json_data.get("Id"),
            IgnoreChangePasswordUponFirstUse=json_data.get("IgnoreChangePasswordUponFirstUse"),
            IgnoreLockoutFailureAttempts=json_data.get("IgnoreLockoutFailureAttempts"),
            IgnorePasswordExpiry=json_data.get("IgnorePasswordExpiry"),
            MultiFactorAuthEnabled=json_data.get("MultiFactorAuthEnabled"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Region=json_data.get("Region"),
            MultiFactorAuthRule=json_data.get("MultiFactorAuthRule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Extra:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Extra"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Extra"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Extra = Extra


@dataclass
class MultiFactorAuthRule:
    Rule: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MultiFactorAuthRule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiFactorAuthRule"]:
        if not json_data:
            return None
        return cls(
            Rule=json_data.get("Rule"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiFactorAuthRule = MultiFactorAuthRule


