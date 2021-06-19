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
    AccessKeyId: Optional[str]
    AccountId: Optional[str]
    AccountSpecificNamespaceRules: Optional[Sequence["_AccountSpecificNamespaceRulesDefinition"]]
    ExcludedRegions: Optional[Sequence[str]]
    ExternalId: Optional[str]
    FilterTags: Optional[Sequence[str]]
    HostTags: Optional[Sequence[str]]
    Id: Optional[str]
    RoleName: Optional[str]
    SecretAccessKey: Optional[str]

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
            AccessKeyId=json_data.get("AccessKeyId"),
            AccountId=json_data.get("AccountId"),
            AccountSpecificNamespaceRules=deserialize_list(json_data.get("AccountSpecificNamespaceRules"), AccountSpecificNamespaceRulesDefinition),
            ExcludedRegions=json_data.get("ExcludedRegions"),
            ExternalId=json_data.get("ExternalId"),
            FilterTags=json_data.get("FilterTags"),
            HostTags=json_data.get("HostTags"),
            Id=json_data.get("Id"),
            RoleName=json_data.get("RoleName"),
            SecretAccessKey=json_data.get("SecretAccessKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AccountSpecificNamespaceRulesDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_AccountSpecificNamespaceRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccountSpecificNamespaceRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccountSpecificNamespaceRulesDefinition = AccountSpecificNamespaceRulesDefinition


