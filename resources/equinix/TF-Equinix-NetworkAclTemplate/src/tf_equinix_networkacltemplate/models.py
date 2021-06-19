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
    DeviceAclStatus: Optional[str]
    DeviceId: Optional[str]
    Id: Optional[str]
    MetroCode: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]
    InboundRule: Optional[Sequence["_InboundRuleDefinition"]]

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
            DeviceAclStatus=json_data.get("DeviceAclStatus"),
            DeviceId=json_data.get("DeviceId"),
            Id=json_data.get("Id"),
            MetroCode=json_data.get("MetroCode"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
            InboundRule=deserialize_list(json_data.get("InboundRule"), InboundRuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InboundRuleDefinition(BaseModel):
    DstPort: Optional[str]
    Protocol: Optional[str]
    SrcPort: Optional[str]
    Subnets: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_InboundRuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InboundRuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DstPort=json_data.get("DstPort"),
            Protocol=json_data.get("Protocol"),
            SrcPort=json_data.get("SrcPort"),
            Subnets=json_data.get("Subnets"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InboundRuleDefinition = InboundRuleDefinition


