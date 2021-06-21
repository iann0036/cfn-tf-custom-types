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
    AdminSt: Optional[str]
    Annotation: Optional[str]
    Description: Optional[str]
    Graceful: Optional[str]
    Id: Optional[str]
    IgnoreCompat: Optional[str]
    InternalLabel: Optional[str]
    Name: Optional[str]
    NameAlias: Optional[str]
    NotifCond: Optional[str]
    RelationMaintRsPolNotif: Optional[str]
    RelationMaintRsPolScheduler: Optional[str]
    RelationTrigRsTriggerable: Optional[str]
    RunMode: Optional[str]
    Version: Optional[str]
    VersionCheckOverride: Optional[str]

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
            AdminSt=json_data.get("AdminSt"),
            Annotation=json_data.get("Annotation"),
            Description=json_data.get("Description"),
            Graceful=json_data.get("Graceful"),
            Id=json_data.get("Id"),
            IgnoreCompat=json_data.get("IgnoreCompat"),
            InternalLabel=json_data.get("InternalLabel"),
            Name=json_data.get("Name"),
            NameAlias=json_data.get("NameAlias"),
            NotifCond=json_data.get("NotifCond"),
            RelationMaintRsPolNotif=json_data.get("RelationMaintRsPolNotif"),
            RelationMaintRsPolScheduler=json_data.get("RelationMaintRsPolScheduler"),
            RelationTrigRsTriggerable=json_data.get("RelationTrigRsTriggerable"),
            RunMode=json_data.get("RunMode"),
            Version=json_data.get("Version"),
            VersionCheckOverride=json_data.get("VersionCheckOverride"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel

