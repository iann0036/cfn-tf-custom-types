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
    AdomPolicyPackages: Optional[str]
    AdomSwitch: Optional[str]
    Assignment: Optional[str]
    ConfigRetrieve: Optional[str]
    ConfigRevert: Optional[str]
    ConsistencyCheck: Optional[str]
    DeployManagement: Optional[str]
    Description: Optional[str]
    DeviceAp: Optional[str]
    DeviceConfig: Optional[str]
    DeviceForticlient: Optional[str]
    DeviceFortiswitch: Optional[str]
    DeviceManager: Optional[str]
    DeviceOperation: Optional[str]
    DeviceProfile: Optional[str]
    DeviceRevisionDeletion: Optional[str]
    DeviceWanLinkLoadBalance: Optional[str]
    FortiguardCenter: Optional[str]
    FortiguardCenterAdvanced: Optional[str]
    FortiguardCenterFirmwareManagerment: Optional[str]
    FortiguardCenterLicensing: Optional[str]
    GlobalPolicyPackages: Optional[str]
    Id: Optional[str]
    ImportPolicyPackages: Optional[str]
    IntfMapping: Optional[str]
    LogViewer: Optional[str]
    PolicyObjects: Optional[str]
    Profileid: Optional[str]
    SetInstallTargets: Optional[str]
    SystemSetting: Optional[str]
    TerminalAccess: Optional[str]
    VpnManager: Optional[str]

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
            AdomPolicyPackages=json_data.get("AdomPolicyPackages"),
            AdomSwitch=json_data.get("AdomSwitch"),
            Assignment=json_data.get("Assignment"),
            ConfigRetrieve=json_data.get("ConfigRetrieve"),
            ConfigRevert=json_data.get("ConfigRevert"),
            ConsistencyCheck=json_data.get("ConsistencyCheck"),
            DeployManagement=json_data.get("DeployManagement"),
            Description=json_data.get("Description"),
            DeviceAp=json_data.get("DeviceAp"),
            DeviceConfig=json_data.get("DeviceConfig"),
            DeviceForticlient=json_data.get("DeviceForticlient"),
            DeviceFortiswitch=json_data.get("DeviceFortiswitch"),
            DeviceManager=json_data.get("DeviceManager"),
            DeviceOperation=json_data.get("DeviceOperation"),
            DeviceProfile=json_data.get("DeviceProfile"),
            DeviceRevisionDeletion=json_data.get("DeviceRevisionDeletion"),
            DeviceWanLinkLoadBalance=json_data.get("DeviceWanLinkLoadBalance"),
            FortiguardCenter=json_data.get("FortiguardCenter"),
            FortiguardCenterAdvanced=json_data.get("FortiguardCenterAdvanced"),
            FortiguardCenterFirmwareManagerment=json_data.get("FortiguardCenterFirmwareManagerment"),
            FortiguardCenterLicensing=json_data.get("FortiguardCenterLicensing"),
            GlobalPolicyPackages=json_data.get("GlobalPolicyPackages"),
            Id=json_data.get("Id"),
            ImportPolicyPackages=json_data.get("ImportPolicyPackages"),
            IntfMapping=json_data.get("IntfMapping"),
            LogViewer=json_data.get("LogViewer"),
            PolicyObjects=json_data.get("PolicyObjects"),
            Profileid=json_data.get("Profileid"),
            SetInstallTargets=json_data.get("SetInstallTargets"),
            SystemSetting=json_data.get("SystemSetting"),
            TerminalAccess=json_data.get("TerminalAccess"),
            VpnManager=json_data.get("VpnManager"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


