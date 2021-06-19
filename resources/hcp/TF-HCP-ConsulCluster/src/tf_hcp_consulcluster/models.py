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
    CloudProvider: Optional[str]
    ClusterId: Optional[str]
    ConnectEnabled: Optional[bool]
    ConsulAutomaticUpgrades: Optional[bool]
    ConsulCaFile: Optional[str]
    ConsulConfigFile: Optional[str]
    ConsulPrivateEndpointUrl: Optional[str]
    ConsulPublicEndpointUrl: Optional[str]
    ConsulRootTokenAccessorId: Optional[str]
    ConsulRootTokenSecretId: Optional[str]
    ConsulSnapshotInterval: Optional[str]
    ConsulSnapshotRetention: Optional[str]
    ConsulVersion: Optional[str]
    Datacenter: Optional[str]
    HvnId: Optional[str]
    Id: Optional[str]
    MinConsulVersion: Optional[str]
    OrganizationId: Optional[str]
    PrimaryLink: Optional[str]
    ProjectId: Optional[str]
    PublicEndpoint: Optional[bool]
    Region: Optional[str]
    Scale: Optional[float]
    SelfLink: Optional[str]
    Size: Optional[str]
    Tier: Optional[str]
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
            CloudProvider=json_data.get("CloudProvider"),
            ClusterId=json_data.get("ClusterId"),
            ConnectEnabled=json_data.get("ConnectEnabled"),
            ConsulAutomaticUpgrades=json_data.get("ConsulAutomaticUpgrades"),
            ConsulCaFile=json_data.get("ConsulCaFile"),
            ConsulConfigFile=json_data.get("ConsulConfigFile"),
            ConsulPrivateEndpointUrl=json_data.get("ConsulPrivateEndpointUrl"),
            ConsulPublicEndpointUrl=json_data.get("ConsulPublicEndpointUrl"),
            ConsulRootTokenAccessorId=json_data.get("ConsulRootTokenAccessorId"),
            ConsulRootTokenSecretId=json_data.get("ConsulRootTokenSecretId"),
            ConsulSnapshotInterval=json_data.get("ConsulSnapshotInterval"),
            ConsulSnapshotRetention=json_data.get("ConsulSnapshotRetention"),
            ConsulVersion=json_data.get("ConsulVersion"),
            Datacenter=json_data.get("Datacenter"),
            HvnId=json_data.get("HvnId"),
            Id=json_data.get("Id"),
            MinConsulVersion=json_data.get("MinConsulVersion"),
            OrganizationId=json_data.get("OrganizationId"),
            PrimaryLink=json_data.get("PrimaryLink"),
            ProjectId=json_data.get("ProjectId"),
            PublicEndpoint=json_data.get("PublicEndpoint"),
            Region=json_data.get("Region"),
            Scale=json_data.get("Scale"),
            SelfLink=json_data.get("SelfLink"),
            Size=json_data.get("Size"),
            Tier=json_data.get("Tier"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Default: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Default=json_data.get("Default"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


