# Terraform::VSphere::HaVmOverride

CloudFormation equivalent of vsphere_ha_vm_override

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::HaVmOverride",
    "Properties" : {
        "<a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>" : <i>String</i>,
        "<a href="#hadatastoreapdrecoveryaction" title="HaDatastoreApdRecoveryAction">HaDatastoreApdRecoveryAction</a>" : <i>String</i>,
        "<a href="#hadatastoreapdresponse" title="HaDatastoreApdResponse">HaDatastoreApdResponse</a>" : <i>String</i>,
        "<a href="#hadatastoreapdresponsedelay" title="HaDatastoreApdResponseDelay">HaDatastoreApdResponseDelay</a>" : <i>Double</i>,
        "<a href="#hadatastorepdlresponse" title="HaDatastorePdlResponse">HaDatastorePdlResponse</a>" : <i>String</i>,
        "<a href="#hahostisolationresponse" title="HaHostIsolationResponse">HaHostIsolationResponse</a>" : <i>String</i>,
        "<a href="#havmfailureinterval" title="HaVmFailureInterval">HaVmFailureInterval</a>" : <i>Double</i>,
        "<a href="#havmmaximumfailurewindow" title="HaVmMaximumFailureWindow">HaVmMaximumFailureWindow</a>" : <i>Double</i>,
        "<a href="#havmmaximumresets" title="HaVmMaximumResets">HaVmMaximumResets</a>" : <i>Double</i>,
        "<a href="#havmminimumuptime" title="HaVmMinimumUptime">HaVmMinimumUptime</a>" : <i>Double</i>,
        "<a href="#havmmonitoring" title="HaVmMonitoring">HaVmMonitoring</a>" : <i>String</i>,
        "<a href="#havmmonitoringuseclusterdefaults" title="HaVmMonitoringUseClusterDefaults">HaVmMonitoringUseClusterDefaults</a>" : <i>Boolean</i>,
        "<a href="#havmrestartpriority" title="HaVmRestartPriority">HaVmRestartPriority</a>" : <i>String</i>,
        "<a href="#havmrestarttimeout" title="HaVmRestartTimeout">HaVmRestartTimeout</a>" : <i>Double</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::HaVmOverride
Properties:
    <a href="#computeclusterid" title="ComputeClusterId">ComputeClusterId</a>: <i>String</i>
    <a href="#hadatastoreapdrecoveryaction" title="HaDatastoreApdRecoveryAction">HaDatastoreApdRecoveryAction</a>: <i>String</i>
    <a href="#hadatastoreapdresponse" title="HaDatastoreApdResponse">HaDatastoreApdResponse</a>: <i>String</i>
    <a href="#hadatastoreapdresponsedelay" title="HaDatastoreApdResponseDelay">HaDatastoreApdResponseDelay</a>: <i>Double</i>
    <a href="#hadatastorepdlresponse" title="HaDatastorePdlResponse">HaDatastorePdlResponse</a>: <i>String</i>
    <a href="#hahostisolationresponse" title="HaHostIsolationResponse">HaHostIsolationResponse</a>: <i>String</i>
    <a href="#havmfailureinterval" title="HaVmFailureInterval">HaVmFailureInterval</a>: <i>Double</i>
    <a href="#havmmaximumfailurewindow" title="HaVmMaximumFailureWindow">HaVmMaximumFailureWindow</a>: <i>Double</i>
    <a href="#havmmaximumresets" title="HaVmMaximumResets">HaVmMaximumResets</a>: <i>Double</i>
    <a href="#havmminimumuptime" title="HaVmMinimumUptime">HaVmMinimumUptime</a>: <i>Double</i>
    <a href="#havmmonitoring" title="HaVmMonitoring">HaVmMonitoring</a>: <i>String</i>
    <a href="#havmmonitoringuseclusterdefaults" title="HaVmMonitoringUseClusterDefaults">HaVmMonitoringUseClusterDefaults</a>: <i>Boolean</i>
    <a href="#havmrestartpriority" title="HaVmRestartPriority">HaVmRestartPriority</a>: <i>String</i>
    <a href="#havmrestarttimeout" title="HaVmRestartTimeout">HaVmRestartTimeout</a>: <i>Double</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#virtualmachineid" title="VirtualMachineId">VirtualMachineId</a>: <i>String</i>
</pre>

## Properties

#### ComputeClusterId

_Required_: Yes

_Type_: String

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

#### HaHostIsolationResponse

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

#### HaVmMonitoringUseClusterDefaults

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmRestartPriority

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HaVmRestartTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualMachineId

_Required_: Yes

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

