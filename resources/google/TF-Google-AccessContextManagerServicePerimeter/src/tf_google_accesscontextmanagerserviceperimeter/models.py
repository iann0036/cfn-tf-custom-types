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
    CreateTime: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Parent: Optional[str]
    PerimeterType: Optional[str]
    Title: Optional[str]
    UpdateTime: Optional[str]
    UseExplicitDryRunSpec: Optional[bool]
    Spec: Optional[Sequence["_SpecDefinition"]]
    Status: Optional[Sequence["_StatusDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Parent=json_data.get("Parent"),
            PerimeterType=json_data.get("PerimeterType"),
            Title=json_data.get("Title"),
            UpdateTime=json_data.get("UpdateTime"),
            UseExplicitDryRunSpec=json_data.get("UseExplicitDryRunSpec"),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
            Status=deserialize_list(json_data.get("Status"), StatusDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SpecDefinition(BaseModel):
    AccessLevels: Optional[Sequence[str]]
    Resources: Optional[Sequence[str]]
    RestrictedServices: Optional[Sequence[str]]
    EgressPolicies: Optional[Sequence["_EgressPoliciesDefinition"]]
    IngressPolicies: Optional[Sequence["_IngressPoliciesDefinition"]]
    VpcAccessibleServices: Optional[Sequence["_VpcAccessibleServicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLevels=json_data.get("AccessLevels"),
            Resources=json_data.get("Resources"),
            RestrictedServices=json_data.get("RestrictedServices"),
            EgressPolicies=deserialize_list(json_data.get("EgressPolicies"), EgressPoliciesDefinition),
            IngressPolicies=deserialize_list(json_data.get("IngressPolicies"), IngressPoliciesDefinition),
            VpcAccessibleServices=deserialize_list(json_data.get("VpcAccessibleServices"), VpcAccessibleServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class EgressPoliciesDefinition(BaseModel):
    EgressFrom: Optional[Sequence["_EgressFromDefinition"]]
    EgressTo: Optional[Sequence["_EgressToDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            EgressFrom=deserialize_list(json_data.get("EgressFrom"), EgressFromDefinition),
            EgressTo=deserialize_list(json_data.get("EgressTo"), EgressToDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressPoliciesDefinition = EgressPoliciesDefinition


@dataclass
class EgressFromDefinition(BaseModel):
    Identities: Optional[Sequence[str]]
    IdentityType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EgressFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressFromDefinition"]:
        if not json_data:
            return None
        return cls(
            Identities=json_data.get("Identities"),
            IdentityType=json_data.get("IdentityType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressFromDefinition = EgressFromDefinition


@dataclass
class EgressToDefinition(BaseModel):
    Resources: Optional[Sequence[str]]
    Operations: Optional[Sequence["_OperationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_EgressToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EgressToDefinition"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            Operations=deserialize_list(json_data.get("Operations"), OperationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_EgressToDefinition = EgressToDefinition


@dataclass
class OperationsDefinition(BaseModel):
    ServiceName: Optional[str]
    MethodSelectors: Optional[Sequence["_MethodSelectorsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_OperationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OperationsDefinition"]:
        if not json_data:
            return None
        return cls(
            ServiceName=json_data.get("ServiceName"),
            MethodSelectors=deserialize_list(json_data.get("MethodSelectors"), MethodSelectorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_OperationsDefinition = OperationsDefinition


@dataclass
class MethodSelectorsDefinition(BaseModel):
    Method: Optional[str]
    Permission: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MethodSelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MethodSelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Method=json_data.get("Method"),
            Permission=json_data.get("Permission"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MethodSelectorsDefinition = MethodSelectorsDefinition


@dataclass
class IngressPoliciesDefinition(BaseModel):
    IngressFrom: Optional[Sequence["_IngressFromDefinition"]]
    IngressTo: Optional[Sequence["_IngressToDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressPoliciesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressPoliciesDefinition"]:
        if not json_data:
            return None
        return cls(
            IngressFrom=deserialize_list(json_data.get("IngressFrom"), IngressFromDefinition),
            IngressTo=deserialize_list(json_data.get("IngressTo"), IngressToDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressPoliciesDefinition = IngressPoliciesDefinition


@dataclass
class IngressFromDefinition(BaseModel):
    Identities: Optional[Sequence[str]]
    IdentityType: Optional[str]
    Sources: Optional[Sequence["_SourcesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressFromDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressFromDefinition"]:
        if not json_data:
            return None
        return cls(
            Identities=json_data.get("Identities"),
            IdentityType=json_data.get("IdentityType"),
            Sources=deserialize_list(json_data.get("Sources"), SourcesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressFromDefinition = IngressFromDefinition


@dataclass
class SourcesDefinition(BaseModel):
    AccessLevel: Optional[str]
    Resource: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SourcesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SourcesDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLevel=json_data.get("AccessLevel"),
            Resource=json_data.get("Resource"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SourcesDefinition = SourcesDefinition


@dataclass
class IngressToDefinition(BaseModel):
    Resources: Optional[Sequence[str]]
    Operations: Optional[Sequence["_OperationsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_IngressToDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IngressToDefinition"]:
        if not json_data:
            return None
        return cls(
            Resources=json_data.get("Resources"),
            Operations=deserialize_list(json_data.get("Operations"), OperationsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_IngressToDefinition = IngressToDefinition


@dataclass
class VpcAccessibleServicesDefinition(BaseModel):
    AllowedServices: Optional[Sequence[str]]
    EnableRestriction: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_VpcAccessibleServicesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VpcAccessibleServicesDefinition"]:
        if not json_data:
            return None
        return cls(
            AllowedServices=json_data.get("AllowedServices"),
            EnableRestriction=json_data.get("EnableRestriction"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VpcAccessibleServicesDefinition = VpcAccessibleServicesDefinition


@dataclass
class StatusDefinition(BaseModel):
    AccessLevels: Optional[Sequence[str]]
    Resources: Optional[Sequence[str]]
    RestrictedServices: Optional[Sequence[str]]
    EgressPolicies: Optional[Sequence["_EgressPoliciesDefinition"]]
    IngressPolicies: Optional[Sequence["_IngressPoliciesDefinition"]]
    VpcAccessibleServices: Optional[Sequence["_VpcAccessibleServicesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_StatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StatusDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLevels=json_data.get("AccessLevels"),
            Resources=json_data.get("Resources"),
            RestrictedServices=json_data.get("RestrictedServices"),
            EgressPolicies=deserialize_list(json_data.get("EgressPolicies"), EgressPoliciesDefinition),
            IngressPolicies=deserialize_list(json_data.get("IngressPolicies"), IngressPoliciesDefinition),
            VpcAccessibleServices=deserialize_list(json_data.get("VpcAccessibleServices"), VpcAccessibleServicesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_StatusDefinition = StatusDefinition


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


