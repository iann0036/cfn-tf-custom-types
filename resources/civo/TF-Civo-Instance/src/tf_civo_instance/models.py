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
    CpuCores: Optional[float]
    CreatedAt: Optional[str]
    DiskGb: Optional[float]
    FirewallId: Optional[str]
    Hostname: Optional[str]
    Id: Optional[str]
    InitialPassword: Optional[str]
    InitialUser: Optional[str]
    NetworkId: Optional[str]
    Notes: Optional[str]
    PrivateIp: Optional[str]
    PseudoIp: Optional[str]
    PublicIp: Optional[str]
    PublicIpRequired: Optional[str]
    RamMb: Optional[float]
    Region: Optional[str]
    ReverseDns: Optional[str]
    Script: Optional[str]
    Size: Optional[str]
    SourceId: Optional[str]
    SourceType: Optional[str]
    SshkeyId: Optional[str]
    Status: Optional[str]
    Tags: Optional[Sequence[str]]
    Template: Optional[str]

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
            CpuCores=json_data.get("CpuCores"),
            CreatedAt=json_data.get("CreatedAt"),
            DiskGb=json_data.get("DiskGb"),
            FirewallId=json_data.get("FirewallId"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            InitialPassword=json_data.get("InitialPassword"),
            InitialUser=json_data.get("InitialUser"),
            NetworkId=json_data.get("NetworkId"),
            Notes=json_data.get("Notes"),
            PrivateIp=json_data.get("PrivateIp"),
            PseudoIp=json_data.get("PseudoIp"),
            PublicIp=json_data.get("PublicIp"),
            PublicIpRequired=json_data.get("PublicIpRequired"),
            RamMb=json_data.get("RamMb"),
            Region=json_data.get("Region"),
            ReverseDns=json_data.get("ReverseDns"),
            Script=json_data.get("Script"),
            Size=json_data.get("Size"),
            SourceId=json_data.get("SourceId"),
            SourceType=json_data.get("SourceType"),
            SshkeyId=json_data.get("SshkeyId"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


