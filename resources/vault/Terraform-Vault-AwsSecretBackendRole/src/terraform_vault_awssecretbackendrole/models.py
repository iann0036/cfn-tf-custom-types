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
    Backend: Optional[str]
    CredentialType: Optional[str]
    DefaultStsTtl: Optional[float]
    MaxStsTtl: Optional[float]
    Name: Optional[str]
    Policy: Optional[str]
    PolicyArn: Optional[str]
    PolicyArns: Optional[Sequence[str]]
    PolicyDocument: Optional[str]
    RoleArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            CredentialType=json_data.get("CredentialType"),
            DefaultStsTtl=json_data.get("DefaultStsTtl"),
            MaxStsTtl=json_data.get("MaxStsTtl"),
            Name=json_data.get("Name"),
            Policy=json_data.get("Policy"),
            PolicyArn=json_data.get("PolicyArn"),
            PolicyArns=json_data.get("PolicyArns"),
            PolicyDocument=json_data.get("PolicyDocument"),
            RoleArns=json_data.get("RoleArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


