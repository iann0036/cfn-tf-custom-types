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
    ConnectionUri: Optional[str]
    DefaultLeaseTtlSeconds: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    MaxLeaseTtlSeconds: Optional[float]
    Password: Optional[str]
    Path: Optional[str]
    Username: Optional[str]
    VerifyConnection: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ConnectionUri=json_data.get("ConnectionUri"),
            DefaultLeaseTtlSeconds=json_data.get("DefaultLeaseTtlSeconds"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaxLeaseTtlSeconds=json_data.get("MaxLeaseTtlSeconds"),
            Password=json_data.get("Password"),
            Path=json_data.get("Path"),
            Username=json_data.get("Username"),
            VerifyConnection=json_data.get("VerifyConnection"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


