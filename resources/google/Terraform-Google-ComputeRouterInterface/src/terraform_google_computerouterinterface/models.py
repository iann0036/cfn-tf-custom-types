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
    Id: Optional[str]
    InterconnectAttachment: Optional[str]
    IpRange: Optional[str]
    Name: Optional[str]
    Project: Optional[str]
    Region: Optional[str]
    Router: Optional[str]
    VpnTunnel: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Id=json_data.get("Id"),
            InterconnectAttachment=json_data.get("InterconnectAttachment"),
            IpRange=json_data.get("IpRange"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            Router=json_data.get("Router"),
            VpnTunnel=json_data.get("VpnTunnel"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


