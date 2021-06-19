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
    Account: Optional[str]
    CidrBlock: Optional[str]
    ClosName: Optional[str]
    CloudProvider: Optional[str]
    Cnps: Optional[str]
    Id: Optional[str]
    Igw: Optional[str]
    Region: Optional[str]
    ResourceGroup: Optional[str]
    RgName: Optional[str]
    Role: Optional[str]
    SecurityGroupId: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TfId: Optional[str]
    TopologyName: Optional[str]
    VnetName: Optional[str]
    VpcId: Optional[str]
    WanName: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

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
            Account=json_data.get("Account"),
            CidrBlock=json_data.get("CidrBlock"),
            ClosName=json_data.get("ClosName"),
            CloudProvider=json_data.get("CloudProvider"),
            Cnps=json_data.get("Cnps"),
            Id=json_data.get("Id"),
            Igw=json_data.get("Igw"),
            Region=json_data.get("Region"),
            ResourceGroup=json_data.get("ResourceGroup"),
            RgName=json_data.get("RgName"),
            Role=json_data.get("Role"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TfId=json_data.get("TfId"),
            TopologyName=json_data.get("TopologyName"),
            VnetName=json_data.get("VnetName"),
            VpcId=json_data.get("VpcId"),
            WanName=json_data.get("WanName"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
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
class TimeoutsDefinition(BaseModel):
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


