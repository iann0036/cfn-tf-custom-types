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
    CreateTime: Optional[str]
    EipId: Optional[str]
    EnableWhiteList: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Remark: Optional[str]
    SecurityGroup: Optional[str]
    SubnetIds: Optional[Sequence[str]]
    Tag: Optional[str]
    VpcId: Optional[str]
    WhiteList: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CreateTime=json_data.get("CreateTime"),
            EipId=json_data.get("EipId"),
            EnableWhiteList=json_data.get("EnableWhiteList"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Remark=json_data.get("Remark"),
            SecurityGroup=json_data.get("SecurityGroup"),
            SubnetIds=json_data.get("SubnetIds"),
            Tag=json_data.get("Tag"),
            VpcId=json_data.get("VpcId"),
            WhiteList=json_data.get("WhiteList"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


