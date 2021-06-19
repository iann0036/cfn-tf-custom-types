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
    Active: Optional[bool]
    AuthToken: Optional[str]
    CertificateCheckEnabled: Optional[bool]
    DavisEventsIntegrationEnabled: Optional[bool]
    EndpointUrl: Optional[str]
    EventsIntegrationEnabled: Optional[bool]
    HostnameVerification: Optional[bool]
    Id: Optional[str]
    Label: Optional[str]
    PrometheusExporters: Optional[bool]
    Unknowns: Optional[str]
    WorkloadIntegrationEnabled: Optional[bool]
    EventsFieldSelectors: Optional[Sequence["_EventsFieldSelectorsDefinition"]]

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
            Active=json_data.get("Active"),
            AuthToken=json_data.get("AuthToken"),
            CertificateCheckEnabled=json_data.get("CertificateCheckEnabled"),
            DavisEventsIntegrationEnabled=json_data.get("DavisEventsIntegrationEnabled"),
            EndpointUrl=json_data.get("EndpointUrl"),
            EventsIntegrationEnabled=json_data.get("EventsIntegrationEnabled"),
            HostnameVerification=json_data.get("HostnameVerification"),
            Id=json_data.get("Id"),
            Label=json_data.get("Label"),
            PrometheusExporters=json_data.get("PrometheusExporters"),
            Unknowns=json_data.get("Unknowns"),
            WorkloadIntegrationEnabled=json_data.get("WorkloadIntegrationEnabled"),
            EventsFieldSelectors=deserialize_list(json_data.get("EventsFieldSelectors"), EventsFieldSelectorsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class EventsFieldSelectorsDefinition(BaseModel):
    Active: Optional[bool]
    FieldSelector: Optional[str]
    Label: Optional[str]
    Unknowns: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_EventsFieldSelectorsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_EventsFieldSelectorsDefinition"]:
        if not json_data:
            return None
        return cls(
            Active=json_data.get("Active"),
            FieldSelector=json_data.get("FieldSelector"),
            Label=json_data.get("Label"),
            Unknowns=json_data.get("Unknowns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_EventsFieldSelectorsDefinition = EventsFieldSelectorsDefinition


