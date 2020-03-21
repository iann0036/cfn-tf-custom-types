# Terraform::VSphere::DatastoreCluster

CloudFormation equivalent of vsphere_datastore_cluster

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::DatastoreCluster",
    "Properties" : {
        "<a href="#customattributes" title="CustomAttributes">CustomAttributes</a>" : <i>[ &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;, ... ]</i>,
        "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>String</i>,
        "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sdrsadvancedoptions" title="SdrsAdvancedOptions">SdrsAdvancedOptions</a>" : <i>[ &lt;a href=&#34;sdrsadvancedoptions.md&#34;&gt;SdrsAdvancedOptions&lt;/a&gt;, ... ]</i>,
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
      - &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;</i>
    <a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>String</i>
    <a href="#folder" title="Folder">Folder</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sdrsadvancedoptions" title="SdrsAdvancedOptions">SdrsAdvancedOptions</a>: <i>
      - &lt;a href=&#34;sdrsadvancedoptions.md&#34;&gt;SdrsAdvancedOptions&lt;/a&gt;</i>
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

_Required_: No

_Type_: List of &lt;a href=&#34;customattributes.md&#34;&gt;CustomAttributes&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdrsAdvancedOptions

_Required_: No

_Type_: List of &lt;a href=&#34;sdrsadvancedoptions.md&#34;&gt;SdrsAdvancedOptions&lt;/a&gt;

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

