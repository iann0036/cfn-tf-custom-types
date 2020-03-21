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
    EnrollmentRead: Optional[bool]
    EnrollmentWrite: Optional[bool]
    Id: Optional[str]
    IothubDpsName: Optional[str]
    Name: Optional[str]
    PrimaryConnectionString: Optional[str]
    PrimaryKey: Optional[str]
    RegistrationRead: Optional[bool]
    RegistrationWrite: Optional[bool]
    ResourceGroupName: Optional[str]
    SecondaryConnectionString: Optional[str]
    SecondaryKey: Optional[str]
    ServiceConfig: Optional[bool]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            EnrollmentRead=json_data.get("EnrollmentRead"),
            EnrollmentWrite=json_data.get("EnrollmentWrite"),
            Id=json_data.get("Id"),
            IothubDpsName=json_data.get("IothubDpsName"),
            Name=json_data.get("Name"),
            PrimaryConnectionString=json_data.get("PrimaryConnectionString"),
            PrimaryKey=json_data.get("PrimaryKey"),
            RegistrationRead=json_data.get("RegistrationRead"),
            RegistrationWrite=json_data.get("RegistrationWrite"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            SecondaryConnectionString=json_data.get("SecondaryConnectionString"),
            SecondaryKey=json_data.get("SecondaryKey"),
            ServiceConfig=json_data.get("ServiceConfig"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


