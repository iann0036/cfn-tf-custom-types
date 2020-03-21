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
    Cluster: Optional[str]
    Connected: Optional[bool]
    Datacenter: Optional[str]
    Force: Optional[bool]
    Hostname: Optional[str]
    Id: Optional[str]
    License: Optional[str]
    Lockdown: Optional[str]
    Maintenance: Optional[bool]
    Password: Optional[str]
    Thumbprint: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cluster=json_data.get("Cluster"),
            Connected=json_data.get("Connected"),
            Datacenter=json_data.get("Datacenter"),
            Force=json_data.get("Force"),
            Hostname=json_data.get("Hostname"),
            Id=json_data.get("Id"),
            License=json_data.get("License"),
            Lockdown=json_data.get("Lockdown"),
            Maintenance=json_data.get("Maintenance"),
            Password=json_data.get("Password"),
            Thumbprint=json_data.get("Thumbprint"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


