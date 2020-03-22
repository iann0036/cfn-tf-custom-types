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
    CreationDate: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    OpenstackRc: Optional[Sequence["_OpenstackRc"]]
    Password: Optional[str]
    ProjectId: Optional[str]
    Status: Optional[str]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreationDate=json_data.get("CreationDate"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            OpenstackRc=json_data.get("OpenstackRc"),
            Password=json_data.get("Password"),
            ProjectId=json_data.get("ProjectId"),
            Status=json_data.get("Status"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OpenstackRc:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackRc"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackRc"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackRc = OpenstackRc


