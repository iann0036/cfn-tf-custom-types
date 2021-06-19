# TF::Intersight::BiosPolicy

Policy for setting BIOS tokens on the endpoint.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::BiosPolicy",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#acscontrolgpu1state" title="AcsControlGpu1state">AcsControlGpu1state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu2state" title="AcsControlGpu2state">AcsControlGpu2state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu3state" title="AcsControlGpu3state">AcsControlGpu3state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu4state" title="AcsControlGpu4state">AcsControlGpu4state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu5state" title="AcsControlGpu5state">AcsControlGpu5state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu6state" title="AcsControlGpu6state">AcsControlGpu6state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu7state" title="AcsControlGpu7state">AcsControlGpu7state</a>" : <i>String</i>,
        "<a href="#acscontrolgpu8state" title="AcsControlGpu8state">AcsControlGpu8state</a>" : <i>String</i>,
        "<a href="#acscontrolslot11state" title="AcsControlSlot11state">AcsControlSlot11state</a>" : <i>String</i>,
        "<a href="#acscontrolslot12state" title="AcsControlSlot12state">AcsControlSlot12state</a>" : <i>String</i>,
        "<a href="#acscontrolslot13state" title="AcsControlSlot13state">AcsControlSlot13state</a>" : <i>String</i>,
        "<a href="#acscontrolslot14state" title="AcsControlSlot14state">AcsControlSlot14state</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#adjacentcachelineprefetch" title="AdjacentCacheLinePrefetch">AdjacentCacheLinePrefetch</a>" : <i>String</i>,
        "<a href="#advancedmemtest" title="AdvancedMemTest">AdvancedMemTest</a>" : <i>String</i>,
        "<a href="#allusbdevices" title="AllUsbDevices">AllUsbDevices</a>" : <i>String</i>,
        "<a href="#altitude" title="Altitude">Altitude</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#aspmsupport" title="AspmSupport">AspmSupport</a>" : <i>String</i>,
        "<a href="#assertnmionperr" title="AssertNmiOnPerr">AssertNmiOnPerr</a>" : <i>String</i>,
        "<a href="#assertnmionserr" title="AssertNmiOnSerr">AssertNmiOnSerr</a>" : <i>String</i>,
        "<a href="#autoccstate" title="AutoCcState">AutoCcState</a>" : <i>String</i>,
        "<a href="#autonumouscstateenable" title="AutonumousCstateEnable">AutonumousCstateEnable</a>" : <i>String</i>,
        "<a href="#baudrate" title="BaudRate">BaudRate</a>" : <i>String</i>,
        "<a href="#bmedmamitigation" title="BmeDmaMitigation">BmeDmaMitigation</a>" : <i>String</i>,
        "<a href="#bootoptionnumretry" title="BootOptionNumRetry">BootOptionNumRetry</a>" : <i>String</i>,
        "<a href="#bootoptionrecooldown" title="BootOptionReCoolDown">BootOptionReCoolDown</a>" : <i>String</i>,
        "<a href="#bootoptionretry" title="BootOptionRetry">BootOptionRetry</a>" : <i>String</i>,
        "<a href="#bootperformancemode" title="BootPerformanceMode">BootPerformanceMode</a>" : <i>String</i>,
        "<a href="#burstandpostponedrefresh" title="BurstAndPostponedRefresh">BurstAndPostponedRefresh</a>" : <i>String</i>,
        "<a href="#cbscmnapbdis" title="CbsCmnApbdis">CbsCmnApbdis</a>" : <i>String</i>,
        "<a href="#cbscmncpucpb" title="CbsCmnCpuCpb">CbsCmnCpuCpb</a>" : <i>String</i>,
        "<a href="#cbscmncpugendowncorectrl" title="CbsCmnCpuGenDowncoreCtrl">CbsCmnCpuGenDowncoreCtrl</a>" : <i>String</i>,
        "<a href="#cbscmncpuglobalcstatectrl" title="CbsCmnCpuGlobalCstateCtrl">CbsCmnCpuGlobalCstateCtrl</a>" : <i>String</i>,
        "<a href="#cbscmncpul1streamhwprefetcher" title="CbsCmnCpuL1streamHwPrefetcher">CbsCmnCpuL1streamHwPrefetcher</a>" : <i>String</i>,
        "<a href="#cbscmncpul2streamhwprefetcher" title="CbsCmnCpuL2streamHwPrefetcher">CbsCmnCpuL2streamHwPrefetcher</a>" : <i>String</i>,
        "<a href="#cbscmncpusmee" title="CbsCmnCpuSmee">CbsCmnCpuSmee</a>" : <i>String</i>,
        "<a href="#cbscmncpustreamingstoresctrl" title="CbsCmnCpuStreamingStoresCtrl">CbsCmnCpuStreamingStoresCtrl</a>" : <i>String</i>,
        "<a href="#cbscmndeterminismslider" title="CbsCmnDeterminismSlider">CbsCmnDeterminismSlider</a>" : <i>String</i>,
        "<a href="#cbscmnefficiencymodeen" title="CbsCmnEfficiencyModeEn">CbsCmnEfficiencyModeEn</a>" : <i>String</i>,
        "<a href="#cbscmnfixedsocpstate" title="CbsCmnFixedSocPstate">CbsCmnFixedSocPstate</a>" : <i>String</i>,
        "<a href="#cbscmngnbnbiommu" title="CbsCmnGnbNbIommu">CbsCmnGnbNbIommu</a>" : <i>String</i>,
        "<a href="#cbscmngnbsmudfcstates" title="CbsCmnGnbSmuDfCstates">CbsCmnGnbSmuDfCstates</a>" : <i>String</i>,
        "<a href="#cbscmngnbsmucppc" title="CbsCmnGnbSmucppc">CbsCmnGnbSmucppc</a>" : <i>String</i>,
        "<a href="#cbscmnmemctrlbankgroupswapddr4" title="CbsCmnMemCtrlBankGroupSwapDdr4">CbsCmnMemCtrlBankGroupSwapDdr4</a>" : <i>String</i>,
        "<a href="#cbscmnmemmapbankinterleaveddr4" title="CbsCmnMemMapBankInterleaveDdr4">CbsCmnMemMapBankInterleaveDdr4</a>" : <i>String</i>,
        "<a href="#cbscmnctdpctl" title="CbsCmncTdpCtl">CbsCmncTdpCtl</a>" : <i>String</i>,
        "<a href="#cbscpuccdctrlssp" title="CbsCpuCcdCtrlSsp">CbsCpuCcdCtrlSsp</a>" : <i>String</i>,
        "<a href="#cbscpucorectrl" title="CbsCpuCoreCtrl">CbsCpuCoreCtrl</a>" : <i>String</i>,
        "<a href="#cbscpusmtctrl" title="CbsCpuSmtCtrl">CbsCpuSmtCtrl</a>" : <i>String</i>,
        "<a href="#cbsdbgcpusnpmemcover" title="CbsDbgCpuSnpMemCover">CbsDbgCpuSnpMemCover</a>" : <i>String</i>,
        "<a href="#cbsdbgcpusnpmemsizecover" title="CbsDbgCpuSnpMemSizeCover">CbsDbgCpuSnpMemSizeCover</a>" : <i>String</i>,
        "<a href="#cbsdfcmnacpisratl3numa" title="CbsDfCmnAcpiSratL3numa">CbsDfCmnAcpiSratL3numa</a>" : <i>String</i>,
        "<a href="#cbsdfcmndramnps" title="CbsDfCmnDramNps">CbsDfCmnDramNps</a>" : <i>String</i>,
        "<a href="#cbsdfcmnmemintlv" title="CbsDfCmnMemIntlv">CbsDfCmnMemIntlv</a>" : <i>String</i>,
        "<a href="#cbsdfcmnmemintlvsize" title="CbsDfCmnMemIntlvSize">CbsDfCmnMemIntlvSize</a>" : <i>String</i>,
        "<a href="#cbssevsnpsupport" title="CbsSevSnpSupport">CbsSevSnpSupport</a>" : <i>String</i>,
        "<a href="#cdnenable" title="CdnEnable">CdnEnable</a>" : <i>String</i>,
        "<a href="#cdnsupport" title="CdnSupport">CdnSupport</a>" : <i>String</i>,
        "<a href="#channelinterleave" title="ChannelInterLeave">ChannelInterLeave</a>" : <i>String</i>,
        "<a href="#ciscoadaptivememtraining" title="CiscoAdaptiveMemTraining">CiscoAdaptiveMemTraining</a>" : <i>String</i>,
        "<a href="#ciscodebuglevel" title="CiscoDebugLevel">CiscoDebugLevel</a>" : <i>String</i>,
        "<a href="#ciscoopromlaunchoptimization" title="CiscoOpromLaunchOptimization">CiscoOpromLaunchOptimization</a>" : <i>String</i>,
        "<a href="#ciscoxgmimaxspeed" title="CiscoXgmiMaxSpeed">CiscoXgmiMaxSpeed</a>" : <i>String</i>,
        "<a href="#ckelowpolicy" title="CkeLowPolicy">CkeLowPolicy</a>" : <i>String</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#closedloopthermthrotl" title="ClosedLoopThermThrotl">ClosedLoopThermThrotl</a>" : <i>String</i>,
        "<a href="#cmcienable" title="CmciEnable">CmciEnable</a>" : <i>String</i>,
        "<a href="#configtdp" title="ConfigTdp">ConfigTdp</a>" : <i>String</i>,
        "<a href="#configtdplevel" title="ConfigTdpLevel">ConfigTdpLevel</a>" : <i>String</i>,
        "<a href="#consoleredirection" title="ConsoleRedirection">ConsoleRedirection</a>" : <i>String</i>,
        "<a href="#coremultiprocessing" title="CoreMultiProcessing">CoreMultiProcessing</a>" : <i>String</i>,
        "<a href="#cpuenergyperformance" title="CpuEnergyPerformance">CpuEnergyPerformance</a>" : <i>String</i>,
        "<a href="#cpufrequencyfloor" title="CpuFrequencyFloor">CpuFrequencyFloor</a>" : <i>String</i>,
        "<a href="#cpuperformance" title="CpuPerformance">CpuPerformance</a>" : <i>String</i>,
        "<a href="#cpupowermanagement" title="CpuPowerManagement">CpuPowerManagement</a>" : <i>String</i>,
        "<a href="#crqos" title="CrQos">CrQos</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#crfastgoconfig" title="CrfastgoConfig">CrfastgoConfig</a>" : <i>String</i>,
        "<a href="#dcpmmfirmwaredowngrade" title="DcpmmFirmwareDowngrade">DcpmmFirmwareDowngrade</a>" : <i>String</i>,
        "<a href="#demandscrub" title="DemandScrub">DemandScrub</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#directcacheaccess" title="DirectCacheAccess">DirectCacheAccess</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#dramclockthrottling" title="DramClockThrottling">DramClockThrottling</a>" : <i>String</i>,
        "<a href="#dramrefreshrate" title="DramRefreshRate">DramRefreshRate</a>" : <i>String</i>,
        "<a href="#dramswthermalthrottling" title="DramSwThermalThrottling">DramSwThermalThrottling</a>" : <i>String</i>,
        "<a href="#eadrsupport" title="EadrSupport">EadrSupport</a>" : <i>String</i>,
        "<a href="#edpcen" title="EdpcEn">EdpcEn</a>" : <i>String</i>,
        "<a href="#enableclockspreadspec" title="EnableClockSpreadSpec">EnableClockSpreadSpec</a>" : <i>String</i>,
        "<a href="#enablemktme" title="EnableMktme">EnableMktme</a>" : <i>String</i>,
        "<a href="#enablesgx" title="EnableSgx">EnableSgx</a>" : <i>String</i>,
        "<a href="#enabletme" title="EnableTme">EnableTme</a>" : <i>String</i>,
        "<a href="#energyefficientturbo" title="EnergyEfficientTurbo">EnergyEfficientTurbo</a>" : <i>String</i>,
        "<a href="#engperftuning" title="EngPerfTuning">EngPerfTuning</a>" : <i>String</i>,
        "<a href="#enhancedintelspeedsteptech" title="EnhancedIntelSpeedStepTech">EnhancedIntelSpeedStepTech</a>" : <i>String</i>,
        "<a href="#epochupdate" title="EpochUpdate">EpochUpdate</a>" : <i>String</i>,
        "<a href="#eppenable" title="EppEnable">EppEnable</a>" : <i>String</i>,
        "<a href="#eppprofile" title="EppProfile">EppProfile</a>" : <i>String</i>,
        "<a href="#executedisablebit" title="ExecuteDisableBit">ExecuteDisableBit</a>" : <i>String</i>,
        "<a href="#extendedapic" title="ExtendedApic">ExtendedApic</a>" : <i>String</i>,
        "<a href="#flowcontrol" title="FlowControl">FlowControl</a>" : <i>String</i>,
        "<a href="#frb2enable" title="Frb2enable">Frb2enable</a>" : <i>String</i>,
        "<a href="#hardwareprefetch" title="HardwarePrefetch">HardwarePrefetch</a>" : <i>String</i>,
        "<a href="#hwpmenable" title="HwpmEnable">HwpmEnable</a>" : <i>String</i>,
        "<a href="#imcinterleave" title="ImcInterleave">ImcInterleave</a>" : <i>String</i>,
        "<a href="#inteldynamicspeedselect" title="IntelDynamicSpeedSelect">IntelDynamicSpeedSelect</a>" : <i>String</i>,
        "<a href="#intelhyperthreadingtech" title="IntelHyperThreadingTech">IntelHyperThreadingTech</a>" : <i>String</i>,
        "<a href="#intelspeedselect" title="IntelSpeedSelect">IntelSpeedSelect</a>" : <i>String</i>,
        "<a href="#intelturboboosttech" title="IntelTurboBoostTech">IntelTurboBoostTech</a>" : <i>String</i>,
        "<a href="#intelvirtualizationtechnology" title="IntelVirtualizationTechnology">IntelVirtualizationTechnology</a>" : <i>String</i>,
        "<a href="#intelvtfordirectedio" title="IntelVtForDirectedIo">IntelVtForDirectedIo</a>" : <i>String</i>,
        "<a href="#intelvtdcoherencysupport" title="IntelVtdCoherencySupport">IntelVtdCoherencySupport</a>" : <i>String</i>,
        "<a href="#intelvtdinterruptremapping" title="IntelVtdInterruptRemapping">IntelVtdInterruptRemapping</a>" : <i>String</i>,
        "<a href="#intelvtdpassthroughdmasupport" title="IntelVtdPassThroughDmaSupport">IntelVtdPassThroughDmaSupport</a>" : <i>String</i>,
        "<a href="#intelvtdatssupport" title="IntelVtdatsSupport">IntelVtdatsSupport</a>" : <i>String</i>,
        "<a href="#ioherrorenable" title="IohErrorEnable">IohErrorEnable</a>" : <i>String</i>,
        "<a href="#iohresource" title="IohResource">IohResource</a>" : <i>String</i>,
        "<a href="#ipprefetch" title="IpPrefetch">IpPrefetch</a>" : <i>String</i>,
        "<a href="#ipv4http" title="Ipv4http">Ipv4http</a>" : <i>String</i>,
        "<a href="#ipv4pxe" title="Ipv4pxe">Ipv4pxe</a>" : <i>String</i>,
        "<a href="#ipv6http" title="Ipv6http">Ipv6http</a>" : <i>String</i>,
        "<a href="#ipv6pxe" title="Ipv6pxe">Ipv6pxe</a>" : <i>String</i>,
        "<a href="#ktiprefetch" title="KtiPrefetch">KtiPrefetch</a>" : <i>String</i>,
        "<a href="#legacyosredirection" title="LegacyOsRedirection">LegacyOsRedirection</a>" : <i>String</i>,
        "<a href="#legacyusbsupport" title="LegacyUsbSupport">LegacyUsbSupport</a>" : <i>String</i>,
        "<a href="#llcprefetch" title="LlcPrefetch">LlcPrefetch</a>" : <i>String</i>,
        "<a href="#lomport0state" title="LomPort0state">LomPort0state</a>" : <i>String</i>,
        "<a href="#lomport1state" title="LomPort1state">LomPort1state</a>" : <i>String</i>,
        "<a href="#lomport2state" title="LomPort2state">LomPort2state</a>" : <i>String</i>,
        "<a href="#lomport3state" title="LomPort3state">LomPort3state</a>" : <i>String</i>,
        "<a href="#lomportsallstate" title="LomPortsAllState">LomPortsAllState</a>" : <i>String</i>,
        "<a href="#lvddrmode" title="LvDdrMode">LvDdrMode</a>" : <i>String</i>,
        "<a href="#makedevicenonbootable" title="MakeDeviceNonBootable">MakeDeviceNonBootable</a>" : <i>String</i>,
        "<a href="#memorybandwidthboost" title="MemoryBandwidthBoost">MemoryBandwidthBoost</a>" : <i>String</i>,
        "<a href="#memoryinterleave" title="MemoryInterLeave">MemoryInterLeave</a>" : <i>String</i>,
        "<a href="#memorymappedioabove4gb" title="MemoryMappedIoAbove4gb">MemoryMappedIoAbove4gb</a>" : <i>String</i>,
        "<a href="#memoryrefreshrate" title="MemoryRefreshRate">MemoryRefreshRate</a>" : <i>String</i>,
        "<a href="#memorysizelimit" title="MemorySizeLimit">MemorySizeLimit</a>" : <i>String</i>,
        "<a href="#memorythermalthrottling" title="MemoryThermalThrottling">MemoryThermalThrottling</a>" : <i>String</i>,
        "<a href="#mirroringmode" title="MirroringMode">MirroringMode</a>" : <i>String</i>,
        "<a href="#mmcfgbase" title="MmcfgBase">MmcfgBase</a>" : <i>String</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkstack" title="NetworkStack">NetworkStack</a>" : <i>String</i>,
        "<a href="#numaoptimized" title="NumaOptimized">NumaOptimized</a>" : <i>String</i>,
        "<a href="#nvmdimmperformconfig" title="NvmdimmPerformConfig">NvmdimmPerformConfig</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#onboard10gbitlom" title="Onboard10gbitLom">Onboard10gbitLom</a>" : <i>String</i>,
        "<a href="#onboardgbitlom" title="OnboardGbitLom">OnboardGbitLom</a>" : <i>String</i>,
        "<a href="#onboardscustoragesupport" title="OnboardScuStorageSupport">OnboardScuStorageSupport</a>" : <i>String</i>,
        "<a href="#onboardscustorageswstack" title="OnboardScuStorageSwStack">OnboardScuStorageSwStack</a>" : <i>String</i>,
        "<a href="#operationmode" title="OperationMode">OperationMode</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>[ <a href="organizationdefinition.md">OrganizationDefinition</a>, ... ]</i>,
        "<a href="#osbootwatchdogtimer" title="OsBootWatchdogTimer">OsBootWatchdogTimer</a>" : <i>String</i>,
        "<a href="#osbootwatchdogtimerpolicy" title="OsBootWatchdogTimerPolicy">OsBootWatchdogTimerPolicy</a>" : <i>String</i>,
        "<a href="#osbootwatchdogtimertimeout" title="OsBootWatchdogTimerTimeout">OsBootWatchdogTimerTimeout</a>" : <i>String</i>,
        "<a href="#outofbandmgmtport" title="OutOfBandMgmtPort">OutOfBandMgmtPort</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#packagecstatelimit" title="PackageCstateLimit">PackageCstateLimit</a>" : <i>String</i>,
        "<a href="#panichighwatermark" title="PanicHighWatermark">PanicHighWatermark</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#partialcachelinesparing" title="PartialCacheLineSparing">PartialCacheLineSparing</a>" : <i>String</i>,
        "<a href="#partialmirrormodeconfig" title="PartialMirrorModeConfig">PartialMirrorModeConfig</a>" : <i>String</i>,
        "<a href="#partialmirrorpercent" title="PartialMirrorPercent">PartialMirrorPercent</a>" : <i>String</i>,
        "<a href="#partialmirrorvalue1" title="PartialMirrorValue1">PartialMirrorValue1</a>" : <i>String</i>,
        "<a href="#partialmirrorvalue2" title="PartialMirrorValue2">PartialMirrorValue2</a>" : <i>String</i>,
        "<a href="#partialmirrorvalue3" title="PartialMirrorValue3">PartialMirrorValue3</a>" : <i>String</i>,
        "<a href="#partialmirrorvalue4" title="PartialMirrorValue4">PartialMirrorValue4</a>" : <i>String</i>,
        "<a href="#patrolscrub" title="PatrolScrub">PatrolScrub</a>" : <i>String</i>,
        "<a href="#patrolscrubduration" title="PatrolScrubDuration">PatrolScrubDuration</a>" : <i>String</i>,
        "<a href="#pcierassupport" title="PcIeRasSupport">PcIeRasSupport</a>" : <i>String</i>,
        "<a href="#pciessdhotplugsupport" title="PcIeSsdHotPlugSupport">PcIeSsdHotPlugSupport</a>" : <i>String</i>,
        "<a href="#pchusb30mode" title="PchUsb30mode">PchUsb30mode</a>" : <i>String</i>,
        "<a href="#pcioptionroms" title="PciOptionRoMs">PciOptionRoMs</a>" : <i>String</i>,
        "<a href="#pciromclp" title="PciRomClp">PciRomClp</a>" : <i>String</i>,
        "<a href="#pciearisupport" title="PcieAriSupport">PcieAriSupport</a>" : <i>String</i>,
        "<a href="#pciepllssc" title="PciePllSsc">PciePllSsc</a>" : <i>String</i>,
        "<a href="#pcieslotmraid1linkspeed" title="PcieSlotMraid1linkSpeed">PcieSlotMraid1linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotmraid1optionrom" title="PcieSlotMraid1optionRom">PcieSlotMraid1optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotmraid2linkspeed" title="PcieSlotMraid2linkSpeed">PcieSlotMraid2linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotmraid2optionrom" title="PcieSlotMraid2optionRom">PcieSlotMraid2optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotmstorraidlinkspeed" title="PcieSlotMstorraidLinkSpeed">PcieSlotMstorraidLinkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotmstorraidoptionrom" title="PcieSlotMstorraidOptionRom">PcieSlotMstorraidOptionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme1linkspeed" title="PcieSlotNvme1linkSpeed">PcieSlotNvme1linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme1optionrom" title="PcieSlotNvme1optionRom">PcieSlotNvme1optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme2linkspeed" title="PcieSlotNvme2linkSpeed">PcieSlotNvme2linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme2optionrom" title="PcieSlotNvme2optionRom">PcieSlotNvme2optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme3linkspeed" title="PcieSlotNvme3linkSpeed">PcieSlotNvme3linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme3optionrom" title="PcieSlotNvme3optionRom">PcieSlotNvme3optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme4linkspeed" title="PcieSlotNvme4linkSpeed">PcieSlotNvme4linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme4optionrom" title="PcieSlotNvme4optionRom">PcieSlotNvme4optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme5linkspeed" title="PcieSlotNvme5linkSpeed">PcieSlotNvme5linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme5optionrom" title="PcieSlotNvme5optionRom">PcieSlotNvme5optionRom</a>" : <i>String</i>,
        "<a href="#pcieslotnvme6linkspeed" title="PcieSlotNvme6linkSpeed">PcieSlotNvme6linkSpeed</a>" : <i>String</i>,
        "<a href="#pcieslotnvme6optionrom" title="PcieSlotNvme6optionRom">PcieSlotNvme6optionRom</a>" : <i>String</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#popsupport" title="PopSupport">PopSupport</a>" : <i>String</i>,
        "<a href="#posterrorpause" title="PostErrorPause">PostErrorPause</a>" : <i>String</i>,
        "<a href="#postpackagerepair" title="PostPackageRepair">PostPackageRepair</a>" : <i>String</i>,
        "<a href="#processorc1e" title="ProcessorC1e">ProcessorC1e</a>" : <i>String</i>,
        "<a href="#processorc3report" title="ProcessorC3report">ProcessorC3report</a>" : <i>String</i>,
        "<a href="#processorc6report" title="ProcessorC6report">ProcessorC6report</a>" : <i>String</i>,
        "<a href="#processorcstate" title="ProcessorCstate">ProcessorCstate</a>" : <i>String</i>,
        "<a href="#profiles" title="Profiles">Profiles</a>" : <i>[ <a href="profilesdefinition.md">ProfilesDefinition</a>, ... ]</i>,
        "<a href="#psata" title="Psata">Psata</a>" : <i>String</i>,
        "<a href="#pstatecoordtype" title="PstateCoordType">PstateCoordType</a>" : <i>String</i>,
        "<a href="#puttykeypad" title="PuttyKeyPad">PuttyKeyPad</a>" : <i>String</i>,
        "<a href="#pwrperftuning" title="PwrPerfTuning">PwrPerfTuning</a>" : <i>String</i>,
        "<a href="#qpilinkfrequency" title="QpiLinkFrequency">QpiLinkFrequency</a>" : <i>String</i>,
        "<a href="#qpilinkspeed" title="QpiLinkSpeed">QpiLinkSpeed</a>" : <i>String</i>,
        "<a href="#qpisnoopmode" title="QpiSnoopMode">QpiSnoopMode</a>" : <i>String</i>,
        "<a href="#rankinterleave" title="RankInterLeave">RankInterLeave</a>" : <i>String</i>,
        "<a href="#redirectionafterpost" title="RedirectionAfterPost">RedirectionAfterPost</a>" : <i>String</i>,
        "<a href="#satamodeselect" title="SataModeSelect">SataModeSelect</a>" : <i>String</i>,
        "<a href="#selectmemoryrasconfiguration" title="SelectMemoryRasConfiguration">SelectMemoryRasConfiguration</a>" : <i>String</i>,
        "<a href="#selectpprtype" title="SelectPprType">SelectPprType</a>" : <i>String</i>,
        "<a href="#serialportaenable" title="SerialPortAenable">SerialPortAenable</a>" : <i>String</i>,
        "<a href="#sev" title="Sev">Sev</a>" : <i>String</i>,
        "<a href="#sgxautoregistrationagent" title="SgxAutoRegistrationAgent">SgxAutoRegistrationAgent</a>" : <i>String</i>,
        "<a href="#sgxepoch0" title="SgxEpoch0">SgxEpoch0</a>" : <i>String</i>,
        "<a href="#sgxepoch1" title="SgxEpoch1">SgxEpoch1</a>" : <i>String</i>,
        "<a href="#sgxfactoryreset" title="SgxFactoryReset">SgxFactoryReset</a>" : <i>String</i>,
        "<a href="#sgxlepubkeyhash0" title="SgxLePubKeyHash0">SgxLePubKeyHash0</a>" : <i>String</i>,
        "<a href="#sgxlepubkeyhash1" title="SgxLePubKeyHash1">SgxLePubKeyHash1</a>" : <i>String</i>,
        "<a href="#sgxlepubkeyhash2" title="SgxLePubKeyHash2">SgxLePubKeyHash2</a>" : <i>String</i>,
        "<a href="#sgxlepubkeyhash3" title="SgxLePubKeyHash3">SgxLePubKeyHash3</a>" : <i>String</i>,
        "<a href="#sgxlewr" title="SgxLeWr">SgxLeWr</a>" : <i>String</i>,
        "<a href="#sgxpackageinfoinbandaccess" title="SgxPackageInfoInBandAccess">SgxPackageInfoInBandAccess</a>" : <i>String</i>,
        "<a href="#sgxqos" title="SgxQos">SgxQos</a>" : <i>String</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#singlepctlenable" title="SinglePctlEnable">SinglePctlEnable</a>" : <i>String</i>,
        "<a href="#slot10linkspeed" title="Slot10linkSpeed">Slot10linkSpeed</a>" : <i>String</i>,
        "<a href="#slot10state" title="Slot10state">Slot10state</a>" : <i>String</i>,
        "<a href="#slot11linkspeed" title="Slot11linkSpeed">Slot11linkSpeed</a>" : <i>String</i>,
        "<a href="#slot11state" title="Slot11state">Slot11state</a>" : <i>String</i>,
        "<a href="#slot12linkspeed" title="Slot12linkSpeed">Slot12linkSpeed</a>" : <i>String</i>,
        "<a href="#slot12state" title="Slot12state">Slot12state</a>" : <i>String</i>,
        "<a href="#slot13state" title="Slot13state">Slot13state</a>" : <i>String</i>,
        "<a href="#slot14state" title="Slot14state">Slot14state</a>" : <i>String</i>,
        "<a href="#slot1linkspeed" title="Slot1linkSpeed">Slot1linkSpeed</a>" : <i>String</i>,
        "<a href="#slot1state" title="Slot1state">Slot1state</a>" : <i>String</i>,
        "<a href="#slot2linkspeed" title="Slot2linkSpeed">Slot2linkSpeed</a>" : <i>String</i>,
        "<a href="#slot2state" title="Slot2state">Slot2state</a>" : <i>String</i>,
        "<a href="#slot3linkspeed" title="Slot3linkSpeed">Slot3linkSpeed</a>" : <i>String</i>,
        "<a href="#slot3state" title="Slot3state">Slot3state</a>" : <i>String</i>,
        "<a href="#slot4linkspeed" title="Slot4linkSpeed">Slot4linkSpeed</a>" : <i>String</i>,
        "<a href="#slot4state" title="Slot4state">Slot4state</a>" : <i>String</i>,
        "<a href="#slot5linkspeed" title="Slot5linkSpeed">Slot5linkSpeed</a>" : <i>String</i>,
        "<a href="#slot5state" title="Slot5state">Slot5state</a>" : <i>String</i>,
        "<a href="#slot6linkspeed" title="Slot6linkSpeed">Slot6linkSpeed</a>" : <i>String</i>,
        "<a href="#slot6state" title="Slot6state">Slot6state</a>" : <i>String</i>,
        "<a href="#slot7linkspeed" title="Slot7linkSpeed">Slot7linkSpeed</a>" : <i>String</i>,
        "<a href="#slot7state" title="Slot7state">Slot7state</a>" : <i>String</i>,
        "<a href="#slot8linkspeed" title="Slot8linkSpeed">Slot8linkSpeed</a>" : <i>String</i>,
        "<a href="#slot8state" title="Slot8state">Slot8state</a>" : <i>String</i>,
        "<a href="#slot9linkspeed" title="Slot9linkSpeed">Slot9linkSpeed</a>" : <i>String</i>,
        "<a href="#slot9state" title="Slot9state">Slot9state</a>" : <i>String</i>,
        "<a href="#slotflomlinkspeed" title="SlotFlomLinkSpeed">SlotFlomLinkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme10linkspeed" title="SlotFrontNvme10linkSpeed">SlotFrontNvme10linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme10optionrom" title="SlotFrontNvme10optionRom">SlotFrontNvme10optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme11linkspeed" title="SlotFrontNvme11linkSpeed">SlotFrontNvme11linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme11optionrom" title="SlotFrontNvme11optionRom">SlotFrontNvme11optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme12linkspeed" title="SlotFrontNvme12linkSpeed">SlotFrontNvme12linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme12optionrom" title="SlotFrontNvme12optionRom">SlotFrontNvme12optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme13optionrom" title="SlotFrontNvme13optionRom">SlotFrontNvme13optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme14optionrom" title="SlotFrontNvme14optionRom">SlotFrontNvme14optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme15optionrom" title="SlotFrontNvme15optionRom">SlotFrontNvme15optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme16optionrom" title="SlotFrontNvme16optionRom">SlotFrontNvme16optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme17optionrom" title="SlotFrontNvme17optionRom">SlotFrontNvme17optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme18optionrom" title="SlotFrontNvme18optionRom">SlotFrontNvme18optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme19optionrom" title="SlotFrontNvme19optionRom">SlotFrontNvme19optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme1linkspeed" title="SlotFrontNvme1linkSpeed">SlotFrontNvme1linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme1optionrom" title="SlotFrontNvme1optionRom">SlotFrontNvme1optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme20optionrom" title="SlotFrontNvme20optionRom">SlotFrontNvme20optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme21optionrom" title="SlotFrontNvme21optionRom">SlotFrontNvme21optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme22optionrom" title="SlotFrontNvme22optionRom">SlotFrontNvme22optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme23optionrom" title="SlotFrontNvme23optionRom">SlotFrontNvme23optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme24optionrom" title="SlotFrontNvme24optionRom">SlotFrontNvme24optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme2linkspeed" title="SlotFrontNvme2linkSpeed">SlotFrontNvme2linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme2optionrom" title="SlotFrontNvme2optionRom">SlotFrontNvme2optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme3linkspeed" title="SlotFrontNvme3linkSpeed">SlotFrontNvme3linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme3optionrom" title="SlotFrontNvme3optionRom">SlotFrontNvme3optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme4linkspeed" title="SlotFrontNvme4linkSpeed">SlotFrontNvme4linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme4optionrom" title="SlotFrontNvme4optionRom">SlotFrontNvme4optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme5linkspeed" title="SlotFrontNvme5linkSpeed">SlotFrontNvme5linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme5optionrom" title="SlotFrontNvme5optionRom">SlotFrontNvme5optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme6linkspeed" title="SlotFrontNvme6linkSpeed">SlotFrontNvme6linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme6optionrom" title="SlotFrontNvme6optionRom">SlotFrontNvme6optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme7linkspeed" title="SlotFrontNvme7linkSpeed">SlotFrontNvme7linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme7optionrom" title="SlotFrontNvme7optionRom">SlotFrontNvme7optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme8linkspeed" title="SlotFrontNvme8linkSpeed">SlotFrontNvme8linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme8optionrom" title="SlotFrontNvme8optionRom">SlotFrontNvme8optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontnvme9linkspeed" title="SlotFrontNvme9linkSpeed">SlotFrontNvme9linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontnvme9optionrom" title="SlotFrontNvme9optionRom">SlotFrontNvme9optionRom</a>" : <i>String</i>,
        "<a href="#slotfrontslot5linkspeed" title="SlotFrontSlot5linkSpeed">SlotFrontSlot5linkSpeed</a>" : <i>String</i>,
        "<a href="#slotfrontslot6linkspeed" title="SlotFrontSlot6linkSpeed">SlotFrontSlot6linkSpeed</a>" : <i>String</i>,
        "<a href="#slotgpu1state" title="SlotGpu1state">SlotGpu1state</a>" : <i>String</i>,
        "<a href="#slotgpu2state" title="SlotGpu2state">SlotGpu2state</a>" : <i>String</i>,
        "<a href="#slotgpu3state" title="SlotGpu3state">SlotGpu3state</a>" : <i>String</i>,
        "<a href="#slotgpu4state" title="SlotGpu4state">SlotGpu4state</a>" : <i>String</i>,
        "<a href="#slotgpu5state" title="SlotGpu5state">SlotGpu5state</a>" : <i>String</i>,
        "<a href="#slotgpu6state" title="SlotGpu6state">SlotGpu6state</a>" : <i>String</i>,
        "<a href="#slotgpu7state" title="SlotGpu7state">SlotGpu7state</a>" : <i>String</i>,
        "<a href="#slotgpu8state" title="SlotGpu8state">SlotGpu8state</a>" : <i>String</i>,
        "<a href="#slothbalinkspeed" title="SlotHbaLinkSpeed">SlotHbaLinkSpeed</a>" : <i>String</i>,
        "<a href="#slothbastate" title="SlotHbaState">SlotHbaState</a>" : <i>String</i>,
        "<a href="#slotlom1link" title="SlotLom1link">SlotLom1link</a>" : <i>String</i>,
        "<a href="#slotlom2link" title="SlotLom2link">SlotLom2link</a>" : <i>String</i>,
        "<a href="#slotmezzstate" title="SlotMezzState">SlotMezzState</a>" : <i>String</i>,
        "<a href="#slotmlomlinkspeed" title="SlotMlomLinkSpeed">SlotMlomLinkSpeed</a>" : <i>String</i>,
        "<a href="#slotmlomstate" title="SlotMlomState">SlotMlomState</a>" : <i>String</i>,
        "<a href="#slotmraidlinkspeed" title="SlotMraidLinkSpeed">SlotMraidLinkSpeed</a>" : <i>String</i>,
        "<a href="#slotmraidstate" title="SlotMraidState">SlotMraidState</a>" : <i>String</i>,
        "<a href="#slotn10state" title="SlotN10state">SlotN10state</a>" : <i>String</i>,
        "<a href="#slotn11state" title="SlotN11state">SlotN11state</a>" : <i>String</i>,
        "<a href="#slotn12state" title="SlotN12state">SlotN12state</a>" : <i>String</i>,
        "<a href="#slotn13state" title="SlotN13state">SlotN13state</a>" : <i>String</i>,
        "<a href="#slotn14state" title="SlotN14state">SlotN14state</a>" : <i>String</i>,
        "<a href="#slotn15state" title="SlotN15state">SlotN15state</a>" : <i>String</i>,
        "<a href="#slotn16state" title="SlotN16state">SlotN16state</a>" : <i>String</i>,
        "<a href="#slotn17state" title="SlotN17state">SlotN17state</a>" : <i>String</i>,
        "<a href="#slotn18state" title="SlotN18state">SlotN18state</a>" : <i>String</i>,
        "<a href="#slotn19state" title="SlotN19state">SlotN19state</a>" : <i>String</i>,
        "<a href="#slotn1state" title="SlotN1state">SlotN1state</a>" : <i>String</i>,
        "<a href="#slotn20state" title="SlotN20state">SlotN20state</a>" : <i>String</i>,
        "<a href="#slotn21state" title="SlotN21state">SlotN21state</a>" : <i>String</i>,
        "<a href="#slotn22state" title="SlotN22state">SlotN22state</a>" : <i>String</i>,
        "<a href="#slotn23state" title="SlotN23state">SlotN23state</a>" : <i>String</i>,
        "<a href="#slotn24state" title="SlotN24state">SlotN24state</a>" : <i>String</i>,
        "<a href="#slotn2state" title="SlotN2state">SlotN2state</a>" : <i>String</i>,
        "<a href="#slotn3state" title="SlotN3state">SlotN3state</a>" : <i>String</i>,
        "<a href="#slotn4state" title="SlotN4state">SlotN4state</a>" : <i>String</i>,
        "<a href="#slotn5state" title="SlotN5state">SlotN5state</a>" : <i>String</i>,
        "<a href="#slotn6state" title="SlotN6state">SlotN6state</a>" : <i>String</i>,
        "<a href="#slotn7state" title="SlotN7state">SlotN7state</a>" : <i>String</i>,
        "<a href="#slotn8state" title="SlotN8state">SlotN8state</a>" : <i>String</i>,
        "<a href="#slotn9state" title="SlotN9state">SlotN9state</a>" : <i>String</i>,
        "<a href="#slotraidlinkspeed" title="SlotRaidLinkSpeed">SlotRaidLinkSpeed</a>" : <i>String</i>,
        "<a href="#slotraidstate" title="SlotRaidState">SlotRaidState</a>" : <i>String</i>,
        "<a href="#slotrearnvme1linkspeed" title="SlotRearNvme1linkSpeed">SlotRearNvme1linkSpeed</a>" : <i>String</i>,
        "<a href="#slotrearnvme1state" title="SlotRearNvme1state">SlotRearNvme1state</a>" : <i>String</i>,
        "<a href="#slotrearnvme2linkspeed" title="SlotRearNvme2linkSpeed">SlotRearNvme2linkSpeed</a>" : <i>String</i>,
        "<a href="#slotrearnvme2state" title="SlotRearNvme2state">SlotRearNvme2state</a>" : <i>String</i>,
        "<a href="#slotrearnvme3linkspeed" title="SlotRearNvme3linkSpeed">SlotRearNvme3linkSpeed</a>" : <i>String</i>,
        "<a href="#slotrearnvme3state" title="SlotRearNvme3state">SlotRearNvme3state</a>" : <i>String</i>,
        "<a href="#slotrearnvme4linkspeed" title="SlotRearNvme4linkSpeed">SlotRearNvme4linkSpeed</a>" : <i>String</i>,
        "<a href="#slotrearnvme4state" title="SlotRearNvme4state">SlotRearNvme4state</a>" : <i>String</i>,
        "<a href="#slotrearnvme5state" title="SlotRearNvme5state">SlotRearNvme5state</a>" : <i>String</i>,
        "<a href="#slotrearnvme6state" title="SlotRearNvme6state">SlotRearNvme6state</a>" : <i>String</i>,
        "<a href="#slotrearnvme7state" title="SlotRearNvme7state">SlotRearNvme7state</a>" : <i>String</i>,
        "<a href="#slotrearnvme8state" title="SlotRearNvme8state">SlotRearNvme8state</a>" : <i>String</i>,
        "<a href="#slotriser1linkspeed" title="SlotRiser1linkSpeed">SlotRiser1linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser1slot1linkspeed" title="SlotRiser1slot1linkSpeed">SlotRiser1slot1linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser1slot2linkspeed" title="SlotRiser1slot2linkSpeed">SlotRiser1slot2linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser1slot3linkspeed" title="SlotRiser1slot3linkSpeed">SlotRiser1slot3linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser2linkspeed" title="SlotRiser2linkSpeed">SlotRiser2linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser2slot4linkspeed" title="SlotRiser2slot4linkSpeed">SlotRiser2slot4linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser2slot5linkspeed" title="SlotRiser2slot5linkSpeed">SlotRiser2slot5linkSpeed</a>" : <i>String</i>,
        "<a href="#slotriser2slot6linkspeed" title="SlotRiser2slot6linkSpeed">SlotRiser2slot6linkSpeed</a>" : <i>String</i>,
        "<a href="#slotsasstate" title="SlotSasState">SlotSasState</a>" : <i>String</i>,
        "<a href="#slotssdslot1linkspeed" title="SlotSsdSlot1linkSpeed">SlotSsdSlot1linkSpeed</a>" : <i>String</i>,
        "<a href="#slotssdslot2linkspeed" title="SlotSsdSlot2linkSpeed">SlotSsdSlot2linkSpeed</a>" : <i>String</i>,
        "<a href="#smee" title="Smee">Smee</a>" : <i>String</i>,
        "<a href="#smtmode" title="SmtMode">SmtMode</a>" : <i>String</i>,
        "<a href="#snc" title="Snc">Snc</a>" : <i>String</i>,
        "<a href="#snoopymodefor2lm" title="SnoopyModeFor2lm">SnoopyModeFor2lm</a>" : <i>String</i>,
        "<a href="#snoopymodeforad" title="SnoopyModeForAd">SnoopyModeForAd</a>" : <i>String</i>,
        "<a href="#sparingmode" title="SparingMode">SparingMode</a>" : <i>String</i>,
        "<a href="#sriov" title="SrIov">SrIov</a>" : <i>String</i>,
        "<a href="#streamerprefetch" title="StreamerPrefetch">StreamerPrefetch</a>" : <i>String</i>,
        "<a href="#svmmode" title="SvmMode">SvmMode</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#terminaltype" title="TerminalType">TerminalType</a>" : <i>String</i>,
        "<a href="#tpmcontrol" title="TpmControl">TpmControl</a>" : <i>String</i>,
        "<a href="#tpmpendingoperation" title="TpmPendingOperation">TpmPendingOperation</a>" : <i>String</i>,
        "<a href="#tpmsupport" title="TpmSupport">TpmSupport</a>" : <i>String</i>,
        "<a href="#tsme" title="Tsme">Tsme</a>" : <i>String</i>,
        "<a href="#txtsupport" title="TxtSupport">TxtSupport</a>" : <i>String</i>,
        "<a href="#ucsmbootorderrule" title="UcsmBootOrderRule">UcsmBootOrderRule</a>" : <i>String</i>,
        "<a href="#ufsdisable" title="UfsDisable">UfsDisable</a>" : <i>String</i>,
        "<a href="#umabasedclustering" title="UmaBasedClustering">UmaBasedClustering</a>" : <i>String</i>,
        "<a href="#usbemul6064" title="UsbEmul6064">UsbEmul6064</a>" : <i>String</i>,
        "<a href="#usbportfront" title="UsbPortFront">UsbPortFront</a>" : <i>String</i>,
        "<a href="#usbportinternal" title="UsbPortInternal">UsbPortInternal</a>" : <i>String</i>,
        "<a href="#usbportkvm" title="UsbPortKvm">UsbPortKvm</a>" : <i>String</i>,
        "<a href="#usbportrear" title="UsbPortRear">UsbPortRear</a>" : <i>String</i>,
        "<a href="#usbportsdcard" title="UsbPortSdCard">UsbPortSdCard</a>" : <i>String</i>,
        "<a href="#usbportvmedia" title="UsbPortVmedia">UsbPortVmedia</a>" : <i>String</i>,
        "<a href="#usbxhcisupport" title="UsbXhciSupport">UsbXhciSupport</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#vgapriority" title="VgaPriority">VgaPriority</a>" : <i>String</i>,
        "<a href="#vmdenable" title="VmdEnable">VmdEnable</a>" : <i>String</i>,
        "<a href="#volmemorymode" title="VolMemoryMode">VolMemoryMode</a>" : <i>String</i>,
        "<a href="#workloadconfig" title="WorkLoadConfig">WorkLoadConfig</a>" : <i>String</i>,
        "<a href="#xptprefetch" title="XptPrefetch">XptPrefetch</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::BiosPolicy
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#acscontrolgpu1state" title="AcsControlGpu1state">AcsControlGpu1state</a>: <i>String</i>
    <a href="#acscontrolgpu2state" title="AcsControlGpu2state">AcsControlGpu2state</a>: <i>String</i>
    <a href="#acscontrolgpu3state" title="AcsControlGpu3state">AcsControlGpu3state</a>: <i>String</i>
    <a href="#acscontrolgpu4state" title="AcsControlGpu4state">AcsControlGpu4state</a>: <i>String</i>
    <a href="#acscontrolgpu5state" title="AcsControlGpu5state">AcsControlGpu5state</a>: <i>String</i>
    <a href="#acscontrolgpu6state" title="AcsControlGpu6state">AcsControlGpu6state</a>: <i>String</i>
    <a href="#acscontrolgpu7state" title="AcsControlGpu7state">AcsControlGpu7state</a>: <i>String</i>
    <a href="#acscontrolgpu8state" title="AcsControlGpu8state">AcsControlGpu8state</a>: <i>String</i>
    <a href="#acscontrolslot11state" title="AcsControlSlot11state">AcsControlSlot11state</a>: <i>String</i>
    <a href="#acscontrolslot12state" title="AcsControlSlot12state">AcsControlSlot12state</a>: <i>String</i>
    <a href="#acscontrolslot13state" title="AcsControlSlot13state">AcsControlSlot13state</a>: <i>String</i>
    <a href="#acscontrolslot14state" title="AcsControlSlot14state">AcsControlSlot14state</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#adjacentcachelineprefetch" title="AdjacentCacheLinePrefetch">AdjacentCacheLinePrefetch</a>: <i>String</i>
    <a href="#advancedmemtest" title="AdvancedMemTest">AdvancedMemTest</a>: <i>String</i>
    <a href="#allusbdevices" title="AllUsbDevices">AllUsbDevices</a>: <i>String</i>
    <a href="#altitude" title="Altitude">Altitude</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#aspmsupport" title="AspmSupport">AspmSupport</a>: <i>String</i>
    <a href="#assertnmionperr" title="AssertNmiOnPerr">AssertNmiOnPerr</a>: <i>String</i>
    <a href="#assertnmionserr" title="AssertNmiOnSerr">AssertNmiOnSerr</a>: <i>String</i>
    <a href="#autoccstate" title="AutoCcState">AutoCcState</a>: <i>String</i>
    <a href="#autonumouscstateenable" title="AutonumousCstateEnable">AutonumousCstateEnable</a>: <i>String</i>
    <a href="#baudrate" title="BaudRate">BaudRate</a>: <i>String</i>
    <a href="#bmedmamitigation" title="BmeDmaMitigation">BmeDmaMitigation</a>: <i>String</i>
    <a href="#bootoptionnumretry" title="BootOptionNumRetry">BootOptionNumRetry</a>: <i>String</i>
    <a href="#bootoptionrecooldown" title="BootOptionReCoolDown">BootOptionReCoolDown</a>: <i>String</i>
    <a href="#bootoptionretry" title="BootOptionRetry">BootOptionRetry</a>: <i>String</i>
    <a href="#bootperformancemode" title="BootPerformanceMode">BootPerformanceMode</a>: <i>String</i>
    <a href="#burstandpostponedrefresh" title="BurstAndPostponedRefresh">BurstAndPostponedRefresh</a>: <i>String</i>
    <a href="#cbscmnapbdis" title="CbsCmnApbdis">CbsCmnApbdis</a>: <i>String</i>
    <a href="#cbscmncpucpb" title="CbsCmnCpuCpb">CbsCmnCpuCpb</a>: <i>String</i>
    <a href="#cbscmncpugendowncorectrl" title="CbsCmnCpuGenDowncoreCtrl">CbsCmnCpuGenDowncoreCtrl</a>: <i>String</i>
    <a href="#cbscmncpuglobalcstatectrl" title="CbsCmnCpuGlobalCstateCtrl">CbsCmnCpuGlobalCstateCtrl</a>: <i>String</i>
    <a href="#cbscmncpul1streamhwprefetcher" title="CbsCmnCpuL1streamHwPrefetcher">CbsCmnCpuL1streamHwPrefetcher</a>: <i>String</i>
    <a href="#cbscmncpul2streamhwprefetcher" title="CbsCmnCpuL2streamHwPrefetcher">CbsCmnCpuL2streamHwPrefetcher</a>: <i>String</i>
    <a href="#cbscmncpusmee" title="CbsCmnCpuSmee">CbsCmnCpuSmee</a>: <i>String</i>
    <a href="#cbscmncpustreamingstoresctrl" title="CbsCmnCpuStreamingStoresCtrl">CbsCmnCpuStreamingStoresCtrl</a>: <i>String</i>
    <a href="#cbscmndeterminismslider" title="CbsCmnDeterminismSlider">CbsCmnDeterminismSlider</a>: <i>String</i>
    <a href="#cbscmnefficiencymodeen" title="CbsCmnEfficiencyModeEn">CbsCmnEfficiencyModeEn</a>: <i>String</i>
    <a href="#cbscmnfixedsocpstate" title="CbsCmnFixedSocPstate">CbsCmnFixedSocPstate</a>: <i>String</i>
    <a href="#cbscmngnbnbiommu" title="CbsCmnGnbNbIommu">CbsCmnGnbNbIommu</a>: <i>String</i>
    <a href="#cbscmngnbsmudfcstates" title="CbsCmnGnbSmuDfCstates">CbsCmnGnbSmuDfCstates</a>: <i>String</i>
    <a href="#cbscmngnbsmucppc" title="CbsCmnGnbSmucppc">CbsCmnGnbSmucppc</a>: <i>String</i>
    <a href="#cbscmnmemctrlbankgroupswapddr4" title="CbsCmnMemCtrlBankGroupSwapDdr4">CbsCmnMemCtrlBankGroupSwapDdr4</a>: <i>String</i>
    <a href="#cbscmnmemmapbankinterleaveddr4" title="CbsCmnMemMapBankInterleaveDdr4">CbsCmnMemMapBankInterleaveDdr4</a>: <i>String</i>
    <a href="#cbscmnctdpctl" title="CbsCmncTdpCtl">CbsCmncTdpCtl</a>: <i>String</i>
    <a href="#cbscpuccdctrlssp" title="CbsCpuCcdCtrlSsp">CbsCpuCcdCtrlSsp</a>: <i>String</i>
    <a href="#cbscpucorectrl" title="CbsCpuCoreCtrl">CbsCpuCoreCtrl</a>: <i>String</i>
    <a href="#cbscpusmtctrl" title="CbsCpuSmtCtrl">CbsCpuSmtCtrl</a>: <i>String</i>
    <a href="#cbsdbgcpusnpmemcover" title="CbsDbgCpuSnpMemCover">CbsDbgCpuSnpMemCover</a>: <i>String</i>
    <a href="#cbsdbgcpusnpmemsizecover" title="CbsDbgCpuSnpMemSizeCover">CbsDbgCpuSnpMemSizeCover</a>: <i>String</i>
    <a href="#cbsdfcmnacpisratl3numa" title="CbsDfCmnAcpiSratL3numa">CbsDfCmnAcpiSratL3numa</a>: <i>String</i>
    <a href="#cbsdfcmndramnps" title="CbsDfCmnDramNps">CbsDfCmnDramNps</a>: <i>String</i>
    <a href="#cbsdfcmnmemintlv" title="CbsDfCmnMemIntlv">CbsDfCmnMemIntlv</a>: <i>String</i>
    <a href="#cbsdfcmnmemintlvsize" title="CbsDfCmnMemIntlvSize">CbsDfCmnMemIntlvSize</a>: <i>String</i>
    <a href="#cbssevsnpsupport" title="CbsSevSnpSupport">CbsSevSnpSupport</a>: <i>String</i>
    <a href="#cdnenable" title="CdnEnable">CdnEnable</a>: <i>String</i>
    <a href="#cdnsupport" title="CdnSupport">CdnSupport</a>: <i>String</i>
    <a href="#channelinterleave" title="ChannelInterLeave">ChannelInterLeave</a>: <i>String</i>
    <a href="#ciscoadaptivememtraining" title="CiscoAdaptiveMemTraining">CiscoAdaptiveMemTraining</a>: <i>String</i>
    <a href="#ciscodebuglevel" title="CiscoDebugLevel">CiscoDebugLevel</a>: <i>String</i>
    <a href="#ciscoopromlaunchoptimization" title="CiscoOpromLaunchOptimization">CiscoOpromLaunchOptimization</a>: <i>String</i>
    <a href="#ciscoxgmimaxspeed" title="CiscoXgmiMaxSpeed">CiscoXgmiMaxSpeed</a>: <i>String</i>
    <a href="#ckelowpolicy" title="CkeLowPolicy">CkeLowPolicy</a>: <i>String</i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#closedloopthermthrotl" title="ClosedLoopThermThrotl">ClosedLoopThermThrotl</a>: <i>String</i>
    <a href="#cmcienable" title="CmciEnable">CmciEnable</a>: <i>String</i>
    <a href="#configtdp" title="ConfigTdp">ConfigTdp</a>: <i>String</i>
    <a href="#configtdplevel" title="ConfigTdpLevel">ConfigTdpLevel</a>: <i>String</i>
    <a href="#consoleredirection" title="ConsoleRedirection">ConsoleRedirection</a>: <i>String</i>
    <a href="#coremultiprocessing" title="CoreMultiProcessing">CoreMultiProcessing</a>: <i>String</i>
    <a href="#cpuenergyperformance" title="CpuEnergyPerformance">CpuEnergyPerformance</a>: <i>String</i>
    <a href="#cpufrequencyfloor" title="CpuFrequencyFloor">CpuFrequencyFloor</a>: <i>String</i>
    <a href="#cpuperformance" title="CpuPerformance">CpuPerformance</a>: <i>String</i>
    <a href="#cpupowermanagement" title="CpuPowerManagement">CpuPowerManagement</a>: <i>String</i>
    <a href="#crqos" title="CrQos">CrQos</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#crfastgoconfig" title="CrfastgoConfig">CrfastgoConfig</a>: <i>String</i>
    <a href="#dcpmmfirmwaredowngrade" title="DcpmmFirmwareDowngrade">DcpmmFirmwareDowngrade</a>: <i>String</i>
    <a href="#demandscrub" title="DemandScrub">DemandScrub</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#directcacheaccess" title="DirectCacheAccess">DirectCacheAccess</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#dramclockthrottling" title="DramClockThrottling">DramClockThrottling</a>: <i>String</i>
    <a href="#dramrefreshrate" title="DramRefreshRate">DramRefreshRate</a>: <i>String</i>
    <a href="#dramswthermalthrottling" title="DramSwThermalThrottling">DramSwThermalThrottling</a>: <i>String</i>
    <a href="#eadrsupport" title="EadrSupport">EadrSupport</a>: <i>String</i>
    <a href="#edpcen" title="EdpcEn">EdpcEn</a>: <i>String</i>
    <a href="#enableclockspreadspec" title="EnableClockSpreadSpec">EnableClockSpreadSpec</a>: <i>String</i>
    <a href="#enablemktme" title="EnableMktme">EnableMktme</a>: <i>String</i>
    <a href="#enablesgx" title="EnableSgx">EnableSgx</a>: <i>String</i>
    <a href="#enabletme" title="EnableTme">EnableTme</a>: <i>String</i>
    <a href="#energyefficientturbo" title="EnergyEfficientTurbo">EnergyEfficientTurbo</a>: <i>String</i>
    <a href="#engperftuning" title="EngPerfTuning">EngPerfTuning</a>: <i>String</i>
    <a href="#enhancedintelspeedsteptech" title="EnhancedIntelSpeedStepTech">EnhancedIntelSpeedStepTech</a>: <i>String</i>
    <a href="#epochupdate" title="EpochUpdate">EpochUpdate</a>: <i>String</i>
    <a href="#eppenable" title="EppEnable">EppEnable</a>: <i>String</i>
    <a href="#eppprofile" title="EppProfile">EppProfile</a>: <i>String</i>
    <a href="#executedisablebit" title="ExecuteDisableBit">ExecuteDisableBit</a>: <i>String</i>
    <a href="#extendedapic" title="ExtendedApic">ExtendedApic</a>: <i>String</i>
    <a href="#flowcontrol" title="FlowControl">FlowControl</a>: <i>String</i>
    <a href="#frb2enable" title="Frb2enable">Frb2enable</a>: <i>String</i>
    <a href="#hardwareprefetch" title="HardwarePrefetch">HardwarePrefetch</a>: <i>String</i>
    <a href="#hwpmenable" title="HwpmEnable">HwpmEnable</a>: <i>String</i>
    <a href="#imcinterleave" title="ImcInterleave">ImcInterleave</a>: <i>String</i>
    <a href="#inteldynamicspeedselect" title="IntelDynamicSpeedSelect">IntelDynamicSpeedSelect</a>: <i>String</i>
    <a href="#intelhyperthreadingtech" title="IntelHyperThreadingTech">IntelHyperThreadingTech</a>: <i>String</i>
    <a href="#intelspeedselect" title="IntelSpeedSelect">IntelSpeedSelect</a>: <i>String</i>
    <a href="#intelturboboosttech" title="IntelTurboBoostTech">IntelTurboBoostTech</a>: <i>String</i>
    <a href="#intelvirtualizationtechnology" title="IntelVirtualizationTechnology">IntelVirtualizationTechnology</a>: <i>String</i>
    <a href="#intelvtfordirectedio" title="IntelVtForDirectedIo">IntelVtForDirectedIo</a>: <i>String</i>
    <a href="#intelvtdcoherencysupport" title="IntelVtdCoherencySupport">IntelVtdCoherencySupport</a>: <i>String</i>
    <a href="#intelvtdinterruptremapping" title="IntelVtdInterruptRemapping">IntelVtdInterruptRemapping</a>: <i>String</i>
    <a href="#intelvtdpassthroughdmasupport" title="IntelVtdPassThroughDmaSupport">IntelVtdPassThroughDmaSupport</a>: <i>String</i>
    <a href="#intelvtdatssupport" title="IntelVtdatsSupport">IntelVtdatsSupport</a>: <i>String</i>
    <a href="#ioherrorenable" title="IohErrorEnable">IohErrorEnable</a>: <i>String</i>
    <a href="#iohresource" title="IohResource">IohResource</a>: <i>String</i>
    <a href="#ipprefetch" title="IpPrefetch">IpPrefetch</a>: <i>String</i>
    <a href="#ipv4http" title="Ipv4http">Ipv4http</a>: <i>String</i>
    <a href="#ipv4pxe" title="Ipv4pxe">Ipv4pxe</a>: <i>String</i>
    <a href="#ipv6http" title="Ipv6http">Ipv6http</a>: <i>String</i>
    <a href="#ipv6pxe" title="Ipv6pxe">Ipv6pxe</a>: <i>String</i>
    <a href="#ktiprefetch" title="KtiPrefetch">KtiPrefetch</a>: <i>String</i>
    <a href="#legacyosredirection" title="LegacyOsRedirection">LegacyOsRedirection</a>: <i>String</i>
    <a href="#legacyusbsupport" title="LegacyUsbSupport">LegacyUsbSupport</a>: <i>String</i>
    <a href="#llcprefetch" title="LlcPrefetch">LlcPrefetch</a>: <i>String</i>
    <a href="#lomport0state" title="LomPort0state">LomPort0state</a>: <i>String</i>
    <a href="#lomport1state" title="LomPort1state">LomPort1state</a>: <i>String</i>
    <a href="#lomport2state" title="LomPort2state">LomPort2state</a>: <i>String</i>
    <a href="#lomport3state" title="LomPort3state">LomPort3state</a>: <i>String</i>
    <a href="#lomportsallstate" title="LomPortsAllState">LomPortsAllState</a>: <i>String</i>
    <a href="#lvddrmode" title="LvDdrMode">LvDdrMode</a>: <i>String</i>
    <a href="#makedevicenonbootable" title="MakeDeviceNonBootable">MakeDeviceNonBootable</a>: <i>String</i>
    <a href="#memorybandwidthboost" title="MemoryBandwidthBoost">MemoryBandwidthBoost</a>: <i>String</i>
    <a href="#memoryinterleave" title="MemoryInterLeave">MemoryInterLeave</a>: <i>String</i>
    <a href="#memorymappedioabove4gb" title="MemoryMappedIoAbove4gb">MemoryMappedIoAbove4gb</a>: <i>String</i>
    <a href="#memoryrefreshrate" title="MemoryRefreshRate">MemoryRefreshRate</a>: <i>String</i>
    <a href="#memorysizelimit" title="MemorySizeLimit">MemorySizeLimit</a>: <i>String</i>
    <a href="#memorythermalthrottling" title="MemoryThermalThrottling">MemoryThermalThrottling</a>: <i>String</i>
    <a href="#mirroringmode" title="MirroringMode">MirroringMode</a>: <i>String</i>
    <a href="#mmcfgbase" title="MmcfgBase">MmcfgBase</a>: <i>String</i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkstack" title="NetworkStack">NetworkStack</a>: <i>String</i>
    <a href="#numaoptimized" title="NumaOptimized">NumaOptimized</a>: <i>String</i>
    <a href="#nvmdimmperformconfig" title="NvmdimmPerformConfig">NvmdimmPerformConfig</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#onboard10gbitlom" title="Onboard10gbitLom">Onboard10gbitLom</a>: <i>String</i>
    <a href="#onboardgbitlom" title="OnboardGbitLom">OnboardGbitLom</a>: <i>String</i>
    <a href="#onboardscustoragesupport" title="OnboardScuStorageSupport">OnboardScuStorageSupport</a>: <i>String</i>
    <a href="#onboardscustorageswstack" title="OnboardScuStorageSwStack">OnboardScuStorageSwStack</a>: <i>String</i>
    <a href="#operationmode" title="OperationMode">OperationMode</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>
      - <a href="organizationdefinition.md">OrganizationDefinition</a></i>
    <a href="#osbootwatchdogtimer" title="OsBootWatchdogTimer">OsBootWatchdogTimer</a>: <i>String</i>
    <a href="#osbootwatchdogtimerpolicy" title="OsBootWatchdogTimerPolicy">OsBootWatchdogTimerPolicy</a>: <i>String</i>
    <a href="#osbootwatchdogtimertimeout" title="OsBootWatchdogTimerTimeout">OsBootWatchdogTimerTimeout</a>: <i>String</i>
    <a href="#outofbandmgmtport" title="OutOfBandMgmtPort">OutOfBandMgmtPort</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#packagecstatelimit" title="PackageCstateLimit">PackageCstateLimit</a>: <i>String</i>
    <a href="#panichighwatermark" title="PanicHighWatermark">PanicHighWatermark</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#partialcachelinesparing" title="PartialCacheLineSparing">PartialCacheLineSparing</a>: <i>String</i>
    <a href="#partialmirrormodeconfig" title="PartialMirrorModeConfig">PartialMirrorModeConfig</a>: <i>String</i>
    <a href="#partialmirrorpercent" title="PartialMirrorPercent">PartialMirrorPercent</a>: <i>String</i>
    <a href="#partialmirrorvalue1" title="PartialMirrorValue1">PartialMirrorValue1</a>: <i>String</i>
    <a href="#partialmirrorvalue2" title="PartialMirrorValue2">PartialMirrorValue2</a>: <i>String</i>
    <a href="#partialmirrorvalue3" title="PartialMirrorValue3">PartialMirrorValue3</a>: <i>String</i>
    <a href="#partialmirrorvalue4" title="PartialMirrorValue4">PartialMirrorValue4</a>: <i>String</i>
    <a href="#patrolscrub" title="PatrolScrub">PatrolScrub</a>: <i>String</i>
    <a href="#patrolscrubduration" title="PatrolScrubDuration">PatrolScrubDuration</a>: <i>String</i>
    <a href="#pcierassupport" title="PcIeRasSupport">PcIeRasSupport</a>: <i>String</i>
    <a href="#pciessdhotplugsupport" title="PcIeSsdHotPlugSupport">PcIeSsdHotPlugSupport</a>: <i>String</i>
    <a href="#pchusb30mode" title="PchUsb30mode">PchUsb30mode</a>: <i>String</i>
    <a href="#pcioptionroms" title="PciOptionRoMs">PciOptionRoMs</a>: <i>String</i>
    <a href="#pciromclp" title="PciRomClp">PciRomClp</a>: <i>String</i>
    <a href="#pciearisupport" title="PcieAriSupport">PcieAriSupport</a>: <i>String</i>
    <a href="#pciepllssc" title="PciePllSsc">PciePllSsc</a>: <i>String</i>
    <a href="#pcieslotmraid1linkspeed" title="PcieSlotMraid1linkSpeed">PcieSlotMraid1linkSpeed</a>: <i>String</i>
    <a href="#pcieslotmraid1optionrom" title="PcieSlotMraid1optionRom">PcieSlotMraid1optionRom</a>: <i>String</i>
    <a href="#pcieslotmraid2linkspeed" title="PcieSlotMraid2linkSpeed">PcieSlotMraid2linkSpeed</a>: <i>String</i>
    <a href="#pcieslotmraid2optionrom" title="PcieSlotMraid2optionRom">PcieSlotMraid2optionRom</a>: <i>String</i>
    <a href="#pcieslotmstorraidlinkspeed" title="PcieSlotMstorraidLinkSpeed">PcieSlotMstorraidLinkSpeed</a>: <i>String</i>
    <a href="#pcieslotmstorraidoptionrom" title="PcieSlotMstorraidOptionRom">PcieSlotMstorraidOptionRom</a>: <i>String</i>
    <a href="#pcieslotnvme1linkspeed" title="PcieSlotNvme1linkSpeed">PcieSlotNvme1linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme1optionrom" title="PcieSlotNvme1optionRom">PcieSlotNvme1optionRom</a>: <i>String</i>
    <a href="#pcieslotnvme2linkspeed" title="PcieSlotNvme2linkSpeed">PcieSlotNvme2linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme2optionrom" title="PcieSlotNvme2optionRom">PcieSlotNvme2optionRom</a>: <i>String</i>
    <a href="#pcieslotnvme3linkspeed" title="PcieSlotNvme3linkSpeed">PcieSlotNvme3linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme3optionrom" title="PcieSlotNvme3optionRom">PcieSlotNvme3optionRom</a>: <i>String</i>
    <a href="#pcieslotnvme4linkspeed" title="PcieSlotNvme4linkSpeed">PcieSlotNvme4linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme4optionrom" title="PcieSlotNvme4optionRom">PcieSlotNvme4optionRom</a>: <i>String</i>
    <a href="#pcieslotnvme5linkspeed" title="PcieSlotNvme5linkSpeed">PcieSlotNvme5linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme5optionrom" title="PcieSlotNvme5optionRom">PcieSlotNvme5optionRom</a>: <i>String</i>
    <a href="#pcieslotnvme6linkspeed" title="PcieSlotNvme6linkSpeed">PcieSlotNvme6linkSpeed</a>: <i>String</i>
    <a href="#pcieslotnvme6optionrom" title="PcieSlotNvme6optionRom">PcieSlotNvme6optionRom</a>: <i>String</i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#popsupport" title="PopSupport">PopSupport</a>: <i>String</i>
    <a href="#posterrorpause" title="PostErrorPause">PostErrorPause</a>: <i>String</i>
    <a href="#postpackagerepair" title="PostPackageRepair">PostPackageRepair</a>: <i>String</i>
    <a href="#processorc1e" title="ProcessorC1e">ProcessorC1e</a>: <i>String</i>
    <a href="#processorc3report" title="ProcessorC3report">ProcessorC3report</a>: <i>String</i>
    <a href="#processorc6report" title="ProcessorC6report">ProcessorC6report</a>: <i>String</i>
    <a href="#processorcstate" title="ProcessorCstate">ProcessorCstate</a>: <i>String</i>
    <a href="#profiles" title="Profiles">Profiles</a>: <i>
      - <a href="profilesdefinition.md">ProfilesDefinition</a></i>
    <a href="#psata" title="Psata">Psata</a>: <i>String</i>
    <a href="#pstatecoordtype" title="PstateCoordType">PstateCoordType</a>: <i>String</i>
    <a href="#puttykeypad" title="PuttyKeyPad">PuttyKeyPad</a>: <i>String</i>
    <a href="#pwrperftuning" title="PwrPerfTuning">PwrPerfTuning</a>: <i>String</i>
    <a href="#qpilinkfrequency" title="QpiLinkFrequency">QpiLinkFrequency</a>: <i>String</i>
    <a href="#qpilinkspeed" title="QpiLinkSpeed">QpiLinkSpeed</a>: <i>String</i>
    <a href="#qpisnoopmode" title="QpiSnoopMode">QpiSnoopMode</a>: <i>String</i>
    <a href="#rankinterleave" title="RankInterLeave">RankInterLeave</a>: <i>String</i>
    <a href="#redirectionafterpost" title="RedirectionAfterPost">RedirectionAfterPost</a>: <i>String</i>
    <a href="#satamodeselect" title="SataModeSelect">SataModeSelect</a>: <i>String</i>
    <a href="#selectmemoryrasconfiguration" title="SelectMemoryRasConfiguration">SelectMemoryRasConfiguration</a>: <i>String</i>
    <a href="#selectpprtype" title="SelectPprType">SelectPprType</a>: <i>String</i>
    <a href="#serialportaenable" title="SerialPortAenable">SerialPortAenable</a>: <i>String</i>
    <a href="#sev" title="Sev">Sev</a>: <i>String</i>
    <a href="#sgxautoregistrationagent" title="SgxAutoRegistrationAgent">SgxAutoRegistrationAgent</a>: <i>String</i>
    <a href="#sgxepoch0" title="SgxEpoch0">SgxEpoch0</a>: <i>String</i>
    <a href="#sgxepoch1" title="SgxEpoch1">SgxEpoch1</a>: <i>String</i>
    <a href="#sgxfactoryreset" title="SgxFactoryReset">SgxFactoryReset</a>: <i>String</i>
    <a href="#sgxlepubkeyhash0" title="SgxLePubKeyHash0">SgxLePubKeyHash0</a>: <i>String</i>
    <a href="#sgxlepubkeyhash1" title="SgxLePubKeyHash1">SgxLePubKeyHash1</a>: <i>String</i>
    <a href="#sgxlepubkeyhash2" title="SgxLePubKeyHash2">SgxLePubKeyHash2</a>: <i>String</i>
    <a href="#sgxlepubkeyhash3" title="SgxLePubKeyHash3">SgxLePubKeyHash3</a>: <i>String</i>
    <a href="#sgxlewr" title="SgxLeWr">SgxLeWr</a>: <i>String</i>
    <a href="#sgxpackageinfoinbandaccess" title="SgxPackageInfoInBandAccess">SgxPackageInfoInBandAccess</a>: <i>String</i>
    <a href="#sgxqos" title="SgxQos">SgxQos</a>: <i>String</i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#singlepctlenable" title="SinglePctlEnable">SinglePctlEnable</a>: <i>String</i>
    <a href="#slot10linkspeed" title="Slot10linkSpeed">Slot10linkSpeed</a>: <i>String</i>
    <a href="#slot10state" title="Slot10state">Slot10state</a>: <i>String</i>
    <a href="#slot11linkspeed" title="Slot11linkSpeed">Slot11linkSpeed</a>: <i>String</i>
    <a href="#slot11state" title="Slot11state">Slot11state</a>: <i>String</i>
    <a href="#slot12linkspeed" title="Slot12linkSpeed">Slot12linkSpeed</a>: <i>String</i>
    <a href="#slot12state" title="Slot12state">Slot12state</a>: <i>String</i>
    <a href="#slot13state" title="Slot13state">Slot13state</a>: <i>String</i>
    <a href="#slot14state" title="Slot14state">Slot14state</a>: <i>String</i>
    <a href="#slot1linkspeed" title="Slot1linkSpeed">Slot1linkSpeed</a>: <i>String</i>
    <a href="#slot1state" title="Slot1state">Slot1state</a>: <i>String</i>
    <a href="#slot2linkspeed" title="Slot2linkSpeed">Slot2linkSpeed</a>: <i>String</i>
    <a href="#slot2state" title="Slot2state">Slot2state</a>: <i>String</i>
    <a href="#slot3linkspeed" title="Slot3linkSpeed">Slot3linkSpeed</a>: <i>String</i>
    <a href="#slot3state" title="Slot3state">Slot3state</a>: <i>String</i>
    <a href="#slot4linkspeed" title="Slot4linkSpeed">Slot4linkSpeed</a>: <i>String</i>
    <a href="#slot4state" title="Slot4state">Slot4state</a>: <i>String</i>
    <a href="#slot5linkspeed" title="Slot5linkSpeed">Slot5linkSpeed</a>: <i>String</i>
    <a href="#slot5state" title="Slot5state">Slot5state</a>: <i>String</i>
    <a href="#slot6linkspeed" title="Slot6linkSpeed">Slot6linkSpeed</a>: <i>String</i>
    <a href="#slot6state" title="Slot6state">Slot6state</a>: <i>String</i>
    <a href="#slot7linkspeed" title="Slot7linkSpeed">Slot7linkSpeed</a>: <i>String</i>
    <a href="#slot7state" title="Slot7state">Slot7state</a>: <i>String</i>
    <a href="#slot8linkspeed" title="Slot8linkSpeed">Slot8linkSpeed</a>: <i>String</i>
    <a href="#slot8state" title="Slot8state">Slot8state</a>: <i>String</i>
    <a href="#slot9linkspeed" title="Slot9linkSpeed">Slot9linkSpeed</a>: <i>String</i>
    <a href="#slot9state" title="Slot9state">Slot9state</a>: <i>String</i>
    <a href="#slotflomlinkspeed" title="SlotFlomLinkSpeed">SlotFlomLinkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme10linkspeed" title="SlotFrontNvme10linkSpeed">SlotFrontNvme10linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme10optionrom" title="SlotFrontNvme10optionRom">SlotFrontNvme10optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme11linkspeed" title="SlotFrontNvme11linkSpeed">SlotFrontNvme11linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme11optionrom" title="SlotFrontNvme11optionRom">SlotFrontNvme11optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme12linkspeed" title="SlotFrontNvme12linkSpeed">SlotFrontNvme12linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme12optionrom" title="SlotFrontNvme12optionRom">SlotFrontNvme12optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme13optionrom" title="SlotFrontNvme13optionRom">SlotFrontNvme13optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme14optionrom" title="SlotFrontNvme14optionRom">SlotFrontNvme14optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme15optionrom" title="SlotFrontNvme15optionRom">SlotFrontNvme15optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme16optionrom" title="SlotFrontNvme16optionRom">SlotFrontNvme16optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme17optionrom" title="SlotFrontNvme17optionRom">SlotFrontNvme17optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme18optionrom" title="SlotFrontNvme18optionRom">SlotFrontNvme18optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme19optionrom" title="SlotFrontNvme19optionRom">SlotFrontNvme19optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme1linkspeed" title="SlotFrontNvme1linkSpeed">SlotFrontNvme1linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme1optionrom" title="SlotFrontNvme1optionRom">SlotFrontNvme1optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme20optionrom" title="SlotFrontNvme20optionRom">SlotFrontNvme20optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme21optionrom" title="SlotFrontNvme21optionRom">SlotFrontNvme21optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme22optionrom" title="SlotFrontNvme22optionRom">SlotFrontNvme22optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme23optionrom" title="SlotFrontNvme23optionRom">SlotFrontNvme23optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme24optionrom" title="SlotFrontNvme24optionRom">SlotFrontNvme24optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme2linkspeed" title="SlotFrontNvme2linkSpeed">SlotFrontNvme2linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme2optionrom" title="SlotFrontNvme2optionRom">SlotFrontNvme2optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme3linkspeed" title="SlotFrontNvme3linkSpeed">SlotFrontNvme3linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme3optionrom" title="SlotFrontNvme3optionRom">SlotFrontNvme3optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme4linkspeed" title="SlotFrontNvme4linkSpeed">SlotFrontNvme4linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme4optionrom" title="SlotFrontNvme4optionRom">SlotFrontNvme4optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme5linkspeed" title="SlotFrontNvme5linkSpeed">SlotFrontNvme5linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme5optionrom" title="SlotFrontNvme5optionRom">SlotFrontNvme5optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme6linkspeed" title="SlotFrontNvme6linkSpeed">SlotFrontNvme6linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme6optionrom" title="SlotFrontNvme6optionRom">SlotFrontNvme6optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme7linkspeed" title="SlotFrontNvme7linkSpeed">SlotFrontNvme7linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme7optionrom" title="SlotFrontNvme7optionRom">SlotFrontNvme7optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme8linkspeed" title="SlotFrontNvme8linkSpeed">SlotFrontNvme8linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme8optionrom" title="SlotFrontNvme8optionRom">SlotFrontNvme8optionRom</a>: <i>String</i>
    <a href="#slotfrontnvme9linkspeed" title="SlotFrontNvme9linkSpeed">SlotFrontNvme9linkSpeed</a>: <i>String</i>
    <a href="#slotfrontnvme9optionrom" title="SlotFrontNvme9optionRom">SlotFrontNvme9optionRom</a>: <i>String</i>
    <a href="#slotfrontslot5linkspeed" title="SlotFrontSlot5linkSpeed">SlotFrontSlot5linkSpeed</a>: <i>String</i>
    <a href="#slotfrontslot6linkspeed" title="SlotFrontSlot6linkSpeed">SlotFrontSlot6linkSpeed</a>: <i>String</i>
    <a href="#slotgpu1state" title="SlotGpu1state">SlotGpu1state</a>: <i>String</i>
    <a href="#slotgpu2state" title="SlotGpu2state">SlotGpu2state</a>: <i>String</i>
    <a href="#slotgpu3state" title="SlotGpu3state">SlotGpu3state</a>: <i>String</i>
    <a href="#slotgpu4state" title="SlotGpu4state">SlotGpu4state</a>: <i>String</i>
    <a href="#slotgpu5state" title="SlotGpu5state">SlotGpu5state</a>: <i>String</i>
    <a href="#slotgpu6state" title="SlotGpu6state">SlotGpu6state</a>: <i>String</i>
    <a href="#slotgpu7state" title="SlotGpu7state">SlotGpu7state</a>: <i>String</i>
    <a href="#slotgpu8state" title="SlotGpu8state">SlotGpu8state</a>: <i>String</i>
    <a href="#slothbalinkspeed" title="SlotHbaLinkSpeed">SlotHbaLinkSpeed</a>: <i>String</i>
    <a href="#slothbastate" title="SlotHbaState">SlotHbaState</a>: <i>String</i>
    <a href="#slotlom1link" title="SlotLom1link">SlotLom1link</a>: <i>String</i>
    <a href="#slotlom2link" title="SlotLom2link">SlotLom2link</a>: <i>String</i>
    <a href="#slotmezzstate" title="SlotMezzState">SlotMezzState</a>: <i>String</i>
    <a href="#slotmlomlinkspeed" title="SlotMlomLinkSpeed">SlotMlomLinkSpeed</a>: <i>String</i>
    <a href="#slotmlomstate" title="SlotMlomState">SlotMlomState</a>: <i>String</i>
    <a href="#slotmraidlinkspeed" title="SlotMraidLinkSpeed">SlotMraidLinkSpeed</a>: <i>String</i>
    <a href="#slotmraidstate" title="SlotMraidState">SlotMraidState</a>: <i>String</i>
    <a href="#slotn10state" title="SlotN10state">SlotN10state</a>: <i>String</i>
    <a href="#slotn11state" title="SlotN11state">SlotN11state</a>: <i>String</i>
    <a href="#slotn12state" title="SlotN12state">SlotN12state</a>: <i>String</i>
    <a href="#slotn13state" title="SlotN13state">SlotN13state</a>: <i>String</i>
    <a href="#slotn14state" title="SlotN14state">SlotN14state</a>: <i>String</i>
    <a href="#slotn15state" title="SlotN15state">SlotN15state</a>: <i>String</i>
    <a href="#slotn16state" title="SlotN16state">SlotN16state</a>: <i>String</i>
    <a href="#slotn17state" title="SlotN17state">SlotN17state</a>: <i>String</i>
    <a href="#slotn18state" title="SlotN18state">SlotN18state</a>: <i>String</i>
    <a href="#slotn19state" title="SlotN19state">SlotN19state</a>: <i>String</i>
    <a href="#slotn1state" title="SlotN1state">SlotN1state</a>: <i>String</i>
    <a href="#slotn20state" title="SlotN20state">SlotN20state</a>: <i>String</i>
    <a href="#slotn21state" title="SlotN21state">SlotN21state</a>: <i>String</i>
    <a href="#slotn22state" title="SlotN22state">SlotN22state</a>: <i>String</i>
    <a href="#slotn23state" title="SlotN23state">SlotN23state</a>: <i>String</i>
    <a href="#slotn24state" title="SlotN24state">SlotN24state</a>: <i>String</i>
    <a href="#slotn2state" title="SlotN2state">SlotN2state</a>: <i>String</i>
    <a href="#slotn3state" title="SlotN3state">SlotN3state</a>: <i>String</i>
    <a href="#slotn4state" title="SlotN4state">SlotN4state</a>: <i>String</i>
    <a href="#slotn5state" title="SlotN5state">SlotN5state</a>: <i>String</i>
    <a href="#slotn6state" title="SlotN6state">SlotN6state</a>: <i>String</i>
    <a href="#slotn7state" title="SlotN7state">SlotN7state</a>: <i>String</i>
    <a href="#slotn8state" title="SlotN8state">SlotN8state</a>: <i>String</i>
    <a href="#slotn9state" title="SlotN9state">SlotN9state</a>: <i>String</i>
    <a href="#slotraidlinkspeed" title="SlotRaidLinkSpeed">SlotRaidLinkSpeed</a>: <i>String</i>
    <a href="#slotraidstate" title="SlotRaidState">SlotRaidState</a>: <i>String</i>
    <a href="#slotrearnvme1linkspeed" title="SlotRearNvme1linkSpeed">SlotRearNvme1linkSpeed</a>: <i>String</i>
    <a href="#slotrearnvme1state" title="SlotRearNvme1state">SlotRearNvme1state</a>: <i>String</i>
    <a href="#slotrearnvme2linkspeed" title="SlotRearNvme2linkSpeed">SlotRearNvme2linkSpeed</a>: <i>String</i>
    <a href="#slotrearnvme2state" title="SlotRearNvme2state">SlotRearNvme2state</a>: <i>String</i>
    <a href="#slotrearnvme3linkspeed" title="SlotRearNvme3linkSpeed">SlotRearNvme3linkSpeed</a>: <i>String</i>
    <a href="#slotrearnvme3state" title="SlotRearNvme3state">SlotRearNvme3state</a>: <i>String</i>
    <a href="#slotrearnvme4linkspeed" title="SlotRearNvme4linkSpeed">SlotRearNvme4linkSpeed</a>: <i>String</i>
    <a href="#slotrearnvme4state" title="SlotRearNvme4state">SlotRearNvme4state</a>: <i>String</i>
    <a href="#slotrearnvme5state" title="SlotRearNvme5state">SlotRearNvme5state</a>: <i>String</i>
    <a href="#slotrearnvme6state" title="SlotRearNvme6state">SlotRearNvme6state</a>: <i>String</i>
    <a href="#slotrearnvme7state" title="SlotRearNvme7state">SlotRearNvme7state</a>: <i>String</i>
    <a href="#slotrearnvme8state" title="SlotRearNvme8state">SlotRearNvme8state</a>: <i>String</i>
    <a href="#slotriser1linkspeed" title="SlotRiser1linkSpeed">SlotRiser1linkSpeed</a>: <i>String</i>
    <a href="#slotriser1slot1linkspeed" title="SlotRiser1slot1linkSpeed">SlotRiser1slot1linkSpeed</a>: <i>String</i>
    <a href="#slotriser1slot2linkspeed" title="SlotRiser1slot2linkSpeed">SlotRiser1slot2linkSpeed</a>: <i>String</i>
    <a href="#slotriser1slot3linkspeed" title="SlotRiser1slot3linkSpeed">SlotRiser1slot3linkSpeed</a>: <i>String</i>
    <a href="#slotriser2linkspeed" title="SlotRiser2linkSpeed">SlotRiser2linkSpeed</a>: <i>String</i>
    <a href="#slotriser2slot4linkspeed" title="SlotRiser2slot4linkSpeed">SlotRiser2slot4linkSpeed</a>: <i>String</i>
    <a href="#slotriser2slot5linkspeed" title="SlotRiser2slot5linkSpeed">SlotRiser2slot5linkSpeed</a>: <i>String</i>
    <a href="#slotriser2slot6linkspeed" title="SlotRiser2slot6linkSpeed">SlotRiser2slot6linkSpeed</a>: <i>String</i>
    <a href="#slotsasstate" title="SlotSasState">SlotSasState</a>: <i>String</i>
    <a href="#slotssdslot1linkspeed" title="SlotSsdSlot1linkSpeed">SlotSsdSlot1linkSpeed</a>: <i>String</i>
    <a href="#slotssdslot2linkspeed" title="SlotSsdSlot2linkSpeed">SlotSsdSlot2linkSpeed</a>: <i>String</i>
    <a href="#smee" title="Smee">Smee</a>: <i>String</i>
    <a href="#smtmode" title="SmtMode">SmtMode</a>: <i>String</i>
    <a href="#snc" title="Snc">Snc</a>: <i>String</i>
    <a href="#snoopymodefor2lm" title="SnoopyModeFor2lm">SnoopyModeFor2lm</a>: <i>String</i>
    <a href="#snoopymodeforad" title="SnoopyModeForAd">SnoopyModeForAd</a>: <i>String</i>
    <a href="#sparingmode" title="SparingMode">SparingMode</a>: <i>String</i>
    <a href="#sriov" title="SrIov">SrIov</a>: <i>String</i>
    <a href="#streamerprefetch" title="StreamerPrefetch">StreamerPrefetch</a>: <i>String</i>
    <a href="#svmmode" title="SvmMode">SvmMode</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#terminaltype" title="TerminalType">TerminalType</a>: <i>String</i>
    <a href="#tpmcontrol" title="TpmControl">TpmControl</a>: <i>String</i>
    <a href="#tpmpendingoperation" title="TpmPendingOperation">TpmPendingOperation</a>: <i>String</i>
    <a href="#tpmsupport" title="TpmSupport">TpmSupport</a>: <i>String</i>
    <a href="#tsme" title="Tsme">Tsme</a>: <i>String</i>
    <a href="#txtsupport" title="TxtSupport">TxtSupport</a>: <i>String</i>
    <a href="#ucsmbootorderrule" title="UcsmBootOrderRule">UcsmBootOrderRule</a>: <i>String</i>
    <a href="#ufsdisable" title="UfsDisable">UfsDisable</a>: <i>String</i>
    <a href="#umabasedclustering" title="UmaBasedClustering">UmaBasedClustering</a>: <i>String</i>
    <a href="#usbemul6064" title="UsbEmul6064">UsbEmul6064</a>: <i>String</i>
    <a href="#usbportfront" title="UsbPortFront">UsbPortFront</a>: <i>String</i>
    <a href="#usbportinternal" title="UsbPortInternal">UsbPortInternal</a>: <i>String</i>
    <a href="#usbportkvm" title="UsbPortKvm">UsbPortKvm</a>: <i>String</i>
    <a href="#usbportrear" title="UsbPortRear">UsbPortRear</a>: <i>String</i>
    <a href="#usbportsdcard" title="UsbPortSdCard">UsbPortSdCard</a>: <i>String</i>
    <a href="#usbportvmedia" title="UsbPortVmedia">UsbPortVmedia</a>: <i>String</i>
    <a href="#usbxhcisupport" title="UsbXhciSupport">UsbXhciSupport</a>: <i>String</i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#vgapriority" title="VgaPriority">VgaPriority</a>: <i>String</i>
    <a href="#vmdenable" title="VmdEnable">VmdEnable</a>: <i>String</i>
    <a href="#volmemorymode" title="VolMemoryMode">VolMemoryMode</a>: <i>String</i>
    <a href="#workloadconfig" title="WorkLoadConfig">WorkLoadConfig</a>: <i>String</i>
    <a href="#xptprefetch" title="XptPrefetch">XptPrefetch</a>: <i>String</i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu4state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu5state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu6state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu7state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlGpu8state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlSlot11state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlSlot12state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlSlot13state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AcsControlSlot14state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdjacentCacheLinePrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedMemTest

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllUsbDevices

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Altitude

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AspmSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssertNmiOnPerr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssertNmiOnSerr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoCcState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutonumousCstateEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BaudRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BmeDmaMitigation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootOptionNumRetry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootOptionReCoolDown

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootOptionRetry

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BootPerformanceMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BurstAndPostponedRefresh

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnApbdis

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuCpb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuGenDowncoreCtrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuGlobalCstateCtrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuL1streamHwPrefetcher

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuL2streamHwPrefetcher

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuSmee

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnCpuStreamingStoresCtrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnDeterminismSlider

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnEfficiencyModeEn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnFixedSocPstate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnGnbNbIommu

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnGnbSmuDfCstates

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnGnbSmucppc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnMemCtrlBankGroupSwapDdr4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmnMemMapBankInterleaveDdr4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCmncTdpCtl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCpuCcdCtrlSsp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCpuCoreCtrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsCpuSmtCtrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDbgCpuSnpMemCover

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDbgCpuSnpMemSizeCover

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDfCmnAcpiSratL3numa

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDfCmnDramNps

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDfCmnMemIntlv

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsDfCmnMemIntlvSize

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CbsSevSnpSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CdnSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelInterLeave

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoAdaptiveMemTraining

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoDebugLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoOpromLaunchOptimization

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CiscoXgmiMaxSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CkeLowPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClosedLoopThermThrotl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CmciEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigTdp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigTdpLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConsoleRedirection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CoreMultiProcessing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuEnergyPerformance

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuFrequencyFloor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPerformance

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CpuPowerManagement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrQos

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrfastgoConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DcpmmFirmwareDowngrade

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DemandScrub

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectCacheAccess

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DramClockThrottling

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DramRefreshRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DramSwThermalThrottling

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EadrSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdpcEn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableClockSpreadSpec

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMktme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSgx

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnergyEfficientTurbo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EngPerfTuning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedIntelSpeedStepTech

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpochUpdate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EppEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EppProfile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecuteDisableBit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedApic

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FlowControl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frb2enable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HardwarePrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HwpmEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImcInterleave

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelDynamicSpeedSelect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelHyperThreadingTech

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelSpeedSelect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelTurboBoostTech

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVirtualizationTechnology

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVtForDirectedIo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVtdCoherencySupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVtdInterruptRemapping

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVtdPassThroughDmaSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntelVtdatsSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IohErrorEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IohResource

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4http

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv4pxe

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6http

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ipv6pxe

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KtiPrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegacyOsRedirection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LegacyUsbSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LlcPrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LomPort0state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LomPort1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LomPort2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LomPort3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LomPortsAllState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LvDdrMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MakeDeviceNonBootable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryBandwidthBoost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryInterLeave

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryMappedIoAbove4gb

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryRefreshRate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemorySizeLimit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MemoryThermalThrottling

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MirroringMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MmcfgBase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumaOptimized

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NvmdimmPerformConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Onboard10gbitLom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnboardGbitLom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnboardScuStorageSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnboardScuStorageSwStack

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperationMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

_Required_: No

_Type_: List of <a href="organizationdefinition.md">OrganizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsBootWatchdogTimer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsBootWatchdogTimerPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OsBootWatchdogTimerTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutOfBandMgmtPort

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageCstateLimit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanicHighWatermark

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialCacheLineSparing

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorModeConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorPercent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorValue1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorValue2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorValue3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartialMirrorValue4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatrolScrub

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PatrolScrubDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcIeRasSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcIeSsdHotPlugSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PchUsb30mode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PciOptionRoMs

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PciRomClp

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieAriSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PciePllSsc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMraid1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMraid1optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMraid2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMraid2optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMstorraidLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotMstorraidOptionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme1optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme2optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme3linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme3optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme4linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme4optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme5linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme5optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme6linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PcieSlotNvme6optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PopSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostErrorPause

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PostPackageRepair

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessorC1e

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessorC3report

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessorC6report

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessorCstate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profiles

_Required_: No

_Type_: List of <a href="profilesdefinition.md">ProfilesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Psata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PstateCoordType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PuttyKeyPad

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PwrPerfTuning

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QpiLinkFrequency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QpiLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QpiSnoopMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RankInterLeave

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RedirectionAfterPost

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SataModeSelect

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectMemoryRasConfiguration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SelectPprType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SerialPortAenable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sev

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxAutoRegistrationAgent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxEpoch0

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxEpoch1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxFactoryReset

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxLePubKeyHash0

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxLePubKeyHash1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxLePubKeyHash2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxLePubKeyHash3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxLeWr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxPackageInfoInBandAccess

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SgxQos

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SinglePctlEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot10linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot10state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot11linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot11state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot12linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot12state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot13state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot14state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot3linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot4linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot4state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot5linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot5state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot6linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot6state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot7linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot7state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot8linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot8state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot9linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slot9state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFlomLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme10linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme10optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme11linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme11optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme12linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme12optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme13optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme14optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme15optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme16optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme17optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme18optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme19optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme1optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme20optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme21optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme22optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme23optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme24optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme2optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme3linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme3optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme4linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme4optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme5linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme5optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme6linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme6optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme7linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme7optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme8linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme8optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme9linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontNvme9optionRom

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontSlot5linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotFrontSlot6linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu4state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu5state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu6state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu7state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotGpu8state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotHbaLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotHbaState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotLom1link

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotLom2link

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotMezzState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotMlomLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotMlomState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotMraidLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotMraidState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN10state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN11state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN12state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN13state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN14state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN15state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN16state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN17state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN18state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN19state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN20state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN21state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN22state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN23state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN24state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN4state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN5state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN6state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN7state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN8state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotN9state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRaidLinkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRaidState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme1state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme2state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme3linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme3state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme4linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme4state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme5state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme6state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme7state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRearNvme8state

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser1slot1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser1slot2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser1slot3linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser2slot4linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser2slot5linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotRiser2slot6linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotSasState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotSsdSlot1linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlotSsdSlot2linkSpeed

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Smee

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SmtMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snc

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnoopyModeFor2lm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnoopyModeForAd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SparingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SrIov

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StreamerPrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SvmMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TerminalType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TpmControl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TpmPendingOperation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TpmSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tsme

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TxtSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UcsmBootOrderRule

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UfsDisable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UmaBasedClustering

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbEmul6064

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortFront

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortInternal

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortKvm

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortRear

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortSdCard

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbPortVmedia

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsbXhciSupport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VgaPriority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmdEnable

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolMemoryMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WorkLoadConfig

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XptPrefetch

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

