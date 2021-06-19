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
    AreaIpv4: Optional[str]
    AreaNum: Optional[float]
    AsNumber: Optional[str]
    DefaultCost: Optional[float]
    Id: Optional[str]
    ProcessId: Optional[float]
    Shortcut: Optional[str]
    Uuid: Optional[str]
    AuthCfg: Optional[Sequence["_AuthCfgDefinition"]]
    FilterLists: Optional[Sequence["_FilterListsDefinition"]]
    NssaCfg: Optional[Sequence["_NssaCfgDefinition"]]
    RangeList: Optional[Sequence["_RangeListDefinition"]]
    StubCfg: Optional[Sequence["_StubCfgDefinition"]]
    VirtualLinkList: Optional[Sequence["_VirtualLinkListDefinition"]]

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
            AreaIpv4=json_data.get("AreaIpv4"),
            AreaNum=json_data.get("AreaNum"),
            AsNumber=json_data.get("AsNumber"),
            DefaultCost=json_data.get("DefaultCost"),
            Id=json_data.get("Id"),
            ProcessId=json_data.get("ProcessId"),
            Shortcut=json_data.get("Shortcut"),
            Uuid=json_data.get("Uuid"),
            AuthCfg=deserialize_list(json_data.get("AuthCfg"), AuthCfgDefinition),
            FilterLists=deserialize_list(json_data.get("FilterLists"), FilterListsDefinition),
            NssaCfg=deserialize_list(json_data.get("NssaCfg"), NssaCfgDefinition),
            RangeList=deserialize_list(json_data.get("RangeList"), RangeListDefinition),
            StubCfg=deserialize_list(json_data.get("StubCfg"), StubCfgDefinition),
            VirtualLinkList=deserialize_list(json_data.get("VirtualLinkList"), VirtualLinkListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuthCfgDefinition(BaseModel):
    Authentication: Optional[float]
    MessageDigest: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AuthCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            Authentication=json_data.get("Authentication"),
            MessageDigest=json_data.get("MessageDigest"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthCfgDefinition = AuthCfgDefinition


@dataclass
class FilterListsDefinition(BaseModel):
    AclDirection: Optional[str]
    AclName: Optional[str]
    FilterList: Optional[float]
    PlistDirection: Optional[str]
    PlistName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilterListsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilterListsDefinition"]:
        if not json_data:
            return None
        return cls(
            AclDirection=json_data.get("AclDirection"),
            AclName=json_data.get("AclName"),
            FilterList=json_data.get("FilterList"),
            PlistDirection=json_data.get("PlistDirection"),
            PlistName=json_data.get("PlistName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilterListsDefinition = FilterListsDefinition


@dataclass
class NssaCfgDefinition(BaseModel):
    DefaultInformationOriginate: Optional[float]
    Metric: Optional[float]
    MetricType: Optional[float]
    NoRedistribution: Optional[float]
    NoSummary: Optional[float]
    Nssa: Optional[float]
    TranslatorRole: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NssaCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NssaCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            DefaultInformationOriginate=json_data.get("DefaultInformationOriginate"),
            Metric=json_data.get("Metric"),
            MetricType=json_data.get("MetricType"),
            NoRedistribution=json_data.get("NoRedistribution"),
            NoSummary=json_data.get("NoSummary"),
            Nssa=json_data.get("Nssa"),
            TranslatorRole=json_data.get("TranslatorRole"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NssaCfgDefinition = NssaCfgDefinition


@dataclass
class RangeListDefinition(BaseModel):
    AreaRangePrefix: Optional[str]
    Option: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RangeListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangeListDefinition"]:
        if not json_data:
            return None
        return cls(
            AreaRangePrefix=json_data.get("AreaRangePrefix"),
            Option=json_data.get("Option"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangeListDefinition = RangeListDefinition


@dataclass
class StubCfgDefinition(BaseModel):
    NoSummary: Optional[float]
    Stub: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_StubCfgDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StubCfgDefinition"]:
        if not json_data:
            return None
        return cls(
            NoSummary=json_data.get("NoSummary"),
            Stub=json_data.get("Stub"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StubCfgDefinition = StubCfgDefinition


@dataclass
class VirtualLinkListDefinition(BaseModel):
    AuthenticationKey: Optional[str]
    Bfd: Optional[float]
    DeadInterval: Optional[float]
    HelloInterval: Optional[float]
    Md5: Optional[str]
    MessageDigestKey: Optional[float]
    RetransmitInterval: Optional[float]
    TransmitDelay: Optional[float]
    VirtualLinkAuthType: Optional[str]
    VirtualLinkAuthentication: Optional[float]
    VirtualLinkIpAddr: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_VirtualLinkListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VirtualLinkListDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthenticationKey=json_data.get("AuthenticationKey"),
            Bfd=json_data.get("Bfd"),
            DeadInterval=json_data.get("DeadInterval"),
            HelloInterval=json_data.get("HelloInterval"),
            Md5=json_data.get("Md5"),
            MessageDigestKey=json_data.get("MessageDigestKey"),
            RetransmitInterval=json_data.get("RetransmitInterval"),
            TransmitDelay=json_data.get("TransmitDelay"),
            VirtualLinkAuthType=json_data.get("VirtualLinkAuthType"),
            VirtualLinkAuthentication=json_data.get("VirtualLinkAuthentication"),
            VirtualLinkIpAddr=json_data.get("VirtualLinkIpAddr"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VirtualLinkListDefinition = VirtualLinkListDefinition


