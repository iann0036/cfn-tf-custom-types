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
    ActivateProtectionsByExtendedAttributes: Optional[Sequence["_ActivateProtectionsByExtendedAttributesDefinition2"]]
    ActiveProtectionsPerformanceImpact: Optional[str]
    ActiveProtectionsSeverity: Optional[str]
    AntiBot: Optional[bool]
    AntiVirus: Optional[bool]
    Color: Optional[str]
    Comments: Optional[str]
    ConfidenceLevelHigh: Optional[str]
    ConfidenceLevelLow: Optional[str]
    ConfidenceLevelMedium: Optional[str]
    Id: Optional[str]
    IgnoreErrors: Optional[bool]
    IgnoreWarnings: Optional[bool]
    Ips: Optional[bool]
    IpsSettings: Optional[Sequence["_IpsSettingsDefinition"]]
    MaliciousMailPolicySettings: Optional[Sequence["_MaliciousMailPolicySettingsDefinition"]]
    Name: Optional[str]
    ScanMaliciousLinks: Optional[Sequence["_ScanMaliciousLinksDefinition"]]
    Tags: Optional[Sequence[str]]
    ThreatEmulation: Optional[bool]
    UseExtendedAttributes: Optional[bool]
    UseIndicators: Optional[bool]
    DeactivateProtectionsByExtendedAttributes: Optional[Sequence["_DeactivateProtectionsByExtendedAttributesDefinition"]]
    IndicatorOverrides: Optional[Sequence["_IndicatorOverridesDefinition"]]
    Overrides: Optional[Sequence["_OverridesDefinition"]]

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
            ActivateProtectionsByExtendedAttributes=deserialize_list(json_data.get("ActivateProtectionsByExtendedAttributes"), ActivateProtectionsByExtendedAttributesDefinition2),
            ActiveProtectionsPerformanceImpact=json_data.get("ActiveProtectionsPerformanceImpact"),
            ActiveProtectionsSeverity=json_data.get("ActiveProtectionsSeverity"),
            AntiBot=json_data.get("AntiBot"),
            AntiVirus=json_data.get("AntiVirus"),
            Color=json_data.get("Color"),
            Comments=json_data.get("Comments"),
            ConfidenceLevelHigh=json_data.get("ConfidenceLevelHigh"),
            ConfidenceLevelLow=json_data.get("ConfidenceLevelLow"),
            ConfidenceLevelMedium=json_data.get("ConfidenceLevelMedium"),
            Id=json_data.get("Id"),
            IgnoreErrors=json_data.get("IgnoreErrors"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Ips=json_data.get("Ips"),
            IpsSettings=deserialize_list(json_data.get("IpsSettings"), IpsSettingsDefinition),
            MaliciousMailPolicySettings=deserialize_list(json_data.get("MaliciousMailPolicySettings"), MaliciousMailPolicySettingsDefinition),
            Name=json_data.get("Name"),
            ScanMaliciousLinks=deserialize_list(json_data.get("ScanMaliciousLinks"), ScanMaliciousLinksDefinition),
            Tags=json_data.get("Tags"),
            ThreatEmulation=json_data.get("ThreatEmulation"),
            UseExtendedAttributes=json_data.get("UseExtendedAttributes"),
            UseIndicators=json_data.get("UseIndicators"),
            DeactivateProtectionsByExtendedAttributes=deserialize_list(json_data.get("DeactivateProtectionsByExtendedAttributes"), DeactivateProtectionsByExtendedAttributesDefinition),
            IndicatorOverrides=deserialize_list(json_data.get("IndicatorOverrides"), IndicatorOverridesDefinition),
            Overrides=deserialize_list(json_data.get("Overrides"), OverridesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ActivateProtectionsByExtendedAttributesDefinition2(BaseModel):
    Category: Optional[str]
    Name: Optional[str]
    Uid: Optional[str]
    Values: Optional[Sequence["_ActivateProtectionsByExtendedAttributesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ActivateProtectionsByExtendedAttributesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActivateProtectionsByExtendedAttributesDefinition2"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Name=json_data.get("Name"),
            Uid=json_data.get("Uid"),
            Values=deserialize_list(json_data.get("Values"), ActivateProtectionsByExtendedAttributesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActivateProtectionsByExtendedAttributesDefinition2 = ActivateProtectionsByExtendedAttributesDefinition2


@dataclass
class ActivateProtectionsByExtendedAttributesDefinition(BaseModel):
    Name: Optional[str]
    Uid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ActivateProtectionsByExtendedAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ActivateProtectionsByExtendedAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Uid=json_data.get("Uid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ActivateProtectionsByExtendedAttributesDefinition = ActivateProtectionsByExtendedAttributesDefinition


@dataclass
class IpsSettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpsSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpsSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpsSettingsDefinition = IpsSettingsDefinition


@dataclass
class MaliciousMailPolicySettingsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaliciousMailPolicySettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaliciousMailPolicySettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaliciousMailPolicySettingsDefinition = MaliciousMailPolicySettingsDefinition


@dataclass
class ScanMaliciousLinksDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ScanMaliciousLinksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ScanMaliciousLinksDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ScanMaliciousLinksDefinition = ScanMaliciousLinksDefinition


@dataclass
class DeactivateProtectionsByExtendedAttributesDefinition(BaseModel):
    Category: Optional[str]
    Name: Optional[str]
    Uid: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeactivateProtectionsByExtendedAttributesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeactivateProtectionsByExtendedAttributesDefinition"]:
        if not json_data:
            return None
        return cls(
            Category=json_data.get("Category"),
            Name=json_data.get("Name"),
            Uid=json_data.get("Uid"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeactivateProtectionsByExtendedAttributesDefinition = DeactivateProtectionsByExtendedAttributesDefinition


@dataclass
class IndicatorOverridesDefinition(BaseModel):
    Action: Optional[str]
    Indicator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IndicatorOverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IndicatorOverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Indicator=json_data.get("Indicator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IndicatorOverridesDefinition = IndicatorOverridesDefinition


@dataclass
class OverridesDefinition(BaseModel):
    Action: Optional[str]
    CapturePackets: Optional[bool]
    Protection: Optional[str]
    Track: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OverridesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OverridesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            CapturePackets=json_data.get("CapturePackets"),
            Protection=json_data.get("Protection"),
            Track=json_data.get("Track"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OverridesDefinition = OverridesDefinition


