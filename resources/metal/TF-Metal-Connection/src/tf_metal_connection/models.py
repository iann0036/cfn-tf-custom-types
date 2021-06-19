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
    Facility: Optional[str]
    Id: Optional[str]
    Metro: Optional[str]
    Name: Optional[str]
    OrganizationId: Optional[str]
    Ports: Optional[Sequence["_PortsDefinition"]]
    ProjectId: Optional[str]
    Redundancy: Optional[str]
    Speed: Optional[float]
    Status: Optional[str]
    Token: Optional[str]
    Type: Optional[str]

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
            Facility=json_data.get("Facility"),
            Id=json_data.get("Id"),
            Metro=json_data.get("Metro"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            Ports=deserialize_list(json_data.get("Ports"), PortsDefinition),
            ProjectId=json_data.get("ProjectId"),
            Redundancy=json_data.get("Redundancy"),
            Speed=json_data.get("Speed"),
            Status=json_data.get("Status"),
            Token=json_data.get("Token"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class PortsDefinition(BaseModel):
    Id: Optional[str]
    LinkStatus: Optional[str]
    Name: Optional[str]
    Role: Optional[str]
    Speed: Optional[float]
    Status: Optional[str]
    VirtualCircuitIds: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_PortsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortsDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            LinkStatus=json_data.get("LinkStatus"),
            Name=json_data.get("Name"),
            Role=json_data.get("Role"),
            Speed=json_data.get("Speed"),
            Status=json_data.get("Status"),
            VirtualCircuitIds=json_data.get("VirtualCircuitIds"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortsDefinition = PortsDefinition


