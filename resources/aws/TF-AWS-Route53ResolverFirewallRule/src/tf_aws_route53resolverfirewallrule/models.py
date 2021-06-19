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
    Action: Optional[str]
    BlockOverrideDnsType: Optional[str]
    BlockOverrideDomain: Optional[str]
    BlockOverrideTtl: Optional[float]
    BlockResponse: Optional[str]
    FirewallDomainListId: Optional[str]
    FirewallRuleGroupId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]

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
            Action=json_data.get("Action"),
            BlockOverrideDnsType=json_data.get("BlockOverrideDnsType"),
            BlockOverrideDomain=json_data.get("BlockOverrideDomain"),
            BlockOverrideTtl=json_data.get("BlockOverrideTtl"),
            BlockResponse=json_data.get("BlockResponse"),
            FirewallDomainListId=json_data.get("FirewallDomainListId"),
            FirewallRuleGroupId=json_data.get("FirewallRuleGroupId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


