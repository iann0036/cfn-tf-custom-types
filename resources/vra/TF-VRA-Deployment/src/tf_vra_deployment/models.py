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
    BlueprintContent: Optional[str]
    BlueprintId: Optional[str]
    BlueprintVersion: Optional[str]
    CatalogItemId: Optional[str]
    CatalogItemVersion: Optional[str]
    CreatedAt: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    ExpandLastRequest: Optional[bool]
    ExpandProject: Optional[bool]
    ExpandResources: Optional[bool]
    Expense: Optional[Sequence["_ExpenseDefinition"]]
    Id: Optional[str]
    Inputs: Optional[Sequence["_InputsDefinition"]]
    InputsIncludingDefaults: Optional[Sequence["_InputsIncludingDefaultsDefinition"]]
    LastRequest: Optional[Sequence["_LastRequestDefinition3"]]
    LastUpdatedAt: Optional[str]
    LastUpdatedBy: Optional[str]
    LeaseExpireAt: Optional[str]
    Name: Optional[str]
    OrgId: Optional[str]
    Owner: Optional[str]
    Project: Optional[Sequence["_ProjectDefinition"]]
    ProjectId: Optional[str]
    Resources: Optional[Sequence["_ResourcesDefinition2"]]
    Status: Optional[str]
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
            BlueprintContent=json_data.get("BlueprintContent"),
            BlueprintId=json_data.get("BlueprintId"),
            BlueprintVersion=json_data.get("BlueprintVersion"),
            CatalogItemId=json_data.get("CatalogItemId"),
            CatalogItemVersion=json_data.get("CatalogItemVersion"),
            CreatedAt=json_data.get("CreatedAt"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            ExpandLastRequest=json_data.get("ExpandLastRequest"),
            ExpandProject=json_data.get("ExpandProject"),
            ExpandResources=json_data.get("ExpandResources"),
            Expense=deserialize_list(json_data.get("Expense"), ExpenseDefinition),
            Id=json_data.get("Id"),
            Inputs=deserialize_list(json_data.get("Inputs"), InputsDefinition),
            InputsIncludingDefaults=deserialize_list(json_data.get("InputsIncludingDefaults"), InputsIncludingDefaultsDefinition),
            LastRequest=deserialize_list(json_data.get("LastRequest"), LastRequestDefinition3),
            LastUpdatedAt=json_data.get("LastUpdatedAt"),
            LastUpdatedBy=json_data.get("LastUpdatedBy"),
            LeaseExpireAt=json_data.get("LeaseExpireAt"),
            Name=json_data.get("Name"),
            OrgId=json_data.get("OrgId"),
            Owner=json_data.get("Owner"),
            Project=deserialize_list(json_data.get("Project"), ProjectDefinition),
            ProjectId=json_data.get("ProjectId"),
            Resources=deserialize_list(json_data.get("Resources"), ResourcesDefinition2),
            Status=json_data.get("Status"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ExpenseDefinition(BaseModel):
    AdditionalExpense: Optional[float]
    Code: Optional[str]
    ComputeExpense: Optional[float]
    LastUpdateTime: Optional[str]
    Message: Optional[str]
    NetworkExpense: Optional[float]
    StorageExpense: Optional[float]
    TotalExpense: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ExpenseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ExpenseDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalExpense=json_data.get("AdditionalExpense"),
            Code=json_data.get("Code"),
            ComputeExpense=json_data.get("ComputeExpense"),
            LastUpdateTime=json_data.get("LastUpdateTime"),
            Message=json_data.get("Message"),
            NetworkExpense=json_data.get("NetworkExpense"),
            StorageExpense=json_data.get("StorageExpense"),
            TotalExpense=json_data.get("TotalExpense"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ExpenseDefinition = ExpenseDefinition


@dataclass
class InputsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputsDefinition = InputsDefinition


@dataclass
class InputsIncludingDefaultsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_InputsIncludingDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_InputsIncludingDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_InputsIncludingDefaultsDefinition = InputsIncludingDefaultsDefinition


@dataclass
class LastRequestDefinition3(BaseModel):
    ActionId: Optional[str]
    ApprovedAt: Optional[str]
    BlueprintId: Optional[str]
    Cancelable: Optional[bool]
    CatalogItemId: Optional[str]
    CompletedAt: Optional[str]
    CompletedTasks: Optional[float]
    CreatedAt: Optional[str]
    Details: Optional[str]
    Dismissed: Optional[bool]
    Id: Optional[str]
    InitializedAt: Optional[str]
    Inputs: Optional[Sequence["_LastRequestDefinition"]]
    Name: Optional[str]
    Outputs: Optional[Sequence["_LastRequestDefinition2"]]
    RequestedBy: Optional[str]
    ResourceName: Optional[str]
    Status: Optional[str]
    TotalTasks: Optional[float]
    UpdatedAt: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastRequestDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastRequestDefinition3"]:
        if not json_data:
            return None
        return cls(
            ActionId=json_data.get("ActionId"),
            ApprovedAt=json_data.get("ApprovedAt"),
            BlueprintId=json_data.get("BlueprintId"),
            Cancelable=json_data.get("Cancelable"),
            CatalogItemId=json_data.get("CatalogItemId"),
            CompletedAt=json_data.get("CompletedAt"),
            CompletedTasks=json_data.get("CompletedTasks"),
            CreatedAt=json_data.get("CreatedAt"),
            Details=json_data.get("Details"),
            Dismissed=json_data.get("Dismissed"),
            Id=json_data.get("Id"),
            InitializedAt=json_data.get("InitializedAt"),
            Inputs=deserialize_list(json_data.get("Inputs"), LastRequestDefinition),
            Name=json_data.get("Name"),
            Outputs=deserialize_list(json_data.get("Outputs"), LastRequestDefinition2),
            RequestedBy=json_data.get("RequestedBy"),
            ResourceName=json_data.get("ResourceName"),
            Status=json_data.get("Status"),
            TotalTasks=json_data.get("TotalTasks"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastRequestDefinition3 = LastRequestDefinition3


@dataclass
class LastRequestDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastRequestDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastRequestDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastRequestDefinition = LastRequestDefinition


@dataclass
class LastRequestDefinition2(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LastRequestDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastRequestDefinition2"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastRequestDefinition2 = LastRequestDefinition2


@dataclass
class ProjectDefinition(BaseModel):
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectDefinition"]:
        if not json_data:
            return None
        return cls(
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectDefinition = ProjectDefinition


@dataclass
class ResourcesDefinition2(BaseModel):
    CreatedAt: Optional[str]
    DependsOn: Optional[Sequence[str]]
    Description: Optional[str]
    Expense: Optional[Sequence["_ResourcesDefinition"]]
    Id: Optional[str]
    Name: Optional[str]
    PropertiesJson: Optional[str]
    State: Optional[str]
    SyncStatus: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition2"]:
        if not json_data:
            return None
        return cls(
            CreatedAt=json_data.get("CreatedAt"),
            DependsOn=json_data.get("DependsOn"),
            Description=json_data.get("Description"),
            Expense=deserialize_list(json_data.get("Expense"), ResourcesDefinition),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            PropertiesJson=json_data.get("PropertiesJson"),
            State=json_data.get("State"),
            SyncStatus=json_data.get("SyncStatus"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition2 = ResourcesDefinition2


@dataclass
class ResourcesDefinition(BaseModel):
    AdditionalExpense: Optional[float]
    Code: Optional[str]
    ComputeExpense: Optional[float]
    LastUpdateTime: Optional[str]
    Message: Optional[str]
    NetworkExpense: Optional[float]
    StorageExpense: Optional[float]
    TotalExpense: Optional[float]
    Unit: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AdditionalExpense=json_data.get("AdditionalExpense"),
            Code=json_data.get("Code"),
            ComputeExpense=json_data.get("ComputeExpense"),
            LastUpdateTime=json_data.get("LastUpdateTime"),
            Message=json_data.get("Message"),
            NetworkExpense=json_data.get("NetworkExpense"),
            StorageExpense=json_data.get("StorageExpense"),
            TotalExpense=json_data.get("TotalExpense"),
            Unit=json_data.get("Unit"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourcesDefinition = ResourcesDefinition


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


