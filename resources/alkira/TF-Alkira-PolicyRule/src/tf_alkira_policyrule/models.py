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
    ApplicationFamilyList: Optional[Sequence[str]]
    ApplicationList: Optional[Sequence[str]]
    Description: Optional[str]
    Dscp: Optional[str]
    DstIp: Optional[str]
    DstPortList: Optional[Sequence[str]]
    Id: Optional[str]
    InternetApplicationId: Optional[float]
    Name: Optional[str]
    Protocol: Optional[str]
    RuleAction: Optional[str]
    RuleActionServiceTypeList: Optional[Sequence[str]]
    RuleId: Optional[float]
    SrcIp: Optional[str]
    SrcPortList: Optional[Sequence[str]]

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
            ApplicationFamilyList=json_data.get("ApplicationFamilyList"),
            ApplicationList=json_data.get("ApplicationList"),
            Description=json_data.get("Description"),
            Dscp=json_data.get("Dscp"),
            DstIp=json_data.get("DstIp"),
            DstPortList=json_data.get("DstPortList"),
            Id=json_data.get("Id"),
            InternetApplicationId=json_data.get("InternetApplicationId"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            RuleAction=json_data.get("RuleAction"),
            RuleActionServiceTypeList=json_data.get("RuleActionServiceTypeList"),
            RuleId=json_data.get("RuleId"),
            SrcIp=json_data.get("SrcIp"),
            SrcPortList=json_data.get("SrcPortList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


