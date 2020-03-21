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
    AccessLogEnabled: Optional[bool]
    ApplicationProfileId: Optional[str]
    DefaultPoolMemberPorts: Optional[Sequence[str]]
    Description: Optional[str]
    DisplayName: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpAddress: Optional[str]
    MaxConcurrentConnections: Optional[float]
    MaxNewConnectionRate: Optional[float]
    PersistenceProfileId: Optional[str]
    PoolId: Optional[str]
    Ports: Optional[Sequence[str]]
    Revision: Optional[float]
    SorryPoolId: Optional[str]
    Tag: Optional[Sequence["_Tag"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessLogEnabled=json_data.get("AccessLogEnabled"),
            ApplicationProfileId=json_data.get("ApplicationProfileId"),
            DefaultPoolMemberPorts=json_data.get("DefaultPoolMemberPorts"),
            Description=json_data.get("Description"),
            DisplayName=json_data.get("DisplayName"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            MaxConcurrentConnections=json_data.get("MaxConcurrentConnections"),
            MaxNewConnectionRate=json_data.get("MaxNewConnectionRate"),
            PersistenceProfileId=json_data.get("PersistenceProfileId"),
            PoolId=json_data.get("PoolId"),
            Ports=json_data.get("Ports"),
            Revision=json_data.get("Revision"),
            SorryPoolId=json_data.get("SorryPoolId"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tag:
    Scope: Optional[str]
    Tag: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Scope=json_data.get("Scope"),
            Tag=json_data.get("Tag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag


