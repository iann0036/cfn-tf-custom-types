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
    Description: Optional[str]
    Id: Optional[str]
    LbMethod: Optional[str]
    ListenerId: Optional[str]
    LoadbalancerId: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    Region: Optional[str]
    TenantId: Optional[str]
    Persistence: Optional[Sequence["_Persistence"]]
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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            LbMethod=json_data.get("LbMethod"),
            ListenerId=json_data.get("ListenerId"),
            LoadbalancerId=json_data.get("LoadbalancerId"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            Region=json_data.get("Region"),
            TenantId=json_data.get("TenantId"),
            Persistence=json_data.get("Persistence"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Persistence:
    CookieName: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Persistence"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Persistence"]:
        if not json_data:
            return None
        return cls(
            CookieName=json_data.get("CookieName"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Persistence = Persistence


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


