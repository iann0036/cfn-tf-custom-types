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
    Arn: Optional[str]
    DatabaseName: Optional[str]
    DeletionProtection: Optional[bool]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    GlobalClusterIdentifier: Optional[str]
    GlobalClusterResourceId: Optional[str]
    Id: Optional[str]
    StorageEncrypted: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Arn=json_data.get("Arn"),
            DatabaseName=json_data.get("DatabaseName"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            GlobalClusterIdentifier=json_data.get("GlobalClusterIdentifier"),
            GlobalClusterResourceId=json_data.get("GlobalClusterResourceId"),
            Id=json_data.get("Id"),
            StorageEncrypted=json_data.get("StorageEncrypted"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


