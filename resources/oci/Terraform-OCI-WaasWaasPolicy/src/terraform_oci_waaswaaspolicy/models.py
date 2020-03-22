# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AdditionalDomains: Optional[Sequence[str]]
    Cname: Optional[str]
    CompartmentId: Optional[str]
    DefinedTags: Optional[Sequence["_DefinedTags"]]
    DisplayName: Optional[str]
    Domain: Optional[str]
    FreeformTags: Optional[Sequence["_FreeformTags"]]
    Id: Optional[str]
    State: Optional[str]
    TimeCreated: Optional[str]
    OriginGroups: Optional[Sequence["_OriginGroups"]]
    Origins: Optional[Sequence["_Origins"]]
    PolicyConfig: Optional[Sequence["_PolicyConfig"]]
    Timeouts: Optional["_Timeouts"]
    WafConfig: Optional[Sequence["_WafConfig"]]
    OriginGroup: Optional[Sequence["_OriginGroup"]]
    CustomHeaders: Optional[Sequence["_CustomHeaders"]]
    AccessRules: Optional[Sequence["_AccessRules"]]
    AddressRateLimiting: Optional[Sequence["_AddressRateLimiting"]]
    CachingRules: Optional[Sequence["_CachingRules"]]
    Captchas: Optional[Sequence["_Captchas"]]
    CustomProtectionRules: Optional[Sequence["_CustomProtectionRules"]]
    DeviceFingerprintChallenge: Optional[Sequence["_DeviceFingerprintChallenge"]]
    HumanInteractionChallenge: Optional[Sequence["_HumanInteractionChallenge"]]
    JsChallenge: Optional[Sequence["_JsChallenge"]]
    ProtectionSettings: Optional[Sequence["_ProtectionSettings"]]
    Whitelists: Optional[Sequence["_Whitelists"]]
    Criteria: Optional[Sequence["_Criteria"]]
    ChallengeSettings: Optional[Sequence["_ChallengeSettings"]]
    SetHttpHeader: Optional[Sequence["_SetHttpHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AdditionalDomains=json_data.get("AdditionalDomains"),
            Cname=json_data.get("Cname"),
            CompartmentId=json_data.get("CompartmentId"),
            DefinedTags=json_data.get("DefinedTags"),
            DisplayName=json_data.get("DisplayName"),
            Domain=json_data.get("Domain"),
            FreeformTags=json_data.get("FreeformTags"),
            Id=json_data.get("Id"),
            State=json_data.get("State"),
            TimeCreated=json_data.get("TimeCreated"),
            OriginGroups=json_data.get("OriginGroups"),
            Origins=json_data.get("Origins"),
            PolicyConfig=json_data.get("PolicyConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
            WafConfig=json_data.get("WafConfig"),
            OriginGroup=json_data.get("OriginGroup"),
            CustomHeaders=json_data.get("CustomHeaders"),
            AccessRules=json_data.get("AccessRules"),
            AddressRateLimiting=json_data.get("AddressRateLimiting"),
            CachingRules=json_data.get("CachingRules"),
            Captchas=json_data.get("Captchas"),
            CustomProtectionRules=json_data.get("CustomProtectionRules"),
            DeviceFingerprintChallenge=json_data.get("DeviceFingerprintChallenge"),
            HumanInteractionChallenge=json_data.get("HumanInteractionChallenge"),
            JsChallenge=json_data.get("JsChallenge"),
            ProtectionSettings=json_data.get("ProtectionSettings"),
            Whitelists=json_data.get("Whitelists"),
            Criteria=json_data.get("Criteria"),
            ChallengeSettings=json_data.get("ChallengeSettings"),
            SetHttpHeader=json_data.get("SetHttpHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DefinedTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefinedTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefinedTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefinedTags = DefinedTags


@dataclass
class FreeformTags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FreeformTags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FreeformTags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FreeformTags = FreeformTags


@dataclass
class OriginGroups:
    Label: Optional[str]
    OriginGroup: Optional[Sequence["_OriginGroup"]]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroups"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroups"]:
        if not json_data:
            return None
        return cls(
            Label=json_data.get("Label"),
            OriginGroup=json_data.get("OriginGroup"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroups = OriginGroups


@dataclass
class OriginGroup:
    Origin: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OriginGroup"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OriginGroup"]:
        if not json_data:
            return None
        return cls(
            Origin=json_data.get("Origin"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OriginGroup = OriginGroup


@dataclass
class Origins:
    HttpPort: Optional[float]
    HttpsPort: Optional[float]
    Label: Optional[str]
    Uri: Optional[str]
    CustomHeaders: Optional[Sequence["_CustomHeaders"]]

    @classmethod
    def _deserialize(
        cls: Type["_Origins"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Origins"]:
        if not json_data:
            return None
        return cls(
            HttpPort=json_data.get("HttpPort"),
            HttpsPort=json_data.get("HttpsPort"),
            Label=json_data.get("Label"),
            Uri=json_data.get("Uri"),
            CustomHeaders=json_data.get("CustomHeaders"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Origins = Origins


@dataclass
class CustomHeaders:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomHeaders"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomHeaders = CustomHeaders


@dataclass
class PolicyConfig:
    CertificateId: Optional[str]
    CipherGroup: Optional[str]
    ClientAddressHeader: Optional[str]
    IsBehindCdn: Optional[bool]
    IsCacheControlRespected: Optional[bool]
    IsHttpsEnabled: Optional[bool]
    IsHttpsForced: Optional[bool]
    IsOriginCompressionEnabled: Optional[bool]
    IsResponseBufferingEnabled: Optional[bool]
    TlsProtocols: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyConfig"]:
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
            TlsProtocols=json_data.get("TlsProtocols"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyConfig = PolicyConfig


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


@dataclass
class WafConfig:
    Origin: Optional[str]
    OriginGroups: Optional[Sequence[str]]
    AccessRules: Optional[Sequence["_AccessRules"]]
    AddressRateLimiting: Optional[Sequence["_AddressRateLimiting"]]
    CachingRules: Optional[Sequence["_CachingRules"]]
    Captchas: Optional[Sequence["_Captchas"]]
    CustomProtectionRules: Optional[Sequence["_CustomProtectionRules"]]
    DeviceFingerprintChallenge: Optional[Sequence["_DeviceFingerprintChallenge"]]
    HumanInteractionChallenge: Optional[Sequence["_HumanInteractionChallenge"]]
    JsChallenge: Optional[Sequence["_JsChallenge"]]
    ProtectionSettings: Optional[Sequence["_ProtectionSettings"]]
    Whitelists: Optional[Sequence["_Whitelists"]]

    @classmethod
    def _deserialize(
        cls: Type["_WafConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_WafConfig"]:
        if not json_data:
            return None
        return cls(
            Origin=json_data.get("Origin"),
            OriginGroups=json_data.get("OriginGroups"),
            AccessRules=json_data.get("AccessRules"),
            AddressRateLimiting=json_data.get("AddressRateLimiting"),
            CachingRules=json_data.get("CachingRules"),
            Captchas=json_data.get("Captchas"),
            CustomProtectionRules=json_data.get("CustomProtectionRules"),
            DeviceFingerprintChallenge=json_data.get("DeviceFingerprintChallenge"),
            HumanInteractionChallenge=json_data.get("HumanInteractionChallenge"),
            JsChallenge=json_data.get("JsChallenge"),
            ProtectionSettings=json_data.get("ProtectionSettings"),
            Whitelists=json_data.get("Whitelists"),
        )


# work around possible type aliasing issues when variable has same name as a model
_WafConfig = WafConfig


@dataclass
class AccessRules:
    Action: Optional[str]
    BlockAction: Optional[str]
    BlockErrorPageCode: Optional[str]
    BlockErrorPageDescription: Optional[str]
    BlockErrorPageMessage: Optional[str]
    BlockResponseCode: Optional[float]
    BypassChallenges: Optional[Sequence[str]]
    Name: Optional[str]
    RedirectResponseCode: Optional[str]
    RedirectUrl: Optional[str]
    Criteria: Optional[Sequence["_Criteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessRules"]:
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
            Name=json_data.get("Name"),
            RedirectResponseCode=json_data.get("RedirectResponseCode"),
            RedirectUrl=json_data.get("RedirectUrl"),
            Criteria=json_data.get("Criteria"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessRules = AccessRules


@dataclass
class Criteria:
    Condition: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Criteria"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Criteria"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Criteria = Criteria


@dataclass
class AddressRateLimiting:
    AllowedRatePerAddress: Optional[float]
    BlockResponseCode: Optional[float]
    IsEnabled: Optional[bool]
    MaxDelayedCountPerAddress: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_AddressRateLimiting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressRateLimiting"]:
        if not json_data:
            return None
        return cls(
            AllowedRatePerAddress=json_data.get("AllowedRatePerAddress"),
            BlockResponseCode=json_data.get("BlockResponseCode"),
            IsEnabled=json_data.get("IsEnabled"),
            MaxDelayedCountPerAddress=json_data.get("MaxDelayedCountPerAddress"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressRateLimiting = AddressRateLimiting


@dataclass
class CachingRules:
    Action: Optional[str]
    CachingDuration: Optional[str]
    ClientCachingDuration: Optional[str]
    IsClientCachingEnabled: Optional[bool]
    Key: Optional[str]
    Name: Optional[str]
    Criteria: Optional[Sequence["_Criteria"]]

    @classmethod
    def _deserialize(
        cls: Type["_CachingRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CachingRules"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CachingDuration=json_data.get("CachingDuration"),
            ClientCachingDuration=json_data.get("ClientCachingDuration"),
            IsClientCachingEnabled=json_data.get("IsClientCachingEnabled"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            Criteria=json_data.get("Criteria"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CachingRules = CachingRules


@dataclass
class Captchas:
    FailureMessage: Optional[str]
    FooterText: Optional[str]
    HeaderText: Optional[str]
    SessionExpirationInSeconds: Optional[float]
    SubmitLabel: Optional[str]
    Title: Optional[str]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Captchas"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Captchas"]:
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
_Captchas = Captchas


@dataclass
class CustomProtectionRules:
    Action: Optional[str]
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomProtectionRules"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomProtectionRules"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomProtectionRules = CustomProtectionRules


@dataclass
class DeviceFingerprintChallenge:
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    FailureThreshold: Optional[float]
    FailureThresholdExpirationInSeconds: Optional[float]
    IsEnabled: Optional[bool]
    MaxAddressCount: Optional[float]
    MaxAddressCountExpirationInSeconds: Optional[float]
    ChallengeSettings: Optional[Sequence["_ChallengeSettings"]]

    @classmethod
    def _deserialize(
        cls: Type["_DeviceFingerprintChallenge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeviceFingerprintChallenge"]:
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
            ChallengeSettings=json_data.get("ChallengeSettings"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeviceFingerprintChallenge = DeviceFingerprintChallenge


@dataclass
class ChallengeSettings:
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
        cls: Type["_ChallengeSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ChallengeSettings"]:
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
_ChallengeSettings = ChallengeSettings


@dataclass
class HumanInteractionChallenge:
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    FailureThreshold: Optional[float]
    FailureThresholdExpirationInSeconds: Optional[float]
    InteractionThreshold: Optional[float]
    IsEnabled: Optional[bool]
    RecordingPeriodInSeconds: Optional[float]
    ChallengeSettings: Optional[Sequence["_ChallengeSettings"]]
    SetHttpHeader: Optional[Sequence["_SetHttpHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_HumanInteractionChallenge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HumanInteractionChallenge"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionExpirationInSeconds=json_data.get("ActionExpirationInSeconds"),
            FailureThreshold=json_data.get("FailureThreshold"),
            FailureThresholdExpirationInSeconds=json_data.get("FailureThresholdExpirationInSeconds"),
            InteractionThreshold=json_data.get("InteractionThreshold"),
            IsEnabled=json_data.get("IsEnabled"),
            RecordingPeriodInSeconds=json_data.get("RecordingPeriodInSeconds"),
            ChallengeSettings=json_data.get("ChallengeSettings"),
            SetHttpHeader=json_data.get("SetHttpHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HumanInteractionChallenge = HumanInteractionChallenge


@dataclass
class SetHttpHeader:
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SetHttpHeader"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SetHttpHeader"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SetHttpHeader = SetHttpHeader


@dataclass
class JsChallenge:
    Action: Optional[str]
    ActionExpirationInSeconds: Optional[float]
    FailureThreshold: Optional[float]
    IsEnabled: Optional[bool]
    ChallengeSettings: Optional[Sequence["_ChallengeSettings"]]
    SetHttpHeader: Optional[Sequence["_SetHttpHeader"]]

    @classmethod
    def _deserialize(
        cls: Type["_JsChallenge"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_JsChallenge"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            ActionExpirationInSeconds=json_data.get("ActionExpirationInSeconds"),
            FailureThreshold=json_data.get("FailureThreshold"),
            IsEnabled=json_data.get("IsEnabled"),
            ChallengeSettings=json_data.get("ChallengeSettings"),
            SetHttpHeader=json_data.get("SetHttpHeader"),
        )


# work around possible type aliasing issues when variable has same name as a model
_JsChallenge = JsChallenge


@dataclass
class ProtectionSettings:
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
        cls: Type["_ProtectionSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProtectionSettings"]:
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
_ProtectionSettings = ProtectionSettings


@dataclass
class Whitelists:
    Addresses: Optional[Sequence[str]]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Whitelists"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Whitelists"]:
        if not json_data:
            return None
        return cls(
            Addresses=json_data.get("Addresses"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Whitelists = Whitelists


