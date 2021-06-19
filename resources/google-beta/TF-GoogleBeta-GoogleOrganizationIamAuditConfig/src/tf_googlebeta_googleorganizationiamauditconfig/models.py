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
    Etag: Optional[str]
    Id: Optional[str]
    OrgId: Optional[str]
    Service: Optional[str]
    AuditLogConfig: Optional[Sequence["_AuditLogConfigDefinition"]]

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
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            OrgId=json_data.get("OrgId"),
            Service=json_data.get("Service"),
            AuditLogConfig=deserialize_list(json_data.get("AuditLogConfig"), AuditLogConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuditLogConfigDefinition(BaseModel):
    ExemptedMembers: Optional[Sequence[str]]
    LogType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuditLogConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditLogConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ExemptedMembers=json_data.get("ExemptedMembers"),
            LogType=json_data.get("LogType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditLogConfigDefinition = AuditLogConfigDefinition


