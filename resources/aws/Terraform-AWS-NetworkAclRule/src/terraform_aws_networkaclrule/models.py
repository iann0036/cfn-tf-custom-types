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
    CidrBlock: Optional[str]
    Egress: Optional[bool]
    FromPort: Optional[float]
    IcmpCode: Optional[str]
    IcmpType: Optional[str]
    Id: Optional[str]
    Ipv6CidrBlock: Optional[str]
    NetworkAclId: Optional[str]
    Protocol: Optional[str]
    RuleAction: Optional[str]
    RuleNumber: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CidrBlock=json_data.get("CidrBlock"),
            Egress=json_data.get("Egress"),
            FromPort=json_data.get("FromPort"),
            IcmpCode=json_data.get("IcmpCode"),
            IcmpType=json_data.get("IcmpType"),
            Id=json_data.get("Id"),
            Ipv6CidrBlock=json_data.get("Ipv6CidrBlock"),
            NetworkAclId=json_data.get("NetworkAclId"),
            Protocol=json_data.get("Protocol"),
            RuleAction=json_data.get("RuleAction"),
            RuleNumber=json_data.get("RuleNumber"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


