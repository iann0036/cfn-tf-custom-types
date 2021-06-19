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
    CustomerVpnGateway: Optional[str]
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IkeIdentifier: Optional[str]
    IpNetwork: Optional[str]
    LocalGatewayIpAddress: Optional[str]
    LocalGatewayPrivateIpAddress: Optional[str]
    Name: Optional[str]
    PreSharedKey: Optional[str]
    ReachableRoutes: Optional[Sequence[str]]
    RequirePerfectForwardSecrecy: Optional[bool]
    Tags: Optional[Sequence[str]]
    TunnelStatus: Optional[str]
    Uri: Optional[str]
    VnicSets: Optional[Sequence[str]]
    PhaseOneSettings: Optional[Sequence["_PhaseOneSettingsDefinition"]]
    PhaseTwoSettings: Optional[Sequence["_PhaseTwoSettingsDefinition"]]
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
            CustomerVpnGateway=json_data.get("CustomerVpnGateway"),
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IkeIdentifier=json_data.get("IkeIdentifier"),
            IpNetwork=json_data.get("IpNetwork"),
            LocalGatewayIpAddress=json_data.get("LocalGatewayIpAddress"),
            LocalGatewayPrivateIpAddress=json_data.get("LocalGatewayPrivateIpAddress"),
            Name=json_data.get("Name"),
            PreSharedKey=json_data.get("PreSharedKey"),
            ReachableRoutes=json_data.get("ReachableRoutes"),
            RequirePerfectForwardSecrecy=json_data.get("RequirePerfectForwardSecrecy"),
            Tags=json_data.get("Tags"),
            TunnelStatus=json_data.get("TunnelStatus"),
            Uri=json_data.get("Uri"),
            VnicSets=json_data.get("VnicSets"),
            PhaseOneSettings=deserialize_list(json_data.get("PhaseOneSettings"), PhaseOneSettingsDefinition),
            PhaseTwoSettings=deserialize_list(json_data.get("PhaseTwoSettings"), PhaseTwoSettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PhaseOneSettingsDefinition(BaseModel):
    DhGroup: Optional[str]
    Encryption: Optional[str]
    Hash: Optional[str]
    Lifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PhaseOneSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhaseOneSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            DhGroup=json_data.get("DhGroup"),
            Encryption=json_data.get("Encryption"),
            Hash=json_data.get("Hash"),
            Lifetime=json_data.get("Lifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhaseOneSettingsDefinition = PhaseOneSettingsDefinition


@dataclass
class PhaseTwoSettingsDefinition(BaseModel):
    Encryption: Optional[str]
    Hash: Optional[str]
    Lifetime: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PhaseTwoSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PhaseTwoSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            Encryption=json_data.get("Encryption"),
            Hash=json_data.get("Hash"),
            Lifetime=json_data.get("Lifetime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PhaseTwoSettingsDefinition = PhaseTwoSettingsDefinition


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


