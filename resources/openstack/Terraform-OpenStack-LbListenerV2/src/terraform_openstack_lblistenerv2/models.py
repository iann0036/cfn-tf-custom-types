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
    AdminStateUp: Optional[bool]
    ConnectionLimit: Optional[float]
    DefaultPoolId: Optional[str]
    DefaultTlsContainerRef: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    InsertHeaders: Optional[Sequence["_InsertHeaders"]]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ProtocolPort: Optional[float]
    Region: Optional[str]
    SniContainerRefs: Optional[Sequence[str]]
    TenantId: Optional[str]
    TimeoutClientData: Optional[float]
    TimeoutMemberConnect: Optional[float]
    TimeoutMemberData: Optional[float]
    TimeoutTcpInspect: Optional[float]
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
            AdminStateUp=json_data.get("AdminStateUp"),
            ConnectionLimit=json_data.get("ConnectionLimit"),
            DefaultPoolId=json_data.get("DefaultPoolId"),
            DefaultTlsContainerRef=json_data.get("DefaultTlsContainerRef"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            InsertHeaders=json_data.get("InsertHeaders"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ProtocolPort=json_data.get("ProtocolPort"),
            Region=json_data.get("Region"),
            SniContainerRefs=json_data.get("SniContainerRefs"),
            TenantId=json_data.get("TenantId"),
            TimeoutClientData=json_data.get("TimeoutClientData"),
            TimeoutMemberConnect=json_data.get("TimeoutMemberConnect"),
            TimeoutMemberData=json_data.get("TimeoutMemberData"),
            TimeoutTcpInspect=json_data.get("TimeoutTcpInspect"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class InsertHeaders:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InsertHeaders"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InsertHeaders"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InsertHeaders = InsertHeaders


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


