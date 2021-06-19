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
    AccountId: Optional[str]
    ConfigId: Optional[str]
    ConfigName: Optional[str]
    CredentialsId: Optional[str]
    DeliveryPathPrefix: Optional[str]
    DeliveryStartTime: Optional[str]
    Id: Optional[str]
    LogType: Optional[str]
    OutputFormat: Optional[str]
    Status: Optional[str]
    StorageConfigurationId: Optional[str]
    WorkspaceIdsFilter: Optional[Sequence[float]]

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
            AccountId=json_data.get("AccountId"),
            ConfigId=json_data.get("ConfigId"),
            ConfigName=json_data.get("ConfigName"),
            CredentialsId=json_data.get("CredentialsId"),
            DeliveryPathPrefix=json_data.get("DeliveryPathPrefix"),
            DeliveryStartTime=json_data.get("DeliveryStartTime"),
            Id=json_data.get("Id"),
            LogType=json_data.get("LogType"),
            OutputFormat=json_data.get("OutputFormat"),
            Status=json_data.get("Status"),
            StorageConfigurationId=json_data.get("StorageConfigurationId"),
            WorkspaceIdsFilter=json_data.get("WorkspaceIdsFilter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


