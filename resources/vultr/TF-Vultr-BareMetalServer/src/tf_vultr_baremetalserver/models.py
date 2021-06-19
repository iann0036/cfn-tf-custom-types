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
    AppId: Optional[float]
    CpuCount: Optional[float]
    DateCreated: Optional[str]
    DefaultPassword: Optional[str]
    Disk: Optional[str]
    EnableIpv6: Optional[bool]
    GatewayV4: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    Label: Optional[str]
    MacAddress: Optional[float]
    MainIp: Optional[str]
    NetmaskV4: Optional[str]
    Os: Optional[str]
    OsId: Optional[float]
    Plan: Optional[str]
    Ram: Optional[str]
    Region: Optional[str]
    ReservedIpv4: Optional[str]
    ScriptId: Optional[str]
    SnapshotId: Optional[str]
    SshKeyIds: Optional[Sequence[str]]
    Status: Optional[str]
    Tag: Optional[str]
    UserData: Optional[str]
    V6MainIp: Optional[str]
    V6Network: Optional[str]
    V6NetworkSize: Optional[float]

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
            AppId=json_data.get("AppId"),
            CpuCount=json_data.get("CpuCount"),
            DateCreated=json_data.get("DateCreated"),
            DefaultPassword=json_data.get("DefaultPassword"),
            Disk=json_data.get("Disk"),
            EnableIpv6=json_data.get("EnableIpv6"),
            GatewayV4=json_data.get("GatewayV4"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            MacAddress=json_data.get("MacAddress"),
            MainIp=json_data.get("MainIp"),
            NetmaskV4=json_data.get("NetmaskV4"),
            Os=json_data.get("Os"),
            OsId=json_data.get("OsId"),
            Plan=json_data.get("Plan"),
            Ram=json_data.get("Ram"),
            Region=json_data.get("Region"),
            ReservedIpv4=json_data.get("ReservedIpv4"),
            ScriptId=json_data.get("ScriptId"),
            SnapshotId=json_data.get("SnapshotId"),
            SshKeyIds=json_data.get("SshKeyIds"),
            Status=json_data.get("Status"),
            Tag=json_data.get("Tag"),
            UserData=json_data.get("UserData"),
            V6MainIp=json_data.get("V6MainIp"),
            V6Network=json_data.get("V6Network"),
            V6NetworkSize=json_data.get("V6NetworkSize"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


