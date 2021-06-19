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
    Comment: Optional[str]
    DynamicSortSubtable: Optional[str]
    ExtendedLog: Optional[str]
    FeatureSet: Optional[str]
    HttpsReplacemsg: Optional[str]
    Id: Optional[str]
    InspectionMode: Optional[str]
    LogAllUrl: Optional[str]
    Name: Optional[str]
    Options: Optional[str]
    OvrdPerm: Optional[str]
    PostAction: Optional[str]
    ReplacemsgGroup: Optional[str]
    Vdomparam: Optional[str]
    WebAntiphishingLog: Optional[str]
    WebContentLog: Optional[str]
    WebExtendedAllActionLog: Optional[str]
    WebFilterActivexLog: Optional[str]
    WebFilterAppletLog: Optional[str]
    WebFilterCommandBlockLog: Optional[str]
    WebFilterCookieLog: Optional[str]
    WebFilterCookieRemovalLog: Optional[str]
    WebFilterJsLog: Optional[str]
    WebFilterJscriptLog: Optional[str]
    WebFilterRefererLog: Optional[str]
    WebFilterUnknownLog: Optional[str]
    WebFilterVbsLog: Optional[str]
    WebFtgdErrLog: Optional[str]
    WebFtgdQuotaUsage: Optional[str]
    WebInvalidDomainLog: Optional[str]
    WebUrlLog: Optional[str]
    Wisp: Optional[str]
    WispAlgorithm: Optional[str]
    YoutubeChannelStatus: Optional[str]
    Antiphish: Optional[Sequence["_AntiphishDefinition"]]
    FileFilter: Optional[Sequence["_FileFilterDefinition"]]
    FtgdWf: Optional[Sequence["_FtgdWfDefinition"]]
    Override: Optional[Sequence["_OverrideDefinition"]]
    Web: Optional[Sequence["_WebDefinition"]]
    WispServers: Optional[Sequence["_WispServersDefinition"]]
    YoutubeChannelFilter: Optional[Sequence["_YoutubeChannelFilterDefinition"]]

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
            Comment=json_data.get("Comment"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            ExtendedLog=json_data.get("ExtendedLog"),
            FeatureSet=json_data.get("FeatureSet"),
            HttpsReplacemsg=json_data.get("HttpsReplacemsg"),
            Id=json_data.get("Id"),
            InspectionMode=json_data.get("InspectionMode"),
            LogAllUrl=json_data.get("LogAllUrl"),
            Name=json_data.get("Name"),
            Options=json_data.get("Options"),
            OvrdPerm=json_data.get("OvrdPerm"),
            PostAction=json_data.get("PostAction"),
            ReplacemsgGroup=json_data.get("ReplacemsgGroup"),
            Vdomparam=json_data.get("Vdomparam"),
            WebAntiphishingLog=json_data.get("WebAntiphishingLog"),
            WebContentLog=json_data.get("WebContentLog"),
            WebExtendedAllActionLog=json_data.get("WebExtendedAllActionLog"),
            WebFilterActivexLog=json_data.get("WebFilterActivexLog"),
            WebFilterAppletLog=json_data.get("WebFilterAppletLog"),
            WebFilterCommandBlockLog=json_data.get("WebFilterCommandBlockLog"),
            WebFilterCookieLog=json_data.get("WebFilterCookieLog"),
            WebFilterCookieRemovalLog=json_data.get("WebFilterCookieRemovalLog"),
            WebFilterJsLog=json_data.get("WebFilterJsLog"),
            WebFilterJscriptLog=json_data.get("WebFilterJscriptLog"),
            WebFilterRefererLog=json_data.get("WebFilterRefererLog"),
            WebFilterUnknownLog=json_data.get("WebFilterUnknownLog"),
            WebFilterVbsLog=json_data.get("WebFilterVbsLog"),
            WebFtgdErrLog=json_data.get("WebFtgdErrLog"),
            WebFtgdQuotaUsage=json_data.get("WebFtgdQuotaUsage"),
            WebInvalidDomainLog=json_data.get("WebInvalidDomainLog"),
            WebUrlLog=json_data.get("WebUrlLog"),
            Wisp=json_data.get("Wisp"),
            WispAlgorithm=json_data.get("WispAlgorithm"),
            YoutubeChannelStatus=json_data.get("YoutubeChannelStatus"),
            Antiphish=deserialize_list(json_data.get("Antiphish"), AntiphishDefinition),
            FileFilter=deserialize_list(json_data.get("FileFilter"), FileFilterDefinition),
            FtgdWf=deserialize_list(json_data.get("FtgdWf"), FtgdWfDefinition),
            Override=deserialize_list(json_data.get("Override"), OverrideDefinition),
            Web=deserialize_list(json_data.get("Web"), WebDefinition),
            WispServers=deserialize_list(json_data.get("WispServers"), WispServersDefinition),
            YoutubeChannelFilter=deserialize_list(json_data.get("YoutubeChannelFilter"), YoutubeChannelFilterDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AntiphishDefinition(BaseModel):
    CheckBasicAuth: Optional[str]
    CheckUri: Optional[str]
    DefaultAction: Optional[str]
    DomainController: Optional[str]
    MaxBodyLen: Optional[float]
    Status: Optional[str]
    CustomPatterns: Optional[Sequence["_CustomPatternsDefinition"]]
    InspectionEntries: Optional[Sequence["_InspectionEntriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AntiphishDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AntiphishDefinition"]:
        if not json_data:
            return None
        return cls(
            CheckBasicAuth=json_data.get("CheckBasicAuth"),
            CheckUri=json_data.get("CheckUri"),
            DefaultAction=json_data.get("DefaultAction"),
            DomainController=json_data.get("DomainController"),
            MaxBodyLen=json_data.get("MaxBodyLen"),
            Status=json_data.get("Status"),
            CustomPatterns=deserialize_list(json_data.get("CustomPatterns"), CustomPatternsDefinition),
            InspectionEntries=deserialize_list(json_data.get("InspectionEntries"), InspectionEntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AntiphishDefinition = AntiphishDefinition


@dataclass
class CustomPatternsDefinition(BaseModel):
    Category: Optional[str]
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomPatternsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomPatternsDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomPatternsDefinition = CustomPatternsDefinition


@dataclass
class InspectionEntriesDefinition(BaseModel):
    Action: Optional[str]
    FortiguardCategory: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InspectionEntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InspectionEntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            FortiguardCategory=json_data.get("FortiguardCategory"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InspectionEntriesDefinition = InspectionEntriesDefinition


@dataclass
class FileFilterDefinition(BaseModel):
    Log: Optional[str]
    ScanArchiveContents: Optional[str]
    Status: Optional[str]
    Entries: Optional[Sequence["_EntriesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FileFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            Log=json_data.get("Log"),
            ScanArchiveContents=json_data.get("ScanArchiveContents"),
            Status=json_data.get("Status"),
            Entries=deserialize_list(json_data.get("Entries"), EntriesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileFilterDefinition = FileFilterDefinition


@dataclass
class EntriesDefinition(BaseModel):
    Action: Optional[str]
    Comment: Optional[str]
    Direction: Optional[str]
    Filter: Optional[str]
    PasswordProtected: Optional[str]
    Protocol: Optional[str]
    FileType: Optional[Sequence["_FileTypeDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EntriesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EntriesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Comment=json_data.get("Comment"),
            Direction=json_data.get("Direction"),
            Filter=json_data.get("Filter"),
            PasswordProtected=json_data.get("PasswordProtected"),
            Protocol=json_data.get("Protocol"),
            FileType=deserialize_list(json_data.get("FileType"), FileTypeDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EntriesDefinition = EntriesDefinition


@dataclass
class FileTypeDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileTypeDefinition = FileTypeDefinition


@dataclass
class FtgdWfDefinition(BaseModel):
    ExemptQuota: Optional[str]
    MaxQuotaTimeout: Optional[float]
    Options: Optional[str]
    Ovrd: Optional[str]
    RateCrlUrls: Optional[str]
    RateCssUrls: Optional[str]
    RateImageUrls: Optional[str]
    RateJavascriptUrls: Optional[str]
    Filters: Optional[Sequence["_FiltersDefinition"]]
    Quota: Optional[Sequence["_QuotaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FtgdWfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FtgdWfDefinition"]:
        if not json_data:
            return None
        return cls(
            ExemptQuota=json_data.get("ExemptQuota"),
            MaxQuotaTimeout=json_data.get("MaxQuotaTimeout"),
            Options=json_data.get("Options"),
            Ovrd=json_data.get("Ovrd"),
            RateCrlUrls=json_data.get("RateCrlUrls"),
            RateCssUrls=json_data.get("RateCssUrls"),
            RateImageUrls=json_data.get("RateImageUrls"),
            RateJavascriptUrls=json_data.get("RateJavascriptUrls"),
            Filters=deserialize_list(json_data.get("Filters"), FiltersDefinition),
            Quota=deserialize_list(json_data.get("Quota"), QuotaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FtgdWfDefinition = FtgdWfDefinition


@dataclass
class FiltersDefinition(BaseModel):
    Action: Optional[str]
    Category: Optional[float]
    Id: Optional[float]
    Log: Optional[str]
    OverrideReplacemsg: Optional[str]
    WarnDuration: Optional[str]
    WarningDurationType: Optional[str]
    WarningPrompt: Optional[str]
    AuthUsrGrp: Optional[Sequence["_AuthUsrGrpDefinition"]]

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
            OverrideReplacemsg=json_data.get("OverrideReplacemsg"),
            WarnDuration=json_data.get("WarnDuration"),
            WarningDurationType=json_data.get("WarningDurationType"),
            WarningPrompt=json_data.get("WarningPrompt"),
            AuthUsrGrp=deserialize_list(json_data.get("AuthUsrGrp"), AuthUsrGrpDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FiltersDefinition = FiltersDefinition


@dataclass
class AuthUsrGrpDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuthUsrGrpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuthUsrGrpDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuthUsrGrpDefinition = AuthUsrGrpDefinition


@dataclass
class QuotaDefinition(BaseModel):
    Category: Optional[str]
    Duration: Optional[str]
    Id: Optional[float]
    OverrideReplacemsg: Optional[str]
    Type: Optional[str]
    Unit: Optional[str]
    Value: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_QuotaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_QuotaDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Duration=json_data.get("Duration"),
            Id=json_data.get("Id"),
            OverrideReplacemsg=json_data.get("OverrideReplacemsg"),
            Type=json_data.get("Type"),
            Unit=json_data.get("Unit"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_QuotaDefinition = QuotaDefinition


@dataclass
class OverrideDefinition(BaseModel):
    OvrdCookie: Optional[str]
    OvrdDur: Optional[str]
    OvrdDurMode: Optional[str]
    OvrdScope: Optional[str]
    ProfileAttribute: Optional[str]
    ProfileType: Optional[str]
    OvrdUserGroup: Optional[Sequence["_OvrdUserGroupDefinition"]]
    Profile: Optional[Sequence["_ProfileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OverrideDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverrideDefinition"]:
        if not json_data:
            return None
        return cls(
            OvrdCookie=json_data.get("OvrdCookie"),
            OvrdDur=json_data.get("OvrdDur"),
            OvrdDurMode=json_data.get("OvrdDurMode"),
            OvrdScope=json_data.get("OvrdScope"),
            ProfileAttribute=json_data.get("ProfileAttribute"),
            ProfileType=json_data.get("ProfileType"),
            OvrdUserGroup=deserialize_list(json_data.get("OvrdUserGroup"), OvrdUserGroupDefinition),
            Profile=deserialize_list(json_data.get("Profile"), ProfileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverrideDefinition = OverrideDefinition


@dataclass
class OvrdUserGroupDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OvrdUserGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OvrdUserGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OvrdUserGroupDefinition = OvrdUserGroupDefinition


@dataclass
class ProfileDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProfileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProfileDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProfileDefinition = ProfileDefinition


@dataclass
class WebDefinition(BaseModel):
    Allowlist: Optional[str]
    Blacklist: Optional[str]
    Blocklist: Optional[str]
    BwordTable: Optional[float]
    BwordThreshold: Optional[float]
    ContentHeaderList: Optional[float]
    LogSearch: Optional[str]
    SafeSearch: Optional[str]
    UrlfilterTable: Optional[float]
    Whitelist: Optional[str]
    YoutubeRestrict: Optional[str]
    KeywordMatch: Optional[Sequence["_KeywordMatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WebDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WebDefinition"]:
        if not json_data:
            return None
        return cls(
            Allowlist=json_data.get("Allowlist"),
            Blacklist=json_data.get("Blacklist"),
            Blocklist=json_data.get("Blocklist"),
            BwordTable=json_data.get("BwordTable"),
            BwordThreshold=json_data.get("BwordThreshold"),
            ContentHeaderList=json_data.get("ContentHeaderList"),
            LogSearch=json_data.get("LogSearch"),
            SafeSearch=json_data.get("SafeSearch"),
            UrlfilterTable=json_data.get("UrlfilterTable"),
            Whitelist=json_data.get("Whitelist"),
            YoutubeRestrict=json_data.get("YoutubeRestrict"),
            KeywordMatch=deserialize_list(json_data.get("KeywordMatch"), KeywordMatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WebDefinition = WebDefinition


@dataclass
class KeywordMatchDefinition(BaseModel):
    Pattern: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KeywordMatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KeywordMatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Pattern=json_data.get("Pattern"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KeywordMatchDefinition = KeywordMatchDefinition


@dataclass
class WispServersDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WispServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WispServersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WispServersDefinition = WispServersDefinition


@dataclass
class YoutubeChannelFilterDefinition(BaseModel):
    ChannelId: Optional[str]
    Comment: Optional[str]
    Id: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_YoutubeChannelFilterDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_YoutubeChannelFilterDefinition"]:
        if not json_data:
            return None
        return cls(
            ChannelId=json_data.get("ChannelId"),
            Comment=json_data.get("Comment"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_YoutubeChannelFilterDefinition = YoutubeChannelFilterDefinition


