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
    AgentIp: Optional[str]
    Command: Optional[str]
    Description: Optional[str]
    EnvironmentId: Optional[str]
    HostLabels: Optional[Sequence["_HostLabels"]]
    Id: Optional[str]
    Image: Optional[str]
    Name: Optional[str]
    RegistrationUrl: Optional[str]
    Token: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AgentIp=json_data.get("AgentIp"),
            Command=json_data.get("Command"),
            Description=json_data.get("Description"),
            EnvironmentId=json_data.get("EnvironmentId"),
            HostLabels=json_data.get("HostLabels"),
            Id=json_data.get("Id"),
            Image=json_data.get("Image"),
            Name=json_data.get("Name"),
            RegistrationUrl=json_data.get("RegistrationUrl"),
            Token=json_data.get("Token"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class HostLabels:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_HostLabels"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HostLabels"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HostLabels = HostLabels


