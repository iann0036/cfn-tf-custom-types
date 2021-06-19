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
    CustomerId: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OrganisationAssignments: Optional[Sequence["_OrganisationAssignmentsDefinition3"]]
    ServiceId: Optional[str]
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
            CustomerId=json_data.get("CustomerId"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OrganisationAssignments=deserialize_list(json_data.get("OrganisationAssignments"), OrganisationAssignmentsDefinition3),
            ServiceId=json_data.get("ServiceId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class OrganisationAssignmentsDefinition3(BaseModel):
    Customer: Optional[Sequence["_OrganisationAssignmentsDefinition"]]
    Service: Optional[Sequence["_OrganisationAssignmentsDefinition2"]]

    @classmethod
    def _deserialize(
        cls: Type["_OrganisationAssignmentsDefinition3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganisationAssignmentsDefinition3"]:
        if not json_data:
            return None
        return cls(
            Customer=deserialize_list(json_data.get("Customer"), OrganisationAssignmentsDefinition),
            Service=deserialize_list(json_data.get("Service"), OrganisationAssignmentsDefinition2),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganisationAssignmentsDefinition3 = OrganisationAssignmentsDefinition3


@dataclass
class OrganisationAssignmentsDefinition(BaseModel):
    CustomerId: Optional[str]
    Demo: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    NameSlug: Optional[str]
    Reseller: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganisationAssignmentsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganisationAssignmentsDefinition"]:
        if not json_data:
            return None
        return cls(
            CustomerId=json_data.get("CustomerId"),
            Demo=json_data.get("Demo"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NameSlug=json_data.get("NameSlug"),
            Reseller=json_data.get("Reseller"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganisationAssignmentsDefinition = OrganisationAssignmentsDefinition


@dataclass
class OrganisationAssignmentsDefinition2(BaseModel):
    Id: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrganisationAssignmentsDefinition2"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrganisationAssignmentsDefinition2"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrganisationAssignmentsDefinition2 = OrganisationAssignmentsDefinition2


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]

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
            Read=json_data.get("Read"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


