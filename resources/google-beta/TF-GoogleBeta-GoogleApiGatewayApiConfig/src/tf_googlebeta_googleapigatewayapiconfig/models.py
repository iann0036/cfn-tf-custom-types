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
    Api: Optional[str]
    ApiConfigId: Optional[str]
    ApiConfigIdPrefix: Optional[str]
    DisplayName: Optional[str]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Project: Optional[str]
    ServiceConfigId: Optional[str]
    GatewayConfig: Optional[Sequence["_GatewayConfigDefinition"]]
    OpenapiDocuments: Optional[Sequence["_OpenapiDocumentsDefinition"]]
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
            Api=json_data.get("Api"),
            ApiConfigId=json_data.get("ApiConfigId"),
            ApiConfigIdPrefix=json_data.get("ApiConfigIdPrefix"),
            DisplayName=json_data.get("DisplayName"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            ServiceConfigId=json_data.get("ServiceConfigId"),
            GatewayConfig=deserialize_list(json_data.get("GatewayConfig"), GatewayConfigDefinition),
            OpenapiDocuments=deserialize_list(json_data.get("OpenapiDocuments"), OpenapiDocumentsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class GatewayConfigDefinition(BaseModel):
    BackendConfig: Optional[Sequence["_BackendConfigDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_GatewayConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GatewayConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendConfig=deserialize_list(json_data.get("BackendConfig"), BackendConfigDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_GatewayConfigDefinition = GatewayConfigDefinition


@dataclass
class BackendConfigDefinition(BaseModel):
    GoogleServiceAccount: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_BackendConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            GoogleServiceAccount=json_data.get("GoogleServiceAccount"),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendConfigDefinition = BackendConfigDefinition


@dataclass
class OpenapiDocumentsDefinition(BaseModel):
    Document: Optional[Sequence["_DocumentDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OpenapiDocumentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenapiDocumentsDefinition"]:
        if not json_data:
            return None
        return cls(
            Document=deserialize_list(json_data.get("Document"), DocumentDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenapiDocumentsDefinition = OpenapiDocumentsDefinition


@dataclass
class DocumentDefinition(BaseModel):
    Contents: Optional[str]
    Path: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DocumentDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DocumentDefinition"]:
        if not json_data:
            return None
        return cls(
            Contents=json_data.get("Contents"),
            Path=json_data.get("Path"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DocumentDefinition = DocumentDefinition


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


