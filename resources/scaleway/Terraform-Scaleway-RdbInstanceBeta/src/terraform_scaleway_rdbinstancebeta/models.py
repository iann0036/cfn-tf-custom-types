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
    Certificate: Optional[str]
    DisableBackup: Optional[bool]
    EndpointIp: Optional[str]
    EndpointPort: Optional[float]
    Engine: Optional[str]
    Id: Optional[str]
    IsHaCluster: Optional[bool]
    Name: Optional[str]
    NodeType: Optional[str]
    OrganizationId: Optional[str]
    Password: Optional[str]
    ReadReplicas: Optional[Sequence["_ReadReplicas"]]
    Region: Optional[str]
    Tags: Optional[Sequence[str]]
    UserName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Certificate=json_data.get("Certificate"),
            DisableBackup=json_data.get("DisableBackup"),
            EndpointIp=json_data.get("EndpointIp"),
            EndpointPort=json_data.get("EndpointPort"),
            Engine=json_data.get("Engine"),
            Id=json_data.get("Id"),
            IsHaCluster=json_data.get("IsHaCluster"),
            Name=json_data.get("Name"),
            NodeType=json_data.get("NodeType"),
            OrganizationId=json_data.get("OrganizationId"),
            Password=json_data.get("Password"),
            ReadReplicas=json_data.get("ReadReplicas"),
            Region=json_data.get("Region"),
            Tags=json_data.get("Tags"),
            UserName=json_data.get("UserName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReadReplicas:
    Ip: Optional[str]
    Name: Optional[str]
    Port: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ReadReplicas"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReadReplicas"]:
        if not json_data:
            return None
        return cls(
            Ip=json_data.get("Ip"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReadReplicas = ReadReplicas


