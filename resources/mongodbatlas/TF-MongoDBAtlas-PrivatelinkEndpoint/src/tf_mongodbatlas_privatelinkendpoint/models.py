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
    EndpointServiceName: Optional[str]
    ErrorMessage: Optional[str]
    Id: Optional[str]
    InterfaceEndpoints: Optional[Sequence[str]]
    PrivateEndpoints: Optional[Sequence[str]]
    PrivateLinkId: Optional[str]
    PrivateLinkServiceName: Optional[str]
    PrivateLinkServiceResourceId: Optional[str]
    ProjectId: Optional[str]
    ProviderName: Optional[str]
    Region: Optional[str]
    Status: Optional[str]

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
            EndpointServiceName=json_data.get("EndpointServiceName"),
            ErrorMessage=json_data.get("ErrorMessage"),
            Id=json_data.get("Id"),
            InterfaceEndpoints=json_data.get("InterfaceEndpoints"),
            PrivateEndpoints=json_data.get("PrivateEndpoints"),
            PrivateLinkId=json_data.get("PrivateLinkId"),
            PrivateLinkServiceName=json_data.get("PrivateLinkServiceName"),
            PrivateLinkServiceResourceId=json_data.get("PrivateLinkServiceResourceId"),
            ProjectId=json_data.get("ProjectId"),
            ProviderName=json_data.get("ProviderName"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


