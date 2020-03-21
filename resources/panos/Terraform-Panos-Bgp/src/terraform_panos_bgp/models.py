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
    AggregateMed: Optional[bool]
    AllowRedistributeDefaultRoute: Optional[bool]
    AlwaysCompareMed: Optional[bool]
    AsFormat: Optional[str]
    AsNumber: Optional[str]
    BfdProfile: Optional[str]
    ConfederationMemberAs: Optional[str]
    DefaultLocalPreference: Optional[str]
    DeterministicMedComparison: Optional[bool]
    EcmpMultiAs: Optional[bool]
    Enable: Optional[bool]
    EnableGracefulRestart: Optional[bool]
    EnforceFirstAs: Optional[bool]
    InstallRoute: Optional[bool]
    LocalRestartTime: Optional[float]
    MaxPeerRestartTime: Optional[float]
    ReflectorClusterId: Optional[str]
    RejectDefaultRoute: Optional[bool]
    RouterId: Optional[str]
    StaleRouteTime: Optional[float]
    VirtualRouter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AggregateMed=json_data.get("AggregateMed"),
            AllowRedistributeDefaultRoute=json_data.get("AllowRedistributeDefaultRoute"),
            AlwaysCompareMed=json_data.get("AlwaysCompareMed"),
            AsFormat=json_data.get("AsFormat"),
            AsNumber=json_data.get("AsNumber"),
            BfdProfile=json_data.get("BfdProfile"),
            ConfederationMemberAs=json_data.get("ConfederationMemberAs"),
            DefaultLocalPreference=json_data.get("DefaultLocalPreference"),
            DeterministicMedComparison=json_data.get("DeterministicMedComparison"),
            EcmpMultiAs=json_data.get("EcmpMultiAs"),
            Enable=json_data.get("Enable"),
            EnableGracefulRestart=json_data.get("EnableGracefulRestart"),
            EnforceFirstAs=json_data.get("EnforceFirstAs"),
            InstallRoute=json_data.get("InstallRoute"),
            LocalRestartTime=json_data.get("LocalRestartTime"),
            MaxPeerRestartTime=json_data.get("MaxPeerRestartTime"),
            ReflectorClusterId=json_data.get("ReflectorClusterId"),
            RejectDefaultRoute=json_data.get("RejectDefaultRoute"),
            RouterId=json_data.get("RouterId"),
            StaleRouteTime=json_data.get("StaleRouteTime"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


