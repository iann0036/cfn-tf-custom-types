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
    BwListName: Optional[str]
    FullDomainTree: Optional[float]
    Id: Optional[str]
    Interval: Optional[float]
    Name: Optional[str]
    OverLimit: Optional[float]
    OverLimitLockup: Optional[float]
    OverLimitLogging: Optional[float]
    OverLimitReset: Optional[float]
    Overlap: Optional[float]
    Share: Optional[float]
    Timeout: Optional[float]
    UseDestinationIp: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    BwListId: Optional[Sequence["_BwListIdDefinition"]]
    ClassList: Optional[Sequence["_ClassListDefinition"]]
    ForwardPolicy: Optional[Sequence["_ForwardPolicyDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

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
            BwListName=json_data.get("BwListName"),
            FullDomainTree=json_data.get("FullDomainTree"),
            Id=json_data.get("Id"),
            Interval=json_data.get("Interval"),
            Name=json_data.get("Name"),
            OverLimit=json_data.get("OverLimit"),
            OverLimitLockup=json_data.get("OverLimitLockup"),
            OverLimitLogging=json_data.get("OverLimitLogging"),
            OverLimitReset=json_data.get("OverLimitReset"),
            Overlap=json_data.get("Overlap"),
            Share=json_data.get("Share"),
            Timeout=json_data.get("Timeout"),
            UseDestinationIp=json_data.get("UseDestinationIp"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            BwListId=deserialize_list(json_data.get("BwListId"), BwListIdDefinition),
            ClassList=deserialize_list(json_data.get("ClassList"), ClassListDefinition),
            ForwardPolicy=deserialize_list(json_data.get("ForwardPolicy"), ForwardPolicyDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BwListIdDefinition(BaseModel):
    ActionInterval: Optional[float]
    BwListAction: Optional[str]
    Fail: Optional[float]
    Id: Optional[float]
    LoggingDrpRst: Optional[float]
    PbslbInterval: Optional[float]
    PbslbLogging: Optional[float]
    ServiceGroup: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BwListIdDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BwListIdDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionInterval=json_data.get("ActionInterval"),
            BwListAction=json_data.get("BwListAction"),
            Fail=json_data.get("Fail"),
            Id=json_data.get("Id"),
            LoggingDrpRst=json_data.get("LoggingDrpRst"),
            PbslbInterval=json_data.get("PbslbInterval"),
            PbslbLogging=json_data.get("PbslbLogging"),
            ServiceGroup=json_data.get("ServiceGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BwListIdDefinition = BwListIdDefinition


@dataclass
class ClassListDefinition(BaseModel):
    ClientIpL3Dest: Optional[float]
    ClientIpL7Header: Optional[float]
    HeaderName: Optional[str]
    Name: Optional[str]
    Uuid: Optional[str]
    LidList: Optional[Sequence["_LidListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClassListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassListDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIpL3Dest=json_data.get("ClientIpL3Dest"),
            ClientIpL7Header=json_data.get("ClientIpL7Header"),
            HeaderName=json_data.get("HeaderName"),
            Name=json_data.get("Name"),
            Uuid=json_data.get("Uuid"),
            LidList=deserialize_list(json_data.get("LidList"), LidListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassListDefinition = ClassListDefinition


@dataclass
class LidListDefinition(BaseModel):
    ActionValue: Optional[str]
    BwPer: Optional[float]
    BwRateLimit: Optional[float]
    ConnLimit: Optional[float]
    ConnPer: Optional[float]
    ConnRateLimit: Optional[float]
    DirectAction: Optional[float]
    DirectActionInterval: Optional[float]
    DirectActionValue: Optional[str]
    DirectFail: Optional[float]
    DirectLoggingDrpRst: Optional[float]
    DirectPbslbInterval: Optional[float]
    DirectPbslbLogging: Optional[float]
    DirectServiceGroup: Optional[str]
    Interval: Optional[float]
    Lidnum: Optional[float]
    Lockout: Optional[float]
    Log: Optional[float]
    OverLimitAction: Optional[float]
    RequestLimit: Optional[float]
    RequestPer: Optional[float]
    RequestRateLimit: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Dns64: Optional[Sequence["_Dns64Definition"]]
    ResponseCodeRateLimit: Optional[Sequence["_ResponseCodeRateLimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LidListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LidListDefinition"]:
        if not json_data:
            return None
        return cls(
            ActionValue=json_data.get("ActionValue"),
            BwPer=json_data.get("BwPer"),
            BwRateLimit=json_data.get("BwRateLimit"),
            ConnLimit=json_data.get("ConnLimit"),
            ConnPer=json_data.get("ConnPer"),
            ConnRateLimit=json_data.get("ConnRateLimit"),
            DirectAction=json_data.get("DirectAction"),
            DirectActionInterval=json_data.get("DirectActionInterval"),
            DirectActionValue=json_data.get("DirectActionValue"),
            DirectFail=json_data.get("DirectFail"),
            DirectLoggingDrpRst=json_data.get("DirectLoggingDrpRst"),
            DirectPbslbInterval=json_data.get("DirectPbslbInterval"),
            DirectPbslbLogging=json_data.get("DirectPbslbLogging"),
            DirectServiceGroup=json_data.get("DirectServiceGroup"),
            Interval=json_data.get("Interval"),
            Lidnum=json_data.get("Lidnum"),
            Lockout=json_data.get("Lockout"),
            Log=json_data.get("Log"),
            OverLimitAction=json_data.get("OverLimitAction"),
            RequestLimit=json_data.get("RequestLimit"),
            RequestPer=json_data.get("RequestPer"),
            RequestRateLimit=json_data.get("RequestRateLimit"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Dns64=deserialize_list(json_data.get("Dns64"), Dns64Definition),
            ResponseCodeRateLimit=deserialize_list(json_data.get("ResponseCodeRateLimit"), ResponseCodeRateLimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LidListDefinition = LidListDefinition


@dataclass
class Dns64Definition(BaseModel):
    Disable: Optional[float]
    ExclusiveAnswer: Optional[float]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Dns64Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dns64Definition"]:
        if not json_data:
            return None
        return cls(
            Disable=json_data.get("Disable"),
            ExclusiveAnswer=json_data.get("ExclusiveAnswer"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dns64Definition = Dns64Definition


@dataclass
class ResponseCodeRateLimitDefinition(BaseModel):
    CodeRangeEnd: Optional[float]
    CodeRangeStart: Optional[float]
    Period: Optional[float]
    Threshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseCodeRateLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseCodeRateLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            CodeRangeEnd=json_data.get("CodeRangeEnd"),
            CodeRangeStart=json_data.get("CodeRangeStart"),
            Period=json_data.get("Period"),
            Threshold=json_data.get("Threshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseCodeRateLimitDefinition = ResponseCodeRateLimitDefinition


@dataclass
class ForwardPolicyDefinition(BaseModel):
    AcosEventLog: Optional[float]
    LocalLogging: Optional[float]
    NoClientConnReuse: Optional[float]
    RequireWebCategory: Optional[float]
    Uuid: Optional[str]
    ActionList: Optional[Sequence["_ActionListDefinition"]]
    Filtering: Optional[Sequence["_FilteringDefinition"]]
    SanFiltering: Optional[Sequence["_SanFilteringDefinition"]]
    SourceList: Optional[Sequence["_SourceListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            AcosEventLog=json_data.get("AcosEventLog"),
            LocalLogging=json_data.get("LocalLogging"),
            NoClientConnReuse=json_data.get("NoClientConnReuse"),
            RequireWebCategory=json_data.get("RequireWebCategory"),
            Uuid=json_data.get("Uuid"),
            ActionList=deserialize_list(json_data.get("ActionList"), ActionListDefinition),
            Filtering=deserialize_list(json_data.get("Filtering"), FilteringDefinition),
            SanFiltering=deserialize_list(json_data.get("SanFiltering"), SanFilteringDefinition),
            SourceList=deserialize_list(json_data.get("SourceList"), SourceListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardPolicyDefinition = ForwardPolicyDefinition


@dataclass
class ActionListDefinition(BaseModel):
    Action1: Optional[str]
    DropMessage: Optional[str]
    DropRedirectUrl: Optional[str]
    DropResponseCode: Optional[float]
    FakeSg: Optional[str]
    FallBack: Optional[str]
    FallBackSnat: Optional[str]
    ForwardSnat: Optional[str]
    HttpStatusCode: Optional[str]
    Log: Optional[float]
    Name: Optional[str]
    RealSg: Optional[str]
    UserTag: Optional[str]
    Uuid: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActionListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActionListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action1=json_data.get("Action1"),
            DropMessage=json_data.get("DropMessage"),
            DropRedirectUrl=json_data.get("DropRedirectUrl"),
            DropResponseCode=json_data.get("DropResponseCode"),
            FakeSg=json_data.get("FakeSg"),
            FallBack=json_data.get("FallBack"),
            FallBackSnat=json_data.get("FallBackSnat"),
            ForwardSnat=json_data.get("ForwardSnat"),
            HttpStatusCode=json_data.get("HttpStatusCode"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            RealSg=json_data.get("RealSg"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActionListDefinition = ActionListDefinition


@dataclass
class SamplingEnableDefinition(BaseModel):
    Counters1: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SamplingEnableDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SamplingEnableDefinition"]:
        if not json_data:
            return None
        return cls(
            Counters1=json_data.get("Counters1"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SamplingEnableDefinition = SamplingEnableDefinition


@dataclass
class FilteringDefinition(BaseModel):
    SsliUrlFiltering: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FilteringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FilteringDefinition"]:
        if not json_data:
            return None
        return cls(
            SsliUrlFiltering=json_data.get("SsliUrlFiltering"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FilteringDefinition = FilteringDefinition


@dataclass
class SanFilteringDefinition(BaseModel):
    SsliUrlFilteringSan: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SanFilteringDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SanFilteringDefinition"]:
        if not json_data:
            return None
        return cls(
            SsliUrlFilteringSan=json_data.get("SsliUrlFilteringSan"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SanFilteringDefinition = SanFilteringDefinition


@dataclass
class SourceListDefinition(BaseModel):
    MatchAny: Optional[float]
    MatchAuthorizePolicy: Optional[str]
    MatchClassList: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    UserTag: Optional[str]
    Uuid: Optional[str]
    Destination: Optional[Sequence["_DestinationDefinition"]]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SourceListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourceListDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchAny=json_data.get("MatchAny"),
            MatchAuthorizePolicy=json_data.get("MatchAuthorizePolicy"),
            MatchClassList=json_data.get("MatchClassList"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            UserTag=json_data.get("UserTag"),
            Uuid=json_data.get("Uuid"),
            Destination=deserialize_list(json_data.get("Destination"), DestinationDefinition),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourceListDefinition = SourceListDefinition


@dataclass
class DestinationDefinition(BaseModel):
    Any: Optional[Sequence["_AnyDefinition"]]
    ClassListList: Optional[Sequence["_ClassListListDefinition"]]
    WebCategoryListList: Optional[Sequence["_WebCategoryListListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DestinationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DestinationDefinition"]:
        if not json_data:
            return None
        return cls(
            Any=deserialize_list(json_data.get("Any"), AnyDefinition),
            ClassListList=deserialize_list(json_data.get("ClassListList"), ClassListListDefinition),
            WebCategoryListList=deserialize_list(json_data.get("WebCategoryListList"), WebCategoryListListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DestinationDefinition = DestinationDefinition


@dataclass
class AnyDefinition(BaseModel):
    Action: Optional[str]
    Uuid: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AnyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnyDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Uuid=json_data.get("Uuid"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnyDefinition = AnyDefinition


@dataclass
class ClassListListDefinition(BaseModel):
    Action: Optional[str]
    DestClassList: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]
    Uuid: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClassListListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClassListListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            DestClassList=json_data.get("DestClassList"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClassListListDefinition = ClassListListDefinition


@dataclass
class WebCategoryListListDefinition(BaseModel):
    Action: Optional[str]
    Priority: Optional[float]
    Type: Optional[str]
    Uuid: Optional[str]
    WebCategoryList: Optional[str]
    SamplingEnable: Optional[Sequence["_SamplingEnableDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebCategoryListListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebCategoryListListDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Priority=json_data.get("Priority"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            WebCategoryList=json_data.get("WebCategoryList"),
            SamplingEnable=deserialize_list(json_data.get("SamplingEnable"), SamplingEnableDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebCategoryListListDefinition = WebCategoryListListDefinition


