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
    AppReplacemsg: Optional[str]
    Comment: Optional[str]
    ControlDefaultNetworkServices: Optional[str]
    DeepAppInspection: Optional[str]
    DynamicSortSubtable: Optional[str]
    EnforceDefaultAppPort: Optional[str]
    ExtendedLog: Optional[str]
    ForceInclusionSslDiSigs: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Options: Optional[str]
    OtherApplicationAction: Optional[str]
    OtherApplicationLog: Optional[str]
    P2pBlackList: Optional[str]
    P2pBlockList: Optional[str]
    ReplacemsgGroup: Optional[str]
    UnknownApplicationAction: Optional[str]
    UnknownApplicationLog: Optional[str]
    Vdomparam: Optional[str]
    DefaultNetworkServices: Optional[Sequence["_DefaultNetworkServicesDefinition"]]
    Entries: Optional[Sequence["_EntriesDefinition"]]

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
            AppReplacemsg=json_data.get("AppReplacemsg"),
            Comment=json_data.get("Comment"),
            ControlDefaultNetworkServices=json_data.get("ControlDefaultNetworkServices"),
            DeepAppInspection=json_data.get("DeepAppInspection"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            EnforceDefaultAppPort=json_data.get("EnforceDefaultAppPort"),
            ExtendedLog=json_data.get("ExtendedLog"),
            ForceInclusionSslDiSigs=json_data.get("ForceInclusionSslDiSigs"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            OtherApplicationAction=json_data.get("OtherApplicationAction"),
            OtherApplicationLog=json_data.get("OtherApplicationLog"),
            P2pBlackList=json_data.get("P2pBlackList"),
            P2pBlockList=json_data.get("P2pBlockList"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            UnknownApplicationAction=json_data.get("UnknownApplicationAction"),
            UnknownApplicationLog=json_data.get("UnknownApplicationLog"),
            Vdomparam=json_data.get("Vdomparam"),
            DefaultNetworkServices=deserialize_list(json_data.get("DefaultNetworkServices"), DefaultNetworkServicesDefinition),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefaultNetworkServicesDefinition(BaseModel):
    Id: Optional[float]
    Port: Optional[float]
    Services: Optional[str]
    ViolationAction: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultNetworkServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultNetworkServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Port=json_data.get("Port"),
            Services=json_data.get("Services"),
            ViolationAction=json_data.get("ViolationAction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultNetworkServicesDefinition = DefaultNetworkServicesDefinition


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    Behavior: Optional[str]
    Id: Optional[float]
    Log: Optional[str]
    LogPacket: Optional[str]
    PerIpShaper: Optional[str]
    Popularity: Optional[str]
    Protocols: Optional[str]
    Quarantine: Optional[str]
    QuarantineExpiry: Optional[str]
    QuarantineLog: Optional[str]
    RateCount: Optional[float]
    RateDuration: Optional[float]
    RateMode: Optional[str]
    RateTrack: Optional[str]
    SessionTtl: Optional[float]
    Shaper: Optional[str]
    ShaperReverse: Optional[str]
    Technology: Optional[str]
    Vendor: Optional[str]
    Application: Optional[Sequence["_ApplicationDefinition"]]
    Category: Optional[Sequence["_CategoryDefinition"]]
    Exclusion: Optional[Sequence["_ExclusionDefinition"]]
    Parameters: Optional[Sequence["_ParametersDefinition"]]
    Risk: Optional[Sequence["_RiskDefinition"]]
    SubCategory: Optional[Sequence["_SubCategoryDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Behavior=json_data.get("Behavior"),
            Id=json_data.get("Id"),
            Log=json_data.get("Log"),
            LogPacket=json_data.get("LogPacket"),
            PerIpShaper=json_data.get("PerIpShaper"),
            Popularity=json_data.get("Popularity"),
            Protocols=json_data.get("Protocols"),
            Quarantine=json_data.get("Quarantine"),
            QuarantineExpiry=json_data.get("QuarantineExpiry"),
            QuarantineLog=json_data.get("QuarantineLog"),
            RateCount=json_data.get("RateCount"),
            RateDuration=json_data.get("RateDuration"),
            RateMode=json_data.get("RateMode"),
            RateTrack=json_data.get("RateTrack"),
            SessionTtl=json_data.get("SessionTtl"),
            Shaper=json_data.get("Shaper"),
            ShaperReverse=json_data.get("ShaperReverse"),
            Technology=json_data.get("Technology"),
            Vendor=json_data.get("Vendor"),
            Application=deserialize_list(json_data.get("Application"), ApplicationDefinition),
            Category=deserialize_list(json_data.get("Category"), CategoryDefinition),
            Exclusion=deserialize_list(json_data.get("Exclusion"), ExclusionDefinition),
            Parameters=deserialize_list(json_data.get("Parameters"), ParametersDefinition),
            Risk=deserialize_list(json_data.get("Risk"), RiskDefinition),
            SubCategory=deserialize_list(json_data.get("SubCategory"), SubCategoryDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition


@dataclass
class ApplicationDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationDefinition = ApplicationDefinition


@dataclass
class CategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_CategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CategoryDefinition = CategoryDefinition


@dataclass
class ExclusionDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionDefinition = ExclusionDefinition


@dataclass
class ParametersDefinition(BaseModel):
    Id: Optional[float]
    Value: Optional[str]
    Members: Optional[Sequence["_MembersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ParametersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ParametersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Value=json_data.get("Value"),
            Members=deserialize_list(json_data.get("Members"), MembersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ParametersDefinition = ParametersDefinition


@dataclass
class MembersDefinition(BaseModel):
    Id: Optional[float]
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MembersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MembersDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MembersDefinition = MembersDefinition


@dataclass
class RiskDefinition(BaseModel):
    Level: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RiskDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RiskDefinition"]:
        if not json_data:
            return None
        return cls(
            Level=json_data.get("Level"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RiskDefinition = RiskDefinition


@dataclass
class SubCategoryDefinition(BaseModel):
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SubCategoryDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubCategoryDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubCategoryDefinition = SubCategoryDefinition


