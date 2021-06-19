# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    AvailabilityZone: Optional[str]
    BasicSecurityType: Optional[float]
    ChargePeriod: Optional[float]
    ChargeType: Optional[str]
    CreateTime: Optional[str]
    DeployMode: Optional[float]
    ElasticsearchDomain: Optional[str]
    ElasticsearchPort: Optional[float]
    ElasticsearchVip: Optional[str]
    Id: Optional[str]
    InstanceName: Optional[str]
    KibanaUrl: Optional[str]
    LicenseType: Optional[str]
    Password: Optional[str]
    RenewFlag: Optional[str]
    SubnetId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    Version: Optional[str]
    VpcId: Optional[str]
    MultiZoneInfos: Optional[Sequence["_MultiZoneInfosDefinition"]]
    NodeInfoList: Optional[Sequence["_NodeInfoListDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AvailabilityZone=json_data.get("AvailabilityZone"),
            BasicSecurityType=json_data.get("BasicSecurityType"),
            ChargePeriod=json_data.get("ChargePeriod"),
            ChargeType=json_data.get("ChargeType"),
            CreateTime=json_data.get("CreateTime"),
            DeployMode=json_data.get("DeployMode"),
            ElasticsearchDomain=json_data.get("ElasticsearchDomain"),
            ElasticsearchPort=json_data.get("ElasticsearchPort"),
            ElasticsearchVip=json_data.get("ElasticsearchVip"),
            Id=json_data.get("Id"),
            InstanceName=json_data.get("InstanceName"),
            KibanaUrl=json_data.get("KibanaUrl"),
            LicenseType=json_data.get("LicenseType"),
            Password=json_data.get("Password"),
            RenewFlag=json_data.get("RenewFlag"),
            SubnetId=json_data.get("SubnetId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            MultiZoneInfos=deserialize_list(json_data.get("MultiZoneInfos"), MultiZoneInfosDefinition),
            NodeInfoList=deserialize_list(json_data.get("NodeInfoList"), NodeInfoListDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class MultiZoneInfosDefinition(BaseModel):
    AvailabilityZone: Optional[str]
    SubnetId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MultiZoneInfosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MultiZoneInfosDefinition"]:
        if not json_data:
            return None
        return cls(
            AvailabilityZone=json_data.get("AvailabilityZone"),
            SubnetId=json_data.get("SubnetId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MultiZoneInfosDefinition = MultiZoneInfosDefinition


@dataclass
class NodeInfoListDefinition(BaseModel):
    DiskSize: Optional[float]
    DiskType: Optional[str]
    Encrypt: Optional[bool]
    NodeNum: Optional[float]
    NodeType: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NodeInfoListDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NodeInfoListDefinition"]:
        if not json_data:
            return None
        return cls(
            DiskSize=json_data.get("DiskSize"),
            DiskType=json_data.get("DiskType"),
            Encrypt=json_data.get("Encrypt"),
            NodeNum=json_data.get("NodeNum"),
            NodeType=json_data.get("NodeType"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NodeInfoListDefinition = NodeInfoListDefinition


