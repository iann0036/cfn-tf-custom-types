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
    BlockAction: Optional[str]
    BlockBotnet: Optional[str]
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    LogAllDomain: Optional[str]
    Name: Optional[str]
    RedirectPortal: Optional[str]
    RedirectPortal6: Optional[str]
    SafeSearch: Optional[str]
    SdnsDomainLog: Optional[str]
    SdnsFtgdErrLog: Optional[str]
    Vdomparam: Optional[str]
    YoutubeRestrict: Optional[str]
    DnsTranslation: Optional[Sequence["_DnsTranslationDefinition"]]
    DomainFilter: Optional[Sequence["_DomainFilterDefinition"]]
    ExternalIpBlocklist: Optional[Sequence["_ExternalIpBlocklistDefinition"]]
    FtgdDns: Optional[Sequence["_FtgdDnsDefinition"]]

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
            BlockAction=json_data.get("BlockAction"),
            BlockBotnet=json_data.get("BlockBotnet"),
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            LogAllDomain=json_data.get("LogAllDomain"),
            Name=json_data.get("Name"),
            RedirectPortal=json_data.get("RedirectPortal"),
            RedirectPortal6=json_data.get("RedirectPortal6"),
            SafeSearch=json_data.get("SafeSearch"),
            SdnsDomainLog=json_data.get("SdnsDomainLog"),
            SdnsFtgdErrLog=json_data.get("SdnsFtgdErrLog"),
            Vdomparam=json_data.get("Vdomparam"),
            YoutubeRestrict=json_data.get("YoutubeRestrict"),
            DnsTranslation=deserialize_list(json_data.get("DnsTranslation"), DnsTranslationDefinition),
            DomainFilter=deserialize_list(json_data.get("DomainFilter"), DomainFilterDefinition),
            ExternalIpBlocklist=deserialize_list(json_data.get("ExternalIpBlocklist"), ExternalIpBlocklistDefinition),
            FtgdDns=deserialize_list(json_data.get("FtgdDns"), FtgdDnsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DnsTranslationDefinition(BaseModel):
    AddrType: Optional[str]
    Dst: Optional[str]
    Dst6: Optional[str]
    Id: Optional[float]
    Netmask: Optional[str]
    Prefix: Optional[float]
    Src: Optional[str]
    Src6: Optional[str]
    Status: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DnsTranslationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnsTranslationDefinition"]:
        if not json_data:
            return None
        return cls(
            AddrType=json_data.get("AddrType"),
            Dst=json_data.get("Dst"),
            Dst6=json_data.get("Dst6"),
            Id=json_data.get("Id"),
            Netmask=json_data.get("Netmask"),
            Prefix=json_data.get("Prefix"),
            Src=json_data.get("Src"),
            Src6=json_data.get("Src6"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnsTranslationDefinition = DnsTranslationDefinition


@dataclass
class DomainFilterDefinition(BaseModel):
    DomainFilterTable: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_DomainFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DomainFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            DomainFilterTable=json_data.get("DomainFilterTable"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DomainFilterDefinition = DomainFilterDefinition


@dataclass
class ExternalIpBlocklistDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExternalIpBlocklistDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExternalIpBlocklistDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExternalIpBlocklistDefinition = ExternalIpBlocklistDefinition


@dataclass
class FtgdDnsDefinition(BaseModel):
    Options: Optional[str]
    Filters: Optional[Sequence["_FiltersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FtgdDnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtgdDnsDefinition"]:
        if not json_data:
            return None
        return cls(
            Options=json_data.get("Options"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtgdDnsDefinition = FtgdDnsDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Action: Optional[str]
    Category: Optional[float]
    Id: Optional[float]
    Log: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FiltersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FiltersDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Category=json_data.get("Category"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


