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
    ClusterId: Optional[str]
    Database: Optional[str]
    Host: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    Port: Optional[float]
    PrivateHost: Optional[str]
    PrivateUri: Optional[str]
    Region: Optional[str]
    Size: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
    User: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            ClusterId=json_data.get("ClusterId"),
            Database=json_data.get("Database"),
            Host=json_data.get("Host"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            PrivateHost=json_data.get("PrivateHost"),
            PrivateUri=json_data.get("PrivateUri"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            User=json_data.get("User"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


