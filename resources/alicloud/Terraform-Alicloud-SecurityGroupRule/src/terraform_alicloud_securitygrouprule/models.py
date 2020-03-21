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
    CidrIp: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpProtocol: Optional[str]
    NicType: Optional[str]
    Policy: Optional[str]
    PortRange: Optional[str]
    Priority: Optional[float]
    SecurityGroupId: Optional[str]
    SourceGroupOwnerAccount: Optional[str]
    SourceSecurityGroupId: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CidrIp=json_data.get("CidrIp"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpProtocol=json_data.get("IpProtocol"),
            NicType=json_data.get("NicType"),
            Policy=json_data.get("Policy"),
            PortRange=json_data.get("PortRange"),
            Priority=json_data.get("Priority"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            SourceGroupOwnerAccount=json_data.get("SourceGroupOwnerAccount"),
            SourceSecurityGroupId=json_data.get("SourceSecurityGroupId"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


