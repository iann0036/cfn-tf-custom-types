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
    Database: Optional[str]
    Engine: Optional[str]
    EvictionPolicy: Optional[str]
    Host: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NodeCount: Optional[float]
    Password: Optional[str]
    Port: Optional[float]
    PrivateHost: Optional[str]
    PrivateNetworkUuid: Optional[str]
    PrivateUri: Optional[str]
    Region: Optional[str]
    Size: Optional[str]
    SqlMode: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]
    Urn: Optional[str]
    User: Optional[str]
    Version: Optional[str]
    MaintenanceWindow: Optional[Sequence["_MaintenanceWindowDefinition"]]

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
            Database=json_data.get("Database"),
            Engine=json_data.get("Engine"),
            EvictionPolicy=json_data.get("EvictionPolicy"),
            Host=json_data.get("Host"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NodeCount=json_data.get("NodeCount"),
            Password=json_data.get("Password"),
            Port=json_data.get("Port"),
            PrivateHost=json_data.get("PrivateHost"),
            PrivateNetworkUuid=json_data.get("PrivateNetworkUuid"),
            PrivateUri=json_data.get("PrivateUri"),
            Region=json_data.get("Region"),
            Size=json_data.get("Size"),
            SqlMode=json_data.get("SqlMode"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
            Urn=json_data.get("Urn"),
            User=json_data.get("User"),
            Version=json_data.get("Version"),
            MaintenanceWindow=deserialize_list(json_data.get("MaintenanceWindow"), MaintenanceWindowDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MaintenanceWindowDefinition(BaseModel):
    Day: Optional[str]
    Hour: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MaintenanceWindowDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MaintenanceWindowDefinition"]:
        if not json_data:
            return None
        return cls(
            Day=json_data.get("Day"),
            Hour=json_data.get("Hour"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MaintenanceWindowDefinition = MaintenanceWindowDefinition


