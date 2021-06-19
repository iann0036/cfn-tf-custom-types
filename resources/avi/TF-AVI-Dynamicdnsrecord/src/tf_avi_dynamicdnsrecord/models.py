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
    Algorithm: Optional[str]
    Delegated: Optional[bool]
    Description: Optional[str]
    DnsVsUuid: Optional[str]
    Fqdn: Optional[str]
    Id: Optional[str]
    Metadata: Optional[str]
    Name: Optional[str]
    NumRecordsInResponse: Optional[float]
    TenantRef: Optional[str]
    Ttl: Optional[float]
    Type: Optional[str]
    Uuid: Optional[str]
    WildcardMatch: Optional[bool]
    Cname: Optional[Sequence["_CnameDefinition"]]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]
    MxRecords: Optional[Sequence["_MxRecordsDefinition"]]
    Ns: Optional[Sequence["_NsDefinition"]]
    ServiceLocators: Optional[Sequence["_ServiceLocatorsDefinition"]]
    TxtRecords: Optional[Sequence["_TxtRecordsDefinition"]]

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
            Algorithm=json_data.get("Algorithm"),
            Delegated=json_data.get("Delegated"),
            Description=json_data.get("Description"),
            DnsVsUuid=json_data.get("DnsVsUuid"),
            Fqdn=json_data.get("Fqdn"),
            Id=json_data.get("Id"),
            Metadata=json_data.get("Metadata"),
            Name=json_data.get("Name"),
            NumRecordsInResponse=json_data.get("NumRecordsInResponse"),
            TenantRef=json_data.get("TenantRef"),
            Ttl=json_data.get("Ttl"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            WildcardMatch=json_data.get("WildcardMatch"),
            Cname=deserialize_list(json_data.get("Cname"), CnameDefinition),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
            MxRecords=deserialize_list(json_data.get("MxRecords"), MxRecordsDefinition),
            Ns=deserialize_list(json_data.get("Ns"), NsDefinition),
            ServiceLocators=deserialize_list(json_data.get("ServiceLocators"), ServiceLocatorsDefinition),
            TxtRecords=deserialize_list(json_data.get("TxtRecords"), TxtRecordsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CnameDefinition(BaseModel):
    Cname: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CnameDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CnameDefinition"]:
        if not json_data:
            return None
        return cls(
            Cname=json_data.get("Cname"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CnameDefinition = CnameDefinition


@dataclass
class Ip6AddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Ip6AddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Ip6AddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Ip6AddressDefinition = Ip6AddressDefinition


@dataclass
class IpAddressDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddressDefinition = IpAddressDefinition


@dataclass
class MxRecordsDefinition(BaseModel):
    Host: Optional[str]
    Priority: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_MxRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MxRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            Host=json_data.get("Host"),
            Priority=json_data.get("Priority"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MxRecordsDefinition = MxRecordsDefinition


@dataclass
class NsDefinition(BaseModel):
    Nsname: Optional[str]
    Ip6Address: Optional[Sequence["_Ip6AddressDefinition"]]
    IpAddress: Optional[Sequence["_IpAddressDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_NsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NsDefinition"]:
        if not json_data:
            return None
        return cls(
            Nsname=json_data.get("Nsname"),
            Ip6Address=deserialize_list(json_data.get("Ip6Address"), Ip6AddressDefinition),
            IpAddress=deserialize_list(json_data.get("IpAddress"), IpAddressDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_NsDefinition = NsDefinition


@dataclass
class ServiceLocatorsDefinition(BaseModel):
    Port: Optional[float]
    Priority: Optional[float]
    Target: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceLocatorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceLocatorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Priority=json_data.get("Priority"),
            Target=json_data.get("Target"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceLocatorsDefinition = ServiceLocatorsDefinition


@dataclass
class TxtRecordsDefinition(BaseModel):
    TextStr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TxtRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TxtRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            TextStr=json_data.get("TextStr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TxtRecordsDefinition = TxtRecordsDefinition


