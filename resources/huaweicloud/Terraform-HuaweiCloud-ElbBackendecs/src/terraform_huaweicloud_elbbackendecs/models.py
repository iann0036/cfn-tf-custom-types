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
    CreateTime: Optional[str]
    HealthStatus: Optional[str]
    Id: Optional[str]
    ListenerId: Optional[str]
    Listeners: Optional[Sequence["_Listeners"]]
    PrivateAddress: Optional[str]
    PublicAddress: Optional[str]
    ServerId: Optional[str]
    ServerName: Optional[str]
    Status: Optional[str]
    UpdateTime: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateTime=json_data.get("CreateTime"),
            HealthStatus=json_data.get("HealthStatus"),
            Id=json_data.get("Id"),
            ListenerId=json_data.get("ListenerId"),
            Listeners=json_data.get("Listeners"),
            PrivateAddress=json_data.get("PrivateAddress"),
            PublicAddress=json_data.get("PublicAddress"),
            ServerId=json_data.get("ServerId"),
            ServerName=json_data.get("ServerName"),
            Status=json_data.get("Status"),
            UpdateTime=json_data.get("UpdateTime"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Listeners:
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Listeners"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Listeners"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Listeners = Listeners


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


