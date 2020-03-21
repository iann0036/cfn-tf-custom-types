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
    AccessMode: Optional[str]
    Accessible: Optional[bool]
    Capacity: Optional[float]
    CustomAttributes: Optional[Sequence["_CustomAttributes"]]
    DatastoreClusterId: Optional[str]
    Folder: Optional[str]
    FreeSpace: Optional[float]
    HostSystemIds: Optional[Sequence[str]]
    Id: Optional[str]
    MaintenanceMode: Optional[str]
    MultipleHostAccess: Optional[bool]
    Name: Optional[str]
    ProtocolEndpoint: Optional[str]
    RemoteHosts: Optional[Sequence[str]]
    RemotePath: Optional[str]
    SecurityType: Optional[str]
    Tags: Optional[Sequence[str]]
    Type: Optional[str]
    UncommittedSpace: Optional[float]
    Url: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AccessMode=json_data.get("AccessMode"),
            Accessible=json_data.get("Accessible"),
            Capacity=json_data.get("Capacity"),
            CustomAttributes=json_data.get("CustomAttributes"),
            DatastoreClusterId=json_data.get("DatastoreClusterId"),
            Folder=json_data.get("Folder"),
            FreeSpace=json_data.get("FreeSpace"),
            HostSystemIds=json_data.get("HostSystemIds"),
            Id=json_data.get("Id"),
            MaintenanceMode=json_data.get("MaintenanceMode"),
            MultipleHostAccess=json_data.get("MultipleHostAccess"),
            Name=json_data.get("Name"),
            ProtocolEndpoint=json_data.get("ProtocolEndpoint"),
            RemoteHosts=json_data.get("RemoteHosts"),
            RemotePath=json_data.get("RemotePath"),
            SecurityType=json_data.get("SecurityType"),
            Tags=json_data.get("Tags"),
            Type=json_data.get("Type"),
            UncommittedSpace=json_data.get("UncommittedSpace"),
            Url=json_data.get("Url"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CustomAttributes:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CustomAttributes"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CustomAttributes"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CustomAttributes = CustomAttributes


