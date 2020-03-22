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
    Arn: Optional[str]
    Description: Optional[str]
    ExcludedAccounts: Optional[Sequence[str]]
    Id: Optional[str]
    InputParameters: Optional[str]
    MaximumExecutionFrequency: Optional[str]
    Name: Optional[str]
    ResourceIdScope: Optional[str]
    ResourceTypesScope: Optional[Sequence[str]]
    RuleIdentifier: Optional[str]
    TagKeyScope: Optional[str]
    TagValueScope: Optional[str]
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
            Arn=json_data.get("Arn"),
            Description=json_data.get("Description"),
            ExcludedAccounts=json_data.get("ExcludedAccounts"),
            Id=json_data.get("Id"),
            InputParameters=json_data.get("InputParameters"),
            MaximumExecutionFrequency=json_data.get("MaximumExecutionFrequency"),
            Name=json_data.get("Name"),
            ResourceIdScope=json_data.get("ResourceIdScope"),
            ResourceTypesScope=json_data.get("ResourceTypesScope"),
            RuleIdentifier=json_data.get("RuleIdentifier"),
            TagKeyScope=json_data.get("TagKeyScope"),
            TagValueScope=json_data.get("TagValueScope"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
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
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


