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
    BackupModel: Optional[str]
    BackupTime: Optional[str]
    BinlogPeriod: Optional[float]
    Id: Optional[str]
    MysqlId: Optional[str]
    RetentionPeriod: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            BackupModel=json_data.get("BackupModel"),
            BackupTime=json_data.get("BackupTime"),
            BinlogPeriod=json_data.get("BinlogPeriod"),
            Id=json_data.get("Id"),
            MysqlId=json_data.get("MysqlId"),
            RetentionPeriod=json_data.get("RetentionPeriod"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


