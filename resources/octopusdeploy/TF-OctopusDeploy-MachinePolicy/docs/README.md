# TF::OctopusDeploy::MachinePolicy

CloudFormation equivalent of octopusdeploy_machine_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OctopusDeploy::MachinePolicy",
    "Properties" : {
        "<a href="#connectionconnecttimeout" title="ConnectionConnectTimeout">ConnectionConnectTimeout</a>" : <i>Double</i>,
        "<a href="#connectionretrycountlimit" title="ConnectionRetryCountLimit">ConnectionRetryCountLimit</a>" : <i>Double</i>,
        "<a href="#connectionretrysleepinterval" title="ConnectionRetrySleepInterval">ConnectionRetrySleepInterval</a>" : <i>Double</i>,
        "<a href="#connectionretrytimelimit" title="ConnectionRetryTimeLimit">ConnectionRetryTimeLimit</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pollingrequestmaximummessageprocessingtimeout" title="PollingRequestMaximumMessageProcessingTimeout">PollingRequestMaximumMessageProcessingTimeout</a>" : <i>Double</i>,
        "<a href="#pollingrequestqueuetimeout" title="PollingRequestQueueTimeout">PollingRequestQueueTimeout</a>" : <i>Double</i>,
        "<a href="#spaceid" title="SpaceId">SpaceId</a>" : <i>String</i>,
        "<a href="#machinecleanuppolicy" title="MachineCleanupPolicy">MachineCleanupPolicy</a>" : <i>[ <a href="machinecleanuppolicydefinition.md">MachineCleanupPolicyDefinition</a>, ... ]</i>,
        "<a href="#machineconnectivitypolicy" title="MachineConnectivityPolicy">MachineConnectivityPolicy</a>" : <i>[ <a href="machineconnectivitypolicydefinition.md">MachineConnectivityPolicyDefinition</a>, ... ]</i>,
        "<a href="#machinehealthcheckpolicy" title="MachineHealthCheckPolicy">MachineHealthCheckPolicy</a>" : <i>[ <a href="machinehealthcheckpolicydefinition.md">MachineHealthCheckPolicyDefinition</a>, ... ]</i>,
        "<a href="#machineupdatepolicy" title="MachineUpdatePolicy">MachineUpdatePolicy</a>" : <i>[ <a href="machineupdatepolicydefinition.md">MachineUpdatePolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OctopusDeploy::MachinePolicy
Properties:
    <a href="#connectionconnecttimeout" title="ConnectionConnectTimeout">ConnectionConnectTimeout</a>: <i>Double</i>
    <a href="#connectionretrycountlimit" title="ConnectionRetryCountLimit">ConnectionRetryCountLimit</a>: <i>Double</i>
    <a href="#connectionretrysleepinterval" title="ConnectionRetrySleepInterval">ConnectionRetrySleepInterval</a>: <i>Double</i>
    <a href="#connectionretrytimelimit" title="ConnectionRetryTimeLimit">ConnectionRetryTimeLimit</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pollingrequestmaximummessageprocessingtimeout" title="PollingRequestMaximumMessageProcessingTimeout">PollingRequestMaximumMessageProcessingTimeout</a>: <i>Double</i>
    <a href="#pollingrequestqueuetimeout" title="PollingRequestQueueTimeout">PollingRequestQueueTimeout</a>: <i>Double</i>
    <a href="#spaceid" title="SpaceId">SpaceId</a>: <i>String</i>
    <a href="#machinecleanuppolicy" title="MachineCleanupPolicy">MachineCleanupPolicy</a>: <i>
      - <a href="machinecleanuppolicydefinition.md">MachineCleanupPolicyDefinition</a></i>
    <a href="#machineconnectivitypolicy" title="MachineConnectivityPolicy">MachineConnectivityPolicy</a>: <i>
      - <a href="machineconnectivitypolicydefinition.md">MachineConnectivityPolicyDefinition</a></i>
    <a href="#machinehealthcheckpolicy" title="MachineHealthCheckPolicy">MachineHealthCheckPolicy</a>: <i>
      - <a href="machinehealthcheckpolicydefinition.md">MachineHealthCheckPolicyDefinition</a></i>
    <a href="#machineupdatepolicy" title="MachineUpdatePolicy">MachineUpdatePolicy</a>: <i>
      - <a href="machineupdatepolicydefinition.md">MachineUpdatePolicyDefinition</a></i>
</pre>

## Properties

#### ConnectionConnectTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionRetryCountLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionRetrySleepInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionRetryTimeLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollingRequestMaximumMessageProcessingTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollingRequestQueueTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineCleanupPolicy

_Required_: No

_Type_: List of <a href="machinecleanuppolicydefinition.md">MachineCleanupPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineConnectivityPolicy

_Required_: No

_Type_: List of <a href="machineconnectivitypolicydefinition.md">MachineConnectivityPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineHealthCheckPolicy

_Required_: No

_Type_: List of <a href="machinehealthcheckpolicydefinition.md">MachineHealthCheckPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MachineUpdatePolicy

_Required_: No

_Type_: List of <a href="machineupdatepolicydefinition.md">MachineUpdatePolicyDefinition</a>

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

#### IsDefault

Returns the <code>IsDefault</code> value.

