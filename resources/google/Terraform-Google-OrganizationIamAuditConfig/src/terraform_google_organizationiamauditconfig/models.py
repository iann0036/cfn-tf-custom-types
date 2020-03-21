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
    Etag: Optional[str]
    Id: Optional[str]
    OrgId: Optional[str]
    Service: Optional[str]
    AuditLogConfig: Optional[Sequence["_AuditLogConfig"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Etag=json_data.get("Etag"),
            Id=json_data.get("Id"),
            OrgId=json_data.get("OrgId"),
            Service=json_data.get("Service"),
            AuditLogConfig=json_data.get("AuditLogConfig"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AuditLogConfig:
    ExemptedMembers: Optional[Sequence[str]]
    LogType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AuditLogConfig"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AuditLogConfig"]:
        if not json_data:
            return None
        return cls(
            ExemptedMembers=json_data.get("ExemptedMembers"),
            LogType=json_data.get("LogType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AuditLogConfig = AuditLogConfig


