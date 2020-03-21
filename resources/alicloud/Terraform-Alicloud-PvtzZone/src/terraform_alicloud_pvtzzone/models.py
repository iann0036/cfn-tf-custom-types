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
    CreationTime: Optional[str]
    IsPtr: Optional[bool]
    Lang: Optional[str]
    Name: Optional[str]
    ProxyPattern: Optional[str]
    RecordCount: Optional[float]
    Remark: Optional[str]
    UpdateTime: Optional[str]
    UserClientIp: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreationTime=json_data.get("CreationTime"),
            IsPtr=json_data.get("IsPtr"),
            Lang=json_data.get("Lang"),
            Name=json_data.get("Name"),
            ProxyPattern=json_data.get("ProxyPattern"),
            RecordCount=json_data.get("RecordCount"),
            Remark=json_data.get("Remark"),
            UpdateTime=json_data.get("UpdateTime"),
            UserClientIp=json_data.get("UserClientIp"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


