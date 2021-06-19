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
    CleanupDeadServers: Optional[bool]
    Datacenter: Optional[str]
    DisableUpgradeMigration: Optional[bool]
    Id: Optional[str]
    LastContactThreshold: Optional[str]
    MaxTrailingLogs: Optional[float]
    RedundancyZoneTag: Optional[str]
    ServerStabilizationTime: Optional[str]
    UpgradeVersionTag: Optional[str]

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
            CleanupDeadServers=json_data.get("CleanupDeadServers"),
            Datacenter=json_data.get("Datacenter"),
            DisableUpgradeMigration=json_data.get("DisableUpgradeMigration"),
            Id=json_data.get("Id"),
            LastContactThreshold=json_data.get("LastContactThreshold"),
            MaxTrailingLogs=json_data.get("MaxTrailingLogs"),
            RedundancyZoneTag=json_data.get("RedundancyZoneTag"),
            ServerStabilizationTime=json_data.get("ServerStabilizationTime"),
            UpgradeVersionTag=json_data.get("UpgradeVersionTag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


