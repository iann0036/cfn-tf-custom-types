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
    ActivationEmail: Optional[bool]
    AllowedBandwidth: Optional[float]
    AppId: Optional[float]
    Backups: Optional[str]
    DateCreated: Optional[str]
    DdosProtection: Optional[bool]
    DefaultPassword: Optional[str]
    Disk: Optional[float]
    EnableIpv6: Optional[bool]
    EnablePrivateNetwork: Optional[bool]
    Features: Optional[Sequence[str]]
    FirewallGroupId: Optional[str]
    GatewayV4: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    InternalIp: Optional[str]
    IsoId: Optional[str]
    Kvm: Optional[str]
    Label: Optional[str]
    MainIp: Optional[str]
    NetmaskV4: Optional[str]
    Os: Optional[str]
    OsId: Optional[float]
    Plan: Optional[str]
    PowerStatus: Optional[str]
    PrivateNetworkIds: Optional[Sequence[str]]
    Ram: Optional[float]
    Region: Optional[str]
    ReservedIpId: Optional[str]
    ScriptId: Optional[str]
    ServerStatus: Optional[str]
    SnapshotId: Optional[str]
    SshKeyIds: Optional[Sequence[str]]
    Status: Optional[str]
    Tag: Optional[str]
    UserData: Optional[str]
    V6MainIp: Optional[str]
    V6Network: Optional[str]
    V6NetworkSize: Optional[float]
    VcpuCount: Optional[float]
    BackupsSchedule: Optional[Sequence["_BackupsScheduleDefinition"]]

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
            ActivationEmail=json_data.get("ActivationEmail"),
            AllowedBandwidth=json_data.get("AllowedBandwidth"),
            AppId=json_data.get("AppId"),
            Backups=json_data.get("Backups"),
            DateCreated=json_data.get("DateCreated"),
            DdosProtection=json_data.get("DdosProtection"),
            DefaultPassword=json_data.get("DefaultPassword"),
            Disk=json_data.get("Disk"),
            EnableIpv6=json_data.get("EnableIpv6"),
            EnablePrivateNetwork=json_data.get("EnablePrivateNetwork"),
            Features=json_data.get("Features"),
            FirewallGroupId=json_data.get("FirewallGroupId"),
            GatewayV4=json_data.get("GatewayV4"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InternalIp=json_data.get("InternalIp"),
            IsoId=json_data.get("IsoId"),
            Kvm=json_data.get("Kvm"),
            Label=json_data.get("Label"),
            MainIp=json_data.get("MainIp"),
            NetmaskV4=json_data.get("NetmaskV4"),
            Os=json_data.get("Os"),
            OsId=json_data.get("OsId"),
            Plan=json_data.get("Plan"),
            PowerStatus=json_data.get("PowerStatus"),
            PrivateNetworkIds=json_data.get("PrivateNetworkIds"),
            Ram=json_data.get("Ram"),
            Region=json_data.get("Region"),
            ReservedIpId=json_data.get("ReservedIpId"),
            ScriptId=json_data.get("ScriptId"),
            ServerStatus=json_data.get("ServerStatus"),
            SnapshotId=json_data.get("SnapshotId"),
            SshKeyIds=json_data.get("SshKeyIds"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            UserData=json_data.get("UserData"),
            V6MainIp=json_data.get("V6MainIp"),
            V6Network=json_data.get("V6Network"),
            V6NetworkSize=json_data.get("V6NetworkSize"),
            VcpuCount=json_data.get("VcpuCount"),
            BackupsSchedule=deserialize_list(json_data.get("BackupsSchedule"), BackupsScheduleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackupsScheduleDefinition(BaseModel):
    Dom: Optional[float]
    Dow: Optional[float]
    Hour: Optional[float]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackupsScheduleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackupsScheduleDefinition"]:
        if not json_data:
            return None
        return cls(
            Dom=json_data.get("Dom"),
            Dow=json_data.get("Dow"),
            Hour=json_data.get("Hour"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackupsScheduleDefinition = BackupsScheduleDefinition


