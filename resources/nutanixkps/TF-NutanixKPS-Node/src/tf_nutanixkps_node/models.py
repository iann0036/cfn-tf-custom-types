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
    Description: Optional[str]
    Gateway: Optional[str]
    Id: Optional[str]
    IpAddress: Optional[str]
    IsBootstrapMaster: Optional[bool]
    Name: Optional[str]
    SerialNumber: Optional[str]
    ServiceDomainId: Optional[str]
    Subnet: Optional[str]
    WaitForOnboarding: Optional[bool]
    WaitTimeoutMinutes: Optional[float]
    Role: Optional[Sequence["_RoleDefinition"]]

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
            Description=json_data.get("Description"),
            Gateway=json_data.get("Gateway"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            IsBootstrapMaster=json_data.get("IsBootstrapMaster"),
            Name=json_data.get("Name"),
            SerialNumber=json_data.get("SerialNumber"),
            ServiceDomainId=json_data.get("ServiceDomainId"),
            Subnet=json_data.get("Subnet"),
            WaitForOnboarding=json_data.get("WaitForOnboarding"),
            WaitTimeoutMinutes=json_data.get("WaitTimeoutMinutes"),
            Role=deserialize_list(json_data.get("Role"), RoleDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class RoleDefinition(BaseModel):
    Master: Optional[bool]
    Worker: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_RoleDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RoleDefinition"]:
        if not json_data:
            return None
        return cls(
            Master=json_data.get("Master"),
            Worker=json_data.get("Worker"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RoleDefinition = RoleDefinition


