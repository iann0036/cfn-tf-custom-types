# Terraform::AWS::BatchComputeEnvironment

CloudFormation equivalent of aws_batch_compute_environment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::BatchComputeEnvironment",
    "Properties" : {
        "<a href="#computeenvironmentname" title="ComputeEnvironmentName">ComputeEnvironmentName</a>" : <i>String</i>,
        "<a href="#computeenvironmentnameprefix" title="ComputeEnvironmentNamePrefix">ComputeEnvironmentNamePrefix</a>" : <i>String</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#computeresources" title="ComputeResources">ComputeResources</a>" : <i>[ <a href="computeresources.md">ComputeResources</a>, ... ]</i>,
        "<a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>" : <i>[ <a href="launchtemplate.md">LaunchTemplate</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::BatchComputeEnvironment
Properties:
    <a href="#computeenvironmentname" title="ComputeEnvironmentName">ComputeEnvironmentName</a>: <i>String</i>
    <a href="#computeenvironmentnameprefix" title="ComputeEnvironmentNamePrefix">ComputeEnvironmentNamePrefix</a>: <i>String</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#computeresources" title="ComputeResources">ComputeResources</a>: <i>
      - <a href="computeresources.md">ComputeResources</a></i>
    <a href="#launchtemplate" title="LaunchTemplate">LaunchTemplate</a>: <i>
      - <a href="launchtemplate.md">LaunchTemplate</a></i>
</pre>

## Properties

#### ComputeEnvironmentName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeEnvironmentNamePrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeResources

_Required_: No

_Type_: List of <a href="computeresources.md">ComputeResources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LaunchTemplate

_Required_: No

_Type_: List of <a href="launchtemplate.md">LaunchTemplate</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### EccClusterArn

Returns the <code>EccClusterArn</code> value.

#### EcsClusterArn

Returns the <code>EcsClusterArn</code> value.

#### Status

Returns the <code>Status</code> value.

#### StatusReason

Returns the <code>StatusReason</code> value.

