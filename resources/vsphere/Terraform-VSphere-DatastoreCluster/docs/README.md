# Terraform::VSphere::DatastoreCluster

The `vsphere_datastore_cluster` resource can be used to create and manage
datastore clusters. This can be used to create groups of datastores with a
shared management interface, allowing for resource control and load balancing
through Storage DRS.

For more information on vSphere datastore clusters and Storage DRS, see [this
page][ref-vsphere-datastore-clusters].

[ref-vsphere-datastore-clusters]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.resmgmt.doc/GUID-598DF695-107E-406B-9C95-0AF961FC227A.html

~> **NOTE:** This resource requires vCenter and is not available on direct ESXi
connections.

~> **NOTE:** Storage DRS requires a vSphere Enterprise Plus license.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DatastoreCluster",
    "Properties" : {
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ <a href="customattributes.md">CustomAttributes</a>, ... ]</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sdrsadvancedoptions" title="SdrsAdvancedOptions">SdrsAdvancedOptions</a>" : <i>[ <a href="sdrsadvancedoptions.md">SdrsAdvancedOptions</a>, ... ]</i>,
        "<a href="#sdrsautomationlevel" title="SdrsAutomationLevel">SdrsAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsdefaultintravmaffinity" title="SdrsDefaultIntraVmAffinity">SdrsDefaultIntraVmAffinity</a>" : <i>Boolean</i>,
        "<a href="#sdrsenabled" title="SdrsEnabled">SdrsEnabled</a>" : <i>Boolean</i>,
        "<a href="#sdrsfreespacethreshold" title="SdrsFreeSpaceThreshold">SdrsFreeSpaceThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsfreespacethresholdmode" title="SdrsFreeSpaceThresholdMode">SdrsFreeSpaceThresholdMode</a>" : <i>String</i>,
        "<a href="#sdrsfreespaceutilizationdifference" title="SdrsFreeSpaceUtilizationDifference">SdrsFreeSpaceUtilizationDifference</a>" : <i>Double</i>,
        "<a href="#sdrsiobalanceautomationlevel" title="SdrsIoBalanceAutomationLevel">SdrsIoBalanceAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsiolatencythreshold" title="SdrsIoLatencyThreshold">SdrsIoLatencyThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsioloadbalanceenabled" title="SdrsIoLoadBalanceEnabled">SdrsIoLoadBalanceEnabled</a>" : <i>Boolean</i>,
        "<a href="#sdrsioloadimbalancethreshold" title="SdrsIoLoadImbalanceThreshold">SdrsIoLoadImbalanceThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsioreservableiopsthreshold" title="SdrsIoReservableIopsThreshold">SdrsIoReservableIopsThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsioreservablepercentthreshold" title="SdrsIoReservablePercentThreshold">SdrsIoReservablePercentThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsioreservablethresholdmode" title="SdrsIoReservableThresholdMode">SdrsIoReservableThresholdMode</a>" : <i>String</i>,
        "<a href="#sdrsloadbalanceinterval" title="SdrsLoadBalanceInterval">SdrsLoadBalanceInterval</a>" : <i>Double</i>,
        "<a href="#sdrspolicyenforcementautomationlevel" title="SdrsPolicyEnforcementAutomationLevel">SdrsPolicyEnforcementAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsruleenforcementautomationlevel" title="SdrsRuleEnforcementAutomationLevel">SdrsRuleEnforcementAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsspacebalanceautomationlevel" title="SdrsSpaceBalanceAutomationLevel">SdrsSpaceBalanceAutomationLevel</a>" : <i>String</i>,
        "<a href="#sdrsspaceutilizationthreshold" title="SdrsSpaceUtilizationThreshold">SdrsSpaceUtilizationThreshold</a>" : <i>Double</i>,
        "<a href="#sdrsvmevacuationautomationlevel" title="SdrsVmEvacuationAutomationLevel">SdrsVmEvacuationAutomationLevel</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::DatastoreCluster
Properties:
    <a href="#customattributes" title="CustomAttributes">CustomAttributes</a>: <i>
      - <a href="customattributes.md">CustomAttributes</a></i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sdrsadvancedoptions" title="SdrsAdvancedOptions">SdrsAdvancedOptions</a>: <i>
      - <a href="sdrsadvancedoptions.md">SdrsAdvancedOptions</a></i>
    <a href="#sdrsautomationlevel" title="SdrsAutomationLevel">SdrsAutomationLevel</a>: <i>String</i>
    <a href="#sdrsdefaultintravmaffinity" title="SdrsDefaultIntraVmAffinity">SdrsDefaultIntraVmAffinity</a>: <i>Boolean</i>
    <a href="#sdrsenabled" title="SdrsEnabled">SdrsEnabled</a>: <i>Boolean</i>
    <a href="#sdrsfreespacethreshold" title="SdrsFreeSpaceThreshold">SdrsFreeSpaceThreshold</a>: <i>Double</i>
    <a href="#sdrsfreespacethresholdmode" title="SdrsFreeSpaceThresholdMode">SdrsFreeSpaceThresholdMode</a>: <i>String</i>
    <a href="#sdrsfreespaceutilizationdifference" title="SdrsFreeSpaceUtilizationDifference">SdrsFreeSpaceUtilizationDifference</a>: <i>Double</i>
    <a href="#sdrsiobalanceautomationlevel" title="SdrsIoBalanceAutomationLevel">SdrsIoBalanceAutomationLevel</a>: <i>String</i>
    <a href="#sdrsiolatencythreshold" title="SdrsIoLatencyThreshold">SdrsIoLatencyThreshold</a>: <i>Double</i>
    <a href="#sdrsioloadbalanceenabled" title="SdrsIoLoadBalanceEnabled">SdrsIoLoadBalanceEnabled</a>: <i>Boolean</i>
    <a href="#sdrsioloadimbalancethreshold" title="SdrsIoLoadImbalanceThreshold">SdrsIoLoadImbalanceThreshold</a>: <i>Double</i>
    <a href="#sdrsioreservableiopsthreshold" title="SdrsIoReservableIopsThreshold">SdrsIoReservableIopsThreshold</a>: <i>Double</i>
    <a href="#sdrsioreservablepercentthreshold" title="SdrsIoReservablePercentThreshold">SdrsIoReservablePercentThreshold</a>: <i>Double</i>
    <a href="#sdrsioreservablethresholdmode" title="SdrsIoReservableThresholdMode">SdrsIoReservableThresholdMode</a>: <i>String</i>
    <a href="#sdrsloadbalanceinterval" title="SdrsLoadBalanceInterval">SdrsLoadBalanceInterval</a>: <i>Double</i>
    <a href="#sdrspolicyenforcementautomationlevel" title="SdrsPolicyEnforcementAutomationLevel">SdrsPolicyEnforcementAutomationLevel</a>: <i>String</i>
    <a href="#sdrsruleenforcementautomationlevel" title="SdrsRuleEnforcementAutomationLevel">SdrsRuleEnforcementAutomationLevel</a>: <i>String</i>
    <a href="#sdrsspacebalanceautomationlevel" title="SdrsSpaceBalanceAutomationLevel">SdrsSpaceBalanceAutomationLevel</a>: <i>String</i>
    <a href="#sdrsspaceutilizationthreshold" title="SdrsSpaceUtilizationThreshold">SdrsSpaceUtilizationThreshold</a>: <i>Double</i>
    <a href="#sdrsvmevacuationautomationlevel" title="SdrsVmEvacuationAutomationLevel">SdrsVmEvacuationAutomationLevel</a>: <i>String</i>
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
the datacenter to create the datastore cluster in. Forces a new resource if
changed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

The relative path to a folder to put this datastore
cluster in.  This is a path relative to the datacenter you are deploying the
datastore to.  Example: for the `dc1` datacenter, and a provided `folder` of
`foo/bar`, Terraform will place a datastore cluster named
`terraform-datastore-cluster-test` in a datastore folder located at
`/dc1/datastore/foo/bar`, with the final inventory path being
`/dc1/datastore/foo/bar/terraform-datastore-cluster-test`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the datastore cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsAdvancedOptions

_Required_: No

_Type_: List of <a href="sdrsadvancedoptions.md">SdrsAdvancedOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsDefaultIntraVmAffinity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsEnabled

Enable Storage DRS for this datastore cluster.
Default: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsFreeSpaceThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsFreeSpaceThresholdMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsFreeSpaceUtilizationDifference

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoBalanceAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoLatencyThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoLoadBalanceEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoLoadImbalanceThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoReservableIopsThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoReservablePercentThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsIoReservableThresholdMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsLoadBalanceInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsPolicyEnforcementAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsRuleEnforcementAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsSpaceBalanceAutomationLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsSpaceUtilizationThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsVmEvacuationAutomationLevel

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

