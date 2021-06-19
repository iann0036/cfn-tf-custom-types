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
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    EventsToExport: Optional[Sequence[str]]
    Id: Optional[str]
    IothubIds: Optional[Sequence[str]]
    Location: Optional[str]
    LogAnalyticsWorkspaceId: Optional[str]
    LogUnmaskedIpsEnabled: Optional[bool]
    Name: Optional[str]
    QueryForResources: Optional[str]
    QuerySubscriptionIds: Optional[Sequence[str]]
    ResourceGroupName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    RecommendationsEnabled: Optional[Sequence["_RecommendationsEnabledDefinition"]]
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
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            EventsToExport=json_data.get("EventsToExport"),
            Id=json_data.get("Id"),
            IothubIds=json_data.get("IothubIds"),
            Location=json_data.get("Location"),
            LogAnalyticsWorkspaceId=json_data.get("LogAnalyticsWorkspaceId"),
            LogUnmaskedIpsEnabled=json_data.get("LogUnmaskedIpsEnabled"),
            Name=json_data.get("Name"),
            QueryForResources=json_data.get("QueryForResources"),
            QuerySubscriptionIds=json_data.get("QuerySubscriptionIds"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            RecommendationsEnabled=deserialize_list(json_data.get("RecommendationsEnabled"), RecommendationsEnabledDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class RecommendationsEnabledDefinition(BaseModel):
    AcrAuthentication: Optional[bool]
    AgentSendUnutilizedMsg: Optional[bool]
    Baseline: Optional[bool]
    EdgeHubMemOptimize: Optional[bool]
    EdgeLoggingOption: Optional[bool]
    InconsistentModuleSettings: Optional[bool]
    InstallAgent: Optional[bool]
    IpFilterDenyAll: Optional[bool]
    IpFilterPermissiveRule: Optional[bool]
    OpenPorts: Optional[bool]
    PermissiveFirewallPolicy: Optional[bool]
    PermissiveInputFirewallRules: Optional[bool]
    PermissiveOutputFirewallRules: Optional[bool]
    PrivilegedDockerOptions: Optional[bool]
    SharedCredentials: Optional[bool]
    VulnerableTlsCipherSuite: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RecommendationsEnabledDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RecommendationsEnabledDefinition"]:
        if not json_data:
            return None
        return cls(
            AcrAuthentication=json_data.get("AcrAuthentication"),
            AgentSendUnutilizedMsg=json_data.get("AgentSendUnutilizedMsg"),
            Baseline=json_data.get("Baseline"),
            EdgeHubMemOptimize=json_data.get("EdgeHubMemOptimize"),
            EdgeLoggingOption=json_data.get("EdgeLoggingOption"),
            InconsistentModuleSettings=json_data.get("InconsistentModuleSettings"),
            InstallAgent=json_data.get("InstallAgent"),
            IpFilterDenyAll=json_data.get("IpFilterDenyAll"),
            IpFilterPermissiveRule=json_data.get("IpFilterPermissiveRule"),
            OpenPorts=json_data.get("OpenPorts"),
            PermissiveFirewallPolicy=json_data.get("PermissiveFirewallPolicy"),
            PermissiveInputFirewallRules=json_data.get("PermissiveInputFirewallRules"),
            PermissiveOutputFirewallRules=json_data.get("PermissiveOutputFirewallRules"),
            PrivilegedDockerOptions=json_data.get("PrivilegedDockerOptions"),
            SharedCredentials=json_data.get("SharedCredentials"),
            VulnerableTlsCipherSuite=json_data.get("VulnerableTlsCipherSuite"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RecommendationsEnabledDefinition = RecommendationsEnabledDefinition


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


