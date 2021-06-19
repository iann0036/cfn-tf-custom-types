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
    EnableIpMasquerade: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    NatType: Optional[str]
    NetworkId: Optional[str]
    Org: Optional[str]
    VappId: Optional[str]
    Vdc: Optional[str]
    Rule: Optional[Sequence["_RuleDefinition"]]

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
            EnableIpMasquerade=json_data.get("EnableIpMasquerade"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            NatType=json_data.get("NatType"),
            NetworkId=json_data.get("NetworkId"),
            Org=json_data.get("Org"),
            VappId=json_data.get("VappId"),
            Vdc=json_data.get("Vdc"),
            Rule=deserialize_list(json_data.get("Rule"), RuleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RuleDefinition(BaseModel):
    ExternalIp: Optional[str]
    ExternalPort: Optional[float]
    ForwardToPort: Optional[float]
    MappingMode: Optional[str]
    Protocol: Optional[str]
    VmId: Optional[str]
    VmNicId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            ExternalIp=json_data.get("ExternalIp"),
            ExternalPort=json_data.get("ExternalPort"),
            ForwardToPort=json_data.get("ForwardToPort"),
            MappingMode=json_data.get("MappingMode"),
            Protocol=json_data.get("Protocol"),
            VmId=json_data.get("VmId"),
            VmNicId=json_data.get("VmNicId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


