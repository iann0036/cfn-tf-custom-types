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
    BaseLogEnabled: Optional[bool]
    BasePolicy: Optional[str]
    GwName: Optional[str]
    Id: Optional[str]
    ManageFirewallPolicies: Optional[bool]
    Policy: Optional[Sequence["_PolicyDefinition"]]

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
            BaseLogEnabled=json_data.get("BaseLogEnabled"),
            BasePolicy=json_data.get("BasePolicy"),
            GwName=json_data.get("GwName"),
            Id=json_data.get("Id"),
            ManageFirewallPolicies=json_data.get("ManageFirewallPolicies"),
            Policy=deserialize_list(json_data.get("Policy"), PolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyDefinition(BaseModel):
    Action: Optional[str]
    Description: Optional[str]
    DstIp: Optional[str]
    LogEnabled: Optional[bool]
    Port: Optional[str]
    Protocol: Optional[str]
    SrcIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Description=json_data.get("Description"),
            DstIp=json_data.get("DstIp"),
            LogEnabled=json_data.get("LogEnabled"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            SrcIp=json_data.get("SrcIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyDefinition = PolicyDefinition


