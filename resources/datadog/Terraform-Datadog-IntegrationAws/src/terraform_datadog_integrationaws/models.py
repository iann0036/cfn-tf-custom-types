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
    AccountId: Optional[str]
    AccountSpecificNamespaceRules: Optional[Sequence["_AccountSpecificNamespaceRules"]]
    ExternalId: Optional[str]
    FilterTags: Optional[Sequence[str]]
    HostTags: Optional[Sequence[str]]
    RoleName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccountId=json_data.get("AccountId"),
            AccountSpecificNamespaceRules=json_data.get("AccountSpecificNamespaceRules"),
            ExternalId=json_data.get("ExternalId"),
            FilterTags=json_data.get("FilterTags"),
            HostTags=json_data.get("HostTags"),
            RoleName=json_data.get("RoleName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountSpecificNamespaceRules:
    Key: Optional[str]
    Value: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccountSpecificNamespaceRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountSpecificNamespaceRules"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountSpecificNamespaceRules = AccountSpecificNamespaceRules


