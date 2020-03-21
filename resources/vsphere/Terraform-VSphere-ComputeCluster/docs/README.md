# Terraform::VSphere::ComputeCluster

CloudFormation equivalent of vsphere_compute_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::ComputeCluster",
    "Properties" : {
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#dpmautomationlevel" title="DpmAutomationLevel">DpmAutomationLevel</a>" : <i>String</i>,
        "<a href="#dpmenabled" title="DpmEnabled">DpmEnabled</a>" : <i>Boolean</i>,
        "<a href="#dpmthreshold" title="DpmThreshold">DpmThreshold</a>" : <i>Double</i>,
        "<a href="#drsadvancedoptions" title="DrsAdvancedOptions">DrsAdvancedOptions</a>" : <i>[ <a href="drsadvancedoptions.md">DrsAdvancedOptions</a>, ... ]</i>,
        "<a href="#drsautomationlevel" title="DrsAutomationLevel">DrsAutomationLevel</a>" : <i>String</i>,
        "<a href="#drsenablepredictivedrs" title="DrsEnablePredictiveDrs">DrsEnablePredictiveDrs</a>" : <i>Boolean</i>,
        "<a href="#drsenablevmoverrides" title="DrsEnableVmOverrides">DrsEnableVmOverrides</a>" : <i>Boolean</i>,
        "<a href="#drsenabled" title="DrsEnabled">DrsEnabled</a>" : <i>Boolean</i>,
        "<a href="#drsmigrationthreshold" title="DrsMigrationThreshold">DrsMigrationThreshold</a>" : <i>Double</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#forceevacuateondestroy" title="ForceEvacuateOnDestroy">ForceEvacuateOnDestroy</a>" : <i>Boolean</i>,
        "<a href="#haadmissioncontrolfailoverhostsystemids" title="HaAdmissionControlFailoverHostSystemIds">HaAdmissionControlFailoverHostSystemIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#haadmissioncontrolhostfailuretolerance" title="HaAdmissionControlHostFailureTolerance">HaAdmissionControlHostFailureTolerance</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolperformancetolerance" title="HaAdmissionControlPerformanceTolerance">HaAdmissionControlPerformanceTolerance</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolpolicy" title="HaAdmissionControlPolicy">HaAdmissionControlPolicy</a>" : <i>String</i>,
        "<a href="#haadmissioncontrolresourcepercentageautocompute" title="HaAdmissionControlResourcePercentageAutoCompute">HaAdmissionControlResourcePercentageAutoCompute</a>" : <i>Boolean</i>,
        "<a href="#haadmissioncontrolresourcepercentagecpu" title="HaAdmissionControlResourcePercentageCpu">HaAdmissionControlResourcePercentageCpu</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolresourcepercentagememory" title="HaAdmissionControlResourcePercentageMemory">HaAdmissionControlResourcePercentageMemory</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolslotpolicyexplicitcpu" title="HaAdmissionControlSlotPolicyExplicitCpu">HaAdmissionControlSlotPolicyExplicitCpu</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolslotpolicyexplicitmemory" title="HaAdmissionControlSlotPolicyExplicitMemory">HaAdmissionControlSlotPolicyExplicitMemory</a>" : <i>Double</i>,
        "<a href="#haadmissioncontrolslotpolicyuseexplicitsize" title="HaAdmissionControlSlotPolicyUseExplicitSize">HaAdmissionControlSlotPolicyUseExplicitSize</a>" : <i>Boolean</i>,
        "<a href="#haadvancedoptions" title="HaAdvancedOptions">HaAdvancedOptions</a>" : <i>[ <a href="haadvancedoptions.md">HaAdvancedOptions</a>, ... ]</i>,
        "<a href="#hadatastoreapdrecoveryaction" title="HaDatastoreApdRecoveryAction">HaDatastoreApdRecoveryAction</a>" : <i>String</i>,
        "<a href="#hadatastoreapdresponse" title="HaDatastoreApdResponse">HaDatastoreApdResponse</a>" : <i>String</i>,
        "<a href="#hadatastoreapdresponsedelay" title="HaDatastoreApdResponseDelay">HaDatastoreApdResponseDelay</a>" : <i>Double</i>,
        "<a href="#hadatastorepdlresponse" title="HaDatastorePdlResponse">HaDatastorePdlResponse</a>" : <i>String</i>,
        "<a href="#haenabled" title="HaEnabled">HaEnabled</a>" : <i>Boolean</i>,
        "<a href="#haheartbeatdatastoreids" title="HaHeartbeatDatastoreIds">HaHeartbeatDatastoreIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#haheartbeatdatastorepolicy" title="HaHeartbeatDatastorePolicy">HaHeartbeatDatastorePolicy</a>" : <i>String</i>,
        "<a href="#hahostisolationresponse" title="HaHostIsolationResponse">HaHostIsolationResponse</a>" : <i>String</i>,
        "<a href="#hahostmonitoring" title="HaHostMonitoring">HaHostMonitoring</a>" : <i>String</i>,
        "<a href="#havmcomponentprotection" title="HaVmComponentProtection">HaVmComponentProtection</a>" : <i>String</i>,
        "<a href="#havmdependencyrestartcondition" title="HaVmDependencyRestartCondition">HaVmDependencyRestartCondition</a>" : <i>String</i>,
        "<a href="#havmfailureinterval" title="HaVmFailureInterval">HaVmFailureInterval</a>" : <i>Double</i>,
        "<a href="#havmmaximumfailurewindow" title="HaVmMaximumFailureWindow">HaVmMaximumFailureWindow</a>" : <i>Double</i>,
        "<a href="#havmmaximumresets" title="HaVmMaximumResets">HaVmMaximumResets</a>" : <i>Double</i>,
        "<a href="#havmminimumuptime" title="HaVmMinimumUptime">HaVmMinimumUptime</a>" : <i>Double</i>,
        "<a href="#havmmonitoring" title="HaVmMonitoring">HaVmMonitoring</a>" : <i>String</i>,
        "<a href="#havmrestartadditionaldelay" title="HaVmRestartAdditionalDelay">HaVmRestartAdditionalDelay</a>" : <i>Double</i>,
        "<a href="#havmrestartpriority" title="HaVmRestartPriority">HaVmRestartPriority</a>" : <i>String</i>,
        "<a href="#havmrestarttimeout" title="HaVmRestartTimeout">HaVmRestartTimeout</a>" : <i>Double</i>,
        "<a href="#hostclusterexittimeout" title="HostClusterExitTimeout">HostClusterExitTimeout</a>" : <i>Double</i>,
        "<a href="#hostsystemids" title="HostSystemIds">HostSystemIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#proactivehaautomationlevel" title="ProactiveHaAutomationLevel">ProactiveHaAutomationLevel</a>" : <i>String</i>,
        "<a href="#proactivehaenabled" title="ProactiveHaEnabled">ProactiveHaEnabled</a>" : <i>Boolean</i>,
        "<a href="#proactivehamoderateremediation" title="ProactiveHaModerateRemediation">ProactiveHaModerateRemediation</a>" : <i>String</i>,
        "<a href="#proactivehaproviderids" title="ProactiveHaProviderIds">ProactiveHaProviderIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#proactivehasevereremediation" title="ProactiveHaSevereRemediation">ProactiveHaSevereRemediation</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::ComputeCluster
Properties:
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#dpmautomationlevel" title="DpmAutomationLevel">DpmAutomationLevel</a>: <i>String</i>
    <a href="#dpmenabled" title="DpmEnabled">DpmEnabled</a>: <i>Boolean</i>
    <a href="#dpmthreshold" title="DpmThreshold">DpmThreshold</a>: <i>Double</i>
    <a href="#drsadvancedoptions" title="DrsAdvancedOptions">DrsAdvancedOptions</a>: <i>
      - <a href="drsadvancedoptions.md">DrsAdvancedOptions</a></i>
    <a href="#drsautomationlevel" title="DrsAutomationLevel">DrsAutomationLevel</a>: <i>String</i>
    <a href="#drsenablepredictivedrs" title="DrsEnablePredictiveDrs">DrsEnablePredictiveDrs</a>: <i>Boolean</i>
    <a href="#drsenablevmoverrides" title="DrsEnableVmOverrides">DrsEnableVmOverrides</a>: <i>Boolean</i>
    <a href="#drsenabled" title="DrsEnabled">DrsEnabled</a>: <i>Boolean</i>
    <a href="#drsmigrationthreshold" title="DrsMigrationThreshold">DrsMigrationThreshold</a>: <i>Double</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#forceevacuateondestroy" title="ForceEvacuateOnDestroy">ForceEvacuateOnDestroy</a>: <i>Boolean</i>
    <a href="#haadmissioncontrolfailoverhostsystemids" title="HaAdmissionControlFailoverHostSystemIds">HaAdmissionControlFailoverHostSystemIds</a>: <i>
      - String</i>
    <a href="#haadmissioncontrolhostfailuretolerance" title="HaAdmissionControlHostFailureTolerance">HaAdmissionControlHostFailureTolerance</a>: <i>Double</i>
    <a href="#haadmissioncontrolperformancetolerance" title="HaAdmissionControlPerformanceTolerance">HaAdmissionControlPerformanceTolerance</a>: <i>Double</i>
    <a href="#haadmissioncontrolpolicy" title="HaAdmissionControlPolicy">HaAdmissionControlPolicy</a>: <i>String</i>
    <a href="#haadmissioncontrolresourcepercentageautocompute" title="HaAdmissionControlResourcePercentageAutoCompute">HaAdmissionControlResourcePercentageAutoCompute</a>: <i>Boolean</i>
    <a href="#haadmissioncontrolresourcepercentagecpu" title="HaAdmissionControlResourcePercentageCpu">HaAdmissionControlResourcePercentageCpu</a>: <i>Double</i>
    <a href="#haadmissioncontrolresourcepercentagememory" title="HaAdmissionControlResourcePercentageMemory">HaAdmissionControlResourcePercentageMemory</a>: <i>Double</i>
    <a href="#haadmissioncontrolslotpolicyexplicitcpu" title="HaAdmissionControlSlotPolicyExplicitCpu">HaAdmissionControlSlotPolicyExplicitCpu</a>: <i>Double</i>
    <a href="#haadmissioncontrolslotpolicyexplicitmemory" title="HaAdmissionControlSlotPolicyExplicitMemory">HaAdmissionControlSlotPolicyExplicitMemory</a>: <i>Double</i>
    <a href="#haadmissioncontrolslotpolicyuseexplicitsize" title="HaAdmissionControlSlotPolicyUseExplicitSize">HaAdmissionControlSlotPolicyUseExplicitSize</a>: <i>Boolean</i>
    <a href="#haadvancedoptions" title="HaAdvancedOptions">HaAdvancedOptions</a>: <i>
      - <a href="haadvancedoptions.md">HaAdvancedOptions</a></i>
    <a href="#hadatastoreapdrecoveryaction" title="HaDatastoreApdRecoveryAction">HaDatastoreApdRecoveryAction</a>: <i>String</i>
    <a href="#hadatastoreapdresponse" title="HaDatastoreApdResponse">HaDatastoreApdResponse</a>: <i>String</i>
    <a href="#hadatastoreapdresponsedelay" title="HaDatastoreApdResponseDelay">HaDatastoreApdResponseDelay</a>: <i>Double</i>
    <a href="#hadatastorepdlresponse" title="HaDatastorePdlResponse">HaDatastorePdlResponse</a>: <i>String</i>
    <a href="#haenabled" title="HaEnabled">HaEnabled</a>: <i>Boolean</i>
    <a href="#haheartbeatdatastoreids" title="HaHeartbeatDatastoreIds">HaHeartbeatDatastoreIds</a>: <i>
      - String</i>
    <a href="#haheartbeatdatastorepolicy" title="HaHeartbeatDatastorePolicy">HaHeartbeatDatastorePolicy</a>: <i>String</i>
    <a href="#hahostisolationresponse" title="HaHostIsolationResponse">HaHostIsolationResponse</a>: <i>String</i>
    <a href="#hahostmonitoring" title="HaHostMonitoring">HaHostMonitoring</a>: <i>String</i>
    <a href="#havmcomponentprotection" title="HaVmComponentProtection">HaVmComponentProtection</a>: <i>String</i>
    <a href="#havmdependencyrestartcondition" title="HaVmDependencyRestartCondition">HaVmDependencyRestartCondition</a>: <i>String</i>
    <a href="#havmfailureinterval" title="HaVmFailureInterval">HaVmFailureInterval</a>: <i>Double</i>
    <a href="#havmmaximumfailurewindow" title="HaVmMaximumFailureWindow">HaVmMaximumFailureWindow</a>: <i>Double</i>
    <a href="#havmmaximumresets" title="HaVmMaximumResets">HaVmMaximumResets</a>: <i>Double</i>
    <a href="#havmminimumuptime" title="HaVmMinimumUptime">HaVmMinimumUptime</a>: <i>Double</i>
    <a href="#havmmonitoring" title="HaVmMonitoring">HaVmMonitoring</a>: <i>String</i>
    <a href="#havmrestartadditionaldelay" title="HaVmRestartAdditionalDelay">HaVmRestartAdditionalDelay</a>: <i>Double</i>
    <a href="#havmrestartpriority" title="HaVmRestartPriority">HaVmRestartPriority</a>: <i>String</i>
    <a href="#havmrestarttimeout" title="HaVmRestartTimeout">HaVmRestartTimeout</a>: <i>Double</i>
    <a href="#hostclusterexittimeout" title="HostClusterExitTimeout">HostClusterExitTimeout</a>: <i>Double</i>
    <a href="#hostsystemids" title="HostSystemIds">HostSystemIds</a>: <i>
      - String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#proactivehaautomationlevel" title="ProactiveHaAutomationLevel">ProactiveHaAutomationLevel</a>: <i>String</i>
    <a href="#proactivehaenabled" title="ProactiveHaEnabled">ProactiveHaEnabled</a>: <i>Boolean</i>
    <a href="#proactivehamoderateremediation" title="ProactiveHaModerateRemediation">ProactiveHaModerateRemediation</a>: <i>String</i>
    <a href="#proactivehaproviderids" title="ProactiveHaProviderIds">ProactiveHaProviderIds</a>: <i>
      - String</i>
    <a href="#proactivehasevereremediation" title="ProactiveHaSevereRemediation">ProactiveHaSevereRemediation</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### CustomAttributes

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DpmThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsAdvancedOptions

_Required_: No

_Type_: List of <a href="drsadvancedoptions.md">DrsAdvancedOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsEnablePredictiveDrs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsEnableVmOverrides

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrsMigrationThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceEvacuateOnDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlFailoverHostSystemIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlHostFailureTolerance

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlPerformanceTolerance

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlResourcePercentageAutoCompute

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlResourcePercentageCpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlResourcePercentageMemory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlSlotPolicyExplicitCpu

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlSlotPolicyExplicitMemory

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdmissionControlSlotPolicyUseExplicitSize

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaAdvancedOptions

_Required_: No

_Type_: List of <a href="haadvancedoptions.md">HaAdvancedOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDatastoreApdRecoveryAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDatastoreApdResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDatastoreApdResponseDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaDatastorePdlResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaHeartbeatDatastoreIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaHeartbeatDatastorePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaHostIsolationResponse

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaHostMonitoring

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmComponentProtection

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmDependencyRestartCondition

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmFailureInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmMaximumFailureWindow

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmMaximumResets

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmMinimumUptime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmMonitoring

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmRestartAdditionalDelay

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmRestartPriority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmRestartTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostClusterExitTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostSystemIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveHaAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveHaEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveHaModerateRemediation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveHaProviderIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProactiveHaSevereRemediation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ResourcePoolId

Returns the <code>ResourcePoolId</code> value.

