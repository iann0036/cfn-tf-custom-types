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
    AvailabilityZone: Optional[str]
    Created: Optional[str]
    Endpoints: Optional[Sequence["_Endpoints"]]
    Id: Optional[str]
    Name: Optional[str]
    NetworkId: Optional[str]
    NodeType: Optional[str]
    NumberOfNode: Optional[float]
    Port: Optional[float]
    PublicEndpoints: Optional[Sequence["_PublicEndpoints"]]
    RecentEvent: Optional[float]
    Region: Optional[str]
    SecurityGroupId: Optional[str]
    Status: Optional[str]
    SubStatus: Optional[str]
    TaskStatus: Optional[str]
    Updated: Optional[str]
    UserName: Optional[str]
    UserPwd: Optional[str]
    Version: Optional[str]
    VpcId: Optional[str]
    PublicIp: Optional[Sequence["_PublicIp"]]
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
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Created=json_data.get("Created"),
            Endpoints=json_data.get("Endpoints"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NetworkId=json_data.get("NetworkId"),
            NodeType=json_data.get("NodeType"),
            NumberOfNode=json_data.get("NumberOfNode"),
            Port=json_data.get("Port"),
            PublicEndpoints=json_data.get("PublicEndpoints"),
            RecentEvent=json_data.get("RecentEvent"),
            Region=json_data.get("Region"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Status=json_data.get("Status"),
            SubStatus=json_data.get("SubStatus"),
            TaskStatus=json_data.get("TaskStatus"),
            Updated=json_data.get("Updated"),
            UserName=json_data.get("UserName"),
            UserPwd=json_data.get("UserPwd"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            PublicIp=json_data.get("PublicIp"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Endpoints:
    ConnectInfo: Optional[str]
    JdbcUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Endpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Endpoints"]:
        if not json_data:
            return None
        return cls(
            ConnectInfo=json_data.get("ConnectInfo"),
            JdbcUrl=json_data.get("JdbcUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Endpoints = Endpoints


@dataclass
class PublicEndpoints:
    JdbcUrl: Optional[str]
    PublicConnectInfo: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicEndpoints"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicEndpoints"]:
        if not json_data:
            return None
        return cls(
            JdbcUrl=json_data.get("JdbcUrl"),
            PublicConnectInfo=json_data.get("PublicConnectInfo"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicEndpoints = PublicEndpoints


@dataclass
class PublicIp:
    EipId: Optional[str]
    PublicBindType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PublicIp"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PublicIp"]:
        if not json_data:
            return None
        return cls(
            EipId=json_data.get("EipId"),
            PublicBindType=json_data.get("PublicBindType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PublicIp = PublicIp


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


