# Terraform::VSphere::ComputeCluster

-> **A note on the naming of this resource:** VMware refers to clusters of
hosts in the UI and documentation as _clusters_, _HA clusters_, or _DRS
clusters_. All of these refer to the same kind of resource (with the latter two
referring to specific features of clustering). In Terraform, we use
`vsphere_compute_cluster` to differentiate host clusters from _datastore
clusters_, which are clusters of datastores that can be used to distribute load
and ensure fault tolerance via distribution of virtual machines. Datastore
clusters can also be managed through Terraform, via the
[`vsphere_datastore_cluster` resource][docs-r-vsphere-datastore-cluster].

[docs-r-vsphere-datastore-cluster]: /docs/providers/vsphere/r/datastore_cluster.html

The `vsphere_compute_cluster` resource can be used to create and manage
clusters of hosts allowing for resource control of compute resources, load
balancing through DRS, and high availability through vSphere HA.

For more information on vSphere clusters and DRS, see [this
page][ref-vsphere-drs-clusters]. For more information on vSphere HA, see [this
page][ref-vsphere-ha-clusters].

[ref-vsphere-drs-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-8ACF3502-5314-469F-8CC9-4A9BD5925BC2.html
[ref-vsphere-ha-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.avail.doc/GUID-5432CA24-14F1-44E3-87FB-61D937831CF6.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** vSphere DRS requires a vSphere Enterprise Plus license.

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

A map of custom attribute ids to attribute
value strings to set for the datastore cluster. See
[here][docs-setting-custom-attributes] for a reference on how to set values
for custom attributes.

_Required_: No

_Type_: List of <a href="customattributes.md">CustomAttributes</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

The [managed object ID][docs-about-morefs] of
the datacenter to create the cluster in. Forces a new resource if changed.

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

The relative path to a folder to put this cluster in.
This is a path relative to the datacenter you are deploying the cluster to.
Example: for the `dc1` datacenter, and a provided `folder` of `foo/bar`,
Terraform will place a cluster named `terraform-compute-cluster-test` in a
host folder located at `/dc1/host/foo/bar`, with the final inventory path
being `/dc1/host/foo/bar/terraform-datastore-cluster-test`.

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

#### Name

The name of the cluster.

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

The IDs of any tags to attach to this resource. See
[here][docs-applying-tags] for a reference on how to apply tags.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### ResourcePoolId

Returns the <code>ResourcePoolId</code> value.

