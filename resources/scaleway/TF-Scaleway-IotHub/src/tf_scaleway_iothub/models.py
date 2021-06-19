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
    ConnectedDeviceCount: Optional[float]
    CreatedAt: Optional[str]
    DeviceAutoProvisioning: Optional[bool]
    DeviceCount: Optional[float]
    DisableEvents: Optional[bool]
    Enabled: Optional[bool]
    Endpoint: Optional[str]
    EventsTopicPrefix: Optional[str]
    HubCa: Optional[str]
    HubCaChallenge: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrganizationId: Optional[str]
    ProductPlan: Optional[str]
    ProjectId: Optional[str]
    Region: Optional[str]
    Status: Optional[str]
    UpdatedAt: Optional[str]

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
            ConnectedDeviceCount=json_data.get("ConnectedDeviceCount"),
            CreatedAt=json_data.get("CreatedAt"),
            DeviceAutoProvisioning=json_data.get("DeviceAutoProvisioning"),
            DeviceCount=json_data.get("DeviceCount"),
            DisableEvents=json_data.get("DisableEvents"),
            Enabled=json_data.get("Enabled"),
            Endpoint=json_data.get("Endpoint"),
            EventsTopicPrefix=json_data.get("EventsTopicPrefix"),
            HubCa=json_data.get("HubCa"),
            HubCaChallenge=json_data.get("HubCaChallenge"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrganizationId=json_data.get("OrganizationId"),
            ProductPlan=json_data.get("ProductPlan"),
            ProjectId=json_data.get("ProjectId"),
            Region=json_data.get("Region"),
            Status=json_data.get("Status"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


