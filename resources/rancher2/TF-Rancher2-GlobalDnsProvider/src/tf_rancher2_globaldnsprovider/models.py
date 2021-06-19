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
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    DnsProvider: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    RootDomain: Optional[str]
    AlidnsConfig: Optional[Sequence["_AlidnsConfigDefinition"]]
    CloudflareConfig: Optional[Sequence["_CloudflareConfigDefinition"]]
    Route53Config: Optional[Sequence["_Route53ConfigDefinition"]]
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
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            DnsProvider=json_data.get("DnsProvider"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            RootDomain=json_data.get("RootDomain"),
            AlidnsConfig=deserialize_list(json_data.get("AlidnsConfig"), AlidnsConfigDefinition),
            CloudflareConfig=deserialize_list(json_data.get("CloudflareConfig"), CloudflareConfigDefinition),
            Route53Config=deserialize_list(json_data.get("Route53Config"), Route53ConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class AlidnsConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    SecretKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AlidnsConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AlidnsConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            SecretKey=json_data.get("SecretKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AlidnsConfigDefinition = AlidnsConfigDefinition


@dataclass
class CloudflareConfigDefinition(BaseModel):
    ApiEmail: Optional[str]
    ApiKey: Optional[str]
    ProxySetting: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_CloudflareConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudflareConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            ApiEmail=json_data.get("ApiEmail"),
            ApiKey=json_data.get("ApiKey"),
            ProxySetting=json_data.get("ProxySetting"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudflareConfigDefinition = CloudflareConfigDefinition


@dataclass
class Route53ConfigDefinition(BaseModel):
    AccessKey: Optional[str]
    CredentialsPath: Optional[str]
    Region: Optional[str]
    RoleArn: Optional[str]
    SecretKey: Optional[str]
    ZoneType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Route53ConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Route53ConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessKey=json_data.get("AccessKey"),
            CredentialsPath=json_data.get("CredentialsPath"),
            Region=json_data.get("Region"),
            RoleArn=json_data.get("RoleArn"),
            SecretKey=json_data.get("SecretKey"),
            ZoneType=json_data.get("ZoneType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Route53ConfigDefinition = Route53ConfigDefinition


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


