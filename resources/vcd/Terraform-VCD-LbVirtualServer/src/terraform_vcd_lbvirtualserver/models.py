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
    AppProfileId: Optional[str]
    AppRuleIds: Optional[Sequence[str]]
    ConnectionLimit: Optional[float]
    ConnectionRateLimit: Optional[float]
    Description: Optional[str]
    EdgeGateway: Optional[str]
    EnableAcceleration: Optional[bool]
    Enabled: Optional[bool]
    Id: Optional[str]
    IpAddress: Optional[str]
    Name: Optional[str]
    Org: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    ServerPoolId: Optional[str]
    Vdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppProfileId=json_data.get("AppProfileId"),
            AppRuleIds=json_data.get("AppRuleIds"),
            ConnectionLimit=json_data.get("ConnectionLimit"),
            ConnectionRateLimit=json_data.get("ConnectionRateLimit"),
            Description=json_data.get("Description"),
            EdgeGateway=json_data.get("EdgeGateway"),
            EnableAcceleration=json_data.get("EnableAcceleration"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            IpAddress=json_data.get("IpAddress"),
            Name=json_data.get("Name"),
            Org=json_data.get("Org"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            ServerPoolId=json_data.get("ServerPoolId"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


