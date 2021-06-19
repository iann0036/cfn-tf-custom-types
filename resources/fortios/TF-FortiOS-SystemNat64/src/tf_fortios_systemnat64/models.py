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
    AlwaysSynthesizeAaaaRecord: Optional[str]
    DynamicSortSubtable: Optional[str]
    GenerateIpv6FragmentHeader: Optional[str]
    Id: Optional[str]
    Nat46ForceIpv4PacketForwarding: Optional[str]
    Nat64Prefix: Optional[str]
    SecondaryPrefixStatus: Optional[str]
    Status: Optional[str]
    Vdomparam: Optional[str]
    SecondaryPrefix: Optional[Sequence["_SecondaryPrefixDefinition"]]

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
            AlwaysSynthesizeAaaaRecord=json_data.get("AlwaysSynthesizeAaaaRecord"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            GenerateIpv6FragmentHeader=json_data.get("GenerateIpv6FragmentHeader"),
            Id=json_data.get("Id"),
            Nat46ForceIpv4PacketForwarding=json_data.get("Nat46ForceIpv4PacketForwarding"),
            Nat64Prefix=json_data.get("Nat64Prefix"),
            SecondaryPrefixStatus=json_data.get("SecondaryPrefixStatus"),
            Status=json_data.get("Status"),
            Vdomparam=json_data.get("Vdomparam"),
            SecondaryPrefix=deserialize_list(json_data.get("SecondaryPrefix"), SecondaryPrefixDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SecondaryPrefixDefinition(BaseModel):
    Name: Optional[str]
    Nat64Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryPrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryPrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Nat64Prefix=json_data.get("Nat64Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryPrefixDefinition = SecondaryPrefixDefinition


