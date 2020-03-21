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
    DeviceGroup: Optional[str]
    PositionKeyword: Optional[str]
    PositionReference: Optional[str]
    Rulebase: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    Target: Optional[Sequence["_Target"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeviceGroup=json_data.get("DeviceGroup"),
            PositionKeyword=json_data.get("PositionKeyword"),
            PositionReference=json_data.get("PositionReference"),
            Rulebase=json_data.get("Rulebase"),
            Rule=json_data.get("Rule"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Action: Optional[str]
    Applications: Optional[Sequence[str]]
    Categories: Optional[Sequence[str]]
    DataFiltering: Optional[str]
    Description: Optional[str]
    DestinationAddresses: Optional[Sequence[str]]
    DestinationZones: Optional[Sequence[str]]
    DisableServerResponseInspection: Optional[bool]
    Disabled: Optional[bool]
    FileBlocking: Optional[str]
    Group: Optional[str]
    HipProfiles: Optional[Sequence[str]]
    IcmpUnreachable: Optional[bool]
    LogEnd: Optional[bool]
    LogSetting: Optional[str]
    LogStart: Optional[bool]
    Name: Optional[str]
    NegateDestination: Optional[bool]
    NegateSource: Optional[bool]
    NegateTarget: Optional[bool]
    Schedule: Optional[str]
    Services: Optional[Sequence[str]]
    SourceAddresses: Optional[Sequence[str]]
    SourceUsers: Optional[Sequence[str]]
    SourceZones: Optional[Sequence[str]]
    Spyware: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    UrlFiltering: Optional[str]
    Virus: Optional[str]
    Vulnerability: Optional[str]
    WildfireAnalysis: Optional[str]
    Target: Optional[Sequence["_Target"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Applications=json_data.get("Applications"),
            Categories=json_data.get("Categories"),
            DataFiltering=json_data.get("DataFiltering"),
            Description=json_data.get("Description"),
            DestinationAddresses=json_data.get("DestinationAddresses"),
            DestinationZones=json_data.get("DestinationZones"),
            DisableServerResponseInspection=json_data.get("DisableServerResponseInspection"),
            Disabled=json_data.get("Disabled"),
            FileBlocking=json_data.get("FileBlocking"),
            Group=json_data.get("Group"),
            HipProfiles=json_data.get("HipProfiles"),
            IcmpUnreachable=json_data.get("IcmpUnreachable"),
            LogEnd=json_data.get("LogEnd"),
            LogSetting=json_data.get("LogSetting"),
            LogStart=json_data.get("LogStart"),
            Name=json_data.get("Name"),
            NegateDestination=json_data.get("NegateDestination"),
            NegateSource=json_data.get("NegateSource"),
            NegateTarget=json_data.get("NegateTarget"),
            Schedule=json_data.get("Schedule"),
            Services=json_data.get("Services"),
            SourceAddresses=json_data.get("SourceAddresses"),
            SourceUsers=json_data.get("SourceUsers"),
            SourceZones=json_data.get("SourceZones"),
            Spyware=json_data.get("Spyware"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UrlFiltering=json_data.get("UrlFiltering"),
            Virus=json_data.get("Virus"),
            Vulnerability=json_data.get("Vulnerability"),
            WildfireAnalysis=json_data.get("WildfireAnalysis"),
            Target=json_data.get("Target"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class Target:
    Serial: Optional[str]
    VsysList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_Target"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Target"]:
        if not json_data:
            return None
        return cls(
            Serial=json_data.get("Serial"),
            VsysList=json_data.get("VsysList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Target = Target


