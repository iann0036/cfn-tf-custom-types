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
    AvailabilityZone: Optional[str]
    Created: Optional[str]
    EnableIamAuth: Optional[bool]
    HbasePublicEndpoint: Optional[str]
    LemonLink: Optional[str]
    LemonNum: Optional[float]
    Name: Optional[str]
    OpenTsdbLink: Optional[str]
    OpentsdbNum: Optional[float]
    OpentsdbPublicEndpoint: Optional[str]
    RsNum: Optional[float]
    SecurityGroupId: Optional[str]
    StorageQuota: Optional[str]
    StorageType: Optional[str]
    SubnetId: Optional[str]
    UsedStorageSize: Optional[str]
    VpcId: Optional[str]
    ZookeeperLink: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            Created=json_data.get("Created"),
            EnableIamAuth=json_data.get("EnableIamAuth"),
            HbasePublicEndpoint=json_data.get("HbasePublicEndpoint"),
            LemonLink=json_data.get("LemonLink"),
            LemonNum=json_data.get("LemonNum"),
            Name=json_data.get("Name"),
            OpenTsdbLink=json_data.get("OpenTsdbLink"),
            OpentsdbNum=json_data.get("OpentsdbNum"),
            OpentsdbPublicEndpoint=json_data.get("OpentsdbPublicEndpoint"),
            RsNum=json_data.get("RsNum"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            StorageQuota=json_data.get("StorageQuota"),
            StorageType=json_data.get("StorageType"),
            SubnetId=json_data.get("SubnetId"),
            UsedStorageSize=json_data.get("UsedStorageSize"),
            VpcId=json_data.get("VpcId"),
            ZookeeperLink=json_data.get("ZookeeperLink"),
            Tags=json_data.get("Tags"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


