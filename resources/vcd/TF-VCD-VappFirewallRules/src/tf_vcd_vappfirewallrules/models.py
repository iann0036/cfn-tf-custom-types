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
    DefaultAction: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    LogDefaultAction: Optional[bool]
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
            DefaultAction=json_data.get("DefaultAction"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            LogDefaultAction=json_data.get("LogDefaultAction"),
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
    DestinationIp: Optional[str]
    DestinationPort: Optional[str]
    DestinationVmId: Optional[str]
    DestinationVmIpType: Optional[str]
    DestinationVmNicId: Optional[float]
    EnableLogging: Optional[bool]
    Enabled: Optional[bool]
    Name: Optional[str]
    Policy: Optional[str]
    Protocol: Optional[str]
    SourceIp: Optional[str]
    SourcePort: Optional[str]
    SourceVmId: Optional[str]
    SourceVmIpType: Optional[str]
    SourceVmNicId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RuleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RuleDefinition"]:
        if not json_data:
            return None
        return cls(
            DestinationIp=json_data.get("DestinationIp"),
            DestinationPort=json_data.get("DestinationPort"),
            DestinationVmId=json_data.get("DestinationVmId"),
            DestinationVmIpType=json_data.get("DestinationVmIpType"),
            DestinationVmNicId=json_data.get("DestinationVmNicId"),
            EnableLogging=json_data.get("EnableLogging"),
            Enabled=json_data.get("Enabled"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            Protocol=json_data.get("Protocol"),
            SourceIp=json_data.get("SourceIp"),
            SourcePort=json_data.get("SourcePort"),
            SourceVmId=json_data.get("SourceVmId"),
            SourceVmIpType=json_data.get("SourceVmIpType"),
            SourceVmNicId=json_data.get("SourceVmNicId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RuleDefinition = RuleDefinition


