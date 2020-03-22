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
    Id: Optional[str]
    PositionKeyword: Optional[str]
    PositionReference: Optional[str]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]
    Rule: Optional[Sequence["_Rule"]]
    MatchAddressPrefix: Optional[Sequence["_MatchAddressPrefix"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            PositionKeyword=json_data.get("PositionKeyword"),
            PositionReference=json_data.get("PositionReference"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
            Rule=json_data.get("Rule"),
            MatchAddressPrefix=json_data.get("MatchAddressPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Rule:
    Action: Optional[str]
    AsPathLimit: Optional[float]
    AsPathType: Optional[str]
    AsPathValue: Optional[str]
    CommunityType: Optional[str]
    CommunityValue: Optional[str]
    Enable: Optional[bool]
    ExtendedCommunityType: Optional[str]
    ExtendedCommunityValue: Optional[str]
    LocalPreference: Optional[str]
    MatchAsPathRegex: Optional[str]
    MatchCommunityRegex: Optional[str]
    MatchExtendedCommunityRegex: Optional[str]
    MatchFromPeers: Optional[Sequence[str]]
    MatchMed: Optional[str]
    MatchNextHops: Optional[Sequence[str]]
    MatchRouteTable: Optional[str]
    Med: Optional[str]
    Name: Optional[str]
    NextHop: Optional[str]
    Origin: Optional[str]
    UsedBy: Optional[Sequence[str]]
    MatchAddressPrefix: Optional[Sequence["_MatchAddressPrefix"]]

    @classmethod
    def _deserialize(
        cls: Type["_Rule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Rule"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            AsPathLimit=json_data.get("AsPathLimit"),
            AsPathType=json_data.get("AsPathType"),
            AsPathValue=json_data.get("AsPathValue"),
            CommunityType=json_data.get("CommunityType"),
            CommunityValue=json_data.get("CommunityValue"),
            Enable=json_data.get("Enable"),
            ExtendedCommunityType=json_data.get("ExtendedCommunityType"),
            ExtendedCommunityValue=json_data.get("ExtendedCommunityValue"),
            LocalPreference=json_data.get("LocalPreference"),
            MatchAsPathRegex=json_data.get("MatchAsPathRegex"),
            MatchCommunityRegex=json_data.get("MatchCommunityRegex"),
            MatchExtendedCommunityRegex=json_data.get("MatchExtendedCommunityRegex"),
            MatchFromPeers=json_data.get("MatchFromPeers"),
            MatchMed=json_data.get("MatchMed"),
            MatchNextHops=json_data.get("MatchNextHops"),
            MatchRouteTable=json_data.get("MatchRouteTable"),
            Med=json_data.get("Med"),
            Name=json_data.get("Name"),
            NextHop=json_data.get("NextHop"),
            Origin=json_data.get("Origin"),
            UsedBy=json_data.get("UsedBy"),
            MatchAddressPrefix=json_data.get("MatchAddressPrefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Rule = Rule


@dataclass
class MatchAddressPrefix:
    Exact: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MatchAddressPrefix"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchAddressPrefix"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchAddressPrefix = MatchAddressPrefix


