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
    CreateTime: Optional[str]
    Name: Optional[str]
    NetworkInfo: Optional[Sequence["_NetworkInfo"]]
    Remark: Optional[str]
    Tag: Optional[str]
    UpdateTime: Optional[str]

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
            CreateTime=json_data.get("CreateTime"),
            Name=json_data.get("Name"),
            NetworkInfo=json_data.get("NetworkInfo"),
            Remark=json_data.get("Remark"),
            Tag=json_data.get("Tag"),
            UpdateTime=json_data.get("UpdateTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class NetworkInfo:
    CidrBlock: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkInfo"]:
        if not json_data:
            return None
        return cls(
            CidrBlock=json_data.get("CidrBlock"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkInfo = NetworkInfo


