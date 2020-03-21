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
    Description: Optional[str]
    Name: Optional[str]
    Policies: Optional[Sequence[str]]
    ServiceIdentities: Optional[Sequence["_ServiceIdentities"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            Policies=json_data.get("Policies"),
            ServiceIdentities=json_data.get("ServiceIdentities"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ServiceIdentities:
    Datacenters: Optional[Sequence[str]]
    ServiceName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceIdentities"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceIdentities"]:
        if not json_data:
            return None
        return cls(
            Datacenters=json_data.get("Datacenters"),
            ServiceName=json_data.get("ServiceName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceIdentities = ServiceIdentities


