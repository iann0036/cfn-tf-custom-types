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
    ActionWhenConflictsOccurDuringPolicyCheck: Optional[str]
    AutoPushPolicyPackagesWhenDeviceBackOnline: Optional[str]
    CentralManagementFortiap: Optional[bool]
    CentralManagementSdwan: Optional[bool]
    CentralManagementVpn: Optional[bool]
    Id: Optional[str]
    Mode: Optional[str]
    Name: Optional[str]
    PerformPolicyCheckBeforeEveryInstall: Optional[bool]
    Status: Optional[float]
    Type: Optional[str]

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
            ActionWhenConflictsOccurDuringPolicyCheck=json_data.get("ActionWhenConflictsOccurDuringPolicyCheck"),
            AutoPushPolicyPackagesWhenDeviceBackOnline=json_data.get("AutoPushPolicyPackagesWhenDeviceBackOnline"),
            CentralManagementFortiap=json_data.get("CentralManagementFortiap"),
            CentralManagementSdwan=json_data.get("CentralManagementSdwan"),
            CentralManagementVpn=json_data.get("CentralManagementVpn"),
            Id=json_data.get("Id"),
            Mode=json_data.get("Mode"),
            Name=json_data.get("Name"),
            PerformPolicyCheckBeforeEveryInstall=json_data.get("PerformPolicyCheckBeforeEveryInstall"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


