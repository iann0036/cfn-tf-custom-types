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
    CidrBlocks: Optional[Sequence[str]]
    Description: Optional[str]
    FromPort: Optional[float]
    Ipv6CidrBlocks: Optional[Sequence[str]]
    PrefixListIds: Optional[Sequence[str]]
    Protocol: Optional[str]
    SecurityGroupId: Optional[str]
    Self: Optional[bool]
    SourceSecurityGroupId: Optional[str]
    ToPort: Optional[float]
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
            CidrBlocks=json_data.get("CidrBlocks"),
            Description=json_data.get("Description"),
            FromPort=json_data.get("FromPort"),
            Ipv6CidrBlocks=json_data.get("Ipv6CidrBlocks"),
            PrefixListIds=json_data.get("PrefixListIds"),
            Protocol=json_data.get("Protocol"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Self=json_data.get("Self"),
            SourceSecurityGroupId=json_data.get("SourceSecurityGroupId"),
            ToPort=json_data.get("ToPort"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


