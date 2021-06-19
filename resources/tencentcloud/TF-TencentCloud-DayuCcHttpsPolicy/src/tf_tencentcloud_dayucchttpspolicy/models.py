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
    CreateTime: Optional[str]
    Domain: Optional[str]
    Id: Optional[str]
    IpList: Optional[Sequence[str]]
    Name: Optional[str]
    PolicyId: Optional[str]
    ResourceId: Optional[str]
    ResourceType: Optional[str]
    RuleId: Optional[str]
    Switch: Optional[bool]
    RuleList: Optional[Sequence["_RuleListDefinition"]]

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
            CreateTime=json_data.get("CreateTime"),
            Domain=json_data.get("Domain"),
            Id=json_data.get("Id"),
            IpList=json_data.get("IpList"),
            Name=json_data.get("Name"),
            PolicyId=json_data.get("PolicyId"),
            ResourceId=json_data.get("ResourceId"),
            ResourceType=json_data.get("ResourceType"),
            RuleId=json_data.get("RuleId"),
            Switch=json_data.get("Switch"),
            RuleList=deserialize_list(json_data.get("RuleList"), RuleListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleListDefinition(BaseModel):
    Operator: Optional[str]
    Skey: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RuleListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleListDefinition"]:
        if not json_data:
            return None
        return cls(
            Operator=json_data.get("Operator"),
            Skey=json_data.get("Skey"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleListDefinition = RuleListDefinition


