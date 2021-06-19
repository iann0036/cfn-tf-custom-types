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
    Access: Optional[bool]
    DesktopSecurity: Optional[bool]
    Id: Optional[str]
    InstallOnAllClusterMembersOrFail: Optional[bool]
    PolicyPackage: Optional[str]
    PrepareOnly: Optional[bool]
    Qos: Optional[bool]
    Revision: Optional[str]
    Targets: Optional[Sequence[str]]
    TaskId: Optional[str]
    ThreatPrevention: Optional[bool]
    Triggers: Optional[Sequence[str]]

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
            Access=json_data.get("Access"),
            DesktopSecurity=json_data.get("DesktopSecurity"),
            Id=json_data.get("Id"),
            InstallOnAllClusterMembersOrFail=json_data.get("InstallOnAllClusterMembersOrFail"),
            PolicyPackage=json_data.get("PolicyPackage"),
            PrepareOnly=json_data.get("PrepareOnly"),
            Qos=json_data.get("Qos"),
            Revision=json_data.get("Revision"),
            Targets=json_data.get("Targets"),
            TaskId=json_data.get("TaskId"),
            ThreatPrevention=json_data.get("ThreatPrevention"),
            Triggers=json_data.get("Triggers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


