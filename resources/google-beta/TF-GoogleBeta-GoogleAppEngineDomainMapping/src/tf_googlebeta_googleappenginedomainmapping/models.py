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
    DomainName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OverrideStrategy: Optional[str]
    Project: Optional[str]
    ResourceRecords: Optional[Sequence["_ResourceRecordsDefinition"]]
    SslSettings: Optional[Sequence["_SslSettingsDefinition"]]
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
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OverrideStrategy=json_data.get("OverrideStrategy"),
            Project=json_data.get("Project"),
            ResourceRecords=deserialize_list(json_data.get("ResourceRecords"), ResourceRecordsDefinition),
            SslSettings=deserialize_list(json_data.get("SslSettings"), SslSettingsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceRecordsDefinition(BaseModel):
    Name: Optional[str]
    Rrdata: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRecordsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRecordsDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Rrdata=json_data.get("Rrdata"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRecordsDefinition = ResourceRecordsDefinition


@dataclass
class SslSettingsDefinition(BaseModel):
    CertificateId: Optional[str]
    SslManagementType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslSettingsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslSettingsDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateId=json_data.get("CertificateId"),
            SslManagementType=json_data.get("SslManagementType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslSettingsDefinition = SslSettingsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
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
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


