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
    AllowConnections: Optional[bool]
    ConnectionLimit: Optional[float]
    Encoding: Optional[str]
    Id: Optional[str]
    IsTemplate: Optional[bool]
    LcCollate: Optional[str]
    LcCtype: Optional[str]
    Name: Optional[str]
    Owner: Optional[str]
    TablespaceName: Optional[str]
    Template: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AllowConnections=json_data.get("AllowConnections"),
            ConnectionLimit=json_data.get("ConnectionLimit"),
            Encoding=json_data.get("Encoding"),
            Id=json_data.get("Id"),
            IsTemplate=json_data.get("IsTemplate"),
            LcCollate=json_data.get("LcCollate"),
            LcCtype=json_data.get("LcCtype"),
            Name=json_data.get("Name"),
            Owner=json_data.get("Owner"),
            TablespaceName=json_data.get("TablespaceName"),
            Template=json_data.get("Template"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


