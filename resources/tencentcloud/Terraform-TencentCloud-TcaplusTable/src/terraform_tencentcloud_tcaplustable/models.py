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
    AppId: Optional[str]
    CreateTime: Optional[str]
    Description: Optional[str]
    Error: Optional[str]
    IdlId: Optional[str]
    ReservedReadQps: Optional[float]
    ReservedVolume: Optional[float]
    ReservedWriteQps: Optional[float]
    Status: Optional[str]
    TableIdlType: Optional[str]
    TableName: Optional[str]
    TableSize: Optional[float]
    TableType: Optional[str]
    ZoneId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppId=json_data.get("AppId"),
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Error=json_data.get("Error"),
            IdlId=json_data.get("IdlId"),
            ReservedReadQps=json_data.get("ReservedReadQps"),
            ReservedVolume=json_data.get("ReservedVolume"),
            ReservedWriteQps=json_data.get("ReservedWriteQps"),
            Status=json_data.get("Status"),
            TableIdlType=json_data.get("TableIdlType"),
            TableName=json_data.get("TableName"),
            TableSize=json_data.get("TableSize"),
            TableType=json_data.get("TableType"),
            ZoneId=json_data.get("ZoneId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


