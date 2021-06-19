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
    DnsSearchList: Optional[str]
    DnsServer1: Optional[str]
    DnsServer2: Optional[str]
    DnsServer3: Optional[str]
    DnsServer4: Optional[str]
    DnsService: Optional[str]
    Domain: Optional[str]
    DynamicSortSubtable: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    IpMode: Optional[str]
    LeaseTime: Optional[float]
    Option1: Optional[str]
    Option2: Optional[str]
    Option3: Optional[str]
    PrefixMode: Optional[str]
    RapidCommit: Optional[str]
    Status: Optional[str]
    Subnet: Optional[str]
    UpstreamInterface: Optional[str]
    Vdomparam: Optional[str]
    IpRange: Optional[Sequence["_IpRangeDefinition"]]
    PrefixRange: Optional[Sequence["_PrefixRangeDefinition"]]

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
            DnsSearchList=json_data.get("DnsSearchList"),
            DnsServer1=json_data.get("DnsServer1"),
            DnsServer2=json_data.get("DnsServer2"),
            DnsServer3=json_data.get("DnsServer3"),
            DnsServer4=json_data.get("DnsServer4"),
            DnsService=json_data.get("DnsService"),
            Domain=json_data.get("Domain"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpMode=json_data.get("IpMode"),
            LeaseTime=json_data.get("LeaseTime"),
            Option1=json_data.get("Option1"),
            Option2=json_data.get("Option2"),
            Option3=json_data.get("Option3"),
            PrefixMode=json_data.get("PrefixMode"),
            RapidCommit=json_data.get("RapidCommit"),
            Status=json_data.get("Status"),
            Subnet=json_data.get("Subnet"),
            UpstreamInterface=json_data.get("UpstreamInterface"),
            Vdomparam=json_data.get("Vdomparam"),
            IpRange=deserialize_list(json_data.get("IpRange"), IpRangeDefinition),
            PrefixRange=deserialize_list(json_data.get("PrefixRange"), PrefixRangeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class IpRangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpRangeDefinition = IpRangeDefinition


@dataclass
class PrefixRangeDefinition(BaseModel):
    EndPrefix: Optional[str]
    Id: Optional[float]
    PrefixLength: Optional[float]
    StartPrefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndPrefix=json_data.get("EndPrefix"),
            Id=json_data.get("Id"),
            PrefixLength=json_data.get("PrefixLength"),
            StartPrefix=json_data.get("StartPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixRangeDefinition = PrefixRangeDefinition


