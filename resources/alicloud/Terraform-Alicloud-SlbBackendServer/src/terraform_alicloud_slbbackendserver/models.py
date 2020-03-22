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
    DeleteProtectionValidation: Optional[bool]
    Id: Optional[str]
    LoadBalancerId: Optional[str]
    BackendServers: Optional[Sequence["_BackendServers"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DeleteProtectionValidation=json_data.get("DeleteProtectionValidation"),
            Id=json_data.get("Id"),
            LoadBalancerId=json_data.get("LoadBalancerId"),
            BackendServers=json_data.get("BackendServers"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class BackendServers:
    ServerId: Optional[str]
    Type: Optional[str]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_BackendServers"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendServers"]:
        if not json_data:
            return None
        return cls(
            ServerId=json_data.get("ServerId"),
            Type=json_data.get("Type"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendServers = BackendServers


