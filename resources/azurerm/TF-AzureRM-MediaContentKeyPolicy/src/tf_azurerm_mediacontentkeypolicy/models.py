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
    Description: Optional[str]
    Id: Optional[str]
    MediaServicesAccountName: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    PolicyOption: Optional[Sequence["_PolicyOptionDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MediaServicesAccountName=json_data.get("MediaServicesAccountName"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            PolicyOption=deserialize_list(json_data.get("PolicyOption"), PolicyOptionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PolicyOptionDefinition(BaseModel):
    ClearKeyConfigurationEnabled: Optional[bool]
    Name: Optional[str]
    OpenRestrictionEnabled: Optional[bool]
    WidevineConfigurationTemplate: Optional[str]
    FairplayConfiguration: Optional[Sequence["_FairplayConfigurationDefinition"]]
    PlayreadyConfigurationLicense: Optional[Sequence["_PlayreadyConfigurationLicenseDefinition"]]
    TokenRestriction: Optional[Sequence["_TokenRestrictionDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PolicyOptionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PolicyOptionDefinition"]:
        if not json_data:
            return None
        return cls(
            ClearKeyConfigurationEnabled=json_data.get("ClearKeyConfigurationEnabled"),
            Name=json_data.get("Name"),
            OpenRestrictionEnabled=json_data.get("OpenRestrictionEnabled"),
            WidevineConfigurationTemplate=json_data.get("WidevineConfigurationTemplate"),
            FairplayConfiguration=deserialize_list(json_data.get("FairplayConfiguration"), FairplayConfigurationDefinition),
            PlayreadyConfigurationLicense=deserialize_list(json_data.get("PlayreadyConfigurationLicense"), PlayreadyConfigurationLicenseDefinition),
            TokenRestriction=deserialize_list(json_data.get("TokenRestriction"), TokenRestrictionDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PolicyOptionDefinition = PolicyOptionDefinition


@dataclass
class FairplayConfigurationDefinition(BaseModel):
    Ask: Optional[str]
    Pfx: Optional[str]
    PfxPassword: Optional[str]
    RentalAndLeaseKeyType: Optional[str]
    RentalDurationSeconds: Optional[float]
    OfflineRentalConfiguration: Optional[Sequence["_OfflineRentalConfigurationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_FairplayConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FairplayConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            Ask=json_data.get("Ask"),
            Pfx=json_data.get("Pfx"),
            PfxPassword=json_data.get("PfxPassword"),
            RentalAndLeaseKeyType=json_data.get("RentalAndLeaseKeyType"),
            RentalDurationSeconds=json_data.get("RentalDurationSeconds"),
            OfflineRentalConfiguration=deserialize_list(json_data.get("OfflineRentalConfiguration"), OfflineRentalConfigurationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_FairplayConfigurationDefinition = FairplayConfigurationDefinition


@dataclass
class OfflineRentalConfigurationDefinition(BaseModel):
    PlaybackDurationSeconds: Optional[float]
    StorageDurationSeconds: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_OfflineRentalConfigurationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OfflineRentalConfigurationDefinition"]:
        if not json_data:
            return None
        return cls(
            PlaybackDurationSeconds=json_data.get("PlaybackDurationSeconds"),
            StorageDurationSeconds=json_data.get("StorageDurationSeconds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OfflineRentalConfigurationDefinition = OfflineRentalConfigurationDefinition


@dataclass
class PlayreadyConfigurationLicenseDefinition(BaseModel):
    AllowTestDevices: Optional[bool]
    BeginDate: Optional[str]
    ContentKeyLocationFromHeaderEnabled: Optional[bool]
    ContentKeyLocationFromKeyId: Optional[str]
    ContentType: Optional[str]
    ExpirationDate: Optional[str]
    GracePeriod: Optional[str]
    LicenseType: Optional[str]
    RelativeBeginDate: Optional[str]
    RelativeExpirationDate: Optional[str]
    PlayRight: Optional[Sequence["_PlayRightDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PlayreadyConfigurationLicenseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlayreadyConfigurationLicenseDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowTestDevices=json_data.get("AllowTestDevices"),
            BeginDate=json_data.get("BeginDate"),
            ContentKeyLocationFromHeaderEnabled=json_data.get("ContentKeyLocationFromHeaderEnabled"),
            ContentKeyLocationFromKeyId=json_data.get("ContentKeyLocationFromKeyId"),
            ContentType=json_data.get("ContentType"),
            ExpirationDate=json_data.get("ExpirationDate"),
            GracePeriod=json_data.get("GracePeriod"),
            LicenseType=json_data.get("LicenseType"),
            RelativeBeginDate=json_data.get("RelativeBeginDate"),
            RelativeExpirationDate=json_data.get("RelativeExpirationDate"),
            PlayRight=deserialize_list(json_data.get("PlayRight"), PlayRightDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlayreadyConfigurationLicenseDefinition = PlayreadyConfigurationLicenseDefinition


@dataclass
class PlayRightDefinition(BaseModel):
    AgcAndColorStripeRestriction: Optional[float]
    AllowPassingVideoContentToUnknownOutput: Optional[str]
    AnalogVideoOpl: Optional[float]
    CompressedDigitalAudioOpl: Optional[float]
    DigitalVideoOnlyContentRestriction: Optional[bool]
    FirstPlayExpiration: Optional[str]
    ImageConstraintForAnalogComponentVideoRestriction: Optional[bool]
    ImageConstraintForAnalogComputerMonitorRestriction: Optional[bool]
    ScmsRestriction: Optional[float]
    UncompressedDigitalAudioOpl: Optional[float]
    UncompressedDigitalVideoOpl: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PlayRightDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PlayRightDefinition"]:
        if not json_data:
            return None
        return cls(
            AgcAndColorStripeRestriction=json_data.get("AgcAndColorStripeRestriction"),
            AllowPassingVideoContentToUnknownOutput=json_data.get("AllowPassingVideoContentToUnknownOutput"),
            AnalogVideoOpl=json_data.get("AnalogVideoOpl"),
            CompressedDigitalAudioOpl=json_data.get("CompressedDigitalAudioOpl"),
            DigitalVideoOnlyContentRestriction=json_data.get("DigitalVideoOnlyContentRestriction"),
            FirstPlayExpiration=json_data.get("FirstPlayExpiration"),
            ImageConstraintForAnalogComponentVideoRestriction=json_data.get("ImageConstraintForAnalogComponentVideoRestriction"),
            ImageConstraintForAnalogComputerMonitorRestriction=json_data.get("ImageConstraintForAnalogComputerMonitorRestriction"),
            ScmsRestriction=json_data.get("ScmsRestriction"),
            UncompressedDigitalAudioOpl=json_data.get("UncompressedDigitalAudioOpl"),
            UncompressedDigitalVideoOpl=json_data.get("UncompressedDigitalVideoOpl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PlayRightDefinition = PlayRightDefinition


@dataclass
class TokenRestrictionDefinition(BaseModel):
    Audience: Optional[str]
    Issuer: Optional[str]
    OpenIdConnectDiscoveryDocument: Optional[str]
    PrimaryRsaTokenKeyExponent: Optional[str]
    PrimaryRsaTokenKeyModulus: Optional[str]
    PrimarySymmetricTokenKey: Optional[str]
    PrimaryX509TokenKeyRaw: Optional[str]
    TokenType: Optional[str]
    RequiredClaim: Optional[Sequence["_RequiredClaimDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TokenRestrictionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TokenRestrictionDefinition"]:
        if not json_data:
            return None
        return cls(
            Audience=json_data.get("Audience"),
            Issuer=json_data.get("Issuer"),
            OpenIdConnectDiscoveryDocument=json_data.get("OpenIdConnectDiscoveryDocument"),
            PrimaryRsaTokenKeyExponent=json_data.get("PrimaryRsaTokenKeyExponent"),
            PrimaryRsaTokenKeyModulus=json_data.get("PrimaryRsaTokenKeyModulus"),
            PrimarySymmetricTokenKey=json_data.get("PrimarySymmetricTokenKey"),
            PrimaryX509TokenKeyRaw=json_data.get("PrimaryX509TokenKeyRaw"),
            TokenType=json_data.get("TokenType"),
            RequiredClaim=deserialize_list(json_data.get("RequiredClaim"), RequiredClaimDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TokenRestrictionDefinition = TokenRestrictionDefinition


@dataclass
class RequiredClaimDefinition(BaseModel):
    Type: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RequiredClaimDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RequiredClaimDefinition"]:
        if not json_data:
            return None
        return cls(
            Type=json_data.get("Type"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RequiredClaimDefinition = RequiredClaimDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


