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
    AutoConfiguration: Optional[str]
    AutoManagedStatus: Optional[str]
    ConflictedIpTimeout: Optional[float]
    DdnsAuth: Optional[str]
    DdnsKey: Optional[str]
    DdnsKeyname: Optional[str]
    DdnsServerIp: Optional[str]
    DdnsTtl: Optional[float]
    DdnsUpdate: Optional[str]
    DdnsUpdateOverride: Optional[str]
    DdnsZone: Optional[str]
    DefaultGateway: Optional[str]
    DhcpSettingsFromFortiipam: Optional[str]
    DnsServer1: Optional[str]
    DnsServer2: Optional[str]
    DnsServer3: Optional[str]
    DnsServer4: Optional[str]
    DnsService: Optional[str]
    Domain: Optional[str]
    DynamicSortSubtable: Optional[str]
    Filename: Optional[str]
    ForticlientOnNetStatus: Optional[str]
    Fosid: Optional[float]
    Id: Optional[str]
    Interface: Optional[str]
    IpMode: Optional[str]
    IpsecLeaseHold: Optional[float]
    LeaseTime: Optional[float]
    MacAclDefaultAction: Optional[str]
    Netmask: Optional[str]
    NextServer: Optional[str]
    NtpServer1: Optional[str]
    NtpServer2: Optional[str]
    NtpServer3: Optional[str]
    NtpService: Optional[str]
    ServerType: Optional[str]
    Status: Optional[str]
    Timezone: Optional[str]
    TimezoneOption: Optional[str]
    VciMatch: Optional[str]
    Vdomparam: Optional[str]
    WifiAc1: Optional[str]
    WifiAc2: Optional[str]
    WifiAc3: Optional[str]
    WifiAcService: Optional[str]
    WinsServer1: Optional[str]
    WinsServer2: Optional[str]
    ExcludeRange: Optional[Sequence["_ExcludeRangeDefinition"]]
    IpRange: Optional[Sequence["_IpRangeDefinition"]]
    Options: Optional[Sequence["_OptionsDefinition"]]
    ReservedAddress: Optional[Sequence["_ReservedAddressDefinition"]]
    TftpServer: Optional[Sequence["_TftpServerDefinition"]]
    VciString: Optional[Sequence["_VciStringDefinition"]]

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
            AutoConfiguration=json_data.get("AutoConfiguration"),
            AutoManagedStatus=json_data.get("AutoManagedStatus"),
            ConflictedIpTimeout=json_data.get("ConflictedIpTimeout"),
            DdnsAuth=json_data.get("DdnsAuth"),
            DdnsKey=json_data.get("DdnsKey"),
            DdnsKeyname=json_data.get("DdnsKeyname"),
            DdnsServerIp=json_data.get("DdnsServerIp"),
            DdnsTtl=json_data.get("DdnsTtl"),
            DdnsUpdate=json_data.get("DdnsUpdate"),
            DdnsUpdateOverride=json_data.get("DdnsUpdateOverride"),
            DdnsZone=json_data.get("DdnsZone"),
            DefaultGateway=json_data.get("DefaultGateway"),
            DhcpSettingsFromFortiipam=json_data.get("DhcpSettingsFromFortiipam"),
            DnsServer1=json_data.get("DnsServer1"),
            DnsServer2=json_data.get("DnsServer2"),
            DnsServer3=json_data.get("DnsServer3"),
            DnsServer4=json_data.get("DnsServer4"),
            DnsService=json_data.get("DnsService"),
            Domain=json_data.get("Domain"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Filename=json_data.get("Filename"),
            ForticlientOnNetStatus=json_data.get("ForticlientOnNetStatus"),
            Fosid=json_data.get("Fosid"),
            Id=json_data.get("Id"),
            Interface=json_data.get("Interface"),
            IpMode=json_data.get("IpMode"),
            IpsecLeaseHold=json_data.get("IpsecLeaseHold"),
            LeaseTime=json_data.get("LeaseTime"),
            MacAclDefaultAction=json_data.get("MacAclDefaultAction"),
            Netmask=json_data.get("Netmask"),
            NextServer=json_data.get("NextServer"),
            NtpServer1=json_data.get("NtpServer1"),
            NtpServer2=json_data.get("NtpServer2"),
            NtpServer3=json_data.get("NtpServer3"),
            NtpService=json_data.get("NtpService"),
            ServerType=json_data.get("ServerType"),
            Status=json_data.get("Status"),
            Timezone=json_data.get("Timezone"),
            TimezoneOption=json_data.get("TimezoneOption"),
            VciMatch=json_data.get("VciMatch"),
            Vdomparam=json_data.get("Vdomparam"),
            WifiAc1=json_data.get("WifiAc1"),
            WifiAc2=json_data.get("WifiAc2"),
            WifiAc3=json_data.get("WifiAc3"),
            WifiAcService=json_data.get("WifiAcService"),
            WinsServer1=json_data.get("WinsServer1"),
            WinsServer2=json_data.get("WinsServer2"),
            ExcludeRange=deserialize_list(json_data.get("ExcludeRange"), ExcludeRangeDefinition),
            IpRange=deserialize_list(json_data.get("IpRange"), IpRangeDefinition),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            ReservedAddress=deserialize_list(json_data.get("ReservedAddress"), ReservedAddressDefinition),
            TftpServer=deserialize_list(json_data.get("TftpServer"), TftpServerDefinition),
            VciString=deserialize_list(json_data.get("VciString"), VciStringDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExcludeRangeDefinition(BaseModel):
    EndIp: Optional[str]
    Id: Optional[float]
    StartIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExcludeRangeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExcludeRangeDefinition"]:
        if not json_data:
            return None
        return cls(
            EndIp=json_data.get("EndIp"),
            Id=json_data.get("Id"),
            StartIp=json_data.get("StartIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExcludeRangeDefinition = ExcludeRangeDefinition


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
class OptionsDefinition(BaseModel):
    Code: Optional[float]
    Id: Optional[float]
    Ip: Optional[str]
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Code=json_data.get("Code"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class ReservedAddressDefinition(BaseModel):
    Action: Optional[str]
    CircuitId: Optional[str]
    CircuitIdType: Optional[str]
    Description: Optional[str]
    Id: Optional[float]
    Ip: Optional[str]
    Mac: Optional[str]
    RemoteId: Optional[str]
    RemoteIdType: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReservedAddressDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReservedAddressDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CircuitId=json_data.get("CircuitId"),
            CircuitIdType=json_data.get("CircuitIdType"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Ip=json_data.get("Ip"),
            Mac=json_data.get("Mac"),
            RemoteId=json_data.get("RemoteId"),
            RemoteIdType=json_data.get("RemoteIdType"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReservedAddressDefinition = ReservedAddressDefinition


@dataclass
class TftpServerDefinition(BaseModel):
    TftpServer: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TftpServerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TftpServerDefinition"]:
        if not json_data:
            return None
        return cls(
            TftpServer=json_data.get("TftpServer"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TftpServerDefinition = TftpServerDefinition


@dataclass
class VciStringDefinition(BaseModel):
    VciString: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VciStringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VciStringDefinition"]:
        if not json_data:
            return None
        return cls(
            VciString=json_data.get("VciString"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VciStringDefinition = VciStringDefinition


