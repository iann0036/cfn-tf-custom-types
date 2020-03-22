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
    BeginTime: Optional[str]
    Content: Optional[str]
    CreateTime: Optional[str]
    EndTime: Optional[str]
    Id: Optional[str]
    IssuerCn: Optional[str]
    Key: Optional[str]
    Name: Optional[str]
    SubjectCn: Optional[str]
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
            BeginTime=json_data.get("BeginTime"),
            Content=json_data.get("Content"),
            CreateTime=json_data.get("CreateTime"),
            EndTime=json_data.get("EndTime"),
            Id=json_data.get("Id"),
            IssuerCn=json_data.get("IssuerCn"),
            Key=json_data.get("Key"),
            Name=json_data.get("Name"),
            SubjectCn=json_data.get("SubjectCn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


