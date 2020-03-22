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
    Algorithm: Optional[str]
    AlgorithmParameters: Optional[str]
    Description: Optional[str]
    EdgeGateway: Optional[str]
    EnableTransparency: Optional[bool]
    Id: Optional[str]
    MonitorId: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Vdc: Optional[str]
    Member: Optional[Sequence["_Member"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Algorithm=json_data.get("Algorithm"),
            AlgorithmParameters=json_data.get("AlgorithmParameters"),
            Description=json_data.get("Description"),
            EdgeGateway=json_data.get("EdgeGateway"),
            EnableTransparency=json_data.get("EnableTransparency"),
            Id=json_data.get("Id"),
            MonitorId=json_data.get("MonitorId"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Vdc=json_data.get("Vdc"),
            Member=json_data.get("Member"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Member:
    Condition: Optional[str]
    IpAddress: Optional[str]
    MaxConnections: Optional[float]
    MinConnections: Optional[float]
    MonitorPort: Optional[float]
    Name: Optional[str]
    Port: Optional[float]
    Weight: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Member"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Member"]:
        if not json_data:
            return None
        return cls(
            Condition=json_data.get("Condition"),
            IpAddress=json_data.get("IpAddress"),
            MaxConnections=json_data.get("MaxConnections"),
            MinConnections=json_data.get("MinConnections"),
            MonitorPort=json_data.get("MonitorPort"),
            Name=json_data.get("Name"),
            Port=json_data.get("Port"),
            Weight=json_data.get("Weight"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Member = Member


