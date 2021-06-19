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
    AllowTransfer: Optional[str]
    Authoritative: Optional[str]
    Contact: Optional[str]
    Domain: Optional[str]
    DynamicSortSubtable: Optional[str]
    Forwarder: Optional[str]
    Id: Optional[str]
    IpMaster: Optional[str]
    IpPrimary: Optional[str]
    Name: Optional[str]
    PrimaryName: Optional[str]
    RrMax: Optional[float]
    SourceIp: Optional[str]
    Status: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    Vdomparam: Optional[str]
    View: Optional[str]
    DnsEntry: Optional[Sequence["_DnsEntryDefinition"]]

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
            AllowTransfer=json_data.get("AllowTransfer"),
            Authoritative=json_data.get("Authoritative"),
            Contact=json_data.get("Contact"),
            Domain=json_data.get("Domain"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Forwarder=json_data.get("Forwarder"),
            Id=json_data.get("Id"),
            IpMaster=json_data.get("IpMaster"),
            IpPrimary=json_data.get("IpPrimary"),
            Name=json_data.get("Name"),
            PrimaryName=json_data.get("PrimaryName"),
            RrMax=json_data.get("RrMax"),
            SourceIp=json_data.get("SourceIp"),
            Status=json_data.get("Status"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Vdomparam=json_data.get("Vdomparam"),
            View=json_data.get("View"),
            DnsEntry=deserialize_list(json_data.get("DnsEntry"), DnsEntryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsEntryDefinition(BaseModel):
    CanonicalName: Optional[str]
    Hostname: Optional[str]
    Id: Optional[float]
    Ip: Optional[str]
    Ipv6: Optional[str]
    Preference: Optional[float]
    Status: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsEntryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsEntryDefinition"]:
        if not json_data:
            return None
        return cls(
            CanonicalName=json_data.get("CanonicalName"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Ipv6=json_data.get("Ipv6"),
            Preference=json_data.get("Preference"),
            Status=json_data.get("Status"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsEntryDefinition = DnsEntryDefinition


