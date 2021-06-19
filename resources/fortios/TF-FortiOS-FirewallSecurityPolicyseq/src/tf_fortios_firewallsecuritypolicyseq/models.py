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
    AlterPosition: Optional[str]
    Comment: Optional[str]
    EnableStateChecking: Optional[bool]
    Id: Optional[str]
    PolicyDstId: Optional[float]
    PolicySrcId: Optional[float]
    StatePolicyList: Optional[Sequence["_StatePolicyListDefinition"]]
    StatePolicySrcdstPos: Optional[str]
    Vdomparam: Optional[str]

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
            AlterPosition=json_data.get("AlterPosition"),
            Comment=json_data.get("Comment"),
            EnableStateChecking=json_data.get("EnableStateChecking"),
            Id=json_data.get("Id"),
            PolicyDstId=json_data.get("PolicyDstId"),
            PolicySrcId=json_data.get("PolicySrcId"),
            StatePolicyList=deserialize_list(json_data.get("StatePolicyList"), StatePolicyListDefinition),
            StatePolicySrcdstPos=json_data.get("StatePolicySrcdstPos"),
            Vdomparam=json_data.get("Vdomparam"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class StatePolicyListDefinition(BaseModel):
    Action: Optional[str]
    Name: Optional[str]
    Policyid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StatePolicyListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatePolicyListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Name=json_data.get("Name"),
            Policyid=json_data.get("Policyid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatePolicyListDefinition = StatePolicyListDefinition


