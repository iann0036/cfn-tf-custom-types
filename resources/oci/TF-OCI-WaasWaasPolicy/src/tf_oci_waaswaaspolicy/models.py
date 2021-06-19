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
    AdditionalDomains: Optional[Sequence[str]]
    Cname: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTagsDefinition"]]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTagsDefinition"]]
    Id: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    OriginGroups: Optional[Sequence["_OriginGroupsDefinition"]]
    Origins: Optional[Sequence["_OriginsDefinition"]]
    PolicyConfig: Optional[Sequence["_PolicyConfigDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]
    WafConfig: Optional[Sequence["_WafConfigDefinition"]]

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
            AdditionalDomains=json_data.get("AdditionalDomains"),
            Cname=json_data.get("Cname"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=deserialize_list(json_data.get("DefinedTags"), DefinedTagsDefinition),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FreeformTags=deserialize_list(json_data.get("FreeformTags"), FreeformTagsDefinition),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            OriginGroups=deserialize_list(json_data.get("OriginGroups"), OriginGroupsDefinition),
            Origins=deserialize_list(json_data.get("Origins"), OriginsDefinition),
            PolicyConfig=deserialize_list(json_data.get("PolicyConfig"), PolicyConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
            WafConfig=deserialize_list(json_data.get("WafConfig"), WafConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTagsDefinition = DefinedTagsDefinition


@dataclass
class FreeformTagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTagsDefinition = FreeformTagsDefinition


@dataclass
class OriginGroupsDefinition(BaseModel):
    Label: Optional[str]
    OriginGroup: Optional[Sequence["_OriginGroupDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupsDefinition"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            OriginGroup=deserialize_list(json_data.get("OriginGroup"), OriginGroupDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupsDefinition = OriginGroupsDefinition


@dataclass
class OriginGroupDefinition(BaseModel):
    Origin: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroupDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroupDefinition"]:
        if not json_data:
            return None
        return cls(
            Origin=json_data.get("Origin"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroupDefinition = OriginGroupDefinition


@dataclass
class OriginsDefinition(BaseModel):
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Label: Optional[str]
    Uri: Optional[str]
    CustomHeaders: Optional[Sequence["_CustomHeadersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginsDefinition"]:
        if not json_data:
            return None
        return cls(
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Label=json_data.get("Label"),
            Uri=json_data.get("Uri"),
            CustomHeaders=deserialize_list(json_data.get("CustomHeaders"), CustomHeadersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginsDefinition = OriginsDefinition


@dataclass
class CustomHeadersDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeadersDefinition = CustomHeadersDefinition


@dataclass
class PolicyConfigDefinition(BaseModel):
    CertificateId: Optional[str]
    CipherGroup: Optional[str]
    ClientAddressHeader: Optional[str]
    IsBehindCdn: Optional[bool]
    IsCacheControlRespected: Optional[bool]
    IsHttpsEnabled: Optional[bool]
    IsHttpsForced: Optional[bool]
    IsOriginCompressionEnabled: Optional[bool]
    IsResponseBufferingEnabled: Optional[bool]
    IsSniEnabled: Optional[bool]
    TlsProtocols: Optional[Sequence[str]]
    WebsocketPathPrefixes: Optional[Sequence[str]]
    HealthChecks: Optional[Sequence["_HealthChecksDefinition"]]
    LoadBalancingMethod: Optional[Sequence["_LoadBalancingMethodDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateId=json_data.get("CertificateId"),
            CipherGroup=json_data.get("CipherGroup"),
            ClientAddressHeader=json_data.get("ClientAddressHeader"),
            IsBehindCdn=json_data.get("IsBehindCdn"),
            IsCacheControlRespected=json_data.get("IsCacheControlRespected"),
            IsHttpsEnabled=json_data.get("IsHttpsEnabled"),
            IsHttpsForced=json_data.get("IsHttpsForced"),
            IsOriginCompressionEnabled=json_data.get("IsOriginCompressionEnabled"),
            IsResponseBufferingEnabled=json_data.get("IsResponseBufferingEnabled"),
            IsSniEnabled=json_data.get("IsSniEnabled"),
            TlsProtocols=json_data.get("TlsProtocols"),
            WebsocketPathPrefixes=json_data.get("WebsocketPathPrefixes"),
            HealthChecks=deserialize_list(json_data.get("HealthChecks"), HealthChecksDefinition),
            LoadBalancingMethod=deserialize_list(json_data.get("LoadBalancingMethod"), LoadBalancingMethodDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyConfigDefinition = PolicyConfigDefinition


@dataclass
class HealthChecksDefinition(BaseModel):
    ExpectedResponseCodeGroup: Optional[Sequence[str]]
    ExpectedResponseText: Optional[str]
    Headers: Optional[Sequence["_HeadersDefinition"]]
    HealthyThreshold: Optional[float]
    IntervalInSeconds: Optional[float]
    IsEnabled: Optional[bool]
    IsResponseTextCheckEnabled: Optional[bool]
    Method: Optional[str]
    Path: Optional[str]
    TimeoutInSeconds: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthChecksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthChecksDefinition"]:
        if not json_data:
            return None
        return cls(
            ExpectedResponseCodeGroup=json_data.get("ExpectedResponseCodeGroup"),
            ExpectedResponseText=json_data.get("ExpectedResponseText"),
            Headers=deserialize_list(json_data.get("Headers"), HeadersDefinition),
            HealthyThreshold=json_data.get("HealthyThreshold"),
            IntervalInSeconds=json_data.get("IntervalInSeconds"),
            IsEnabled=json_data.get("IsEnabled"),
            IsResponseTextCheckEnabled=json_data.get("IsResponseTextCheckEnabled"),
            Method=json_data.get("Method"),
            Path=json_data.get("Path"),
            TimeoutInSeconds=json_data.get("TimeoutInSeconds"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthChecksDefinition = HealthChecksDefinition


@dataclass
class HeadersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HeadersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HeadersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HeadersDefinition = HeadersDefinition


@dataclass
class LoadBalancingMethodDefinition(BaseModel):
    Domain: Optional[str]
    ExpirationTimeInSeconds: Optional[float]
    Method: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LoadBalancingMethodDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoadBalancingMethodDefinition"]:
        if not json_data:
            return None
        return cls(
            Domain=json_data.get("Domain"),
            ExpirationTimeInSeconds=json_data.get("ExpirationTimeInSeconds"),
            Method=json_data.get("Method"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoadBalancingMethodDefinition = LoadBalancingMethodDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


@dataclass
class WafConfigDefinition(BaseModel):
    Origin: Optional[str]
    OriginGroups: Optional[Sequence[str]]
    AccessRules: Optional[Sequence["_AccessRulesDefinition"]]
    AddressRateLimiting: Optional[Sequence["_AddressRateLimitingDefinition"]]
    CachingRules: Optional[Sequence["_CachingRulesDefinition"]]
    Captchas: Optional[Sequence["_CaptchasDefinition"]]
    CustomProtectionRules: Optional[Sequence["_CustomProtectionRulesDefinition"]]
    DeviceFingerprintChallenge: Optional[Sequence["_DeviceFingerprintChallengeDefinition"]]
    HumanInteractionChallenge: Optional[Sequence["_HumanInteractionChallengeDefinition"]]
    JsChallenge: Optional[Sequence["_JsChallengeDefinition"]]
    ProtectionSettings: Optional[Sequence["_ProtectionSettingsDefinition"]]
    Whitelists: Optional[Sequence["_WhitelistsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Origin=json_data.get("Origin"),
            OriginGroups=json_data.get("OriginGroups"),
            AccessRules=deserialize_list(json_data.get("AccessRules"), AccessRulesDefinition),
            AddressRateLimiting=deserialize_list(json_data.get("AddressRateLimiting"), AddressRateLimitingDefinition),
            CachingRules=deserialize_list(json_data.get("CachingRules"), CachingRulesDefinition),
            Captchas=deserialize_list(json_data.get("Captchas"), CaptchasDefinition),
            CustomProtectionRules=deserialize_list(json_data.get("CustomProtectionRules"), CustomProtectionRulesDefinition),
            DeviceFingerprintChallenge=deserialize_list(json_data.get("DeviceFingerprintChallenge"), DeviceFingerprintChallengeDefinition),
            HumanInteractionChallenge=deserialize_list(json_data.get("HumanInteractionChallenge"), HumanInteractionChallengeDefinition),
            JsChallenge=deserialize_list(json_data.get("JsChallenge"), JsChallengeDefinition),
            ProtectionSettings=deserialize_list(json_data.get("ProtectionSettings"), ProtectionSettingsDefinition),
            Whitelists=deserialize_list(json_data.get("Whitelists"), WhitelistsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafConfigDefinition = WafConfigDefinition


@dataclass
class AccessRulesDefinition(BaseModel):
    Action: Optional[str]
    BlockAction: Optional[str]
    BlockErrorPageCode: Optional[str]
    BlockErrorPageDescription: Optional[str]
    BlockErrorPageMessage: Optional[str]
    BlockResponseCode: Optional[float]
    BypassChallenges: Optional[Sequence[str]]
    CaptchaFooter: Optional[str]
    CaptchaHeader: Optional[str]
    CaptchaSubmitLabel: Optional[str]
    CaptchaTitle: Optional[str]
    Name: Optional[str]
    RedirectResponseCode: Optional[str]
    RedirectUrl: Optional[str]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    ResponseHeaderManipulation: Optional[Sequence["_ResponseHeaderManipulationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            BlockAction=json_data.get("BlockAction"),
            BlockErrorPageCode=json_data.get("BlockErrorPageCode"),
            BlockErrorPageDescription=json_data.get("BlockErrorPageDescription"),
            BlockErrorPageMessage=json_data.get("BlockErrorPageMessage"),
            BlockResponseCode=json_data.get("BlockResponseCode"),
            BypassChallenges=json_data.get("BypassChallenges"),
            CaptchaFooter=json_data.get("CaptchaFooter"),
            CaptchaHeader=json_data.get("CaptchaHeader"),
            CaptchaSubmitLabel=json_data.get("CaptchaSubmitLabel"),
            CaptchaTitle=json_data.get("CaptchaTitle"),
            Name=json_data.get("Name"),
            RedirectResponseCode=json_data.get("RedirectResponseCode"),
            RedirectUrl=json_data.get("RedirectUrl"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            ResponseHeaderManipulation=deserialize_list(json_data.get("ResponseHeaderManipulation"), ResponseHeaderManipulationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRulesDefinition = AccessRulesDefinition


@dataclass
class CriteriaDefinition(BaseModel):
    Condition: Optional[str]
    IsCaseSensitive: Optional[bool]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CriteriaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CriteriaDefinition"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            IsCaseSensitive=json_data.get("IsCaseSensitive"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CriteriaDefinition = CriteriaDefinition


@dataclass
class ResponseHeaderManipulationDefinition(BaseModel):
    Action: Optional[str]
    Header: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResponseHeaderManipulationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResponseHeaderManipulationDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Header=json_data.get("Header"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResponseHeaderManipulationDefinition = ResponseHeaderManipulationDefinition


@dataclass
class AddressRateLimitingDefinition(BaseModel):
    AllowedRatePerAddress: Optional[float]
    BlockResponseCode: Optional[float]
    IsEnabled: Optional[bool]
    MaxDelayedCountPerAddress: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddressRateLimitingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressRateLimitingDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedRatePerAddress=json_data.get("AllowedRatePerAddress"),
            BlockResponseCode=json_data.get("BlockResponseCode"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxDelayedCountPerAddress=json_data.get("MaxDelayedCountPerAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressRateLimitingDefinition = AddressRateLimitingDefinition


@dataclass
class CachingRulesDefinition(BaseModel):
    Action: Optional[str]
    CachingDuration: Optional[str]
    ClientCachingDuration: Optional[str]
    IsClientCachingEnabled: Optional[bool]
    Key: Optional[str]
    Name: Optional[str]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CachingRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CachingRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CachingDuration=json_data.get("CachingDuration"),
            ClientCachingDuration=json_data.get("ClientCachingDuration"),
            IsClientCachingEnabled=json_data.get("IsClientCachingEnabled"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CachingRulesDefinition = CachingRulesDefinition


@dataclass
class CaptchasDefinition(BaseModel):
    FailureMessage: Optional[str]
    FooterText: Optional[str]
    HeaderText: Optional[str]
    SessionExpirationInSeconds: Optional[float]
    SubmitLabel: Optional[str]
    Title: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CaptchasDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CaptchasDefinition"]:
        if not json_data:
            return None
        return cls(
            FailureMessage=json_data.get("FailureMessage"),
            FooterText=json_data.get("FooterText"),
            HeaderText=json_data.get("HeaderText"),
            SessionExpirationInSeconds=json_data.get("SessionExpirationInSeconds"),
            SubmitLabel=json_data.get("SubmitLabel"),
            Title=json_data.get("Title"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CaptchasDefinition = CaptchasDefinition


@dataclass
class CustomProtectionRulesDefinition(BaseModel):
    Action: Optional[str]
    Id: Optional[str]
    Exclusions: Optional[Sequence["_ExclusionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CustomProtectionRulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomProtectionRulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
            Exclusions=deserialize_list(json_data.get("Exclusions"), ExclusionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomProtectionRulesDefinition = CustomProtectionRulesDefinition


@dataclass
class ExclusionsDefinition(BaseModel):
    Exclusions: Optional[Sequence[str]]
    Target: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExclusionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExclusionsDefinition"]:
        if not json_data:
            return None
        return cls(
            Exclusions=json_data.get("Exclusions"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExclusionsDefinition = ExclusionsDefinition


@dataclass
class DeviceFingerprintChallengeDefinition(BaseModel):
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    FailureThreshold: Optional[float]
    FailureThresholdExpirationInSeconds: Optional[float]
    IsEnabled: Optional[bool]
    MaxAddressCount: Optional[float]
    MaxAddressCountExpirationInSeconds: Optional[float]
    ChallengeSettings: Optional[Sequence["_ChallengeSettingsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceFingerprintChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceFingerprintChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionExpirationInSeconds=json_data.get("ActionExpirationInSeconds"),
            FailureThreshold=json_data.get("FailureThreshold"),
            FailureThresholdExpirationInSeconds=json_data.get("FailureThresholdExpirationInSeconds"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxAddressCount=json_data.get("MaxAddressCount"),
            MaxAddressCountExpirationInSeconds=json_data.get("MaxAddressCountExpirationInSeconds"),
            ChallengeSettings=deserialize_list(json_data.get("ChallengeSettings"), ChallengeSettingsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceFingerprintChallengeDefinition = DeviceFingerprintChallengeDefinition


@dataclass
class ChallengeSettingsDefinition(BaseModel):
    BlockAction: Optional[str]
    BlockErrorPageCode: Optional[str]
    BlockErrorPageDescription: Optional[str]
    BlockErrorPageMessage: Optional[str]
    BlockResponseCode: Optional[float]
    CaptchaFooter: Optional[str]
    CaptchaHeader: Optional[str]
    CaptchaSubmitLabel: Optional[str]
    CaptchaTitle: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ChallengeSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChallengeSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            BlockAction=json_data.get("BlockAction"),
            BlockErrorPageCode=json_data.get("BlockErrorPageCode"),
            BlockErrorPageDescription=json_data.get("BlockErrorPageDescription"),
            BlockErrorPageMessage=json_data.get("BlockErrorPageMessage"),
            BlockResponseCode=json_data.get("BlockResponseCode"),
            CaptchaFooter=json_data.get("CaptchaFooter"),
            CaptchaHeader=json_data.get("CaptchaHeader"),
            CaptchaSubmitLabel=json_data.get("CaptchaSubmitLabel"),
            CaptchaTitle=json_data.get("CaptchaTitle"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ChallengeSettingsDefinition = ChallengeSettingsDefinition


@dataclass
class HumanInteractionChallengeDefinition(BaseModel):
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    FailureThreshold: Optional[float]
    FailureThresholdExpirationInSeconds: Optional[float]
    InteractionThreshold: Optional[float]
    IsEnabled: Optional[bool]
    IsNatEnabled: Optional[bool]
    RecordingPeriodInSeconds: Optional[float]
    ChallengeSettings: Optional[Sequence["_ChallengeSettingsDefinition"]]
    SetHttpHeader: Optional[Sequence["_SetHttpHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_HumanInteractionChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HumanInteractionChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionExpirationInSeconds=json_data.get("ActionExpirationInSeconds"),
            FailureThreshold=json_data.get("FailureThreshold"),
            FailureThresholdExpirationInSeconds=json_data.get("FailureThresholdExpirationInSeconds"),
            InteractionThreshold=json_data.get("InteractionThreshold"),
            IsEnabled=json_data.get("IsEnabled"),
            IsNatEnabled=json_data.get("IsNatEnabled"),
            RecordingPeriodInSeconds=json_data.get("RecordingPeriodInSeconds"),
            ChallengeSettings=deserialize_list(json_data.get("ChallengeSettings"), ChallengeSettingsDefinition),
            SetHttpHeader=deserialize_list(json_data.get("SetHttpHeader"), SetHttpHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_HumanInteractionChallengeDefinition = HumanInteractionChallengeDefinition


@dataclass
class SetHttpHeaderDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetHttpHeaderDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetHttpHeaderDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetHttpHeaderDefinition = SetHttpHeaderDefinition


@dataclass
class JsChallengeDefinition(BaseModel):
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    AreRedirectsChallenged: Optional[bool]
    FailureThreshold: Optional[float]
    IsEnabled: Optional[bool]
    IsNatEnabled: Optional[bool]
    ChallengeSettings: Optional[Sequence["_ChallengeSettingsDefinition"]]
    Criteria: Optional[Sequence["_CriteriaDefinition"]]
    SetHttpHeader: Optional[Sequence["_SetHttpHeaderDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_JsChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionExpirationInSeconds=json_data.get("ActionExpirationInSeconds"),
            AreRedirectsChallenged=json_data.get("AreRedirectsChallenged"),
            FailureThreshold=json_data.get("FailureThreshold"),
            IsEnabled=json_data.get("IsEnabled"),
            IsNatEnabled=json_data.get("IsNatEnabled"),
            ChallengeSettings=deserialize_list(json_data.get("ChallengeSettings"), ChallengeSettingsDefinition),
            Criteria=deserialize_list(json_data.get("Criteria"), CriteriaDefinition),
            SetHttpHeader=deserialize_list(json_data.get("SetHttpHeader"), SetHttpHeaderDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsChallengeDefinition = JsChallengeDefinition


@dataclass
class ProtectionSettingsDefinition(BaseModel):
    AllowedHttpMethods: Optional[Sequence[str]]
    BlockAction: Optional[str]
    BlockErrorPageCode: Optional[str]
    BlockErrorPageDescription: Optional[str]
    BlockErrorPageMessage: Optional[str]
    BlockResponseCode: Optional[float]
    IsResponseInspected: Optional[bool]
    MaxArgumentCount: Optional[float]
    MaxNameLengthPerArgument: Optional[float]
    MaxResponseSizeInKiB: Optional[float]
    MaxTotalNameLengthOfArguments: Optional[float]
    MediaTypes: Optional[Sequence[str]]
    RecommendationsPeriodInDays: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ProtectionSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtectionSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedHttpMethods=json_data.get("AllowedHttpMethods"),
            BlockAction=json_data.get("BlockAction"),
            BlockErrorPageCode=json_data.get("BlockErrorPageCode"),
            BlockErrorPageDescription=json_data.get("BlockErrorPageDescription"),
            BlockErrorPageMessage=json_data.get("BlockErrorPageMessage"),
            BlockResponseCode=json_data.get("BlockResponseCode"),
            IsResponseInspected=json_data.get("IsResponseInspected"),
            MaxArgumentCount=json_data.get("MaxArgumentCount"),
            MaxNameLengthPerArgument=json_data.get("MaxNameLengthPerArgument"),
            MaxResponseSizeInKiB=json_data.get("MaxResponseSizeInKiB"),
            MaxTotalNameLengthOfArguments=json_data.get("MaxTotalNameLengthOfArguments"),
            MediaTypes=json_data.get("MediaTypes"),
            RecommendationsPeriodInDays=json_data.get("RecommendationsPeriodInDays"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProtectionSettingsDefinition = ProtectionSettingsDefinition


@dataclass
class WhitelistsDefinition(BaseModel):
    AddressLists: Optional[Sequence[str]]
    Addresses: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_WhitelistsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WhitelistsDefinition"]:
        if not json_data:
            return None
        return cls(
            AddressLists=json_data.get("AddressLists"),
            Addresses=json_data.get("Addresses"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WhitelistsDefinition = WhitelistsDefinition


